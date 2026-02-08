# Django Starter - Full-Stack Framework

A professional, production-ready Django starter with React 19 frontend. Features custom user model, role-based access control, REST API, admin dashboard, and enterprise-grade configuration.

## Features

### Backend (Django 5.1+)
- Custom user model with email-based authentication
- Role-based access control (USER, STAFF, ADMIN)
- RESTful API with Django REST Framework
- Enhanced admin dashboard with custom styling
- Environment-based configuration (dev/prod)
- Production-ready with Gunicorn/Uvicorn
- Celery support for background tasks
- Comprehensive security settings
- PostgreSQL/SQLite database support

### Frontend (React 19)
- Modern React 19 with TypeScript
- Vite 6 for lightning-fast builds
- Tailwind CSS v4 for styling
- Framer Motion for animations
- Lucide React icons
- Responsive design
- Enterprise/Corporate SaaS theme

## Tech Stack

**Backend:**
- Django 5.1+ - Web framework
- Django REST Framework - API layer
- PostgreSQL/SQLite - Database
- Gunicorn/Uvicorn - Production server
- Celery - Background tasks
- django-environ - Configuration management

**Frontend:**
- React 19 - UI library
- TypeScript - Type safety
- Vite 6 - Build tool
- Tailwind CSS v4 - Styling
- Framer Motion - Animations

## Project Structure

```
47-starter-django/
├── config/                 # Django configuration
│   ├── settings.py         # Main settings (with environment loading)
│   ├── urls.py             # URL routing
│   ├── wsgi.py             # WSGI config
│   ├── asgi.py             # ASGI config
│   ├── celery.py           # Celery config
│   ├── gunicorn.py         # Gunicorn config
│   └── uvicorn.py          # Uvicorn config
├── users/                  # Custom user app
│   ├── models.py           # User model with email auth
│   ├── views.py            # API views
│   ├── serializers.py      # DRF serializers
│   ├── permissions.py      # Custom permissions
│   ├── admin.py            # Admin configuration
│   └── signals.py          # User signals
├── apps/
│   └── blog/               # Example CRUD app
│       ├── models.py       # Post, Category, Tag, Comment
│       ├── views.py        # API viewsets
│       ├── serializers.py  # DRF serializers
│       └── admin.py        # Enhanced admin
├── static/                 # Static files
├── templates/              # Django templates
├── src/                    # React frontend
├── .claude/                # Claude workflows & scripts
├── requirements.txt        # Python dependencies
└── manage.py               # Django management
```

## Quick Start

### Prerequisites
- Python 3.10+
- Node.js 18+
- Git

### Backend Setup

1. **Clone the repository:**
```bash
git clone https://github.com/mk-knight23/47-starter-django.git
cd 47-starter-django
```

2. **Run setup workflow:**
```bash
bash .claude/workflows/setup.sh
```

This will:
- Create virtual environment
- Install Python dependencies
- Set up environment files
- Run migrations
- Create superuser
- Collect static files

3. **Start development server:**
```bash
bash .claude/workflows/dev.sh
```

Backend will be available at:
- Admin: http://localhost:8000/admin
- API: http://localhost:8000/api/

### Frontend Setup

1. **Install dependencies:**
```bash
npm install
```

2. **Start development server:**
```bash
npm run dev
```

Frontend will be available at:
- App: http://localhost:5173

## Environment Configuration

Copy `.env.example` to `.env.local` and configure:

```bash
# Core Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DATABASE_URL=sqlite:///db.sqlite3

# CORS
CORS_ALLOWED_ORIGINS=http://localhost:5173,http://127.0.0.1:5173
```

## API Endpoints

### Authentication
- `POST /api/auth/register/` - Register new user
- `POST /api/auth/login/` - Login (returns token)
- `POST /api/auth/logout/` - Logout
- `GET /api/auth/user/` - Get current user

### Users
- `GET /api/users/` - List users (admin only)
- `GET /api/users/me/` - Get current user profile
- `PUT /api/users/me/` - Update current user profile
- `GET /api/users/{id}/` - Get user by ID

### Blog (CRUD Example)
- `GET /api/blog/posts/` - List all posts
- `POST /api/blog/posts/` - Create new post
- `GET /api/blog/posts/{slug}/` - Get post detail
- `PUT /api/blog/posts/{slug}/` - Update post
- `DELETE /api/blog/posts/{slug}/` - Delete post
- `GET /api/blog/categories/` - List categories
- `GET /api/blog/tags/` - List tags
- `GET /api/blog/comments/` - List comments
- `POST /api/blog/comments/` - Create comment

## Custom User Model

The starter uses a custom user model with:
- **Email-based authentication** (no username)
- **Role-based access control** (USER, STAFF, ADMIN)
- **Extended profile** with address, social links, preferences
- **Email verification** support
- **Avatar upload**

### User Roles

```python
class User(models.Model):
    class Role(models.TextChoices):
        USER = 'USER', 'User'        # Regular user
        STAFF = 'STAFF', 'Staff'    # Staff member
        ADMIN = 'ADMIN', 'Admin'    # Administrator
```

## Admin Dashboard

Customized admin with:
- Professional styling
- Enhanced list displays
- Inline editing
- Bulk actions
- Custom filters
- Search functionality
- Image previews

Access at: http://localhost:8000/admin

## Development Workflows

### Available Scripts

**Setup:**
```bash
bash .claude/workflows/setup.sh
```

**Development Server:**
```bash
bash .claude/workflows/dev.sh
```

**Run Tests:**
```bash
bash .claude/workflows/test.sh
```

**Production Deployment:**
```bash
bash .claude/workflows/deploy.sh
```

### Utility Scripts

**Create Superuser:**
```bash
bash .claude/scripts/createsuperuser.sh
```

**Reset Database:**
```bash
bash .claude/scripts/reset-db.sh
```

## Testing

Run tests with coverage:
```bash
pytest --cov=. --cov-report=html
```

Coverage report: `htmlcov/index.html`

## Production Deployment

### Using Gunicorn

```bash
gunicorn -c config/gunicorn.py config.wsgi:application
```

### Using Uvicorn

```bash
uvicorn config.asgi:application --host 0.0.0.0 --port 8000 --workers 4
```

### Environment Checklist

- [ ] Set `DEBUG=False` in `.env.local`
- [ ] Set strong `SECRET_KEY`
- [ ] Configure production database (PostgreSQL)
- [ ] Set `ALLOWED_HOSTS` to your domain
- [ ] Configure email backend
- [ ] Set up static file serving (S3 or Whitenoise)
- [ ] Configure HTTPS with SSL certificates
- [ ] Set up Celery workers (if using background tasks)
- [ ] Configure logging and monitoring

## Deployment Platforms

### Heroku
```bash
heroku create your-app-name
heroku addons:create heroku-postgresql:mini
git push heroku main
```

### DigitalOcean
```bash
# Use App Platform or Droplet
# Configure environment variables in control panel
# Deploy using provided workflow
```

### AWS
- Use Elastic Beanstalk or ECS
- Configure RDS for PostgreSQL
- Use S3 for static files
- Set up load balancer with SSL

## Security

- Password validation
- CSRF protection
- SQL injection prevention (ORM)
- XSS protection
- Clickjacking protection
- Secure headers (HSTS, X-Frame-Options)
- Environment-based secrets
- Rate limiting ready

## Architecture

### Custom User Model
Email-based authentication with role-based access control.

### Apps Structure
- **users**: Authentication and user management
- **apps/blog**: Example CRUD implementation
- **apps/***: Add your custom apps here

### API Design
- RESTful conventions
- Token-based authentication
- Permission classes
- Pagination
- Filtering and search

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## License

MIT License - see LICENSE file for details

## Author

**Kazi Musharraf**
- GitHub: [@mk-knight23](https://github.com/mk-knight23)
- Project: [47-starter-django](https://github.com/mk-knight23/47-starter-django)

## Live Demo

- **Vercel**: https://47-starter-django.vercel.app ✓
- **Firebase**: https://web-apps-7e3fa.web.app ✓
- **Cloudflare Pages**: https://322004fa.django-starter.pages.dev ✓
- **Note**: Backend API requires Python deployment (Render/Railway recommended)

## Deployment URLs

| Platform | URL | Status |
|----------|-----|--------|
| Vercel | https://47-starter-django.vercel.app | ✓ Active |
| Firebase | https://web-apps-7e3fa.web.app | ✓ Active |
| Cloudflare Pages | https://322004fa.django-starter.pages.dev | ✓ Active |

## Deployment Configuration

This project includes deployment configurations for multiple platforms:

- `vercel.json` - Vercel static hosting configuration
- `firebase.json` - Firebase Hosting configuration
- `wrangler.toml` - Cloudflare Pages configuration
- `render.yaml` - Render web service blueprint (validated)
- `amplify.yml` - AWS Amplify configuration
- `azure-static-web-apps.yml` - Azure Static Web Apps configuration

## Support

For issues and questions:
- Open a GitHub issue
- Check documentation in `/docs`
- Review code comments

---

Built with ❤️ using Django and React
