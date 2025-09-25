from rest_framework import serializers
from .models import User

"""
Serializer converts User model data into JSON and validates input.
"""

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone']
