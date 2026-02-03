"""
Tests for User API endpoints.
"""
import pytest
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
class TestAuthenticationAPI:
    """Test authentication endpoints."""

    def test_login(self, api_client, regular_user):
        """Test user login."""
        url = reverse('rest_login')
        data = {
            'email': 'user@example.com',
            'password': 'testpass123',
        }
        response = api_client.post(url, data)
        assert response.status_code == status.HTTP_200_OK
        assert 'access' in response.data
        assert 'refresh' in response.data

    def test_login_invalid_credentials(self, api_client, regular_user):
        """Test login with invalid credentials."""
        url = reverse('rest_login')
        data = {
            'email': 'user@example.com',
            'password': 'wrongpass',
        }
        response = api_client.post(url, data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_logout(self, authenticated_client):
        """Test user logout."""
        url = reverse('rest_logout')
        response = authenticated_client.post(url)
        assert response.status_code == status.HTTP_200_OK

    def test_token_refresh(self, api_client, regular_user):
        """Test refreshing access token."""
        from rest_framework_simplejwt.tokens import RefreshToken

        refresh = RefreshToken.for_user(regular_user)
        url = reverse('token_refresh')
        data = {
            'refresh': str(refresh),
        }
        response = api_client.post(url, data)
        assert response.status_code == status.HTTP_200_OK
        assert 'access' in response.data


@pytest.mark.django_db
class TestUserAPI:
    """Test User management endpoints."""

    def test_list_users_unauthenticated(self, api_client):
        """Test that unauthenticated users cannot list users."""
        url = reverse('user-list')
        response = api_client.get(url)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_list_users_authenticated(self, authenticated_client, regular_user):
        """Test listing users as authenticated user."""
        url = reverse('user-list')
        response = authenticated_client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_retrieve_user(self, api_client, regular_user):
        """Test retrieving a user."""
        url = reverse('user-detail', kwargs={'pk': regular_user.id})
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['email'] == regular_user.email

    def test_retrieve_own_profile(self, authenticated_client, regular_user):
        """Test retrieving own profile."""
        url = reverse('user-me')
        response = authenticated_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['email'] == regular_user.email

    def test_update_own_profile(self, authenticated_client, regular_user):
        """Test updating own profile."""
        url = reverse('user-me')
        data = {
            'first_name': 'Updated',
        }
        response = authenticated_client.patch(url, data)
        assert response.status_code == status.HTTP_200_OK
        regular_user.refresh_from_db()
        assert regular_user.first_name == 'Updated'

    def test_change_password(self, authenticated_client):
        """Test changing password."""
        url = reverse('rest_password_change')
        data = {
            'new_password1': 'newpass123',
            'new_password2': 'newpass123',
        }
        response = authenticated_client.post(url, data)
        assert response.status_code == status.HTTP_200_OK

    def test_change_password_mismatch(self, authenticated_client):
        """Test changing password with mismatched confirmation."""
        url = reverse('rest_password_change')
        data = {
            'new_password1': 'newpass123',
            'new_password2': 'different',
        }
        response = authenticated_client.post(url, data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_filter_users_by_role(self, admin_client, regular_user, staff_user):
        """Test filtering users by role."""
        url = reverse('user-list')
        response = admin_client.get(url, {'role': 'USER'})
        assert response.status_code == status.HTTP_200_OK
        # At least the regular user should be in results
        user_ids = [u['id'] for u in response.data['results']]
        assert regular_user.id in user_ids
