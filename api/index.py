import os
import sys

# add project path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# set settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'niveda.settings')

# setup django
import django
django.setup()

# import application
from django.core.handlers.wsgi import WSGIHandler

app = WSGIHandler()
