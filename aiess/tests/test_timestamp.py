from datetime import datetime
import os
from contextlib import suppress

from aiess import timestamp

def test_get_missing_created():
    time_id = "test_missing"
    expected_path = timestamp.get_path(time_id)
    with suppress(OSError):
        os.remove(expected_path)

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
    assert not timestamp.exists("test_missing")
    assert timestamp.exists("test")

def test_from_string():
    assert timestamp.from_string("2020-01-12 05:00:00")

def test_from_string_alt():
    assert timestamp.from_string("2020-01-12T05:00:00+00:00")

def test_from_string_alt_2():
    assert timestamp.from_string("2020-01-12T05:00:00.302Z")