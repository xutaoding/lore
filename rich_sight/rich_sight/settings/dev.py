from .base import *

DJANGO_SETTINGS_MODULE = 'rich_sight.settings.dev'

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
    # 'debug_toolbar'
]
