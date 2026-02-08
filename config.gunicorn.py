"""
Gunicorn configuration for Django production.
"""

import os

# Server socket
bind = "0.0.0.0:8000"
backlog = 100

# Worker processes
workers = 4
worker_class = "sync"
worker_connections = 1000

# Server mechanics
worker_tmp_dir = "/dev/shm"
timeout = 30
graceful_timeout = 30
keepalive = 2
max_requests = 1000
max_requests_jitter = 100

# Process naming
proc_name = "gunicorn"

# Logging
accesslog = "/logs/gunicorn.access.log"
errorlog = "/logs/gunicorn.error.log"
loglevel = "info"
accesslog_format = '%(t)s %(h)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

# Security
limit_request_line = 4094
limit_request_fields = 100
limit_request_field_size = 8190

# Django-specific
raw_env = [
    "DJANGO_SETTINGS_MODULE=config.settings",
    "PYTHONPATH=/app",
]

# Preload app
preload_app = True

# Redirect stdout/stderr to log files
if "GUNICORN_LOG_LEVEL" in os.environ:
    loglevel = os.environ["GUNICORN_LOG_LEVEL"]