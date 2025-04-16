import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pms.settings")
django.setup()

from django.utils import timezone
from api.models import Permission, Role, User

# Define users
users = [
    {
        "id": 1,
        "username": "test",
        "email": "test@example.com",
        "name": "Test",
        "profile_status": "Current",
        "is_delete": "No",
        "role": "basic",
    },
]

# Define roles and permissions (unchanged)
roles = [
    {
        "name": "Basic",
        "code_name": "basic",
        "permissions": [
            "dashboard_show",
            "show_parking_spots",
            "read_parking_spot",
            "show_charging_requests",
            "create_charging_request",
            "read_charging_request",
            "update_charging_request",
            "delete_charging_request",
        ],
    },
    {
        "name": "Premium",
        "code_name": "premium",
        "permissions": [
            "dashboard_show",
            "show_parking_spots",
            "read_parking_spot",
            "show_charging_requests",
            "create_charging_request",
            "read_charging_request",
            "update_charging_request",
            "delete_charging_request",
            "show_reservations",
            "create_reservation",
            "read_reservation",
            "update_reservation",
            "delete_reservation",
        ],
    },
]

def populate():
    print("Starting PMS population script...")

    # Fetch all permissions into a dictionary for quick lookup
    existing_permissions = {p.code_name: p for p in Permission.objects.all()}

    # Ensure SuperUser Role exists
    su_role, _ = Role.objects.get_or_create(name="SuperUser", code_name="su")
    su_role.permissions.set(existing_permissions.values())  # Assign all permissions
    su_role.save()

    # Ensure superuser exists
    superuser, created = User.objects.get_or_create(
        id=999,
        username="superuser",
        defaults={"name": "Superuser", "email": "superuser@example.com"},
    )
    if created:
        superuser.set_password("123")
    superuser.role = su_role
    superuser.save()

    # Populate roles and permissions
    for role_data in roles:
        role, created = Role.objects.get_or_create(
            code_name=role_data["code_name"],
            defaults={
                "name": role_data["name"],
                "created_by": superuser,
                "updated_by": superuser,
            },
        )

        missing_perms = []
        for perm_code in role_data["permissions"]:
            if perm_code in existing_permissions:
                role.permissions.add(existing_permissions[perm_code])
            else:
                missing_perms.append(perm_code)

        if missing_perms:
            print(f"Warning: Some permissions not found for role '{role.code_name}': {missing_perms}")

        role.save()

    # Populate users
    for user_data in users:
        try:
            user_role = Role.objects.get(code_name=user_data["role"])
        except Role.DoesNotExist:
            print(f"Warning: Role '{user_data['role']}' does not exist. Skipping user '{user_data['username']}'")
            continue

        User.objects.update_or_create(
            id=user_data["id"],
            defaults={
                "username": user_data["username"],
                "email": user_data["email"],
                "name": user_data["name"],
                "contact": user_data.get("contact"),  # Optional
                "profile_status": user_data["profile_status"],
                "is_delete": user_data["is_delete"],
                "role": user_role,
            },
        )

    print("PMS population script completed successfully!")

if __name__ == "__main__":
    populate()
