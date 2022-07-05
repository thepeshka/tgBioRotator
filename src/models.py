from datetime import datetime

from peewee import Model as BaseModel, SqliteDatabase, CharField, ForeignKeyField, DateTimeField
from settings import DB_PATH


database = SqliteDatabase(DB_PATH)
TABLES_CREATED = False


class Model(BaseModel):
    class Meta:
        database = database


class Phrase(Model):
    content = CharField(max_length=140)


class HistoryEntry(Model):
    phrase = ForeignKeyField(Phrase, related_name='history', on_delete='CASCADE')
    created_at = DateTimeField(default=lambda: datetime.now())


def create_tables():
    global TABLES_CREATED
    if not TABLES_CREATED:
        TABLES_CREATED = True
        database.create_tables(Model.__subclasses__())
