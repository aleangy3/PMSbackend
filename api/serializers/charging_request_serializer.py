from rest_framework import serializers

from api.models import ChargingRequest


class ChargingRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChargingRequest
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]
