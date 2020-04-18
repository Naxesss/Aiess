from typing import Callable, Generator, List
from datetime import datetime
import asyncio

from aiess.objects import Event
from aiess.database import database
from aiess import timestamp

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
        # Needs to be a separate generator from the loop, would otherwise become exhausted.
        await self.on_event_batch(self.events_between(last_time, current_time))

        last_event = None
        for event in self.events_between(last_time, current_time):
            last_event = event
        
        return last_event.time if last_event else None

    def __time_id(self):
        """Returns the identifier of the file the reader creates to keep track of the last time.
        This is based on the identifier supplied to the reader on initialization."""
        return f"reader-{self.reader_id}"

    def events_between(self, _from: datetime, to: datetime) -> Generator[Event, None, None]:
        """Yields each event found in the database, from (excluding) the first time to (including) the second time."""
        return self.database.retrieve_events(f"time > \"{_from}\" AND time <= \"{to}\"")


    async def on_events(self, events: List[Event]) -> None:
        """Called for each new event batch found in the running loop of the reader.
        A batch of events always include every event up to and equal to the last time,
        since the previous batch."""
        pass