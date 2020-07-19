import sys
sys.path.append('..')

from bot.database import Database, BOT_TEST_DB_NAME
from bot import prefixes
from bot.objects import Prefix
from bot.prefixes import set_prefix, get_prefix
from bot.prefixes import DEFAULT_PREFIX

def setup_function():
    prefixes.DEFAULT_DB_NAME = BOT_TEST_DB_NAME
    Database(BOT_TEST_DB_NAME).clear_table_data("prefixes")
    prefixes.cache = {}

def test_load():
    Database(BOT_TEST_DB_NAME).insert_prefix(Prefix(3, "&"))
    assert not prefixes.cache
    prefixes.load()
    assert prefixes.cache[3] == "&"

def test_set_prefix():
    assert not prefixes.cache
    set_prefix(3, "&")
    assert Database(BOT_TEST_DB_NAME).retrieve_prefix("guild_id=%s", (3,)) == Prefix(3, "&")
    assert prefixes.cache[3] == "&"

def test_set_prefix_none():
    assert not prefixes.cache
    set_prefix(3, "&")
    assert Database(BOT_TEST_DB_NAME).retrieve_prefix("guild_id=%s", (3,)) == Prefix(3, "&")
    assert prefixes.cache[3] == "&"
    set_prefix(3, None)
    assert Database(BOT_TEST_DB_NAME).retrieve_prefix("guild_id=%s", (3,)) == None
    assert not prefixes.cache

def test_get_prefix():
    set_prefix(3, "&")
    assert get_prefix(3) == "&"

def test_get_prefix_default():
    set_prefix(3, None)
    assert Database(BOT_TEST_DB_NAME).retrieve_prefix("guild_id=%s", (3,)) == None
    assert not prefixes.cache
    assert get_prefix(3) == DEFAULT_PREFIX