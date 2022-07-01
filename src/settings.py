from pathlib import Path
from os import environ

BASE_DIR = Path(__file__).resolve().parent
STORAGE_DIR = BASE_DIR / 'storage'
DB_PATH = STORAGE_DIR / 'db.db'
CELERY_REDIS_BROKER = environ.get("CELERY_REDIS_BROKER", 'redis://localhost:6379/0/')
TG_API_ID = environ.get("TG_API_ID")
TG_API_HASH = environ.get("TG_API_HASH")