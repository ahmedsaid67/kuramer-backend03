from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first.settings')

app = Celery('first')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
