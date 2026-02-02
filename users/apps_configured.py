"""
Users app configuration with signals.
"""
from django.apps import AppConfig


class UsersConfig(AppConfig):
    """Configuration for users app with signal registration."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    verbose_name = 'Users'

    def ready(self):
        """Import signals when app is ready."""
        import users.signals  # noqa: F401
