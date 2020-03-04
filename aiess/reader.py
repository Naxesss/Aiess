from typing import Callable, Generator
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

    def run(self) -> None:
        """A blocking method which initiates a loop looking through events in the database.
        This is from where on_event is called, for each new event found.
        
        Being a blocking call, any statement after calling this method will not be executed,
        so place this after any setup code."""
        while True:
            self.__push_new_events()

    def __push_new_events(self) -> None:
        """Triggers the on_event method for each new event since the last stored datetime.
        Updates the last stored datetime to the current time afterwards."""
        last_time = timestamp.get_last(self.__time_id())
        current_time = datetime.utcnow()

        self.__push_events_between(last_time, current_time)

        timestamp.set_last(current_time, self.__time_id())
    
    def __push_events_between(self, last_time: datetime, current_time: datetime) -> None:
        """Triggers the on_event method for each event between the two datetimes."""
        loop = asyncio.get_event_loop()
        for event in (events_between(last_time, current_time) or []):
            loop.run_until_complete(self.on_event(event))
    
    def __time_id(self):
        """Returns the identifier of the file the reader creates to keep track of the last time.
        This is based on the identifier supplied to the reader on initialization."""
        return f"reader-{self.reader_id}"

    async def on_event(self, event: Event) -> None:
        """Called for each new event found in the running loop of the reader."""
        pass

def events_between(_from: datetime, to: datetime) -> Generator[Event, None, None]:
    """Yields each new event found in the database, from the given time to the current time."""
    pass