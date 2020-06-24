import sys
sys.path.append('..')

from bot.subscriptions import Subscription

def test_sub_init_str_ids():
    sub = Subscription(guild_id="1", channel_id="3", _filter="type:nominate")
    assert sub.guild_id == 1
    assert sub.channel_id == 3

def test_sub_str():
    sub = Subscription(guild_id=1, channel_id=3, _filter="type:nominate")
    assert "\"type:nominate\"" in str(sub)
    assert "1" in str(sub)
    assert "3" in str(sub)

def test_sub_eq():
    sub1 = Subscription(guild_id=1, channel_id=3, _filter="type:nominate")
    sub2 = Subscription(guild_id=1, channel_id=3, _filter="type:nominate")
    sub3 = Subscription(guild_id=1, channel_id=4, _filter="type:nominate")
    assert sub1 == sub2
    assert sub1 != sub3

def test_sub_eq_type_mismatch():
    sub = Subscription(guild_id=1, channel_id=3, _filter="type:nominate")
    assert sub != "not a sub"

def test_sub_hash():
    sub = Subscription(guild_id=1, channel_id=3, _filter="type:nominate")
    assert sub.__hash__()