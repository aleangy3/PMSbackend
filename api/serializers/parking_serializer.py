from rest_framework import serializers

from api.models import ParkingSpot
from .utils import get_user_data


class ParkingSpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSpot
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]
    
    def to_representation(self, instance):
        obj = instance
        instance = super().to_representation(instance)
        instance['created_by_data'] = get_user_data(obj.created_by)
        instance['updated_by_data'] = get_user_data(obj.updated_by)
        return instance
