import sys
sys.path.append('..')

import pytest
from datetime import datetime
from time import sleep

from bot.tests.commands.mock_command import MockCommand, MockMessage, MockChannel, MockClient
from bot.cmd_modules import cmd_ping
from bot.receiver import receive_command

@pytest.mark.asyncio
async def test_ping():
    mock_channel = MockChannel()
    mock_client = MockClient(latency=0.13429)
    mock_message = MockMessage(channel=mock_channel)
    mock_command = MockCommand("ping", context=mock_message, client=mock_client)
    
    assert await receive_command(mock_command)
    assert mock_command.response == "134 ms"
    assert mock_channel.messages[0].content == "134 ms"

@pytest.mark.asyncio
async def test_ping_small():
    mock_client = MockClient(latency=0.00029)
    mock_message = MockMessage(channel=MockChannel())
    mock_command = MockCommand("ping", context=mock_message, client=mock_client)

    assert await receive_command(mock_command)
    assert mock_command.response == "< 1 ms"