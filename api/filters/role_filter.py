import django_filters as filters

from api.models import Role


class RoleFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="contains")
    role = filters.CharFilter(field_name="role__code_name", lookup_expr="exact")

    class Meta:
        model = Role
        fields = ["name", "code_name"]
