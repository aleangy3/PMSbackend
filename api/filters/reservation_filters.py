import django_filters as filters

from api.models import Reservation


class ReservationFilter(filters.FilterSet):
    user = filters.NumberFilter(field_name="user__id", lookup_expr="exact")
    spot = filters.NumberFilter(field_name="spot__id", lookup_expr="exact")
    start_time_after = filters.DateTimeFilter(
        field_name="start_time", lookup_expr="gte"
    )
    start_time_before = filters.DateTimeFilter(
        field_name="start_time", lookup_expr="lte"
    )
    end_time_after = filters.DateTimeFilter(field_name="end_time", lookup_expr="gte")
    end_time_before = filters.DateTimeFilter(field_name="end_time", lookup_expr="lte")
    is_active = filters.BooleanFilter(field_name="is_active")
    created_by = filters.NumberFilter(field_name="created_by__id", lookup_expr="exact")
    updated_by = filters.NumberFilter(field_name="updated_by__id", lookup_expr="exact")
    created_at_after = filters.DateTimeFilter(
        field_name="created_at", lookup_expr="gte"
    )
    created_at_before = filters.DateTimeFilter(
        field_name="created_at", lookup_expr="lte"
    )
    updated_at_after = filters.DateTimeFilter(
        field_name="updated_at", lookup_expr="gte"
    )
    updated_at_before = filters.DateTimeFilter(
        field_name="updated_at", lookup_expr="lte"
    )

    class Meta:
        model = Reservation
        fields = [
            "user",
            "spot",
            "start_time_after",
            "start_time_before",
            "end_time_after",
            "end_time_before",
            "is_active",
            "created_by",
            "updated_by",
            "created_at_after",
            "created_at_before",
            "updated_at_after",
            "updated_at_before",
        ]
