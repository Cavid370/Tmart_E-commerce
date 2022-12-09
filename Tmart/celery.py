from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Tmart.settings')
app = Celery('Tmart')
app.conf.enable_utc=False
app.conf.update(timezone='Asia/Baku')
app.config_from_object(settings, namespace='CELERY')
# Load task modules from all registered Django apps.
# Celery Beat tasks registration
app.autodiscover_tasks(lambda:settings.INSTALLED_APPS)

# app.conf.beat_schedule = {
# 'add-every-sunday': {
# 'task': 'send_mail',
#     'schedule': crontab(hour=0, minute=0,day_of_week="*/1")
# }
# }

app.conf.beat_schedule = {
'add-every-minute': {
'task': 'send_mail',
    'schedule': crontab(minute="*/1")
}
}
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')