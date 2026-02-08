"""
URL configuration for web_project.
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from config import views

urlpatterns = [
    # Home page
    path('', views.home, name='home'),

    # Health check (must be first for load balancers)
    path('api/health/', views.health_check, name='health-check'),

    # Admin
    path('admin/', admin.site.urls),

    # API: Auth
    path('api/auth/', include('dj_rest_auth.urls')),
    # JWT URLs - conditionally imported
    # path('api/auth/registration/', include('dj_rest_auth.registration.urls')),  # Disabled - incompatible with username-less User model

    # API: Blog
    path('api/blog/', include('apps.blog.urls')),

    # API: Users
    path('api/users/', include('users.urls')),

    # API: Schema & Documentation
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

# Static and media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    # Django Debug Toolbar
    try:
        import debug_toolbar
        urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns
    except ImportError:
        pass

# Error handlers (custom 404, 500)
handler404 = 'config.views.custom_404'
handler500 = 'config.views.custom_500'
