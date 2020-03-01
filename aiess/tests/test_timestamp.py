from datetime import datetime
import os

import aiess.timestamp

def test_get_missing_created():
    time_id = "test_missing"
    expected_path = timestamp.get_path(time_id)

    assert not timestamp.exists(time_id)
    assert not os.path.exists(expected_path)

    time_empty = timestamp.get_last(time_id)
    time_delta = datetime.utcnow() - time_empty

    assert timestamp.exists(time_id)
    assert os.path.exists(expected_path)
    os.remove(expected_path)

    assert not timestamp.exists(time_id)
    assert time_delta.total_seconds() < 1

def test_get_set():
    new_time = datetime.utcnow()
    assert timestamp.get_last("test") < new_time

    timestamp.set_last(new_time, "test")
    assert abs((new_time - timestamp.get_last("test")).total_seconds()) < 1

def test_exists():
    assert timestamp.exists("test_missing") == False
    assert timestamp.exists("test") == True