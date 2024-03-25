from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView
from rest_framework.permissions import IsAuthenticated, AllowAny

from django.contrib.auth import get_user_model

from .serializers import *


__all__ = [
    'SignUpView',
    'LoginView',
    'LogoutView',
    'RefreshTokenView'
]


User = get_user_model()


class SignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = SignUpSerializer


class LoginView(TokenObtainPairView):
    permission_classes = (AllowAny,)


class LogoutView(TokenBlacklistView):
    pass


class RefreshTokenView(TokenRefreshView):
    pass
