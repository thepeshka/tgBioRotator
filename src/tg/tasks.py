from celery import current_app
from utils import get_phrase
from tg.app import get_tg_app


@current_app.task
def update_bio():
    with get_tg_app() as tg:
        tg.update_profile(bio=get_phrase())
