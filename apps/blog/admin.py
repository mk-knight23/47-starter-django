"""
Admin configuration for blog app.
"""
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html

from .models import Category, Tag, Post, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin for Category model."""

    list_display = ['name', 'slug', 'parent', 'is_active', 'post_count', 'created_at']
    list_filter = ['is_active', 'parent', 'created_at']
    search_fields = ['name', 'slug', 'description']
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['created_at', 'updated_at']

    def post_count(self, obj):
        """Display number of posts in category."""
        return obj.posts.count()
    post_count.short_description = _('Posts')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Admin for Tag model."""

    list_display = ['name', 'slug', 'post_count', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'slug', 'description']
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['created_at']

    def post_count(self, obj):
        """Display number of posts with this tag."""
        return obj.posts.count()
    post_count.short_description = _('Posts')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Admin for Post model."""

    list_display = [
        'title',
        'author',
        'category',
        'status',
        'thumbnail',
        'view_count',
        'like_count',
        'published_at',
        'created_at',
    ]
    list_filter = ['status', 'category', 'tags', 'created_at', 'published_at']
    search_fields = ['title', 'slug', 'excerpt', 'content']
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ['tags']
    readonly_fields = [
        'view_count',
        'like_count',
        'created_at',
        'updated_at',
        'thumbnail_preview',
    ]
    date_hierarchy = 'published_at'

    fieldsets = (
        (_('Basic Information'), {
            'fields': (
                'title',
                'slug',
                'excerpt',
                'status',
                'author',
            )
        }),
        (_('Content'), {
            'fields': (
                'content',
                'featured_image',
                'thumbnail_preview',
            )
        }),
        (_('Organization'), {
            'fields': (
                'category',
                'tags',
            )
        }),
        (_('SEO'), {
            'fields': (
                'meta_title',
                'meta_description',
                'meta_keywords',
            ),
            'classes': ('collapse',),
        }),
        (_('Engagement'), {
            'fields': (
                'view_count',
                'like_count',
            ),
            'classes': ('collapse',),
        }),
        (_('Publishing'), {
            'fields': (
                'published_at',
                'created_at',
                'updated_at',
            ),
        }),
    )

    def thumbnail(self, obj):
        """Display thumbnail in list view."""
        if obj.featured_image:
            return format_html('<img src="{}" style="width: 50px; height: 50px; object-fit: cover;" />', obj.featured_image.url)
        return _('No image')
    thumbnail.short_description = _('Image')

    def thumbnail_preview(self, obj):
        """Display full-size image preview."""
        if obj.featured_image:
            return format_html('<img src="{}" style="max-width: 100%; max-height: 400px;" />', obj.featured_image.url)
        return _('No image uploaded')
    thumbnail_preview.short_description = _('Preview')

    def save_model(self, request, obj, form, change):
        """Set author to current user on create."""
        if not change:
            obj.author = request.user
        super().save_model(request, obj, form, change)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Admin for Comment model."""

    list_display = [
        'id',
        'post',
        'author',
        'content_preview',
        'status',
        'parent',
        'created_at',
    ]
    list_filter = ['status', 'created_at', 'post']
    search_fields = ['content', 'author__email', 'post__title']
    readonly_fields = ['created_at', 'updated_at']

    def content_preview(self, obj):
        """Display preview of comment content."""
        return obj.content[:100] + '...' if len(obj.content) > 100 else obj.content
    content_preview.short_description = _('Content')

    def get_actions(self, request):
        """Add custom bulk actions."""
        actions = super().get_actions(request)
        if actions:
            actions['approve_selected'] = (
                self.approve_selected,
                'approve_selected',
                _('Approve selected comments')
            )
            actions['reject_selected'] = (
                self.reject_selected,
                'reject_selected',
                _('Reject selected comments')
            )
        return actions

    def approve_selected(self, request, queryset):
        """Approve selected comments."""
        updated = queryset.update(status=Comment.Status.APPROVED)
        self.message_user(request, _(f'{updated} comments approved.'))
    approve_selected.short_description = _('Approve selected comments')

    def reject_selected(self, request, queryset):
        """Reject selected comments."""
        updated = queryset.update(status=Comment.Status.REJECTED)
        self.message_user(request, _(f'{updated} comments rejected.'))
    reject_selected.short_description = _('Reject selected comments')
