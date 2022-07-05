from pyrogram import Client
from settings import STORAGE_DIR, TG_API_HASH, TG_API_ID

app = None


def get_tg_app():
    return Client('sessions', workdir=STORAGE_DIR, api_id=TG_API_ID, api_hash=TG_API_HASH)
