from django.contrib.auth import get_user_model
from django.http import Http404
from rest_framework.generics import get_object_or_404, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Comment
from .serializers import UserCreateSerializer, UserUpdateSerializer, CommentSerializer
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


class CommentList(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request, format=None):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CommentSerializer(
            data={
                'text': request.data["text"],
                'to': request.data['to'],
                'author': request.user.id
            }
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentsByUser(generics.ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        user_id = self.kwargs['id']
        get_object_or_404(UserModel, id=user_id)
        comments = Comment.objects.filter(to=user_id)
        return comments
