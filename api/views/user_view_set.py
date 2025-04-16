from django_filters import rest_framework as filters
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from api.decorator import route_permissions
from api.filters import UserFilter
from api.models import Logs, User
from api.paginations import CustomPagination
from api.serializers import UserSerializer


class UserViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = User.objects.exclude(role__code_name="su")
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = UserFilter

    @route_permissions(["read_user"])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @route_permissions(["read_user"])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @route_permissions(["update_user"])
    def update(self, request, *args, **kwargs):

        Logs.objects.create(text="User updated", created_by=request.user)
        return super().update(request, *args, **kwargs)

    @route_permissions(["update_user"])
    def partial_update(self, request, *args, **kwargs):
        Logs.objects.create(text="User updated", created_by=request.user)
        return super().partial_update(request, *args, **kwargs)
