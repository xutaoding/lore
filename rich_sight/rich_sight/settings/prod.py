from .base import *

DJANGO_SETTINGS_MODULE = 'rich_sight.settings.prod'

DEBUG = False

WSGI_APPLICATION = 'rich_sight.wsgi_prod.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'article',
        'HOST': 'xxx.xxx.xxx.xxx',
        'PORT': 3306,
        'USER': 'root',
        'PASSEORD': ''
    }
}

INSTALLED_APPS += []

