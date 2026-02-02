"""
Admin configuration for User model.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User, UserProfile


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Custom admin for User model."""

    list_display = [
        'email',
        'first_name',
        'last_name',
        'role',
        'is_staff',
        'is_active',
        'email_verified',
        'date_joined',
    ]
    list_filter = ['role', 'is_staff', 'is_active', 'email_verified', 'date_joined']
    search_fields = ['email', 'first_name', 'last_name']
    ordering = ['-date_joined']

    # Fieldsets for detail view
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {
            'fields': (
                'first_name',
                'last_name',
                'phone',
                'avatar',
                'bio',
            )
        }),
        (_('Role & Permissions'), {
            'fields': (
                'role',
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            ),
        }),
        (_('Important Dates'), {'fields': ('last_login', 'date_joined', 'updated_at', 'last_seen')}),
        (_('Verification'), {'fields': ('email_verified',)}),
        (_('Settings'), {'fields': ('language', 'timezone')}),
    )

    # Fieldsets for add user form
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'role',
                'is_staff',
                'is_active',
            ),
        }),
    )

    readonly_fields = ['date_joined', 'updated_at', 'last_login']


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """Admin for UserProfile model."""

    list_display = ['user', 'city', 'country', 'newsletter', 'notification_email']
    list_filter = ['newsletter', 'notification_email', 'notification_sms', 'country']
    search_fields = ['user__email', 'city', 'address_line1']
    readonly_fields = ['user']

    fieldsets = (
        (_('User'), {'fields': ('user',)}),
        (_('Address'), {
            'fields': (
                'address_line1',
                'address_line2',
                'city',
                'state',
                'postal_code',
                'country',
            )
        }),
        (_('Social Links'), {
            'fields': ('website', 'linkedin', 'github', 'twitter')
        }),
        (_('Preferences'), {
            'fields': (
                'notification_email',
                'notification_sms',
                'newsletter',
            )
        }),
        (_('Additional Info'), {'fields': ('birth_date',)}),
    )
