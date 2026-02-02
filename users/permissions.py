"""
Custom permissions for User app.
"""
from rest_framework import permissions


class IsOwnerOrStaff(permissions.BasePermission):
    """
    Permission to only allow owners of an object or staff to edit it.

    Rules:
    - Admin users can access any object
    - Staff users can access any object
    - Regular users can only access their own objects
    """

    def has_object_permission(self, request, view, obj):
        """Check if user has permission to access the object."""
        # Admin and staff can access any object
        if request.user.is_staff or request.user.is_superuser:
            return True

        # Check if object has a user field (direct relationship)
        if hasattr(obj, 'user'):
            return obj.user == request.user

        # Check if object is the user itself
        if hasattr(obj, 'email'):  # User model
            return obj == request.user

        # Default: deny access
        return False


class IsRole(permissions.BasePermission):
    """
    Permission to only allow users with specific roles.

    Usage:
    permission_classes = [IsRole('ADMIN', 'STAFF')]
    """

    def __init__(self, *allowed_roles):
        """Initialize with allowed roles."""
        self.allowed_roles = allowed_roles

    def has_permission(self, request, view):
        """Check if user has one of the allowed roles."""
        if not request.user or not request.user.is_authenticated:
            return False
        return request.user.has_role(*self.allowed_roles)
