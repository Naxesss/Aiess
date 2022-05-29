import sys
sys.path.append('..')

import mock
import pytest
from datetime import datetime

from discord import Game, Status

from aiess import timestamp

from bot.activity import get_activity
from bot.activity import get_status

@pytest.fixture
def mock_client():
    client = mock.MagicMock()
    client.guilds = [object()] * 3
    client.is_ready = lambda: True
    return client

@pytest.fixture
def mock_reader():
    reader = mock.MagicMock()
    reader.latest_event_time = None
    return reader

def test_activity(mock_client, mock_reader):
    assert get_activity(mock_client, mock_reader) == Game("/subscribe | 3 servers")

def test_activity_singular(mock_client, mock_reader):
    mock_client.guilds = [object()] * 1
    assert get_activity(mock_client, mock_reader) == Game("/subscribe | 1 server")

def test_activity_not_ready(mock_client, mock_reader):
    mock_client.is_ready = lambda: False
    assert get_activity(mock_client, mock_reader) == Game("/subscribe | Starting...")

def test_activity_delay_small(mock_client, mock_reader):
    mock_reader.latest_event_time = timestamp.from_string("2020-01-01 00:00:00")
    
    with mock.patch("bot.activity.datetime") as mock_datetime:
        mock_datetime.utcnow.return_value = timestamp.from_string("2020-01-01 00:03:30")
        mock_datetime.side_effect = datetime

        # Delay is too small to be worth displaying here.
        assert get_activity(mock_client, mock_reader) == Game("/subscribe | 3 servers")

def test_activity_delay_large(mock_client, mock_reader):
    mock_reader.latest_event_time = timestamp.from_string("2020-01-01 00:00:00")
    
    with mock.patch("bot.activity.datetime") as mock_datetime:
        mock_datetime.utcnow.return_value = timestamp.from_string("2020-01-01 04:01:30")
        mock_datetime.side_effect = datetime

        assert get_activity(mock_client, mock_reader) == Game("/subscribe | 3 servers | 4 hours delay")



def test_status_no_event_time(mock_client, mock_reader):
    with mock.patch("bot.activity.datetime") as mock_datetime:
        # Mock `datetime.utcnow`, but retain the original datetime class functionality through the `side_effect` attribute.
        mock_datetime.utcnow.return_value = timestamp.from_string("2020-01-01 00:00:31")
        mock_datetime.side_effect = datetime

        assert get_status(mock_client, mock_reader) == Status.do_not_disturb

def test_status_online(mock_client, mock_reader):
    mock_reader.latest_event_time = timestamp.from_string("2020-01-01 00:00:00")
    
    with mock.patch("bot.activity.datetime") as mock_datetime:
        mock_datetime.utcnow.return_value = timestamp.from_string("2020-01-01 00:00:31")
        mock_datetime.side_effect = datetime

        assert get_status(mock_client, mock_reader) == Status.online

def test_status_idle(mock_client, mock_reader):
    mock_reader.latest_event_time = timestamp.from_string("2020-01-01 00:00:00")
    
    with mock.patch("bot.activity.datetime") as mock_datetime:
        mock_datetime.utcnow.return_value = timestamp.from_string("2020-01-01 00:30:01")
        mock_datetime.side_effect = datetime

        assert get_status(mock_client, mock_reader) == Status.idle

def test_status_do_not_disturb(mock_client, mock_reader):
    mock_reader.latest_event_time = timestamp.from_string("2020-01-01 00:00:00")
    
    with mock.patch("bot.activity.datetime") as mock_datetime:
        mock_datetime.utcnow.return_value = timestamp.from_string("2020-01-01 02:00:01")
        mock_datetime.side_effect = datetime

        assert get_status(mock_client, mock_reader) == Status.do_not_disturb

def test_status_not_ready(mock_client, mock_reader):
    mock_client.is_ready = lambda: False

    with mock.patch("bot.activity.datetime") as mock_datetime:
        mock_datetime.utcnow.return_value = timestamp.from_string("2020-01-01 00:00:00")
        mock_datetime.side_effect = datetime

        assert get_status(mock_client, mock_reader) == Status.do_not_disturb