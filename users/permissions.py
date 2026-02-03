"""
Custom permissions for User app.
"""
from rest_framework import permissions
from users.models import User


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

        # Check if object has an author field
        if hasattr(obj, 'author'):
            return obj.author == request.user

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


class IsAdminUser(permissions.BasePermission):
    """
    Permission to only allow admin users.

    Checks for both Django's is_superuser and custom ADMIN role.
    """

    def has_permission(self, request, view):
        """Check if user is admin."""
        return request.user and request.user.is_authenticated and request.user.is_admin_user


class IsStaffUser(permissions.BasePermission):
    """
    Permission to only allow staff users.

    Checks for both Django's is_staff and custom STAFF role.
    """

    def has_permission(self, request, view):
        """Check if user is staff."""
        return request.user and request.user.is_authenticated and request.user.is_staff_user


class IsAuthorOrStaff(permissions.BasePermission):
    """
    Permission to only allow authors of an object or staff to edit it.

    Similar to IsOwnerOrStaff but specifically for content with 'author' field.
    Used for blog posts, comments, etc.
    """

    def has_object_permission(self, request, view, obj):
        """Check if user has permission to access the object."""
        # Staff can edit any object
        if request.user.is_staff or request.user.is_superuser:
            return True

        # Authors can edit their own objects
        if hasattr(obj, 'author'):
            return obj.author == request.user

        # Check if object has a user field
        if hasattr(obj, 'user'):
            return obj.user == request.user

        # Default: deny access
        return False


class IsVerifiedUser(permissions.BasePermission):
    """
    Permission to only allow verified users.

    Checks if user's email is verified.
    """

    def has_permission(self, request, view):
        """Check if user is verified."""
        return (
            request.user
            and request.user.is_authenticated
            and request.user.email_verified
        )


class ReadOnly(permissions.BasePermission):
    """
    Permission to only allow read-only access.

    Allows GET, HEAD, and OPTIONS requests.
    """

    def has_permission(self, request, view):
        """Check if request is read-only."""
        return request.method in permissions.SAFE_METHODS


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Permission to allow admin users full access, others read-only.

    Rules:
    - Admin users: full access
    - Other users: read-only
    """

    def has_permission(self, request, view):
        """Check if user has permission."""
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated and request.user.is_admin_user


class IsStaffOrReadOnly(permissions.BasePermission):
    """
    Permission to allow staff users full access, others read-only.

    Rules:
    - Staff users: full access
    - Other users: read-only
    """

    def has_permission(self, request, view):
        """Check if user has permission."""
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated and request.user.is_staff_user


class CanCreatePost(permissions.BasePermission):
    """
    Permission to create posts.

    Rules:
    - Staff and Admin users can create posts
    - Regular users can create posts (if verified)
    """

    def has_permission(self, request, view):
        """Check if user can create posts."""
        if not request.user or not request.user.is_authenticated:
            return False

        # Staff and admin can always create
        if request.user.is_staff_user:
            return True

        # Regular users must be verified
        return request.user.email_verified


class CanModerateComment(permissions.BasePermission):
    """
    Permission to moderate comments.

    Only staff users can moderate comments.
    """

    def has_permission(self, request, view):
        """Check if user can moderate."""
        return request.user and request.user.is_authenticated and request.user.is_staff_user


class DenyUnverified(permissions.BasePermission):
    """
    Deny access to unverified users.

    Used for sensitive operations.
    """

    def has_permission(self, request, view):
        """Check if user is verified."""
        if not request.user or not request.user.is_authenticated:
            return False
        return request.user.email_verified or request.user.is_staff_user

