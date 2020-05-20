import sys
sys.path.append('..')

import pytest

from bot.tests.commands.mock_command import MockCommand
from bot.cmd_modules import cmd_ping
from bot.receiver import receive_command

@pytest.mark.asyncio
async def test_ping():
    mock_command = MockCommand("ping")
    await receive_command(mock_command)
    assert mock_command.response == "pong"