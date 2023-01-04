import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "em_asd.settings")
app = Celery("em_asd")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
