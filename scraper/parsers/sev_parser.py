import sys
sys.path.append('..')

from typing import Generator, List
from bs4 import BeautifulSoup
from datetime import datetime

from aiess.errors import DeletedContextError
from aiess import Event
from aiess import event_types as types
from aiess.database import Database, SCRAPER_DB_NAME

def parse(discussion_id: int, obv: int, sev: int, time: datetime) -> Event:
    """Returns an SEV event representing the given discussion and sev/obv arguments."""
    discussion = Database(SCRAPER_DB_NAME).retrieve_discussion("id=%s", (discussion_id,))
    if discussion is None:
        raise DeletedContextError("Missing discussion, it's possible the mapset was deleted.")
    if sev is None and obv is None:
        raise DeletedContextError("Neither severity nor obviousness have been set, so this is incomplete.")

    # Since the values we process here are *changes*, we need to populate the *current* state as well.
    # obv/sev as None means no change, -1 means set to null, so we swap those values accordingly.
    old_obv = obv
    old_sev = sev
    cached_obv, cached_sev = Database(SCRAPER_DB_NAME).retrieve_obv_sev(discussion_id=discussion_id)
    if obv is None: obv = cached_obv
    if sev is None: sev = cached_sev
    if obv == -1: obv = None
    if sev == -1: sev = None

    obv_str = str(obv) if obv is not None else "?"
    sev_str = str(sev) if sev is not None else "?"

    #if old_obv == cached_obv and old_sev == cached_sev:
    #    raise DeletedContextError(""
    #        "Whatever happened before this changed the obv/sev is irrelevant, as it seems to have been changed back.")

    return Event(
            _type      = types.SEV,
            time       = time,
            beatmapset = discussion.beatmapset,
            discussion = discussion,
            content    = f"{obv_str}/{sev_str}"
        )