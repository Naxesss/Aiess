import sys
sys.path.append('..')

import mock

from discord import Game

from bot.prefixes import DEFAULT_PREFIX
from bot.activity import get_activity

def test_activity():
    mock_client = mock.MagicMock()
    mock_client.guilds = [object()] * 3
    assert get_activity(mock_client) == Game("+help | 3 servers")