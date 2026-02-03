"""
Tests for Blog models.
"""
import pytest
from django.utils import timezone
from datetime import timedelta
from apps.blog.models import Category, Tag, Post, Comment


@pytest.mark.django_db
class TestCategoryModel:
    """Test Category model functionality."""

    def test_create_category(self):
        """Test creating a category."""
        category = Category.objects.create(
            name='Technology',
            slug='technology',
        )
        assert category.name == 'Technology'
        assert category.slug == 'technology'
        assert category.is_active

    def test_category_parent_child_relationship(self):
        """Test hierarchical categories."""
        parent = Category.objects.create(
            name='Tech',
            slug='tech',
        )
        child = Category.objects.create(
            name='Python',
            slug='python',
            parent=parent,
        )
        assert child.parent == parent
        assert parent.children.count() == 1

    def test_category_str_representation(self):
        """Test string representation."""
        category = Category.objects.create(
            name='Technology',
            slug='technology',
        )
        assert str(category) == 'Technology'


@pytest.mark.django_db
class TestTagModel:
    """Test Tag model functionality."""

    def test_create_tag(self):
        """Test creating a tag."""
        tag = Tag.objects.create(
            name='Python',
            slug='python',
        )
        assert tag.name == 'Python'
        assert tag.slug == 'python'

    def test_tag_str_representation(self):
        """Test string representation."""
        tag = Tag.objects.create(
            name='Python',
            slug='python',
        )
        assert str(tag) == 'Python'


@pytest.mark.django_db
class TestPostModel:
    """Test Post model functionality."""

    def test_create_post(self, regular_user, category):
        """Test creating a post."""
        post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            content='Test content',
            author=regular_user,
            category=category,
        )
        assert post.title == 'Test Post'
        assert post.slug == 'test-post'
        assert post.author == regular_user
        assert post.category == category
        assert post.status == Post.Status.DRAFT

    def test_post_with_tags(self, regular_user, category, tag):
        """Test post with tags."""
        post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            content='Test content',
            author=regular_user,
            category=category,
        )
        post.tags.add(tag)
        assert post.tags.count() == 1
        assert tag in post.tags.all()

    def test_published_post(self, regular_user, category):
        """Test creating a published post."""
        post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            content='Test content',
            author=regular_user,
            category=category,
            status=Post.Status.PUBLISHED,
            published_at=timezone.now(),
        )
        assert post.is_published

    def test_post_increment_view_count(self, regular_user, category):
        """Test incrementing view count."""
        post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            content='Test content',
            author=regular_user,
            category=category,
        )
        initial_count = post.view_count
        post.increment_view_count()
        post.refresh_from_db()
        assert post.view_count == initial_count + 1

    def test_post_str_representation(self, regular_user, category):
        """Test string representation."""
        post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            content='Test content',
            author=regular_user,
            category=category,
        )
        assert str(post) == 'Test Post'


@pytest.mark.django_db
class TestCommentModel:
    """Test Comment model functionality."""

    def test_create_comment(self, post, regular_user):
        """Test creating a comment."""
        comment = Comment.objects.create(
            post=post,
            author=regular_user,
            content='Test comment',
        )
        assert comment.post == post
        assert comment.author == regular_user
        assert comment.content == 'Test comment'
        assert comment.status == Comment.Status.PENDING

    def test_approved_comment(self, post, regular_user):
        """Test approved comment."""
        comment = Comment.objects.create(
            post=post,
            author=regular_user,
            content='Test comment',
            status=Comment.Status.APPROVED,
        )
        assert comment.is_approved

    def test_nested_comments(self, post, regular_user):
        """Test nested comment replies."""
        parent = Comment.objects.create(
            post=post,
            author=regular_user,
            content='Parent comment',
            status=Comment.Status.APPROVED,
        )
        child = Comment.objects.create(
            post=post,
            author=regular_user,
            content='Child comment',
            parent=parent,
        )
        assert child.parent == parent
        assert parent.replies.count() == 1

    def test_comment_str_representation(self, post, regular_user):
        """Test string representation."""
        comment = Comment.objects.create(
            post=post,
            author=regular_user,
            content='Test comment',
        )
        assert str(comment) == f'Comment by {regular_user.email} on {post.title}'
