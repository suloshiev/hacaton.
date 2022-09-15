import os
import django
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_app.settings') # путь к настройкам
django.setup()
app = Celery('social_app') # название приложения
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS) # для поисков задач

app.conf.beat_schedule = {
    'send_spam_from_john': {
        'task': 'applications.spam.tasks.spam_email2',
        'schedule': crontab(minute='*/1')
    }
}
