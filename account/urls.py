from django.urls import path, include
from .views import UserRegisterView, UserUpdateView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


app_name = 'account'

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', UserRegisterView.as_view(), name='user-register'),
    path('api/update/<int:pk>', UserUpdateView.as_view(), name='user-update'),
]
