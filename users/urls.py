
from django.urls import path
from .views import UserListCreateView

"""
App-specific routes for user management.
"""

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user-list-create'),
]