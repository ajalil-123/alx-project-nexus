from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import User
from .serializers import UserSerializer

"""
View for listing and creating users.
Later we’ll add JWT authentication for login/register.
"""

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
