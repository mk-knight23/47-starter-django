"""
Uvicorn configuration for production deployment.

Usage:
    uvicorn config.asgi:application --host 0.0.0.0 --port 8000
    uvicorn config.asgi:application --config config/uvicorn.py
"""

import os

# Host and port
host = "0.0.0.0"
port = 8000

# Worker settings
workers = os.cpu_count() * 2 + 1
loop = "auto"  # auto, asyncio, uvloop
http = "auto"  # auto, h11, httptools
ws = "auto"  # auto, websockets, none
lifespan = "auto"

# Logging
log_level = "info"  # critical, error, warning, info, debug, trace
access_log = True
use_colors = True

# SSL/TLS (if using HTTPS)
# ssl_keyfile = "/path/to/ssl/key.pem"
# ssl_certfile = "/path/to/ssl/cert.pem"

# Performance
limit_concurrency = 1000
limit_max_requests = 10000
timeout_keep_alive = 5

# Application reload (development only)
reload = False

# Headers
forwarded_allow_ips = "*"
proxy_headers = True
server_header = True

# Process management
# pid_file = "/tmp/uvicorn.pid"
