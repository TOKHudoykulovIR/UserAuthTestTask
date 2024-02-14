from django.urls import path, include
from .views import UserRegisterView, UserUpdateView, CommentList, CommentsByUser
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'account'

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('accounts/register/', UserRegisterView.as_view(), name='user-register'),
    path('accounts/<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),

    path('comments/', CommentList.as_view(), name='comments'),
    path('accounts/<int:id>/received_comments/', CommentsByUser.as_view(), name='author-received-comments'),
]
