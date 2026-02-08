"""
Custom error views and health check endpoint.
"""
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.db import connection, DatabaseError
from django.core.cache import cache
from django.core.cache.backends.base import BaseCache
from django.conf import settings


def home(request):
    """Home page view for the Django Starter."""
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Django Starter</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body {
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
            }
            .container {
                text-align: center;
                padding: 2rem;
                max-width: 800px;
            }
            h1 {
                font-size: 3rem;
                margin-bottom: 1rem;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
            }
            p {
                font-size: 1.2rem;
                margin-bottom: 2rem;
                opacity: 0.9;
            }
            .links {
                display: flex;
                gap: 1rem;
                justify-content: center;
                flex-wrap: wrap;
            }
            .link {
                background: rgba(255,255,255,0.2);
                color: white;
                padding: 0.75rem 1.5rem;
                border-radius: 8px;
                text-decoration: none;
                transition: all 0.3s ease;
                border: 1px solid rgba(255,255,255,0.3);
            }
            .link:hover {
                background: rgba(255,255,255,0.3);
                transform: translateY(-2px);
            }
            .badge {
                display: inline-block;
                background: rgba(255,255,255,0.2);
                padding: 0.5rem 1rem;
                border-radius: 20px;
                font-size: 0.9rem;
                margin-top: 2rem;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Django Starter</h1>
            <p>A production-ready Django REST API with JWT authentication</p>
            <div class="links">
                <a href="/api/docs/" class="link">API Documentation</a>
                <a href="/api/health/" class="link">Health Check</a>
                <a href="/admin/" class="link">Admin Panel</a>
            </div>
            <div class="badge">Django 5.1 + DRF + JWT Auth</div>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)


def custom_404(request, exception):
    """Custom 404 error page."""
    return render(request, 'errors/404.html', status=404)


def custom_500(request):
    """Custom 500 error page."""
    return render(request, 'errors/500.html', status=500)


def health_check(request):
    """
    Health check endpoint for monitoring.

    Returns:
        JsonResponse: Health status with database and cache connection info
    """
    health_status = {
        'status': 'healthy',
        'database': 'connected',
        'cache': 'connected',
        'version': '1.0.0',
    }

    # Check database connection
    try:
        with connection.cursor() as cursor:
            cursor.execute('SELECT 1')
            connection.connection.ping()
    except (DatabaseError, Exception):
        health_status['database'] = 'disconnected'
        health_status['status'] = 'unhealthy'

    # Check cache connection
    try:
        if cache and isinstance(cache, BaseCache):
            # Try to get and set a value to test cache
            cache_key = 'health_check_test'
            cache.set(cache_key, 'test', 1)
            cache_value = cache.get(cache_key)
            if cache_value != 'test':
                health_status['cache'] = 'disconnected'
                health_status['status'] = 'unhealthy'
    except Exception:
        health_status['cache'] = 'disconnected'
        health_status['status'] = 'unhealthy'

    # Set appropriate HTTP status code
    status_code = 200 if health_status['status'] == 'healthy' else 503

    return JsonResponse(health_status, status=status_code)
