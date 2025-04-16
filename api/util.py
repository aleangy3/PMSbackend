from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken

from api.models import User


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


def set_access_cookies(response, access_token):
    response.set_cookie(
        key=settings.SIMPLE_JWT["AUTH_ACCESS_COOKIE"],
        value=access_token,
        expires=settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"],
        secure=settings.SIMPLE_JWT["AUTH_COOKIE_SECURE"],
        httponly=settings.SIMPLE_JWT["AUTH_COOKIE_HTTP_ONLY"],
        samesite=settings.SIMPLE_JWT["AUTH_COOKIE_SAMESITE"],
    )


def set_refresh_cookies(response, refresh_token):
    response.set_cookie(
        key=settings.SIMPLE_JWT["AUTH_REFRESH_COOKIE"],
        value=refresh_token,
        expires=settings.SIMPLE_JWT["REFRESH_TOKEN_LIFETIME"],
        secure=settings.SIMPLE_JWT["AUTH_COOKIE_SECURE"],
        httponly=settings.SIMPLE_JWT["AUTH_COOKIE_HTTP_ONLY"],
        samesite=settings.SIMPLE_JWT["AUTH_COOKIE_SAMESITE"],
    )


def unset_cookies(response):
    response.delete_cookie(settings.SIMPLE_JWT["AUTH_ACCESS_COOKIE"])
    response.delete_cookie(settings.SIMPLE_JWT["AUTH_REFRESH_COOKIE"])
    response.delete_cookie(settings.CSRF_COOKIE_NAME)


def combine_role_permissions(role):
    permissions = {}
    print("role", role)

    role_permissions = role.permissions.all()
    for permission in role_permissions:
        permissions[permission.code_name] = True

    return permissions
