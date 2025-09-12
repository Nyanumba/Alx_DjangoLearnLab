# LibraryProject

This is the initial setup for the Django project.
# Django Security Best Practices

## Settings
- `DEBUG = False` in production
- `SECURE_BROWSER_XSS_FILTER = True`, `X_FRAME_OPTIONS = 'DENY'`, `SECURE_CONTENT_TYPE_NOSNIFF = True`
- `CSRF_COOKIE_SECURE = True`, `SESSION_COOKIE_SECURE = True` (enforce HTTPS)

## Templates
- All forms include `{% csrf_token %}` to prevent CSRF attacks

## Views
- ORM used for all database queries to avoid SQL injection
- User inputs validated via Django Forms

## CSP
- Added Content Security Policy (CSP) to mitigate XSS
