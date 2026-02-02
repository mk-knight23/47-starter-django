"""
API views for User model.
"""
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import User, UserProfile
from .serializers import (
    UserSerializer,
    UserCreateSerializer,
    UserUpdateSerializer,
    UserProfileSerializer,
)
from .permissions import IsOwnerOrStaff


class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for User model.

    Provides:
    - list: List all users (staff only)
    - retrieve: Get user by ID
    - create: Create new user (public)
    - update: Update user (owner or staff)
    - partial_update: Partially update user (owner or staff)
    - destroy: Delete user (owner or staff)
    - me: Get current user profile
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        """Get appropriate serializer based on action."""
        if self.action == 'create':
            return UserCreateSerializer
        if self.action in ['update', 'partial_update']:
            return UserUpdateSerializer
        return UserSerializer

    def get_permissions(self):
        """Get permissions based on action."""
        if self.action == 'create':
            return [permissions.AllowAny()]
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsOwnerOrStaff()]
        if self.action == 'list':
            return [permissions.IsAdminUser()]
        return super().get_permissions()

    def get_queryset(self):
        """Filter queryset based on user role."""
        user = self.request.user
        if user.is_admin_user:
            return User.objects.all()
        return User.objects.filter(id=user.id)

    @action(detail=False, methods=['get', 'put', 'patch'])
    def me(self, request):
        """
        Get or update current user's profile.

        GET /api/users/me/ - Get current user
        PUT /api/users/me/ - Update current user
        PATCH /api/users/me/ - Partially update current user
        """
        user = request.user

        if request.method == 'GET':
            serializer = UserSerializer(user)
            return Response(serializer.data)

        elif request.method in ['PUT', 'PATCH']:
            serializer = UserUpdateSerializer(user, data=request.data, partial=request.method == 'PATCH')
            if serializer.is_valid():
                serializer.save()
                return Response(UserSerializer(user).data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileViewSet(viewsets.ModelViewSet):
    """
    ViewSet for UserProfile model.

    Provides full CRUD operations for user profiles.
    """

    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrStaff]

    def get_queryset(self):
        """Get profiles for current user or all if admin."""
        user = self.request.user
        if user.is_admin_user:
            return UserProfile.objects.all()
        return UserProfile.objects.filter(user=user)

    def perform_create(self, serializer):
        """Associate profile with current user."""
        serializer.save(user=self.request.user)
