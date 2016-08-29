"""
WSGI config for rich_sight project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
import sys
from os.path import dirname, abspath

from django.core.wsgi import get_wsgi_application

sys.path.append(dirname(dirname(abspath(__file__))))

from .settings.dev import DJANGO_SETTINGS_MODULE

os.environ.setdefault("DJANGO_SETTINGS_MODULE", DJANGO_SETTINGS_MODULE)

application = get_wsgi_application()
