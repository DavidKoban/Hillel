from celery import Celery
from celery.schedules import crontab
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'send_email.settings')
app = Celery('send_email')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.beat_schedule = {
    'send-spam-every-10-minute':{
        'task': 'Garden.tasks.send_beat_email',
        'schedule': crontab(minute='*/10'),
    }
}
