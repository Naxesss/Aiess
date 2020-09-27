from typing import Generator, List, Iterable, Callable
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

class Scope():
    """Determines which events should be read in a Reader. The `sql_target` WHERE clause is used
    whenever events are retrieved using this scope."""
    def __init__(self, name: str, sql_target: str="TRUE"):
        self.name = name
        self.sql_target = sql_target

class Reader():
    """This has an async method `run`, which starts a loop that reads Aiess events every 10 seconds.

    If an event is found that is after an internal timestamp (initially current time on first run),
    then `on_event` is called with this; basically called for every new event.

    For each of these reads, `on_event_batch` is called, regardless of if any new events were found.
    
    Use this by creating a class inheriting Reader, and override above methods with custom functionality."""
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
            await self.__push_all_new_events()
            await asyncio.sleep(10)

    async def __push_all_new_events(self) -> None:
        """Triggers the on_event method for each new event since the last stored datetime for each scope."""
        news_target   = f"type=\"{types.NEWS}\""
        groups_target = f"type=\"{types.ADD}\" OR type=\"{types.REMOVE}\""

        await self.__push_new_events(Scope("mapset", sql_target=f"NOT ({news_target}) AND NOT ({groups_target})"))
        await self.__push_new_events(Scope("news",   sql_target=news_target))
        await self.__push_new_events(Scope("groups", sql_target=groups_target))

    async def __push_new_events(self, scope: Scope) -> None:
        """Triggers the on_event method for each new event since the last stored datetime for the given scope."""
        last_time = timestamp.get_last(self.__time_id(scope))
        await self.__push_events_between(last_time, datetime.utcnow(), scope)
    
    async def __push_events_between(self, last_time: datetime, current_time: datetime, scope: Scope) -> datetime:
        """Triggers the on_event method for each event between the two datetimes.
        Updates the last stored datetime after each on_event call."""
        await self.on_event_batch()
        async for event in await self.events_between(last_time, current_time, scope.sql_target):
            await self.on_event(event)
            timestamp.set_last(event.time, self.__time_id(scope))

    def __time_id(self, scope: Scope):
        """Returns the identifier of the file the reader creates to keep track of the last time for this scope.
        This is based on the identifier supplied to the reader on initialization."""
        return f"reader-{self.reader_id}-{scope.name}"

    async def events_between(self, _from: datetime, to: datetime, sql_target: str="TRUE") -> Generator[Event, None, None]:
        """Yields each event found in the database, from (excluding) the later time to (including) the earlier time.
        Optionally only retrieves events matching the `sql_target` WHERE clause."""
        return self.database.retrieve_events(where=f"({sql_target}) AND time > %s AND time <= %s ORDER BY time ASC", where_values=(_from, to))

    async def on_event_batch(self) -> None:
        """Called for each new event batch found in the running loop of the reader.
        This happens before on_event is called for each event."""

    async def on_event(self, event: Event) -> None:
        """Called for each new event found in the running loop of the reader."""

def merge_concurrent(events: Iterable[Event]) -> List[Event]:
    """Returns a list of events where certain concurrent events are merged
    (e.g. user nominates + system qualifies -> user qualifies)."""
    # `dict.fromkeys` removes duplicates in the db, as keys in a dictonary are unique. We essentially merge same events.
    # This is copied such that any modification we make to this list won't affect the original references.
    new_events = list(dict.fromkeys(copy.deepcopy(list(events))))
    merged_events = []

    # `reversed(new_events)` is to go through events closer to each other first.
    for event, other_event in itertools.permutations(reversed(new_events), 2):
        # The system event is rarely 1 second late, hence the leniency.
        if abs((event.time - other_event.time).total_seconds()) > 1:
            continue

        if event.beatmapset != other_event.beatmapset:
            continue

        if (event.type, other_event.type) in MERGABLE_TYPES:
            if event in merged_events or other_event in merged_events:
                # This would result in lost information (e.g. overriding a user attribute).
                continue

            # Ensure that we have not already merged this event (e.g. nominate 1s <- nominate 0s <- qualify 0s).
            if other_event in new_events:
                # Former event has all properties the second does and more,
                # and is represented better having the type of the latter.
                event.type = other_event.type
                merged_events.append(event)
                new_events.remove(other_event)

    return new_events