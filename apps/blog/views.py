"""
API views for blog app.
"""
from rest_framework import viewsets, permissions, filters, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import Category, Tag, Post, Comment
from .serializers import (
    CategorySerializer,
    TagSerializer,
    PostListSerializer,
    PostDetailSerializer,
    PostCreateUpdateSerializer,
    CommentSerializer,
)
from .permissions import IsAuthorOrStaff


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for Category model (read-only).

    Provides:
    - list: List all categories
    - retrieve: Get category by slug
    - posts: Get all posts in category
    """

    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer
    lookup_field = 'slug'
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']

    @action(detail=True, methods=['get'])
    def posts(self, request, slug=None):
        """
        Get all published posts in this category.

        GET /api/blog/categories/{slug}/posts/
        """
        category = self.get_object()
        posts = category.posts.filter(status=Post.Status.PUBLISHED)
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for Tag model (read-only).

    Provides:
    - list: List all tags
    - retrieve: Get tag by slug
    - posts: Get all posts with this tag
    """

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = 'slug'
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']

    @action(detail=True, methods=['get'])
    def posts(self, request, slug=None):
        """
        Get all published posts with this tag.

        GET /api/blog/tags/{slug}/posts/
        """
        tag = self.get_object()
        posts = tag.posts.filter(status=Post.Status.PUBLISHED)
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)


class PostViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Post model.

    Provides:
    - list: List all posts (filtering by status)
    - retrieve: Get post by slug
    - create: Create new post (authenticated users)
    - update: Update post (author or staff)
    - partial_update: Partially update post (author or staff)
    - destroy: Delete post (author or staff)
    - published: List all published posts (public)
    - comments: Get comments for post
    - like: Like/unlike post
    """

    @action(detail=False, methods=['get'])
    def published(self, request):
        """
        Get all published posts (public endpoint).
        Rate limited to 100 requests per minute for anonymous users.
        """
        posts = Post.objects.filter(status=Post.Status.PUBLISHED)
        page = self.paginate_queryset(posts)
        serializer = PostListSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    queryset = Post.objects.all()
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'category', 'tags', 'author']
    search_fields = ['title', 'excerpt', 'content']
    ordering_fields = ['created_at', 'published_at', 'view_count', 'like_count']
    ordering = ['-published_at', '-created_at']

    def get_queryset(self):
        """Filter queryset based on user role."""
        user = self.request.user

        if user.is_authenticated and (user.is_staff or user.is_superuser):
            # Staff can see all posts
            return Post.objects.all()

        # Regular users only see published posts
        return Post.objects.filter(status=Post.Status.PUBLISHED)

    def get_serializer_class(self):
        """Get appropriate serializer based on action."""
        if self.action == 'list':
            return PostListSerializer
        if self.action in ['create', 'update', 'partial_update']:
            return PostCreateUpdateSerializer
        return PostDetailSerializer

    def get_permissions(self):
        """Get permissions based on action."""
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthorOrStaff()]
        if self.action == 'create':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def retrieve(self, request, *args, **kwargs):
        """Retrieve post and increment view count."""
        instance = self.get_object()
        instance.increment_view_count()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def published(self, request):
        """
        Get all published posts (public endpoint).

        GET /api/blog/posts/published/
        """
        posts = Post.objects.filter(status=Post.Status.PUBLISHED)
        page = self.paginate_queryset(posts)
        serializer = PostListSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    @action(detail=True, methods=['get'])
    def comments(self, request, slug=None):
        """
        Get approved comments for this post.

        GET /api/blog/posts/{slug}/comments/
        """
        post = self.get_object()
        comments = post.comments.filter(status=Comment.Status.APPROVED, parent=None)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def like(self, request, slug=None):
        """
        Like/unlike post.

        POST /api/blog/posts/{slug}/like/
        """
        post = self.get_object()
        post.like_count += 1
        post.save(update_fields=['like_count'])
        return Response({'like_count': post.like_count})


class CommentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Comment model.

    Provides:
    - list: List all comments
    - retrieve: Get comment by ID
    - create: Create new comment (authenticated users)
    - update: Update comment (author or staff)
    - destroy: Delete comment (author or staff)
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post', 'status', 'parent']

    def get_queryset(self):
        """Filter queryset based on user role."""
        user = self.request.user

        if user.is_authenticated and (user.is_staff or user.is_superuser):
            # Staff can see all comments
            return Comment.objects.all()

        # Regular users only see approved comments
        return Comment.objects.filter(status=Comment.Status.APPROVED)

    def get_permissions(self):
        """Get permissions based on action."""
        if self.action in ['update', 'destroy']:
            return [IsAuthorOrStaff()]
        if self.action == 'create':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        """Save comment with current user as author."""
        serializer.save(author=self.request.user)
