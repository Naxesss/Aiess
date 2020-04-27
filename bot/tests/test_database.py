import pytest
from mysql.connector.errors import IntegrityError

from database import Database
from subscriptions import Subscription

@pytest.fixture
def test_database():
    database = Database("aiess_test")
    # Reset database to state before any tests ran.
    database.clear_table_data("events")
    return database

@pytest.fixture
def test_bot_database():
    database = Database("aiess_bot_test")
    database.clear_table_data("subscriptions")
    return database

def test_correct_setup(test_bot_database):
    assert not test_bot_database.retrieve_table_data("subscriptions")

def test_insert_retrieve_channel_sub(test_bot_database):
    sub1 = Subscription(guild_id=3, channel_id=1, _filter="type:problem and state:qualified")
    sub2 = Subscription(guild_id=3, channel_id=2, _filter="type:ranked")

    test_bot_database.insert_subscription(sub1)
    test_bot_database.insert_subscription(sub2)

    retrieved_subs = test_bot_database.retrieve_subscriptions()
    assert next(retrieved_subs, None) == sub1
    assert next(retrieved_subs, None) == sub2
    assert next(retrieved_subs, None) == None

def test_insert_retrieve_channel_sub_no_filter(test_bot_database):
    sub = Subscription(guild_id=1, channel_id=1, _filter=None)

    # A subscription should always have an explicit filter to prevent
    # the creation of an unfiltered subscription unintentionally.
    with pytest.raises(IntegrityError) as err:
        test_bot_database.insert_subscription(sub)
    
    assert "cannot be null" in str(err)