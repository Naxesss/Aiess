import sys
sys.path.append('..')

import asyncio

import aiess
from aiess import Event
from aiess.reader import Reader
from aiess.database import SCRAPER_DB_NAME
from aiess import logger
from aiess import event_types as types

from bnplanner import interface

EXPECTED_TYPES = [
    types.NOMINATE,
    types.QUALIFY,
    types.RESET,
    types.DISQUALIFY,
    types.RANK
]

class Reader(aiess.Reader):
    async def on_event(self, event: Event):
        if event.type in EXPECTED_TYPES: #and "catch" in event.beatmapset.modes:
            logger.log(event, postfix=self.reader_id)
            interface.insert_event(event)

logger.init()
reader = Reader("bnplanner", db_name=SCRAPER_DB_NAME)
loop = asyncio.get_event_loop()
loop.run_until_complete(reader.run())