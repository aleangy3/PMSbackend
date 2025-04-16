from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.decorator import route_permissions
from api.models import Logs, Role
from api.paginations import CustomPagination
from api.serializers import RoleSerializer
from django_filters.rest_framework import DjangoFilterBackend

from api.filters import RoleFilter


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.exclude(code_name="su").order_by("id")
    serializer_class = RoleSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RoleFilter

    @route_permissions(["read_role"])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @route_permissions(["create_role"])
    def create(self, request, *args, **kwargs):
        Logs.objects.create(text="Role created", created_by=request.user)
        return super().create(request, *args, **kwargs)

    @route_permissions(["read_role"])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @route_permissions(["update_role"])
    def update(self, request, *args, **kwargs):
        Logs.objects.create(text="Role updated", created_by=request.user)
        return super().update(request, *args, **kwargs)

    @route_permissions(["update_role"])
    def partial_update(self, request, *args, **kwargs):
        Logs.objects.create(text="Role updated", created_by=request.user)
        return super().partial_update(request, *args, **kwargs)

    @route_permissions(["delete_role"])
    def destroy(self, request, *args, **kwargs):
        Logs.objects.create(text="Role deleted", created_by=request.user)
        return super().destroy(request, *args, **kwargs)
