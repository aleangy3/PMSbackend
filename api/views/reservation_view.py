from django_filters import rest_framework as filters
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from api.filters import ReservationFilter
from api.models import ParkingSpot, Reservation, User
from api.serializers import ReservationSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ReservationFilter

    def create(self, request, *args, **kwargs):
        user_id = request.data.get("user")
        spot_id = request.data.get("parking_spot")
        start_time = request.data.get("start_time")
        end_time = request.data.get("end_time")

        user = User.objects.get(id=user_id)
        spot = ParkingSpot.objects.get(id=spot_id)

        # Check if the user is premium
        print("user:", user)
        print("user.role:", user.role)
        if not (user.role.code_name == "premium" or user.role.code_name == "su"):
            return Response(
                {"error": "Only premium users can reserve spots"},
                status=status.HTTP_403_FORBIDDEN,
            )
        if spot.is_occupied:
            return Response(
                {"error": "Spot is already occupied"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        reservation = Reservation(
            user=user, spot=spot, start_time=start_time, end_time=end_time
        )
        reservation.save()

        spot.is_occupied = True
        spot.save()

        return Response(
            {"message": f"Spot {spot.spot_id} reserved for {user.name}"},
            status=status.HTTP_201_CREATED,
        )
