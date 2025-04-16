import os

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import UserSerializer
from api.util import combine_role_permissions


class LoggedInUser(APIView):

    authentication_classes = ()
    permission_classes = (AllowAny,)

    def get(self, request):
        try:
            name = os.getlogin()
        except Exception as e:
            name = ""
        return Response({"username": name}, status=status.HTTP_200_OK)
