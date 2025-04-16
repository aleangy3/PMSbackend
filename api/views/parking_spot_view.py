from django_filters import rest_framework as filters
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from api.filters import ParkingSpotFilter
from api.models import ParkingSpot
from api.serializers import ParkingSpotSerializer


class ParkingSpotViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    # permission_classes = (IsAuthenticated, )
    queryset = ParkingSpot.objects.order_by("id")
    serializer_class = ParkingSpotSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ParkingSpotFilter

    # @route_permissions(['read_role'])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    # @route_permissions(['create_role'])
    def create(self, request, *args, **kwargs):
        # Logs.objects.create(text='Role created', created_by=request.user)
        return super().create(request, *args, **kwargs)

    # @route_permissions(['read_role'])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    # @route_permissions(['update_role'])
    def update(self, request, *args, **kwargs):
        # Logs.objects.create(text='Role updated', created_by=request.user)
        return super().update(request, *args, **kwargs)

    # @route_permissions(['update_role'])
    def partial_update(self, request, *args, **kwargs):
        # Logs.objects.create(text='Role updated', created_by=request.user)
        return super().partial_update(request, *args, **kwargs)

    # @route_permissions(['delete_role'])
    def destroy(self, request, *args, **kwargs):
        # Logs.objects.create(text='Role deleted', created_by=request.user)
        return super().destroy(request, *args, **kwargs)
