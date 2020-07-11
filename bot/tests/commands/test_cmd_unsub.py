import sys
sys.path.append('..')

import pytest

from bot import subscriber
from bot.subscriptions import Subscription
from bot.tests.commands.mock_command import MockCommand, MockMessage, MockChannel, MockGuild
from bot.cmd_modules import cmd_unsub
from bot.receiver import receive_command
from bot.database import Database, BOT_TEST_DB_NAME

def setup_function():
    database = Database(BOT_TEST_DB_NAME)
    # Reset database to state before any tests ran.
    database.clear_table_data("subscriptions")
    # Use the test database by default, so we don't clutter the production one.
    subscriber.DEFAULT_DB_NAME = BOT_TEST_DB_NAME
    subscriber.cache = []

def test_correct_setup():
    assert not Database(BOT_TEST_DB_NAME).retrieve_table_data("subscriptions")

@pytest.mark.asyncio
async def test_unsub():
    subs = [
        Subscription(guild_id=2, channel_id=6, _filter="type:nominate"),
        Subscription(guild_id=2, channel_id=4, _filter="user:someone"),
        Subscription(guild_id=1, channel_id=6, _filter="type:nominate")
    ]
    database = Database(BOT_TEST_DB_NAME)
    for sub in subs:
        database.insert_subscription(sub)
    subscriber.load()

    mock_message = MockMessage(channel=MockChannel(_id=6, guild=MockGuild(_id=2)))
    mock_command = MockCommand("unsub", context=mock_message)

    assert all(sub in subscriber.cache for sub in subs)
    
    assert await receive_command(mock_command)
    assert mock_command.response.startswith("✓")
    assert "🔕" in mock_command.response_embed.fields[0].name.lower()
    assert "unsubscribed from" in mock_command.response_embed.fields[0].name.lower()
    assert "type:nominate" in mock_command.response_embed.fields[0].value
    assert "`type:nominate`" in mock_command.response_embed.fields[0].value
    assert subs[0] not in subscriber.cache
    assert subs[1] in subscriber.cache
    assert subs[2] in subscriber.cache

@pytest.mark.asyncio
async def test_unsub_no_sub():
    mock_message = MockMessage(channel=MockChannel(_id=6, guild=MockGuild(_id=2)))
    mock_command = MockCommand("unsub", context=mock_message)

    assert not subscriber.cache

    assert await receive_command(mock_command)
    assert mock_command.response.startswith("✓")
    assert "nothing to unsub" in mock_command.response.lower()