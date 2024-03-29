import sys
sys.path.append('..')

import pytest
import asyncio
from mock import patch
from datetime import datetime

from aiess import Event

from bot import subscriber
from bot.objects import Subscription
from bot.database import Database, BOT_TEST_DB_NAME

def setup_function():
    subscriber.DEFAULT_DB_NAME = BOT_TEST_DB_NAME
    # Reset database to state before any tests ran.
    Database(BOT_TEST_DB_NAME).clear_table_data("subscriptions")

def test_correct_setup():
    assert not Database(BOT_TEST_DB_NAME).retrieve_table_data("subscriptions")

def test_load():
    sub1 = Subscription(guild_id=1, channel_id=1, _filter="type:nominate")
    sub2 = Subscription(guild_id=1, channel_id=2, _filter="type:ranked")

    database = Database(BOT_TEST_DB_NAME)
    database.insert_subscription(sub1)
    database.insert_subscription(sub2)

    subscriber.load()

    assert sub1 in subscriber.cache
    assert sub2 in subscriber.cache

def test_add_subscription():
    sub1 = Subscription(guild_id=1, channel_id=1, _filter="type:nominate")
    sub2 = Subscription(guild_id=1, channel_id=2, _filter="type:ranked")
    sub3 = Subscription(guild_id=1, channel_id=2, _filter="type:qualify")

    subscriber.add_subscription(sub1)
    subscriber.add_subscription(sub2)
    subscriber.add_subscription(sub3)

    assert sub1 in subscriber.cache
    assert sub2 not in subscriber.cache
    assert sub3 in subscriber.cache

def test_add_subscription_dm_channel():
    sub = Subscription(guild_id=None, channel_id=1, _filter="type:nominate")

    with pytest.raises(ValueError) as err:
        subscriber.add_subscription(sub)
    
    assert "DM channel" in str(err)

def test_remove_subscription():
    sub1 = Subscription(guild_id=1, channel_id=1, _filter="type:nominate")

    subscriber.add_subscription(sub1)
    assert sub1 in subscriber.cache

    subscriber.remove_subscription(sub1)
    assert sub1 not in subscriber.cache

class MockBot():
    def __init__(self):
        self.event_sub_pairs = []
    
    async def get_channel(self, _):
        return True

    async def send_event(self, event: Event, sub: Subscription, _, __) -> None:
        self.event_sub_pairs.append((sub, event))

@pytest.mark.asyncio
async def test_forward():
    sub_both = Subscription(guild_id=1, channel_id=2, _filter="type:test1 or type:test2")
    sub_one = Subscription(guild_id=1, channel_id=1, _filter="type:test1")

    subscriber.add_subscription(sub_both)
    subscriber.add_subscription(sub_one)

    event1 = Event(_type="test1", time=datetime.utcnow())
    event2 = Event(_type="test2", time=datetime.utcnow())
    bot = MockBot()

    with patch("bot.subscriber.format_embed", return_value=None):
        with patch("bot.subscriber.send_event", new=bot.send_event):
            await subscriber.forward(event1, bot)
            await subscriber.forward(event2, bot)

    await asyncio.sleep(2)

    assert (sub_both, event1) in bot.event_sub_pairs
    assert (sub_both, event2) in bot.event_sub_pairs

    assert (sub_one, event1) in bot.event_sub_pairs
    assert (sub_one, event2) not in bot.event_sub_pairs, "A subscription was forwarded an event it was supposed to filter."