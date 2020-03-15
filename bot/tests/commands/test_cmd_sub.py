import pytest

from tests.mock_command import MockGuild, MockChannel, MockMessage, MockCommand
from cmd_modules import cmd_sub
from receiver import receive_command
from subscriptions import Subscription
import subscriber

@pytest.mark.asyncio
async def test_sub():
    channel = MockChannel(1, MockGuild(3))
    sub = Subscription(guild_id=3, channel_id=1, _filter="type:suggestion")

    mock_command = MockCommand("sub", "type:suggestion", context=MockMessage(channel))
    await receive_command(mock_command)

    assert "✓" in mock_command.response
    assert sub in subscriber.cache

@pytest.mark.asyncio
async def test_sub_no_arg():
    mock_command = MockCommand("sub")
    await receive_command(mock_command)
    assert "✗" in mock_command.response