from django_filters import rest_framework as filters
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from api.decorator import route_permissions
from api.filters import UserFilter
from api.models import User
from api.serializers import UserSerializer


class UserListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = User.objects.exclude(role__code_name="su").filter(
        profile_status="Current"
    )
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = UserFilter

    @route_permissions(["user_read"])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
