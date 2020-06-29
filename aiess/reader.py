from typing import Generator, List, Iterable
from datetime import datetime
import itertools
import asyncio
import copy

from aiess import Event
from aiess.database import Database
from aiess import timestamp
from aiess import event_types as types

# The former element takes the type of the second, which is removed.
MERGABLE_TYPES = [
    (types.NOMINATE, types.QUALIFY),
    (types.PROBLEM,  types.RESET),
    (types.PROBLEM,  types.DISQUALIFY),
    (types.REPLY,    types.RESOLVE),
    (types.REPLY,    types.REOPEN)
]

class Reader():
    """This constitutes an object from which a loop, looking through new events in the database, can be executed.
    In this case, "new" refers to any event after the previously stored datetime in the respective file,
    named after the given identifier.
    
    Use this by creating a class inheriting Reader, and override methods (e.g. on_event) as desired."""
    def __init__(self, reader_id: str, db_name: str):
        self.reader_id = reader_id
        self.database = Database(db_name)
        self.running = False

    async def run(self) -> None:
        """A blocking method which initiates a loop looking through events in the database.
        This is from where on_event is called, for each new event found.
        
        Being a blocking call, any statement after calling this method will not be executed,
        so place this after any setup code."""
        if self.running:
            raise ValueError("Reader is already running.")

        self.running = True
        while True:
            await self.__push_new_events()
            await asyncio.sleep(10)

    async def __push_new_events(self) -> None:
        """Triggers the on_event method for each new event since the last stored datetime.
        Updates the last stored datetime after each on_event call."""
        last_time = timestamp.get_last(self.__time_id())
        await self.__push_events_between(last_time, datetime.utcnow())
    
    async def __push_events_between(self, last_time: datetime, current_time: datetime) -> datetime:
        """Triggers the on_event method for each event between the two datetimes."""
        await self.on_event_batch()
        async for event in await self.events_between(last_time, current_time):
            await self.on_event(event)
            timestamp.set_last(event.time, self.__time_id())

    def __time_id(self):
        """Returns the identifier of the file the reader creates to keep track of the last time.
        This is based on the identifier supplied to the reader on initialization."""
        return f"reader-{self.reader_id}"

    async def events_between(self, _from: datetime, to: datetime) -> Generator[Event, None, None]:
        """Yields each event found in the database, from (excluding) the first time to (including) the second time."""
        return self.database.retrieve_events(where="time > %s AND time <= %s", where_values=(_from, to))

    async def on_event_batch(self) -> None:
        """Called for each new event batch found in the running loop of the reader.
        This happens before on_event is called for each event."""

    async def on_event(self, event: Event) -> None:
        """Called for each new event found in the running loop of the reader."""

def merge_concurrent(events: Iterable[Event]) -> List[Event]:
    """Returns a list of events where certain types of events are combined if they happened together
    (e.g. user nominates + system qualifies -> user qualifies)."""
    # `dict.fromkeys` removes duplicates in the db, as keys in a dictonary are unique. We essentially merge same events.
    # This is copied such that any modification we make to this list won't affect the original references.
    new_events = list(dict.fromkeys(copy.deepcopy(list(events))))

    for event, other_event in itertools.permutations(new_events, 2):
        # The system event is rarely 1 second late, hence the leniency.
        if abs((event.time - other_event.time).total_seconds()) > 1:
            continue

        if event.beatmapset != other_event.beatmapset:
            continue

        if (event.type, other_event.type) in MERGABLE_TYPES:
            # Former event has all properties the second does and more,
            # and is represented better having the type of the latter.
            event.type = other_event.type
            if other_event in new_events:
                new_events.remove(other_event)

    return new_events