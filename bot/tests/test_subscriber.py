import pytest

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