"""
Tests for Blog API endpoints.
"""
import pytest
from django.urls import reverse
from rest_framework import status
from apps.blog.models import Category, Tag, Post, Comment


@pytest.mark.django_db
class TestCategoryAPI:
    """Test Category API endpoints."""

    def test_list_categories(self, api_client, category):
        """Test listing all categories."""
        url = reverse('blog:category-list')
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data['results']) >= 1

    def test_retrieve_category(self, api_client, category):
        """Test retrieving a single category."""
        url = reverse('blog:category-detail', kwargs={'slug': category.slug})
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['slug'] == category.slug

    def test_category_posts(self, api_client, category, post):
        """Test getting posts for a category."""
        url = reverse('blog:category-posts', kwargs={'slug': category.slug})
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
class TestTagAPI:
    """Test Tag API endpoints."""

    def test_list_tags(self, api_client, tag):
        """Test listing all tags."""
        url = reverse('blog:tag-list')
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data['results']) >= 1

    def test_retrieve_tag(self, api_client, tag):
        """Test retrieving a single tag."""
        url = reverse('blog:tag-detail', kwargs={'slug': tag.slug})
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['slug'] == tag.slug

    def test_tag_posts(self, api_client, tag, post):
        """Test getting posts with a tag."""
        url = reverse('blog:tag-posts', kwargs={'slug': tag.slug})
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
class TestPostAPI:
    """Test Post API endpoints."""

    def test_list_posts_unauthenticated(self, api_client, post):
        """Test listing posts as unauthenticated user."""
        url = reverse('blog:post-list')
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_list_posts_authenticated(self, authenticated_client, post):
        """Test listing posts as authenticated user."""
        url = reverse('blog:post-list')
        response = authenticated_client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_list_draft_posts_unauthenticated(self, api_client, draft_post):
        """Test that unauthenticated users cannot see draft posts."""
        url = reverse('blog:post-list')
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        # Draft post should not be in results
        post_ids = [p['slug'] for p in response.data['results']]
        assert draft_post.slug not in post_ids

    def test_list_draft_posts_staff(self, staff_client, draft_post):
        """Test that staff users can see draft posts."""
        url = reverse('blog:post-list')
        response = staff_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        # Draft post should be in results
        post_ids = [p['slug'] for p in response.data['results']]
        assert draft_post.slug in post_ids

    def test_retrieve_post(self, api_client, post):
        """Test retrieving a single post."""
        url = reverse('blog:post-detail', kwargs={'slug': post.slug})
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['slug'] == post.slug
        # View count should be incremented
        post.refresh_from_db()
        assert post.view_count == 1

    def test_create_post_unauthenticated(self, api_client):
        """Test that unauthenticated users cannot create posts."""
        url = reverse('blog:post-list')
        data = {
            'title': 'New Post',
            'slug': 'new-post',
            'content': 'New content',
        }
        response = api_client.post(url, data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_create_post_authenticated(self, authenticated_client, category):
        """Test creating a post as authenticated user."""
        url = reverse('blog:post-list')
        data = {
            'title': 'New Post',
            'slug': 'new-post',
            'content': 'New content',
            'category': category.id,
        }
        response = authenticated_client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert Post.objects.filter(slug='new-post').exists()

    def test_update_post_by_author(self, authenticated_client, post):
        """Test updating a post by the author."""
        url = reverse('blog:post-detail', kwargs={'slug': post.slug})
        data = {
            'title': 'Updated Post',
        }
        response = authenticated_client.patch(url, data)
        assert response.status_code == status.HTTP_200_OK
        post.refresh_from_db()
        assert post.title == 'Updated Post'

    def test_update_post_by_other_user(self, authenticated_client, draft_post):
        """Test that non-authors cannot update posts."""
        url = reverse('blog:post-detail', kwargs={'slug': draft_post.slug})
        data = {
            'title': 'Updated Post',
        }
        response = authenticated_client.patch(url, data)
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_delete_post_by_author(self, authenticated_client, post):
        """Test deleting a post by the author."""
        url = reverse('blog:post-detail', kwargs={'slug': post.slug})
        response = authenticated_client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not Post.objects.filter(slug=post.slug).exists()

    def test_filter_posts_by_status(self, staff_client, post, draft_post):
        """Test filtering posts by status."""
        url = reverse('blog:post-list')
        response = staff_client.get(url, {'status': 'PUBLISHED'})
        assert response.status_code == status.HTTP_200_OK
        post_ids = [p['slug'] for p in response.data['results']]
        assert post.slug in post_ids
        assert draft_post.slug not in post_ids

    def test_search_posts(self, api_client, post):
        """Test searching posts."""
        url = reverse('blog:post-list')
        response = api_client.get(url, {'search': 'Test'})
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data['results']) >= 1


@pytest.mark.django_db
class TestCommentAPI:
    """Test Comment API endpoints."""

    def test_list_comments(self, api_client, comment):
        """Test listing comments."""
        url = reverse('blog:comment-list')
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_create_comment_unauthenticated(self, api_client, post):
        """Test that unauthenticated users cannot create comments."""
        url = reverse('blog:comment-list')
        data = {
            'post': post.id,
            'content': 'New comment',
        }
        response = api_client.post(url, data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_create_comment_authenticated(self, authenticated_client, post):
        """Test creating a comment as authenticated user."""
        url = reverse('blog:comment-list')
        data = {
            'post': post.id,
            'content': 'New comment',
        }
        response = authenticated_client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert Comment.objects.filter(content='New comment').exists()

    def test_create_reply_to_comment(self, authenticated_client, comment):
        """Test creating a reply to a comment."""
        url = reverse('blog:comment-list')
        data = {
            'post': comment.post.id,
            'content': 'Reply to comment',
            'parent': comment.id,
        }
        response = authenticated_client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_update_comment_by_author(self, authenticated_client, comment):
        """Test updating a comment by the author."""
        url = reverse('blog:comment-detail', kwargs={'pk': comment.id})
        data = {
            'content': 'Updated comment',
        }
        response = authenticated_client.patch(url, data)
        assert response.status_code == status.HTTP_200_OK
        comment.refresh_from_db()
        assert comment.content == 'Updated comment'
