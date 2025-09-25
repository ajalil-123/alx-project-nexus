
from django.urls import path
from .views import UserListCreateView
from .views import RegisterView, LoginView
from rest_framework_simplejwt.views import TokenRefreshView

"""
App-specific routes for user management.
"""

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user-list-create'),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]