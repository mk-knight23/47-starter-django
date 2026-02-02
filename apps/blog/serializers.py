"""
Serializers for blog app API endpoints.
"""
from rest_framework import serializers
from .models import Category, Tag, Post, Comment


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for Category model."""

    post_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'slug',
            'description',
            'parent',
            'is_active',
            'post_count',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']

    def get_post_count(self, obj):
        """Get number of posts in category."""
        return obj.posts.filter(status=Post.Status.PUBLISHED).count()


class TagSerializer(serializers.ModelSerializer):
    """Serializer for Tag model."""

    post_count = serializers.SerializerMethodField()

    class Meta:
        model = Tag
        fields = [
            'id',
            'name',
            'slug',
            'description',
            'post_count',
            'created_at',
        ]
        read_only_fields = ['created_at']

    def get_post_count(self, obj):
        """Get number of posts with this tag."""
        return obj.posts.filter(status=Post.Status.PUBLISHED).count()


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for Comment model."""

    author_email = serializers.EmailField(source='author.email', read_only=True)
    author_name = serializers.CharField(source='author.get_full_name', read_only=True)
    replies_count = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            'id',
            'post',
            'author',
            'author_email',
            'author_name',
            'parent',
            'content',
            'status',
            'replies_count',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['author', 'created_at', 'updated_at']

    def get_replies_count(self, obj):
        """Get number of replies."""
        return obj.replies.count()


class PostListSerializer(serializers.ModelSerializer):
    """Serializer for Post list view (lightweight)."""

    author_name = serializers.CharField(source='author.get_full_name', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True, allow_null=True)
    tags_list = serializers.SerializerMethodField()
    is_published = serializers.BooleanField(read_only=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'slug',
            'excerpt',
            'featured_image',
            'author',
            'author_name',
            'category',
            'category_name',
            'tags_list',
            'status',
            'is_published',
            'view_count',
            'like_count',
            'published_at',
            'created_at',
        ]

    def get_tags_list(self, obj):
        """Get list of tag names."""
        return [tag.name for tag in obj.tags.all()]


class PostDetailSerializer(serializers.ModelSerializer):
    """Serializer for Post detail view (full information)."""

    author_name = serializers.CharField(source='author.get_full_name', read_only=True)
    author_email = serializers.EmailField(source='author.email', read_only=True)
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    comments_count = serializers.SerializerMethodField()
    is_published = serializers.BooleanField(read_only=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'slug',
            'excerpt',
            'content',
            'featured_image',
            'author',
            'author_name',
            'author_email',
            'category',
            'tags',
            'status',
            'is_published',
            'meta_title',
            'meta_description',
            'meta_keywords',
            'view_count',
            'like_count',
            'comments_count',
            'published_at',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['author', 'view_count', 'like_count', 'created_at', 'updated_at']

    def get_comments_count(self, obj):
        """Get number of approved comments."""
        return obj.comments.filter(status=Comment.Status.APPROVED).count()


class PostCreateUpdateSerializer(serializers.ModelSerializer):
    """Serializer for creating and updating posts."""

    class Meta:
        model = Post
        fields = [
            'title',
            'slug',
            'excerpt',
            'content',
            'featured_image',
            'category',
            'tags',
            'status',
            'meta_title',
            'meta_description',
            'meta_keywords',
            'published_at',
        ]
