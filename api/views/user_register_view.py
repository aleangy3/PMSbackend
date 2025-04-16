from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from api.models import User
from api.serializers import UserRegistrationSerializer

class UserRegistrationViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]
    http_method_names = ['post']

    def perform_create(self, serializer):
        last_user = User.objects.order_by('-id').first()
        new_id = (last_user.id + 1) if last_user else 1
        serializer.save(id=new_id)