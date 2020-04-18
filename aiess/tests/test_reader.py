import pytest
from typing import List

import aiess
from aiess import Event
from aiess import timestamp
from aiess.database import Database

received_event_batches = []

class Reader(aiess.Reader):
    def __init__(self, reader_id: str):
        super().__init__(reader_id)
        self.database = Database("aiess_test")
    
    async def on_events(self, events: List[Event]):
        received_event_batches.append(events)

@pytest.fixture
def reader():
    global received_events
    global received_event_batches
    received_events = []
    received_event_batches = []

    temp_reader = Reader("test")
    temp_reader.database.clear_table_data("events")
    return temp_reader

def test_file_created(reader):
    expected_id = reader._Reader__time_id()
    reader._Reader__push_new_events()

    assert "test" in expected_id
    assert timestamp.exists(expected_id)

def test_events_between(reader):
    event1 = Event(_type="test", time=timestamp.from_string("2020-01-01 05:00:00"))
    event2 = Event(_type="test", time=timestamp.from_string("2020-01-01 07:00:00"))
    event3 = Event(_type="test", time=timestamp.from_string("2020-01-02 03:00:00"))

    reader.database.insert_event(event1)
    reader.database.insert_event(event2)
    reader.database.insert_event(event3)

    all_events = reader.events_between(timestamp.from_string("2020-01-01 00:00:00"), timestamp.from_string("2020-01-03 00:00:00"))
    assert next(all_events, None) == event1
    assert next(all_events, None) == event2
    assert next(all_events, None) == event3
    assert next(all_events, None) == None

    latter_events = reader.events_between(timestamp.from_string("2020-01-01 06:00:00"), timestamp.from_string("2020-01-03 00:00:00"))
    assert next(latter_events, None) == event2
    assert next(latter_events, None) == event3
    assert next(latter_events, None) == None

def test_events_between_greater_than(reader):
    event1 = Event(_type="test", time=timestamp.from_string("2020-01-01 05:00:00"))
    event2 = Event(_type="test", time=timestamp.from_string("2020-01-01 07:00:00"))

    reader.database.insert_event(event1)
    reader.database.insert_event(event2)

    # If we resume at 05:00:00, the event at exactly 05:00:00 should be ignored.
    events = reader.events_between(timestamp.from_string("2020-01-01 05:00:00"), timestamp.from_string("2020-01-01 07:00:00"))
    assert next(events, None) == event2
    assert next(events, None) == None

@pytest.mark.asyncio
async def test_on_event_batch(reader):
    event1 = Event(_type="hello", time=timestamp.from_string("2020-01-01 05:00:00"))
    event2 = Event(_type="there", time=timestamp.from_string("2020-01-01 07:00:00"))
    event3 = Event(_type="hi", time=timestamp.from_string("2020-01-01 11:00:00"))
    event4 = Event(_type="yes", time=timestamp.from_string("2020-01-01 13:00:00"))
    event5 = Event(_type="no", time=timestamp.from_string("2020-01-01 15:00:00"))

    reader.database.insert_event(event1)
    reader.database.insert_event(event2)
    reader.database.insert_event(event3)
    reader.database.insert_event(event4)
    reader.database.insert_event(event5)

    start = timestamp.from_string("2020-01-01 00:00:00")
    middle = timestamp.from_string("2020-01-01 10:00:00")
    end = timestamp.from_string("2020-01-01 18:00:00")
    await reader._Reader__push_events_between(start, middle)
    await reader._Reader__push_events_between(middle, end)

    assert len(received_event_batches) == 2
    assert received_event_batches[0] == [event1, event2]
    assert received_event_batches[1] == [event3, event4, event5]


