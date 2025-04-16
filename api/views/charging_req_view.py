import json

import paho.mqtt.publish as mqtt_publish
from django_filters import rest_framework as filters
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from api.filters import ChargingRequestFilter
from api.models import ChargingRequest, ParkingSpot, User
from api.serializers import ChargingRequestSerializer

MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "parking/charging"


class ChargingRequestViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = ChargingRequest.objects.all()
    serializer_class = ChargingRequestSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ChargingRequestFilter

    def create(self, request, *args, **kwargs):
        user_id = request.data.get("user")
        spot_id = request.data.get("parking_spot")
        car_model = request.data.get("car_model")
        battery_capacity = request.data.get("battery_capacity")
        duration = request.data.get("duration")

        # Validate user existence
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response(
                {"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND
            )

        # Validate parking spot existence
        try:
            spot = ParkingSpot.objects.get(id=spot_id)
        except ParkingSpot.DoesNotExist:
            return Response(
                {"error": "Parking spot does not exist"},
                status=status.HTTP_404_NOT_FOUND,
            )

        # Check if the spot is occupied
        if spot.is_occupied:
            return Response(
                {"error": "Spot is occupied"}, status=status.HTTP_400_BAD_REQUEST
            )

        # Check if the user already requested the same spot
        if ChargingRequest.objects.filter(user=user, spot=spot, status='pending').exists():
            return Response(
                {"error": "You already have a charging request for this spot"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Create Charging Request
        charging_request = ChargingRequest(
            user=user,
            spot=spot,
            car_model=car_model,
            battery_capacity=battery_capacity,
            duration=duration,
            bot_id=1,
        )
        charging_request.save()
        spot.is_occupied = True
        spot.save()

        # # Publish message to MQTT broker
        # mqtt_publish.single(
        #     MQTT_TOPIC,
        #     payload=f"charge {car_model} at spot {spot.spot_id}",
        #     hostname=MQTT_BROKER,
        #     port=MQTT_PORT
        # )

        # Publish MQTT Message
        message = json.dumps({"botID": 1, "spotID": spot.id, "action": "dispatch"})
        mqtt_publish.single(
            f"mwbot/dispatch/1", message, hostname=MQTT_BROKER, port=MQTT_PORT
        )

        return Response(
            {
                "message": f"Charging requested for {car_model} at spot {spot.spot_id} for {duration} minutes by {user.name}"
            },
            status=status.HTTP_201_CREATED,
        )
