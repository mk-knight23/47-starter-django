"""
Pytest configuration and fixtures for Django testing.
"""
import pytest
from datetime import datetime, timedelta
from django.utils import timezone
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import get_user_model
from apps.blog.models import Category, Tag, Post, Comment

User = get_user_model()


@pytest.fixture
def api_client():
    """Return an API client instance."""
    return APIClient()


@pytest.fixture
def admin_user(db):
    """Create an admin user for testing."""
    user = User.objects.create_user(
        email='admin@example.com',
        password='testpass123',
        role=User.Role.ADMIN,
        is_staff=True,
        is_superuser=True,
        email_verified=True,
    )
    return user


@pytest.fixture
def staff_user(db):
    """Create a staff user for testing."""
    user = User.objects.create_user(
        email='staff@example.com',
        password='testpass123',
        role=User.Role.STAFF,
        is_staff=True,
        email_verified=True,
    )
    return user


@pytest.fixture
def regular_user(db):
    """Create a regular user for testing."""
    user = User.objects.create_user(
        email='user@example.com',
        password='testpass123',
        role=User.Role.USER,
        email_verified=True,
    )
    return user


@pytest.fixture
def authenticated_client(api_client, regular_user):
    """Return an authenticated API client."""
    refresh = RefreshToken.for_user(regular_user)
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
    return api_client


@pytest.fixture
def admin_client(api_client, admin_user):
    """Return an authenticated admin API client."""
    refresh = RefreshToken.for_user(admin_user)
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
    return api_client


@pytest.fixture
def staff_client(api_client, staff_user):
    """Return an authenticated staff API client."""
    refresh = RefreshToken.for_user(staff_user)
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
    return api_client


@pytest.fixture
def category(db):
    """Create a blog category for testing."""
    return Category.objects.create(
        name='Technology',
        slug='technology',
        description='Technology related posts',
    )


@pytest.fixture
def tag(db):
    """Create a blog tag for testing."""
    return Tag.objects.create(
        name='Python',
        slug='python',
        description='Python programming',
    )


@pytest.fixture
def post(db, regular_user, category, tag):
    """Create a published blog post for testing."""
    post = Post.objects.create(
        title='Test Post',
        slug='test-post',
        excerpt='Test excerpt',
        content='Test content',
        author=regular_user,
        category=category,
        status=Post.Status.PUBLISHED,
        published_at=timezone.now(),
    )
    post.tags.add(tag)
    return post


@pytest.fixture
def draft_post(db, staff_user, category):
    """Create a draft blog post for testing."""
    return Post.objects.create(
        title='Draft Post',
        slug='draft-post',
        excerpt='Draft excerpt',
        content='Draft content',
        author=staff_user,
        category=category,
        status=Post.Status.DRAFT,
    )


@pytest.fixture
def comment(db, post, regular_user):
    """Create an approved comment for testing."""
    return Comment.objects.create(
        post=post,
        author=regular_user,
        content='Test comment',
        status=Comment.Status.APPROVED,
    )


@pytest.fixture
def sample_users(db):
    """Create multiple users for testing pagination and filtering."""
    users = []
    for i in range(5):
        user = User.objects.create_user(
            email=f'user{i}@example.com',
            password='testpass123',
            first_name=f'User',
            last_name=f'{i}',
            role=User.Role.USER,
        )
        users.append(user)
    return users


@pytest.fixture
def sample_posts(db, regular_user, category):
    """Create multiple posts for testing pagination and filtering."""
    posts = []
    for i in range(5):
        post = Post.objects.create(
            title=f'Post {i}',
            slug=f'post-{i}',
            excerpt=f'Excerpt {i}',
            content=f'Content {i}',
            author=regular_user,
            category=category,
            status=Post.Status.PUBLISHED,
            published_at=timezone.now() - timedelta(days=i),
        )
        posts.append(post)
    return posts
