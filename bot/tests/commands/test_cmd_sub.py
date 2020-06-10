import sys
sys.path.append('..')

import pytest

from bot import subscriber
from bot.tests.commands.mock_command import MockCommand, MockMessage, MockChannel, MockGuild
from bot.cmd_modules import cmd_sub
from bot.receiver import receive_command
from bot.database import Database, BOT_TEST_DB_NAME

def setup_function():
    # Reset database to state before any tests ran.
    Database(BOT_TEST_DB_NAME).clear_table_data("subscriptions")
    # Use the test database by default, so we don't clutter the production one.
    subscriber.DEFAULT_DB_NAME = BOT_TEST_DB_NAME

def test_correct_setup():
    assert not Database(BOT_TEST_DB_NAME).retrieve_table_data("subscriptions")

@pytest.mark.asyncio
async def test_sub():
    mock_message = MockMessage(channel=MockChannel(_id=6, guild=MockGuild(_id=2)))
    mock_command = MockCommand("sub", "type:nominate", context=mock_message)

    assert await receive_command(mock_command)
    assert mock_command.response.startswith("✓")
    assert subscriber.cache[0].channel_id == mock_message.channel.id
    assert subscriber.cache[0].filter == mock_command.args[0]

@pytest.mark.asyncio
async def test_sub_no_arg():
    mock_message = MockMessage(channel=MockChannel(_id=6, guild=MockGuild(_id=2)))
    mock_command = MockCommand("sub", context=mock_message)

    assert await receive_command(mock_command)
    assert mock_command.response.startswith("✗")