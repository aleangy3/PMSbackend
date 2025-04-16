import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pms.settings")

import django

django.setup()

from api.models import Permission

permissions = [
    # User
    Permission(
        name="Create User",
        code_name="create_user",
        module_name="User",
        description="User can create user",
    ),
    Permission(
        name="Read User",
        code_name="read_user",
        module_name="User",
        description="User can read user",
    ),
    Permission(
        name="Update User",
        code_name="update_user",
        module_name="User",
        description="User can update user",
    ),
    Permission(
        name="Show User",
        code_name="show_user",
        module_name="User",
        description="User can view user",
    ),
    # Role
    Permission(
        name="Create Role",
        code_name="create_role",
        module_name="Role",
        description="User can create role",
    ),
    Permission(
        name="Read Role",
        code_name="read_role",
        module_name="Role",
        description="User can read role",
    ),
    Permission(
        name="Update Role",
        code_name="update_role",
        module_name="Role",
        description="User can update role",
    ),
    Permission(
        name="Delete Role",
        code_name="delete_role",
        module_name="Role",
        description="User can delete role",
    ),
    Permission(
        name="Show Role",
        code_name="show_role",
        module_name="Role",
        description="User can view role",
    ),
    # Dashboard
    Permission(
        name="Show Dashboard",
        code_name="dashboard_show",
        module_name="Dashboard",
        description="User can show dashboard",
    ),
    # Parking Spots
    Permission(
        name="Show Parking Spots",
        code_name="show_parking_spots",
        module_name="Parking Spot",
        description="User can show parking spots",
    ),
    Permission(
        name="Read Parking Spot",
        code_name="read_parking_spot",
        module_name="Parking Spot",
        description="User can read parking spot",
    ),
    Permission(
        name="Create Parking Spot",
        code_name="create_parking_spot",
        module_name="Parking Spot",
        description="User can create parking spot",
    ),
    Permission(
        name="Update Parking Spot",
        code_name="update_parking_spot",
        module_name="Parking Spot",
        description="User can update parking spot",
    ),
    Permission(
        name="Delete Parking Spot",
        code_name="delete_parking_spot",
        module_name="Parking Spot",
        description="User can delete parking spot",
    ),
    # Charging Requests
    Permission(
        name="Show Charging Requests",
        code_name="show_charging_requests",
        module_name="Charging Request",
        description="User can show charging requests",
    ),
    Permission(
        name="Read Charging Requests",
        code_name="read_charging_request",
        module_name="Charging Request",
        description="User can read charging requests",
    ),
    Permission(
        name="Create Charging Request",
        code_name="create_charging_request",
        module_name="Charging Request",
        description="User can create charging request",
    ),
    Permission(
        name="Update Charging Request",
        code_name="update_charging_request",
        module_name="Charging Request",
        description="User can update charging request",
    ),
    Permission(
        name="Delete Charging Request",
        code_name="delete_charging_request",
        module_name="Charging Request",
        description="User can delete charging request",
    ),
    # Reservations
    Permission(
        name="Show Reservations",
        code_name="show_reservations",
        module_name="Reservation",
        description="User can show reservations",
    ),
    Permission(
        name="Read Reservations",
        code_name="read_reservation",
        module_name="Reservation",
        description="User can read reservations",
    ),
    Permission(
        name="Create Reservation",
        code_name="create_reservation",
        module_name="Reservation",
        description="User can create reservation",
    ),
    Permission(
        name="Update Reservation",
        code_name="update_reservation",
        module_name="Reservation",
        description="User can update reservation",
    ),
    Permission(
        name="Delete Reservation",
        code_name="delete_reservation",
        module_name="Reservation",
        description="User can delete reservation",
    ),
]


def add_permission():
    for permission in permissions:
        try:
            Permission.objects.get(code_name=permission.code_name)
        except Permission.DoesNotExist:
            permission.save()


if __name__ == "__main__":
    print("Adding permissions to PMS...")
    add_permission()
