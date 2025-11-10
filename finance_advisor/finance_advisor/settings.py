"""
Django settings for finance_advisor project.
"""

import os
from pathlib import Path

import dj_database_url
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-j2x8f3n5k7m9p0q2w4e6r8t0y2u4i6o8')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DJANGO_DEBUG', 'False').lower() == 'true'

default_allowed_hosts = ['localhost', '127.0.0.1']
allowed_hosts_env = os.getenv('DJANGO_ALLOWED_HOSTS')

if allowed_hosts_env:
    # Use environment variable if set (e.g., in Render dashboard)
    ALLOWED_HOSTS = [host.strip() for host in allowed_hosts_env.split(',') if host.strip()]
else:
    # **FIXED:** Default to localhost/127.0.0.1 and allow all Render domains (*.onrender.com)
    # This prevents the 400 Bad Request error.
    ALLOWED_HOSTS = default_allowed_hosts + ['.onrender.com']

# **NEW FIXES FOR RENDER PROXY:**
# These settings correctly process the Host header passed by Render's proxy,
# which helps Django determine the correct domain.
USE_X_FORWARDED_HOST = True
# USE_X_FORWARDED_PORT is often useful, setting it for robustness.
USE_X_FORWARDED_PORT = True
# Your existing setting is correct for forcing secure links:
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# CSRF settings
csrf_trusted_origins_env = os.getenv('DJANGO_CSRF_TRUSTED_ORIGINS')
if csrf_trusted_origins_env:
    CSRF_TRUSTED_ORIGINS = [origin.strip() for origin in csrf_trusted_origins_env.split(',') if origin.strip()]
else:
    # **FIXED:** Added https:// for secure origins, important for Render deployment
    CSRF_TRUSTED_ORIGINS = ['http://127.0.0.1:51173', 'http://localhost:51173', 'https://*.onrender.com']
CSRF_COOKIE_SECURE = not DEBUG # Set secure to true in production
CSRF_COOKIE_HTTPONLY = True # Recommended security practice
CSRF_USE_SESSIONS = False

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'advisor',  # Our finance advisor app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # **FIXED:** Uncommenting CSRF middleware is essential for security.
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# (Rest of the file remains the same)
# ...
# Database config
DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600,
        ssl_require=not DEBUG,
    )
}
# ...
# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ...
# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Login URL
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/login/'

# Gemini settings
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', '')
GEMINI_MODEL = os.getenv('GEMINI_MODEL', 'models/gemini-1.5-flash')

# SECURE_PROXY_SSL_HEADER was moved to the proxy settings block at the top for clarity.
