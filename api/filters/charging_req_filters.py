import django_filters as filters

from api.models import ChargingRequest


class ChargingRequestFilter(filters.FilterSet):
    user = filters.NumberFilter(field_name="user__id", lookup_expr="exact")
    spot = filters.NumberFilter(field_name="spot__id", lookup_expr="exact")
    bot_id = filters.NumberFilter(field_name="bot_id", lookup_expr="exact")
    car_model = filters.CharFilter(field_name="car_model", lookup_expr="icontains")
    battery_capacity_min = filters.NumberFilter(
        field_name="battery_capacity", lookup_expr="gte"
    )
    battery_capacity_max = filters.NumberFilter(
        field_name="battery_capacity", lookup_expr="lte"
    )
    duration_min = filters.NumberFilter(field_name="duration", lookup_expr="gte")
    duration_max = filters.NumberFilter(field_name="duration", lookup_expr="lte")
    status = filters.CharFilter(field_name="status", lookup_expr="icontains")
    request_time_after = filters.DateTimeFilter(
        field_name="request_time", lookup_expr="gte"
    )
    request_time_before = filters.DateTimeFilter(
        field_name="request_time", lookup_expr="lte"
    )
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
        model = ChargingRequest
        fields = [
            "user",
            "spot",
            "bot_id",
            "car_model",
            "battery_capacity_min",
            "battery_capacity_max",
            "duration_min",
            "duration_max",
            "status",
            "request_time_after",
            "request_time_before",
            "created_by",
            "updated_by",
            "created_at_after",
            "created_at_before",
            "updated_at_after",
            "updated_at_before",
        ]
