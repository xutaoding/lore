from .base import *

DJANGO_SETTINGS_MODULE = 'rich_sight.settings.dev'

DEBUG = True

WSGI_APPLICATION = 'rich_sight.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'lore',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': 'python'
    }
}

INSTALLED_APPS += [
    'debug_toolbar'
]

# Start Settings django-debug-toolbar

MIDDLEWARE_CLASSES = MIDDLEWARE + ['debug_toolbar.middleware.DebugToolbarMiddleware']
del MIDDLEWARE

INTERNAL_IPS = ['127.0.0.1', '192.167.1.22']

DEBUG_TOOLBAR_PATCH_SETTINGS = False

DEBUG_TOOLBAR_CONFIG = {'JQUERY_URL': r"http://code.jquery.com/jquery-2.1.1.min.js"}

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]
# End Settings django-debug-toolbar
