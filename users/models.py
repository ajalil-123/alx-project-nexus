from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

"""
Custom User model extending Django's AbstractUser.
We add extra fields if needed (e.g., phone, address).
"""

class User(AbstractUser):
    # Example extra field
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username
