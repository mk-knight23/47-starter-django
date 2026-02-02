"""
Celery configuration for production deployment.

Usage:
    celery -A config worker -l info -c 4
    celery -A config beat -l info
"""
import os

# Broker settings
BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379/0')
RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379/0')

# Task settings
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TIMEZONE = 'UTC'
CELERY_ENABLE_UTC = True

# Task routing
CELERY_ROUTES = {
    'apps.blog.tasks.*': {'queue': 'blog'},
    'users.tasks.*': {'queue': 'users'},
}

# Task execution
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60  # 30 minutes
CELERY_WORKER_PREFETCH_MULTIPLIER = 4

# Task result settings
CELERY_RESULT_COMPRESSION = 'gzip'
CELERY_RESULT_EXPIRES = 3600  # 1 hour

# Task scheduling
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

# Worker settings
CELERY_WORKER_MAX_TASKS_PER_CHILD = 1000
CELERY_WORKER_CONCURRENCY = os.cpu_count() * 2
