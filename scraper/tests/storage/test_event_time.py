from datetime import datetime
import os

from storage import event_time

def test_get_missing_created():
    time_id = "test_missing"
    expected_path = event_time.get_path(time_id)

    assert not event_time.exists(time_id)
    assert not os.path.exists(expected_path)

    time_empty = event_time.get_last(time_id)
    time_delta = datetime.utcnow() - time_empty

    assert event_time.exists(time_id)
    assert os.path.exists(expected_path)
    os.remove(expected_path)

    assert not event_time.exists(time_id)
    assert time_delta.total_seconds() < 1

def test_get_set():
    new_time = datetime.utcnow()
    assert event_time.get_last("test") < new_time

    event_time.set_last(new_time, "test")
    assert abs((new_time - event_time.get_last("test")).total_seconds()) < 1

def test_exists():
    assert event_time.exists("test_missing") == False
    assert event_time.exists("test") == True