import pytest

import aiess
from aiess import Event
from aiess import timestamp
from aiess.database import Database

received_events = []

class Reader(aiess.Reader):
    def __init__(self, reader_id: str):
        super().__init__(reader_id)
        self.database = Database("aiess_test")

    def on_event(self, event: Event):
        received_events.append(event)

@pytest.fixture
def reader():
    global received_events
    received_events = []

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