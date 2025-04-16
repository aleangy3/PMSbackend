import django_filters as filters

from api.models import ParkingSpot


class ParkingSpotFilter(filters.FilterSet):
    spot_id = filters.CharFilter(field_name="spot_id", lookup_expr="icontains")
    is_occupied = filters.BooleanFilter(field_name="is_occupied")
    has_charger = filters.BooleanFilter(field_name="has_charger")
    created_by = filters.NumberFilter(field_name="created_by__id", lookup_expr="exact")
    updated_by = filters.NumberFilter(field_name="updated_by__id", lookup_expr="exact")

    class Meta:
        model = ParkingSpot
        fields = ["spot_id", "is_occupied", "has_charger", "created_by", "updated_by"]
