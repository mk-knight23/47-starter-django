# Django Starter - Quick Reference

## 🚀 Quick Start Commands

### Initial Setup
```bash
bash .claude/workflows/setup.sh
```

### Development Server
```bash
bash .claude/workflows/dev.sh
# Or: python manage.py runserver
```

### Run Tests
```bash
bash .claude/workflows/test.sh
# Or: pytest --cov=. --cov-report=html
```

### Create Superuser
```bash
bash .claude/scripts/createsuperuser.sh
# Or: python manage.py createsuperuser
```

### Reset Database
```bash
bash .claude/scripts/reset-db.sh
```

---

## 📁 Key File Locations

| Purpose | Location |
|---------|----------|
| Settings | `/config/settings.py` |
| URLs | `/config/urls.py` |
| User Model | `/users/models.py` |
| Blog Models | `/apps/blog/models.py` |
| Admin Config | `/config/admin.py` |
| Environment | `.env.local` |

---

## 🔐 Authentication & Users

### Create User
```python
from users.models import User
user = User.objects.create_user(
    email='user@example.com',
    password='securepass',
    first_name='John',
    last_name='Doe'
)
```

### Check User Role
```python
user.is_staff_user    # Staff or admin
user.is_admin_user    # Admin only
user.has_role(User.Role.ADMIN)  # Check specific role
```

### Custom Permissions
```python
from users.permissions import IsOwnerOrStaff

class MyViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrStaff]
```

---

## 🌐 API Endpoints

### Authentication
- `POST /api/auth/register/` - Register
- `POST /api/auth/login/` - Login (get token)
- `POST /api/auth/logout/` - Logout
- `GET /api/auth/user/` - Current user

### Users
- `GET /api/users/` - List users (admin only)
- `GET /api/users/me/` - Current user profile
- `PUT /api/users/me/` - Update profile

### Blog
- `GET /api/blog/posts/` - List posts
- `POST /api/blog/posts/` - Create post
- `GET /api/blog/posts/{slug}/` - Get post
- `PUT /api/blog/posts/{slug}/` - Update post
- `DELETE /api/blog/posts/{slug}/` - Delete post
- `GET /api/blog/categories/` - List categories
- `GET /api/blog/tags/` - List tags

---

## 🗄️ Database Operations

### Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Create Migration
```bash
python manage.py makemigrations yourapp
```

### Show Migrations
```bash
python manage.py showmigrations
```

### Reset Migrations (Warning!)
```bash
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
python manage.py makemigrations
python manage.py migrate
```

---

## 🎨 Admin Customization

### Add Model to Admin
```python
# yourapp/admin.py
from django.contrib import admin
from .models import YourModel

@admin.register(YourModel)
class YourModelAdmin(admin.ModelAdmin):
    list_display = ['field1', 'field2']
    search_fields = ['field1']
    list_filter = ['field2']
```

### Custom Admin Action
```python
def custom_action(modeladmin, request, queryset):
    queryset.update(status='active')

custom_action.short_description = 'Mark as active'
YourModelAdmin.actions = [custom_action]
```

---

## 🔧 Configuration

### Environment Variables
```bash
# .env.local
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
CORS_ALLOWED_ORIGINS=http://localhost:5173
```

### Production Settings
```python
# settings.py automatically applies when DEBUG=False
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    # ... more security settings
```

---

## 🧪 Testing

### Run All Tests
```bash
pytest
```

### Run Specific Test
```bash
pytest apps/blog/tests/test_views.py
```

### With Coverage
```bash
pytest --cov=apps.blog --cov-report=html
```

### Watch Mode
```bash
pytest-watch
```

---

## 📝 Code Quality

### Format Code
```bash
black .
```

### Check Linting
```bash
ruff check .
```

### Type Checking
```bash
mypy .
```

### Run All
```bash
black . && ruff check . && mypy . && pytest
```

---

## 🚢 Deployment

### Gunicorn
```bash
gunicorn -c config/gunicorn.py config.wsgi:application
```

### Uvicorn
```bash
uvicorn config.asgi:application --host 0.0.0.0 --port 8000
```

### Collect Static
```bash
python manage.py collectstatic --noinput
```

### Create Superuser
```bash
python manage.py createsuperuser --noinput
```

---

## 🔍 Debugging

### Django Shell
```bash
python manage.py shell
```

### Check Settings
```python
from django.conf import settings
print(settings.DEBUG)
print(settings.DATABASES)
```

### Test Query
```python
from users.models import User
User.objects.all()
User.objects.filter(email__contains='@')
```

### View SQL Queries
```python
from django.db import connection
print(connection.queries)
```

---

## 🛠️ Common Tasks

### Add New App
```bash
python manage.py startapp myapp apps/
```

Then add to `INSTALLED_APPS` in settings.

### Create Custom Command
```bash
python manage.py startapp myapp apps/
# Create: apps/myapp/management/commands/yourcommand.py
```

Use: `python manage.py yourcommand`

### Import Data
```python
from apps.blog.models import Post
Post.objects.create(title='Test', content='Content')
```

### Export Data
```bash
python manage.py dumpdata blog > blog.json
```

### Load Data
```bash
python manage.py loaddata blog.json
```

---

## 📊 Monitoring

### Check Logs
```bash
tail -f logs/django.log
```

### Database Size
```python
from django.db import connection
cursor = connection.cursor()
cursor.execute("SELECT pg_size_pretty(pg_database_size('dbname'))")
print(cursor.fetchone())
```

### Active Users
```python
from users.models import User
active_users = User.objects.filter(is_active=True)
print(f"Active users: {active_users.count()}")
```

---

## 🎯 Best Practices

### Model Fields
```python
# Good
title = models.CharField(max_length=200)
created_at = models.DateTimeField(auto_now_add=True)

# Bad
title = models.CharField()  # Missing max_length
created = models.DateTimeField()  # Should auto-populate
```

### Queries
```python
# Good (efficient)
users = User.objects.only('email', 'first_name')

# Bad (N+1 queries)
for user in users:
    print(user.profile.city)  # Separate query per user
```

### Serializers
```python
# Good
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name']

# Bad (exposing sensitive data)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  # Exposes password hash!
```

---

## 🔐 Security Checklist

- [ ] Set `DEBUG=False` in production
- [ ] Use strong `SECRET_KEY`
- [ ] Use environment variables for secrets
- [ ] Enable HTTPS
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Set up `CORS_ALLOWED_ORIGINS`
- [ ] Use PostgreSQL in production
- [ ] Regularly update dependencies
- [ ] Review admin access
- [ ] Monitor error logs

---

## 📚 Documentation

- **README.md** - Main documentation
- **GETTING_STARTED.md** - Setup guide
- **PROJECT_STRUCTURE.md** - File structure
- **CHECKLIST.md** - RALPH checklist
- **RALPH_SUMMARY.md** - Implementation summary
- **.claude/README.md** - Workflow documentation

---

## 🆘 Troubleshooting

### Port in Use
```bash
lsof -ti:8000 | xargs kill -9
```

### Migration Conflicts
```bash
python manage.py migrate --fake-initial
```

### Import Errors
```bash
pip install -r requirements.txt --force-reinstall
```

### Static Files Not Loading
```bash
python manage.py collectstatic --clear --noinput
```

---

## 🌟 Pro Tips

1. **Use Django Shell** - Test code before implementing
2. **Check SQL Queries** - Use `connection.queries`
3. **Use Signals** - Auto-create related objects
4. **Custom Managers** - Encapsulate query logic
5. **ViewSets** - Consistent API structure
6. **Permissions** - Reusable permission classes
7. **Serializers** - Validate input data
8. **Admin Actions** - Bulk operations
9. **Middleware** - Cross-cutting concerns
10. **Context Processors** - Global template variables

---

*Last Updated: 2026-02-02*
*Django 5.1 + DRF + React 19*
