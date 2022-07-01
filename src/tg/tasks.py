from celery import current_app
from utils import get_phrase
from tg.app import get_tg_app


@current_app.task
def update_bio():
    tg = get_tg_app()
    if not tg.is_initialized:
        tg.start()
    tg.update_profile(bio=get_phrase())
