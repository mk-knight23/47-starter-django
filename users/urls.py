"""
URL configuration for users app.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from .views import UserViewSet, UserProfileViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'profiles', UserProfileViewSet, basename='userprofile')

urlpatterns = [
    # Router URLs
    path('', include(router.urls)),

    # Token authentication
    path('token/', obtain_auth_token, name='api_token_auth'),
]
