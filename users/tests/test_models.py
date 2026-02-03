"""
Tests for User models.
"""
import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
class TestUserModel:
    """Test User model functionality."""

    def test_create_user(self):
        """Test creating a standard user."""
        user = User.objects.create_user(
            email='test@example.com',
            password='testpass123',
        )
        assert user.email == 'test@example.com'
        assert user.role == User.Role.USER
        assert user.check_password('testpass123')
        assert not user.is_staff
        assert not user.is_superuser

    def test_create_user_with_role(self):
        """Test creating a user with specific role."""
        user = User.objects.create_user(
            email='staff@example.com',
            password='testpass123',
            role=User.Role.STAFF,
        )
        assert user.role == User.Role.STAFF

    def test_create_superuser(self):
        """Test creating a superuser."""
        user = User.objects.create_superuser(
            email='admin@example.com',
            password='adminpass123',
        )
        assert user.email == 'admin@example.com'
        assert user.is_staff
        assert user.is_superuser
        assert user.role == User.Role.ADMIN

    def test_user_email_normalized(self):
        """Test email is normalized."""
        email = 'test@EXAMPLE.COM'
        user = User.objects.create_user(
            email=email,
            password='testpass123',
        )
        assert user.email == email.lower()

    def test_user_str_representation(self):
        """Test string representation of user."""
        user = User.objects.create_user(
            email='test@example.com',
            password='testpass123',
        )
        assert str(user) == 'test@example.com'

    def test_get_full_name(self):
        """Test get_full_name method."""
        user = User.objects.create_user(
            email='test@example.com',
            password='testpass123',
            first_name='John',
            last_name='Doe',
        )
        assert user.get_full_name() == 'John Doe'

    def test_get_full_name_without_names(self):
        """Test get_full_name returns email when names are missing."""
        user = User.objects.create_user(
            email='test@example.com',
            password='testpass123',
        )
        assert user.get_full_name() == 'test@example.com'

    def test_get_short_name(self):
        """Test get_short_name method."""
        user = User.objects.create_user(
            email='test@example.com',
            password='testpass123',
            first_name='John',
        )
        assert user.get_short_name() == 'John'

    def test_has_role_method(self):
        """Test has_role method."""
        user = User.objects.create_user(
            email='test@example.com',
            password='testpass123',
            role=User.Role.USER,
        )
        assert user.has_role(User.Role.USER)
        assert not user.has_role(User.Role.ADMIN)

    def test_is_staff_user_property(self):
        """Test is_staff_user property."""
        user = User.objects.create_user(
            email='test@example.com',
            password='testpass123',
            role=User.Role.STAFF,
            is_staff=True,
        )
        assert user.is_staff_user

    def test_is_admin_user_property(self):
        """Test is_admin_user property."""
        user = User.objects.create_user(
            email='admin@example.com',
            password='testpass123',
            role=User.Role.ADMIN,
        )
        assert user.is_admin_user


@pytest.mark.django_db
class TestUserProfile:
    """Test UserProfile model functionality."""

    def test_create_user_profile(self, regular_user):
        """Test creating a user profile."""
        from users.models import UserProfile

        profile = UserProfile.objects.create(
            user=regular_user,
            city='New York',
            country='USA',
        )
        assert profile.user == regular_user
        assert profile.city == 'New York'
        assert profile.country == 'USA'

    def test_profile_str_representation(self, regular_user):
        """Test string representation of profile."""
        from users.models import UserProfile

        profile = UserProfile.objects.create(
            user=regular_user,
        )
        assert str(profile) == f"{regular_user.email}'s profile"
