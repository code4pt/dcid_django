import os, sys

sys.path.append('c:/wamp/www/dcid')
os.environ['DJANGO_SETTINGS_MODULE'] = 'dcid.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()