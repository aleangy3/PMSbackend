from rest_framework.exceptions import PermissionDenied

from api.models import Role


def route_permissions(permissions):
    def decorator(drf_custom_method):
        def _decorator(self, *args, **kwargs):
            if Role.objects.filter(
                pk=self.request.user.role.pk, permissions__code_name__in=permissions
            ).exists():
                return drf_custom_method(self, *args, **kwargs)
            else:
                raise PermissionDenied()

        return _decorator

    return decorator
