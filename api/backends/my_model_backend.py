from django.contrib.auth.backends import ModelBackend

from api.models import User


class MyModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username != "superuser":
            return None

        if username is None:
            username = kwargs.get(User.USERNAME_FIELD)
        if username is None or password is None:
            return

        try:
            user = User._default_manager.get_by_natural_key(username)
        except User.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        else:
            return None
