from rest_framework import serializers
from .models import User
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


"""
Serializer converts User model data into JSON and validates input.
"""

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone']




User = get_user_model()

"""
Serializer for user registration.
Validates password and creates new user.
"""
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )

    class Meta:
        model = User
        fields = ["id", "username", "email", "phone", "password"]

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            phone=validated_data.get("phone", "")
        )
        user.set_password(validated_data["password"])  # Hash password
        user.save()
        return user


"""
Custom JWT Token serializer to include extra user info in response.
"""
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        # Add extra fields
        data.update({
            "user_id": self.user.id,
            "username": self.user.username,
            "email": self.user.email,
        })
        return data
