import sys
sys.path.append('..')

import mock
import pytest
from datetime import datetime

from discord import Game, Status

from aiess import timestamp

from bot.prefixes import DEFAULT_PREFIX
from bot.activity import get_activity
from bot.activity import get_status

def test_activity():
    mock_client = mock.MagicMock()
    mock_client.guilds = [object()] * 3
    assert get_activity(mock_client) == Game("+help | 3 servers")

def test_activity_singular():
    mock_client = mock.MagicMock()
    mock_client.guilds = [object()] * 1
    assert get_activity(mock_client) == Game("+help | 1 server")


@pytest.fixture
def mock_reader():
    reader = mock.MagicMock()
    reader.last_heartbeat = timestamp.from_string("2020-01-01 00:00:00")
    return reader

def test_status_online(mock_reader):
    with mock.patch("bot.activity.datetime") as mock_datetime:
        # Mock `datetime.utcnow`, but retain the original datetime class functionality through the `side_effect` attribute.
        mock_datetime.utcnow.return_value = timestamp.from_string("2020-01-01 00:00:31")
        mock_datetime.side_effect = datetime

        assert get_status(mock_reader) == Status.online

def test_status_idle(mock_reader):
    with mock.patch("bot.activity.datetime") as mock_datetime:
        mock_datetime.utcnow.return_value = timestamp.from_string("2020-01-01 00:30:01")
        mock_datetime.side_effect = datetime

        assert get_status(mock_reader) == Status.idle

def test_status_do_not_disturb(mock_reader):
    with mock.patch("bot.activity.datetime") as mock_datetime:
        mock_datetime.utcnow.return_value = timestamp.from_string("2020-01-01 01:00:01")
        mock_datetime.side_effect = datetime

        assert get_status(mock_reader) == Status.do_not_disturb