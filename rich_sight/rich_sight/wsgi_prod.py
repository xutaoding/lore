import os
import sys
from os.path import dirname, abspath

import django
from django.core.handlers.wsgi import WSGIHandler

sys.path.append(dirname(dirname(abspath(__file__))))

from .settings.prod import DJANGO_SETTINGS_MODULE

os.environ.setdefault("DJANGO_SETTINGS_MODULE", DJANGO_SETTINGS_MODULE)
django.setup()
application = WSGIHandler()
