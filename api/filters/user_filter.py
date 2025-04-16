import django_filters as filters

from api.models import User


class UserFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="contains")
    username = filters.CharFilter(field_name="username", lookup_expr="contains")
    role = filters.CharFilter(field_name="role__code_name", lookup_expr="exact")
    exclude_user = filters.NumberFilter(field_name="id", exclude=True)
    profile_status = filters.CharFilter(
        field_name="profile_status", lookup_expr="exact"
    )

    class Meta:
        model = User
        fields = ["name", "username", "role", "exclude_user", "profile_status"]
