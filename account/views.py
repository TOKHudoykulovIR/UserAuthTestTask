from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Comment
from .serializers import UserCreateSerializer, UserUpdateSerializer
from rest_framework import generics, status
from rest_framework import permissions

UserModel = get_user_model()


class UserRegisterView(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    permission_classes = [permissions.AllowAny, ]  # also available for anon users
    serializer_class = UserCreateSerializer


class UserUpdateView(generics.UpdateAPIView):
    queryset = UserModel.objects.all()
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UserUpdateSerializer

