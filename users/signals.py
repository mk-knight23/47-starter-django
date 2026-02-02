"""
Signals for users app.

Automatically creates UserProfile when User is created.
"""
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, UserProfile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Create UserProfile automatically when User is created.

    This ensures every user has an associated profile.
    """
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Save UserProfile when User is saved.

    This ensures the profile stays in sync with the user.
    """
    if hasattr(instance, 'profile'):
        instance.profile.save()
