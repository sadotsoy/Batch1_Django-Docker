from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .serializer import UserSerializer
from .models import User

class UsersApi(APIView):
    permission_classes = (AllowAny,)

    def post(self, req):
        user=UserSerializer(data=req.data)
        if user.is_valid():
            user.save()
            return Response(user.data,status=status.HTTP_201_CREATED)
        else:
            return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)

