from celery import Celery
from celery.schedules import crontab
from settings import CELERY_REDIS_BROKER

app = Celery('bioRotator', broker=CELERY_REDIS_BROKER)
app.conf.beat_schedule = {
    'rotate-bio': {
        'task': 'tg.tasks.update_bio',
        'schedule': crontab(hour=2, minute=32)
    }
}

app.autodiscover_tasks(['tg'])
