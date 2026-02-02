"""
Django Admin customization and configuration.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Admin site configuration
admin.site.site_header = 'Django Starter Admin'
admin.site.site_title = 'Django Starter Admin Portal'
admin.site.index_title = 'Welcome to Django Starter Administration'

# Register all models
from users.admin import UserAdmin, UserProfileAdmin
from users.models import User, UserProfile

admin.site.register(User, UserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)

# Unregister default Django models we don't use
from django.contrib.auth.models import Group
try:
    admin.site.unregister(Group)
except admin.sites.NotRegistered:
    pass
