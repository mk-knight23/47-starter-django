"""
Custom permissions for blog app.
"""
from rest_framework import permissions


class IsAuthorOrStaff(permissions.BasePermission):
    """
    Permission to only allow authors of an object or staff to edit it.

    Rules:
    - Admin users can access any object
    - Staff users can access any object
    - Authors can only access their own objects
    """

    def has_object_permission(self, request, view, obj):
        """Check if user has permission to access the object."""
        # Admin and staff can access any object
        if request.user.is_staff or request.user.is_superuser:
            return True

        # Check if object has an author field
        if hasattr(obj, 'author'):
            return obj.author == request.user

        # Default: deny access
        return False
