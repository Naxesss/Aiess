import pytest

import aiess
from aiess import Event
from aiess import timestamp

received_events = []

class Reader(aiess.Reader):
    def on_event(self, event: Event):
        received_events.append(event)

@pytest.fixture
def reader():
    global received_events
    received_events = []

    return Reader("test")

def test_file_created(reader):
    expected_id = reader._Reader__time_id()
    reader._Reader__push_new_events()

    assert "test" in expected_id
    assert timestamp.exists(expected_id)

def test_read():
    pass