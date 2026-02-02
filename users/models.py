"""
Custom User model with email-based authentication and role-based access.
"""
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Custom User model with email as the primary identifier.

    Features:
    - Email-based authentication (username is None)
    - Role-based access control (USER, STAFF, ADMIN)
    - Enhanced profile fields
    """

    class Role(models.TextChoices):
        """User roles for access control."""
        USER = 'USER', _('User')
        STAFF = 'STAFF', _('Staff')
        ADMIN = 'ADMIN', _('Admin')

    # Remove username field, use email instead
    username = None  # type: ignore[assignment]
    email = models.EmailField(
        _('email address'),
        unique=True,
        db_index=True,
        help_text=_('Required. A valid email address.'),
    )

    # Personal Information
    first_name = models.CharField(_('first name'), max_length=150, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    phone = models.CharField(_('phone number'), max_length=20, blank=True)
    avatar = models.ImageField(_('avatar'), upload_to='avatars/', blank=True, null=True)
    bio = models.TextField(_('bio'), blank=True)

    # Role and Permissions
    role = models.CharField(
        _('role'),
        max_length=10,
        choices=Role.choices,
        default=Role.USER,
        help_text=_('Designates the user role for access control.'),
    )

    # Timestamps
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)
    last_seen = models.DateTimeField(_('last seen'), blank=True, null=True)

    # Email verification
    email_verified = models.BooleanField(_('email verified'), default=False)

    # User settings
    language = models.CharField(_('language'), max_length=10, default='en')
    timezone = models.CharField(_('timezone'), max_length=50, default='UTC')

    objects = models.Manager()  # Default manager

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Email & Password are required by default

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ['-date_joined']
        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['role']),
            models.Index(fields=['date_joined']),
        ]

    def __str__(self):
        """Return string representation of user."""
        return self.email

    def get_full_name(self):
        """Return the user's full name."""
        full_name = f'{self.first_name} {self.last_name}'.strip()
        return full_name if full_name else self.email

    def get_short_name(self):
        """Return the user's short name (first name)."""
        return self.first_name or self.email.split('@')[0]

    @property
    def is_staff_user(self):
        """Check if user has staff role."""
        return self.role == self.Role.STAFF or self.is_staff

    @property
    def is_admin_user(self):
        """Check if user has admin role."""
        return self.role == self.Role.ADMIN or self.is_superuser

    def has_role(self, *roles):
        """
        Check if user has any of the specified roles.

        Args:
            *roles: One or more Role values to check

        Returns:
            bool: True if user has any of the specified roles
        """
        return self.role in roles


class UserProfile(models.Model):
    """
    Extended user profile with additional information.

    This model extends the User model with additional fields
    while keeping the User model clean and focused on authentication.
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
        verbose_name=_('user'),
    )

    # Address
    address_line1 = models.CharField(_('address line 1'), max_length=255, blank=True)
    address_line2 = models.CharField(_('address line 2'), max_length=255, blank=True)
    city = models.CharField(_('city'), max_length=100, blank=True)
    state = models.CharField(_('state'), max_length=100, blank=True)
    postal_code = models.CharField(_('postal code'), max_length=20, blank=True)
    country = models.CharField(_('country'), max_length=100, blank=True)

    # Social Links
    website = models.URLField(_('website'), blank=True)
    linkedin = models.URLField(_('LinkedIn'), blank=True)
    github = models.URLField(_('GitHub'), blank=True)
    twitter = models.URLField(_('Twitter'), blank=True)

    # Preferences
    notification_email = models.BooleanField(_('email notifications'), default=True)
    notification_sms = models.BooleanField(_('SMS notifications'), default=False)
    newsletter = models.BooleanField(_('newsletter'), default=False)

    # Timestamps
    birth_date = models.DateField(_('birth date'), blank=True, null=True)

    class Meta:
        verbose_name = _('user profile')
        verbose_name_plural = _('user profiles')

    def __str__(self):
        """Return string representation of profile."""
        return f"{self.user.email}'s profile"
