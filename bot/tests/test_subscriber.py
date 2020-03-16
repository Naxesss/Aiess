import pytest
from datetime import datetime

from aiess import Event

import subscriber
from subscriptions import Subscription
from database import Database

@pytest.fixture
def test_database():
    database = Database("aiess_bot_test")
    # Reset database to state before any tests ran.
    database.clear_table_data("subscriptions")
    return database

def test_correct_setup(test_database: Database):
    assert not test_database.retrieve_table_data("subscriptions")

def test_load(test_database: Database):
    sub1 = Subscription(guild_id=1, channel_id=1, _filter="type:nominate")
    sub2 = Subscription(guild_id=1, channel_id=2, _filter="type:ranked")

    test_database.insert_subscription(sub1)
    test_database.insert_subscription(sub2)

    subscriber.load(test_database)

    assert sub1 in subscriber.cache
    assert sub2 in subscriber.cache

def test_add_subscription(test_database: Database):
    sub1 = Subscription(guild_id=1, channel_id=1, _filter="type:nominate")
    sub2 = Subscription(guild_id=1, channel_id=2, _filter="type:ranked")
    sub3 = Subscription(guild_id=1, channel_id=2, _filter="type:qualify")

    subscriber.add_subscription(sub1, test_database)
    subscriber.add_subscription(sub2, test_database)
    subscriber.add_subscription(sub3, test_database)

    assert sub1 in subscriber.cache
    assert sub2 not in subscriber.cache
    assert sub3 in subscriber.cache

def test_remove_subscription(test_database: Database):
    sub1 = Subscription(guild_id=1, channel_id=1, _filter="type:nominate")

    subscriber.add_subscription(sub1, test_database)
    assert sub1 in subscriber.cache

    subscriber.remove_subscription(sub1, test_database)
    assert sub1 not in subscriber.cache

class MockClient():
    def __init__(self):
        self.event_sub_pairs = []

    async def send_event(self, event: Event, sub: Subscription) -> None:
        self.event_sub_pairs.append((sub, event))

@pytest.mark.asyncio
async def test_forward(test_database: Database):
    sub_both = Subscription(guild_id=1, channel_id=2, _filter="type:test1 or type:test2")
    sub_one = Subscription(guild_id=1, channel_id=1, _filter="type:test1")

    subscriber.add_subscription(sub_both, test_database)
    subscriber.add_subscription(sub_one, test_database)

    event1 = Event(_type="test1", time=datetime.utcnow())
    event2 = Event(_type="test2", time=datetime.utcnow())
    client = MockClient()

    await subscriber.forward(event1, client)
    await subscriber.forward(event2, client)

    assert (sub_both, event1) in client.event_sub_pairs
    assert (sub_both, event2) in client.event_sub_pairs

    assert (sub_one, event1) in client.event_sub_pairs
    assert (sub_one, event2) not in client.event_sub_pairs, "A subscription was forwarded an event it was supposed to filter."