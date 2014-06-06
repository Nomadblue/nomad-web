import os
import settings

# ########### BEGIN -- Edit your settings ###
# The following constants are joined to build STATIC_ROOT and MEDIA_ROOT
MEDIA_CONTAINER_PATH = '/path/to/prj_media/'
STATIC_CONTAINER_PATH = '/path/to/prj_static/'
PRJ_NAME = 'django_project_name'
# ########### END -- No need to edit anything more below this section ###

# Fallback to default storage and media serve from local filesystem
if getattr(settings, 'LOCAL_STORAGE', False):
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
    DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
    STATIC_ROOT = os.path.join(STATIC_CONTAINER_PATH, PRJ_NAME)
    MEDIA_ROOT = os.path.join(MEDIA_CONTAINER_PATH, PRJ_NAME)
    STATIC_URL = '/static/'
    MEDIA_URL = '/media/'

# Django debug toolbar
if getattr(settings, 'ENABLE_DEBUG_TOOLBAR', False):
    try:
        from debug_toolbar import VERSION
    except ImportError:
        pass
    else:
        DEBUG_TOOLBAR_VERSION = VERSION  # Dummy assign to avoid flake8 complain
        from settings import INSTALLED_APPS
        INSTALLED_APPS = INSTALLED_APPS + ('debug_toolbar',)
