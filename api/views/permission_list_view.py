from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from api.models import Permission
from api.serializers import PermissionSerializer


class PermissionListView(ListAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = (IsAuthenticated,)
