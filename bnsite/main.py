import sys
sys.path.append('..')

import aiess
from aiess.reader import Reader
from aiess.database import SCRAPER_DB_NAME
from aiess.logger import log
from aiess import event_types as types

from bnsite import interface

EXPECTED_TYPES = [
    types.NOMINATE,
    types.QUALIFY,
    types.NOMINATION_RESET,
    types.DISQUALIFY,
    types.RANK,
    types.LOVE
]

class Reader(aiess.Reader):
    async def on_event(self, event: Event):
        log(event, postfix=self.reader_id)
        if event.type in EXPECTED_TYPES:
            interface.insert_event(event)

reader = Reader("bnsite", db_name=SCRAPER_DB_NAME)
reader.run()