from django.contrib.auth import authenticate
from django.middleware import csrf
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import User
from api.serializers import UserSerializer
from api.util import (combine_role_permissions, get_tokens_for_user,
                      set_access_cookies, set_refresh_cookies)


class LoginView(APIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)

    def post(self, request):
        data = request.data
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return Response({"msg": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                user = authenticate(username=username, password=password)  # Still use authenticate for session
                if user is not None:
                    response = Response()
                    token = get_tokens_for_user(user)
                    set_access_cookies(response, token["access"])
                    set_refresh_cookies(response, token["refresh"])
                    csrf.get_token(request)

                    data = UserSerializer(user, context={"request": request}).data
                    data["permissions"] = combine_role_permissions(user.role)

                    response.status_code = status.HTTP_200_OK
                    response.data = {"msg": "Login successfully", "user": data}
                    return response

            else:
                return Response({"msg": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({"msg": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        # user = authenticate(username=username, password=password)
        # if user is not None:
        #     response = Response()
        #     token = get_tokens_for_user(user)
        #     set_access_cookies(response, token["access"])
        #     set_refresh_cookies(response, token["refresh"])
        #     csrf.get_token(request)

        #     data = UserSerializer(user, context={"request": request}).data
        #     data["permissions"] = combine_role_permissions(user.role)

        #     response.status_code = status.HTTP_200_OK
        #     response.data = {"msg": "Login successfully", "user": data}
        #     return response

        # return Response(
        #     {"msg": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST
        # )
