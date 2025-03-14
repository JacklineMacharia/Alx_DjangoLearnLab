"""
Django settings for LibraryProject project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import os
from django.core.exceptions import ImproperlyConfigured
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-e_w^vy(x9-6-ftawc)w=c=4et7^(sniz++b!+8-#!=&@i^xu(h'

def get_env_variable(var_name):
    """ Get the environment variable or return exceprtion """
    try:
        return os.environ[var_name]
    except KeyError:
        raise ImproperlyConfigured(f"Set the {var_name} environment variable")
    
# Security Settings
DEBUG = False # Disable debug mode in production


ALLOWED_HOSTS = []

SECURE_BROWSER_XSS_FILTER = True #Prevent XSS attacks
X_FRAME_OPTIONS = 'DENY' #Prevent clickjacking
SECURE_CONTENT_TYPE_NOSNIFF = True # Prevent MIME-type sniffing

# Enforce HTTPS (only enable if using HTTPS)
CSRF_COOKIE_SECURE = True # Ensures CSRF cookies are sent over HTTPS
SESSION_COOKIE_SECURE = True # Ensures session cookies are sent over HTTPS
SECURE_SSL_REDIRECT = True # Redirect HTTP to HTTPS

# HTTP Strict Transport Security (HSTS)
SECURE_HSTS_SECONDS = 31536000  # One year in seconds
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Apply HSTS to all subdomains
SECURE_HSTS_PRELOAD = True  # Allow browser preload of HSTS policy

#Content Security Policy
CSP_DEFAULT_SRC = ("'self'",) # Restrict default content sources
CSP_SCRIPT_SCR = ("'self'", "trusted-scripts.com")
CSP_STYLE_REDIRECT = ("'self'", "trusted-style.com")

# Prevent Host Header Injection
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO' 'https')

# Secret Key Management
SECRET_KEY = get_env_variable('DJANGO_SECRET_KEY') # Store secret key in environment variable

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookshelf',
    'relationship_app',
    'csp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'csp.middleware.CSPMiddleware',  # Add CSP Middleware
]

# Content Security Policy (CSP)
CSP_DEFAULT_SRC = ("'self'",)  # Restrict default sources
CSP_SCRIPT_SRC = ("'self'", "https://trusted-scripts.com")  # Allow safe script sources
CSP_STYLE_SRC = ("'self'", "https://trusted-styles.com")  # Allow safe style sources
CSP_IMG_SRC = ("'self'", "https://trusted-images.com")  # Allow images from trusted sources
ROOT_URLCONF = 'LibraryProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "relationship_app/templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'LibraryProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'bookshelf.CustomUser'



