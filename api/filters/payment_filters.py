import django_filters as filters

from api.models import Payment


class PaymentFilter(filters.FilterSet):
    user = filters.NumberFilter(field_name="user__id", lookup_expr="exact")
    amount_min = filters.NumberFilter(field_name="amount", lookup_expr="gte")
    amount_max = filters.NumberFilter(field_name="amount", lookup_expr="lte")
    status = filters.CharFilter(field_name="status", lookup_expr="icontains")
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
        model = Payment
        fields = [
            "user",
            "amount_min",
            "amount_max",
            "status",
            "created_by",
            "updated_by",
            "created_at_after",
            "created_at_before",
            "updated_at_after",
            "updated_at_before",
        ]
