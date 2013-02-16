import os, sys

sys.path.append('c:/wamp/www/daas')
os.environ['DJANGO_SETTINGS_MODULE'] = 'daas.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()