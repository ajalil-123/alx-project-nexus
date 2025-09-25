from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer, CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

"""
View for listing and creating users.
Later we’ll add JWT authentication for login/register.
"""

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

User = get_user_model()

"""
User registration view.
Anyone can register a new account.
"""
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer


"""
Login view using JWT.
Returns access + refresh tokens and user info.
"""
class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer