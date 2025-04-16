from django.contrib.auth.backends import BaseBackend

from api.models import User


class PasswordLessAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            if username == "superuser":
                return None
            pk = kwargs.get("pk", None)
            if pk is None:
                users = User.objects.filter(
                    username=username, role__isnull=False, profile_status="Current"
                ).all()
                if len(users) == 0:
                    return None
                return users[0]
            else:
                return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return None
