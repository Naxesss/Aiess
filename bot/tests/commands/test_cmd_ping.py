import sys
sys.path.append('..')

import pytest

from bot.tests.commands.mock_command import MockCommand, MockMessage, MockChannel
from bot.cmd_modules import cmd_ping
from bot.receiver import receive_command

@pytest.mark.asyncio
async def test_ping():
    mock_channel = MockChannel()
    mock_command = MockCommand("ping", context=MockMessage(channel=mock_channel))
    
    assert await receive_command(mock_command)
    assert mock_command.response == "pong"
    assert mock_channel.messages[0].content == "pong"