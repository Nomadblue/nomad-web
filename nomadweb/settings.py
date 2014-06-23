#! -.- coding: utf-8 -.-

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


def env_var(key, default=None):
    """Retrieves env vars and makes Python boolean replacements"""
    val = os.environ.get(key, default)
    if val == 'True':
        val = True
    elif val == 'False':
        val = False
    return val

SECRET_KEY = env_var('SECRET_KEY', 'your$%&/defaultsecretkeygoesheremyfriend!')

DEBUG = env_var('DEBUG', False)
TEMPLATE_DEBUG = DEBUG
INTERNAL_IPS = ('127.0.0.1',)

ALLOWED_HOSTS = env_var('ALLOWED_HOSTS', '*').split(',')

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.humanize',
    'django_extensions',
    'imagekit',
    'storages',
    'gunicorn',
    'south',
    'propaganda',
    'website',
    'contact',
    'blog',
    'nomadblog',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'website.context_processors.template_extra_context',
)

ROOT_URLCONF = 'nomadweb.urls'

WSGI_APPLICATION = 'nomadweb.wsgi.application'

LANGUAGE_CODE = env_var('LANGUAGE_CODE', 'en')
TIME_ZONE = 'America/Chicago'
USE_TZ = False
USE_I18N = True
USE_L10N = True

# i18n
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Database
import dj_database_url
DATABASES = {'default': dj_database_url.config(default=env_var('DATABASE_URL'))}

# Django Admin
ADMIN_URL = env_var('ADMIN_URL', 'admin/')

# Amazon credentials
AWS_ACCESS_KEY_ID = env_var('AWS_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = env_var('AWS_SECRET_ACCESS_KEY', '')

# Django-storages for S3
AWS_STORAGE_BUCKET_NAME = env_var('AWS_STORAGE_BUCKET_NAME', '')
AWS_S3_SECURE_URLS = False  # Use http instead of https
AWS_QUERYSTRING_AUTH = False  # Don't add complex authentication-related query parameters for requests

# Use django-s3-folder-storage to contain static and media folders inside bucket
DEFAULT_FILE_STORAGE = 's3_folder_storage.s3.DefaultStorage'
DEFAULT_S3_PATH = 'media'
STATICFILES_STORAGE = 's3_folder_storage.s3.StaticStorage'
STATIC_S3_PATH = 'static'

# Paths to statics and media
MEDIA_ROOT = '/%s/' % DEFAULT_S3_PATH
STATIC_ROOT = "/%s/" % STATIC_S3_PATH
MEDIA_URL = 'http://%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = 'http://%s.s3.amazonaws.com/static/' % AWS_STORAGE_BUCKET_NAME

# SMTP with Amazon SES
# https://github.com/bancek/django-smtp-ssl
EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
EMAIL_HOST = 'email-smtp.us-east-1.amazonaws.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = env_var('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = env_var('EMAIL_HOST_PASSWORD', '')
DEFAULT_FROM_EMAIL = env_var('DEFAULT_FROM_EMAIL', '')

# Nomadblog
POST_MODEL = 'blog.NomadPost'
DEFAULT_BLOG_SLUG = 'blog'

# Specially useful for apps that depend on custom user
SOUTH_MIGRATION_MODULES = {
    'nomadblog': 'website.nomadblog_migrations',
}

# Allow sending emails for new contact forms, etc
SEND_EMAIL_NOTIFICATIONS = env_var('SEND_EMAIL_NOTIFICATIONS', False)

# See localsettings.py for how to enable the toolbar
ENABLE_DEBUG_TOOLBAR = env_var('ENABLE_DEBUG_TOOLBAR', False)

# If False, it will use S3
LOCAL_STORAGE = env_var('LOCAL_STORAGE', False)

TEMPLATE_EXTRA_CONTEXT = {
    # Site url, no trailing slah (me no like contrib.sites, ugh)
    'site_url': env_var('SITE_URL', 'http://www.nomadblue.com'),
    # Compile LESS using client-side Javascript (only for dev envs!)
    'use_less': env_var('USE_LESS', False),
    # Use holder.js to dinamically render local customizable placeholders
    'use_holder_js': env_var('USE_HOLDER_JS', False),
    # Inject some CSS hacks as helpers to scaffolding, styling, etc
    'use_dev_css': env_var('USE_DEV_CSS', False),
    # Use proper locale in FB open graph
    'og_locale': env_var('OG_LOCALE', 'en_US'),
    # Switch to this site
    'alt_site': env_var('ALT_SITE', 'http://www.nomadblue.cl'),
    # Switch to this site link text
    'alt_site_text': env_var('ALT_SITE_TEXT', 'Español'),
    # Show google analytics tracking code for proper site
    'ga_template_path': env_var('GA_TEMPLATE_PATH', "website/includes/ga_nomadblue_com.html"),
}

try:
    from nomadweb.localsettings import *
except:
    pass
