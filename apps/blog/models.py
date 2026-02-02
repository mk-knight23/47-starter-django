"""
Blog models with posts, categories, and tags.
"""
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

User = get_user_model()


class Category(models.Model):
    """
    Blog category for organizing posts.

    Features:
    - Hierarchical structure (parent/child categories)
    - Slug-based URLs
    - Active/inactive status
    """

    name = models.CharField(_('name'), max_length=100, unique=True)
    slug = models.SlugField(_('slug'), unique=True, max_length=100)
    description = models.TextField(_('description'), blank=True)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        verbose_name=_('parent category'),
    )
    is_active = models.BooleanField(_('is active'), default=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')
        ordering = ['name']
        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['is_active']),
        ]

    def __str__(self):
        """Return string representation."""
        return self.name

    def get_absolute_url(self):
        """Get URL for category detail."""
        return reverse('blog:category-detail', kwargs={'slug': self.slug})


class Tag(models.Model):
    """
    Blog tag for labeling posts.

    Tags are flat (non-hierarchical) and can be applied to multiple posts.
    """

    name = models.CharField(_('name'), max_length=50, unique=True)
    slug = models.SlugField(_('slug'), unique=True, max_length=50)
    description = models.TextField(_('description'), blank=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')
        ordering = ['name']
        indexes = [
            models.Index(fields=['slug']),
        ]

    def __str__(self):
        """Return string representation."""
        return self.name


class Post(models.Model):
    """
    Blog post with rich content and metadata.

    Features:
    - Draft/published status
    - SEO metadata
    - Featured image
    - View count
    - Like/like functionality
    """

    class Status(models.TextChoices):
        """Post status options."""
        DRAFT = 'DRAFT', _('Draft')
        PUBLISHED = 'PUBLISHED', _('Published')
        ARCHIVED = 'ARCHIVED', _('Archived')

    # Basic Information
    title = models.CharField(_('title'), max_length=200)
    slug = models.SlugField(_('slug'), unique=True, max_length=200)
    excerpt = models.TextField(_('excerpt'), max_length=300, blank=True, help_text=_('Short description for listings'))

    # Content
    content = models.TextField(_('content'))
    featured_image = models.ImageField(_('featured image'), upload_to='blog/images/', blank=True, null=True)

    # Author and Status
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='blog_posts',
        verbose_name=_('author'),
    )
    status = models.CharField(
        _('status'),
        max_length=20,
        choices=Status.choices,
        default=Status.DRAFT,
    )

    # Categories and Tags
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='posts',
        verbose_name=_('category'),
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name='posts',
        verbose_name=_('tags'),
    )

    # SEO
    meta_title = models.CharField(_('meta title'), max_length=60, blank=True)
    meta_description = models.CharField(_('meta description'), max_length=160, blank=True)
    meta_keywords = models.CharField(_('meta keywords'), max_length=255, blank=True)

    # Engagement
    view_count = models.PositiveIntegerField(_('view count'), default=0)
    like_count = models.PositiveIntegerField(_('like count'), default=0)

    # Timestamps
    published_at = models.DateTimeField(_('published at'), blank=True, null=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')
        ordering = ['-published_at', '-created_at']
        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['status']),
            models.Index(fields=['-published_at']),
            models.Index(fields=['author', 'status']),
        ]

    def __str__(self):
        """Return string representation."""
        return self.title

    def get_absolute_url(self):
        """Get URL for post detail."""
        return reverse('blog:post-detail', kwargs={'slug': self.slug})

    @property
    def is_published(self):
        """Check if post is published."""
        return self.status == self.Status.PUBLISHED

    def increment_view_count(self):
        """Increment view count."""
        self.view_count += 1
        self.save(update_fields=['view_count'])


class Comment(models.Model):
    """
    Blog comment with nested replies.

    Features:
    - Nested comments (parent/child)
    - Moderation status
    - Email notifications
    """

    class Status(models.TextChoices):
        """Comment status options."""
        PENDING = 'PENDING', _('Pending')
        APPROVED = 'APPROVED', _('Approved')
        REJECTED = 'REJECTED', _('Rejected')
        SPAM = 'SPAM', _('Spam')

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name=_('post'),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='blog_comments',
        verbose_name=_('author'),
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='replies',
        verbose_name=_('parent comment'),
    )
    content = models.TextField(_('content'))
    status = models.CharField(
        _('status'),
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['post', 'status']),
            models.Index(fields=['author']),
        ]

    def __str__(self):
        """Return string representation."""
        return f'Comment by {self.author.email} on {self.post.title}'

    @property
    def is_approved(self):
        """Check if comment is approved."""
        return self.status == self.Status.APPROVED
