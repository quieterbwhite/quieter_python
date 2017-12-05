"""
WSGI config for zoowatch project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from logs.mylog import flogger

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zoowatch.settings")

flogger.info("before get_wsgi_application")

application = get_wsgi_application()

flogger.info("after get_wsgi_application")

