from typing import Generator, List
from datetime import datetime
import asyncio

from aiess.objects import Event
from aiess.database import database
from aiess import timestamp
from aiess import event_types as types

# The former element takes the type of the second, which is removed.
mergable_types = [
    (types.NOMINATE, types.QUALIFY),
    (types.PROBLEM,  types.RESET),
    (types.PROBLEM,  types.DISQUALIFY),
    (types.REPLY,    types.RESOLVE),
    (types.REPLY,    types.REOPEN)
]

class Reader():
    """This constitutes an object from which a loop looking through new events in the database can be executed.
    In this case, "new" refers to any event after the previously stored datetime in the respective file,
    named after the given identifier.
    
    Use this by creating a class inheriting Reader, and override methods (e.g. on_event) as desired."""
    def __init__(self, reader_id: str):
        self.reader_id = reader_id
        self.database = database
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
        Updates the last stored datetime to the current time afterwards."""
        last_time = timestamp.get_last(self.__time_id())

        current_time = await self.__push_events_between(last_time, datetime.utcnow())
        
        if current_time:
            timestamp.set_last(current_time, self.__time_id())
    
    async def __push_events_between(self, last_time: datetime, current_time: datetime) -> datetime:
        """Triggers the on_event method for each event between the two datetimes.
        Returns the last event's datetime, if any, otherwise None."""
        events = list(self.events_between(last_time, current_time))
        if not events:
            return None

        merged_events = self.merge_concurrent(events)
        await self.on_events(merged_events)
        for event in merged_events:
            await self.on_event(event)

        last_event = merged_events[-1]
        return last_event.time if last_event else None

    def __time_id(self):
        """Returns the identifier of the file the reader creates to keep track of the last time.
        This is based on the identifier supplied to the reader on initialization."""
        return f"reader-{self.reader_id}"

    def events_between(self, _from: datetime, to: datetime) -> Generator[Event, None, None]:
        """Yields each event found in the database, from (excluding) the first time to (including) the second time."""
        return self.database.retrieve_events(f"time > \"{_from}\" AND time <= \"{to}\"")

    def merge_concurrent(self, events: List[Event]) -> List[Event]:
        """Returns a list of events where certain types of events are combined if they happened together
        (e.g. user nominates + system qualifies -> user qualifies)."""
        for event in events:
            for other_event in events:
                if event.time != other_event.time:
                    continue

                if (event.type, other_event.type) in mergable_types:
                    # Former event has all properties the second does and more,
                    # and is represented better having the type of the latter.
                    event.type = other_event.type
                    other_event.marked_for_deletion = True

        return list(filter(lambda event: not event.marked_for_deletion, events))

    async def on_events(self, events: List[Event]) -> None:
        """Called for each new event batch found in the running loop of the reader.
        
        Some types of events in this batch are merged together if concurrent
        (e.g. user nominates + system qualifies -> user qualifies)."""
        pass

    async def on_event(self, event: Event) -> None:
        """Called for each new event found in the running loop of the reader.
        
        Some types of events are merged together if concurrent
        (e.g. user nominates + system qualifies -> user qualifies)."""
        pass