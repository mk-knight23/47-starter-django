# Django Starter - Project Structure

```
47-starter-django/
│
├── 📁 config/                          # Django configuration package
│   ├── __init__.py                     # Package initializer
│   ├── settings.py                     # Main settings (env-based configuration)
│   ├── urls.py                         # URL routing
│   ├── wsgi.py                         # WSGI configuration
│   ├── asgi.py                         # ASGI configuration
│   ├── celery.py                       # Celery integration
│   ├── celery_config.py                # Celery settings
│   ├── gunicorn.py                     # Gunicorn config (production)
│   ├── uvicorn.py                      # Uvicorn config (production)
│   ├── views.py                        # Custom error views
│   └── admin.py                        # Admin customization
│
├── 📁 users/                           # Custom user app
│   ├── __init__.py                     # Package initializer
│   ├── apps.py                         # App configuration
│   ├── apps_configured.py              # App config with signals
│   ├── models.py                       # User & UserProfile models
│   ├── managers.py                     # Custom UserManager
│   ├── views.py                        # API viewsets
│   ├── serializers.py                  # DRF serializers
│   ├── permissions.py                  # Custom permissions
│   ├── urls.py                         # User URLs
│   ├── admin.py                        # User admin
│   └── signals.py                      # User signals
│
├── 📁 apps/                            # Django applications
│   ├── __init__.py                     # Apps package
│   └── 📁 blog/                        # Example CRUD app
│       ├── __init__.py                 # Blog package
│       ├── apps.py                     # Blog app config
│       ├── models.py                   # Post, Category, Tag, Comment
│       ├── views.py                    # Blog API viewsets
│       ├── serializers.py              # Blog serializers
│       ├── permissions.py              # Blog permissions
│       ├── urls.py                     # Blog URLs
│       └── admin.py                    # Blog admin
│
├── 📁 static/                          # Static files
│   └── 📁 admin/
│       └── 📁 css/
│           └── custom.css              # Custom admin styling
│
├── 📁 templates/                       # Django templates
│   ├── 📁 admin/
│   │   ├── base_site.html             # Custom admin base
│   │   └── index.html                 # Custom admin dashboard
│   └── 📁 errors/
│       ├── 404.html                   # Custom 404 page
│       └── 500.html                   # Custom 500 page
│
├── 📁 media/                           # User uploaded files
├── 📁 staticfiles/                     # Collected static files
├── 📁 logs/                            # Application logs
│
├── 📁 .claude/                         # Claude workflows & scripts
│   ├── README.md                       # Workflow documentation
│   ├── 📁 workflows/
│   │   ├── setup.sh                    # Automated setup
│   │   ├── dev.sh                      # Development server
│   │   ├── test.sh                     # Test runner
│   │   └── deploy.sh                   # Production deployment
│   ├── 📁 scripts/
│   │   ├── createsuperuser.sh          # Quick superuser creation
│   │   └── reset-db.sh                 # Database reset
│   └── 📁 hooks/
│       ├── pre-commit.sh               # Pre-commit hook
│       └── pre-push.sh                 # Pre-push hook
│
├── 📁 docs/                            # Additional documentation
│   ├── ARCHITECTURE.md                 # Architecture overview
│   ├── DESIGN.md                       # Design system
│   └── CHANGELOG.md                    # Version history
│
├── 📁 src/                             # React frontend
│   ├── App.tsx                         # Main React app
│   ├── main.tsx                        # React entry point
│   └── index.css                       # Global styles
│
├── manage.py                           # Django management script
├── requirements.txt                    # Python dependencies
├── requirements-dev.txt                # Development dependencies
├── requirements-base.txt               # Base dependencies
├── pyproject.toml                      # Python project config
├── .env.example                        # Environment template
├── .env.local                          # Local environment (gitignored)
├── .gitignore                          # Git ignore rules
│
├── README.md                           # Main documentation
├── GETTING_STARTED.md                  # Setup guide
├── CHECKLIST.md                        # RALPH checklist
├── RALPH_SUMMARY.md                    # RALPH completion report
├── PROJECT_STRUCTURE.md                # This file
│
├── package.json                        # Node.js dependencies
├── tsconfig.json                       # TypeScript config
├── vite.config.ts                      # Vite config
├── index.html                          # HTML entry point
└── LICENSE                             # MIT License
```

## Key Components

### Configuration (`/config/`)
- **settings.py**: Environment-based Django settings
- **urls.py**: API and admin URL routing
- **wsgi.py/asgi.py**: Server interfaces
- **celery.py**: Background task setup

### Custom User (`/users/`)
- **models.py**: Email-based user with roles
- **permissions.py**: Role-based access control
- **admin.py**: Enhanced user management
- **serializers.py**: User API serialization

### Blog App (`/apps/blog/`)
- **models.py**: Post, Category, Tag, Comment models
- **views.py**: RESTful API viewsets
- **admin.py**: Enhanced admin interface
- **urls.py**: API endpoint routing

### Workflows (`/.claude/`)
- **setup.sh**: One-command project setup
- **dev.sh**: Start development server
- **test.sh**: Run tests with coverage
- **deploy.sh**: Production deployment

## Data Flow

```
User Request
    ↓
Django URLs (/config/urls.py)
    ↓
API Viewsets (/apps/blog/views.py, /users/views.py)
    ↓
Serializers (validate data)
    ↓
Models (save to database)
    ↓
Response (JSON)
```

## Architecture Layers

1. **Presentation Layer**
   - Django Templates (`/templates/`)
   - React Frontend (`/src/`)
   - Static Files (`/static/`)

2. **Business Logic Layer**
   - Views (`/apps/*/views.py`, `/users/views.py`)
   - Serializers (`/apps/*/serializers.py`)
   - Permissions (`/apps/*/permissions.py`)

3. **Data Access Layer**
   - Models (`/apps/*/models.py`, `/users/models.py`)
   - Managers (`/users/managers.py`)

4. **Configuration Layer**
   - Settings (`/config/settings.py`)
   - URLs (`/config/urls.py`)
   - Admin (`/config/admin.py`)

## Design Patterns

### Repository Pattern
- Models handle data access
- Views handle business logic
- Serializers handle data validation

### Factory Pattern
- Custom UserManager in `/users/managers.py`
- Creates users with email authentication

### Strategy Pattern
- Multiple permission classes
- Different authentication strategies

### Observer Pattern
- Django signals in `/users/signals.py`
- Auto-create UserProfile on User creation

## File Naming Conventions

- **Models**: `models.py` (singular: User, Post)
- **Views**: `views.py` (singular: UserViewSet)
- **URLs**: `urls.py` (singular: user/, post/)
- **Serializers**: `serializers.py` (singular: UserSerializer)
- **Admin**: `admin.py` (singular: UserAdmin)

## Import Structure

```python
# Django imports
from django.db import models
from django.contrib.auth import get_user_model

# DRF imports
from rest_framework import viewsets, serializers

# Project imports
from users.models import User
from apps.blog.models import Post
```

## Environment-Based Loading

```python
# .env.local → Django settings
SECRET_KEY → config.settings → Available everywhere
DATABASE_URL → config.settings → Database connection
CORS_ALLOWED_ORIGINS → config.settings → CORS config
```

## Extension Points

### Adding a New App
1. Create app in `/apps/yourapp/`
2. Add to `INSTALLED_APPS` in settings
3. Create models, views, serializers
4. Add URLs in `/config/urls.py`
5. Register in admin

### Adding Custom Permissions
1. Create permission class in `permissions.py`
2. Add to viewsets
3. Test with different user roles

### Adding API Endpoints
1. Create ViewSet in `views.py`
2. Register in router
3. Include in `/config/urls.py`

---

This structure provides a solid foundation for building scalable Django applications with React frontends.
