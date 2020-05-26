import pytest
from typing import List

import aiess
from aiess import Event, Beatmapset, User
from aiess import timestamp
from aiess.database import SCRAPER_TEST_DB_NAME
from aiess.reader import merge_concurrent

received_events = []
received_event_batches = []

class Reader(aiess.Reader):
    def __init__(self, reader_id: str):
        super().__init__(reader_id, db_name=SCRAPER_TEST_DB_NAME)
    
    async def on_events(self, events: List[Event]):
        received_event_batches.append(events)
    
    async def on_event(self, event: Event):
        received_events.append(event)

@pytest.fixture
def reader():
    global received_events
    global received_event_batches
    received_events = []
    received_event_batches = []

    temp_reader = Reader("test")
    temp_reader.database.clear_table_data("events")
    return temp_reader

@pytest.mark.asyncio
async def test_file_created(reader):
    expected_id = reader._Reader__time_id()
    await reader._Reader__push_new_events()

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
    assert next(all_events, None) is None

    latter_events = reader.events_between(timestamp.from_string("2020-01-01 06:00:00"), timestamp.from_string("2020-01-03 00:00:00"))
    assert next(latter_events, None) == event2
    assert next(latter_events, None) == event3
    assert next(latter_events, None) is None

def test_events_between_greater_than(reader):
    event1 = Event(_type="test", time=timestamp.from_string("2020-01-01 05:00:00"))
    event2 = Event(_type="test", time=timestamp.from_string("2020-01-01 07:00:00"))

    reader.database.insert_event(event1)
    reader.database.insert_event(event2)

    # If we resume at 05:00:00, the event at exactly 05:00:00 should be ignored.
    events = reader.events_between(timestamp.from_string("2020-01-01 05:00:00"), timestamp.from_string("2020-01-01 07:00:00"))
    assert next(events, None) == event2
    assert next(events, None) is None

@pytest.mark.asyncio
async def test_on_events(reader):
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

@pytest.mark.asyncio
async def test_on_event(reader):
    event1 = Event(_type="hello", time=timestamp.from_string("2020-01-01 05:00:00"))
    event2 = Event(_type="there", time=timestamp.from_string("2020-01-01 07:00:00"))

    reader.database.insert_event(event1)
    reader.database.insert_event(event2)

    _from = timestamp.from_string("2020-01-01 00:00:00")
    to = timestamp.from_string("2020-01-01 10:00:00")
    await reader._Reader__push_events_between(_from, to)

    assert received_events == [event1, event2]

def test_merge_concurrent():
    event1 = Event(_type="nominate", time=timestamp.from_string("2020-01-01 05:00:00"), user=User(1, "someone"))
    event2 = Event(_type="qualify", time=timestamp.from_string("2020-01-01 05:00:00"))
    event3 = Event(_type="something else", time=timestamp.from_string("2020-01-01 07:00:00"))

    merged_events = merge_concurrent([event1, event2, event3])
    assert len(merged_events) == 2
    assert merged_events[0].type == event2.type
    assert merged_events[0].user == event1.user
    assert merged_events[1] == event3

def test_merge_concurrent_different_times():
    event1 = Event(_type="nominate", time=timestamp.from_string("2020-01-01 11:00:00"), user=User(1, "someone"))
    event2 = Event(_type="qualify", time=timestamp.from_string("2020-01-01 13:00:00"))

    merged_events = merge_concurrent([event1, event2])
    assert len(merged_events) == 2
    assert merged_events[0] == event1
    assert merged_events[1] == event2

def test_merge_concurrent_1_second_off():
    event1 = Event(_type="nominate", time=timestamp.from_string("2020-01-01 13:00:00"), user=User(1, "someone"))
    event2 = Event(_type="qualify", time=timestamp.from_string("2020-01-01 13:00:01"))

    merged_events = merge_concurrent([event1, event2])
    assert len(merged_events) == 1
    assert merged_events[0].type == event2.type
    assert merged_events[0].user == event1.user

def test_merge_concurrent_different_beatmapsets():
    beatmapset1 = Beatmapset(1, "artist", "title", User(1, "someone"), modes=["osu"])
    beatmapset2 = Beatmapset(2, "artist", "title", User(2, "sometwo"), modes=["osu"])
    event1 = Event(_type="nominate", time=timestamp.from_string("2020-01-01 13:00:00"), beatmapset=beatmapset1, user=User(1, "someone"))
    event2 = Event(_type="qualify", time=timestamp.from_string("2020-01-01 13:00:01"), beatmapset=beatmapset2)

    merged_events = merge_concurrent([event1, event2])
    assert len(merged_events) == 2
    assert merged_events[0] == event1
    assert merged_events[1] == event2

def test_merge_concurrent_duplicates():
    nom_event1 = Event(_type="nominate", time=timestamp.from_string("2020-01-01 05:00:00"), user=User(1, "someone"))
    nom_event2 = Event(_type="nominate", time=timestamp.from_string("2020-01-01 05:00:00"), user=User(1, "someone"))
    nom_event3 = Event(_type="nominate", time=timestamp.from_string("2020-01-01 05:00:00"), user=User(1, "someone"))
    qual_event1 = Event(_type="qualify", time=timestamp.from_string("2020-01-01 05:00:00"))
    qual_event2 = Event(_type="qualify", time=timestamp.from_string("2020-01-01 05:00:00"))

    merged_events = merge_concurrent([nom_event1, nom_event2, nom_event3, qual_event1, qual_event2])
    assert len(merged_events) == 1
    assert merged_events[0].type == qual_event1.type
    assert merged_events[0].user == nom_event1.user