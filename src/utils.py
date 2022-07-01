from peewee import fn

from models import Phrase, HistoryEntry


def add_phrase(content):
    phrase = Phrase()
    phrase.content = content
    phrase.save()
    return phrase


def get_phrase():
    history_entry = HistoryEntry.select().order_by("-created_at").first()
    phrase = Phrase.select()
    if history_entry:
        phrase = phrase.filter(Phrase.id != history_entry.id)
    phrase = phrase.order_by(fn.Random()).first()
    if not phrase:
        raise EnvironmentError("There is no phrases in db. Use utils.add_phrase to add phrases!")
    history_entry = HistoryEntry()
    history_entry.phrase = phrase
    history_entry.save()
    return phrase.content
