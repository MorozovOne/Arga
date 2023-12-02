# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/home/a/abdull57/abdull57.beget.tech/main/main')
sys.path.insert(1, '/home/a/abdull57/abdull57.beget.tech/venv_django/lib/python3.11/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'main.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()