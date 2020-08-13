import sys
sys.path.append('..')

import mock

from bot.objects import CommandPermission
from bot.commands import FunctionWrapper
from bot.database import Database, BOT_TEST_DB_NAME
from bot import permissions
from bot.permissions import set_permission_filter, get_permission_filter

def setup_function():
    Database(BOT_TEST_DB_NAME).clear_table_data("permissions")

def test_set_permission_filter():
    command_wrapper = FunctionWrapper(category=None, names=["test1", "test2", "test3"], execute=None)

    with mock.patch("bot.permissions.BOT_DB_NAME", BOT_TEST_DB_NAME):
        set_permission_filter(guild_id=3, command_wrapper=command_wrapper, permission_filter="filter")

    assert "test1" in permissions.cache[3]
    assert "test2" not in permissions.cache[3]
    assert permissions.cache[3]["test1"] == "filter"

def test_get_permission_filter():
    command_wrapper = FunctionWrapper(category=None, names=["test1", "test2", "test3"], execute=None)

    with mock.patch("bot.permissions.BOT_DB_NAME", BOT_TEST_DB_NAME):
        set_permission_filter(guild_id=3, command_wrapper=command_wrapper, permission_filter="filter")
        permission_filter = get_permission_filter(guild_id=3, command_wrapper=command_wrapper)

    assert permission_filter == "filter"

def test_load():
    with mock.patch("bot.permissions.BOT_DB_NAME", BOT_TEST_DB_NAME):
        permissions.load()
    assert not permissions.cache

    Database(BOT_TEST_DB_NAME).insert_permission(CommandPermission(guild_id=3, command_name="test1", permission_filter="filter"))

    with mock.patch("bot.permissions.BOT_DB_NAME", BOT_TEST_DB_NAME):
        permissions.load()
    assert permissions.cache
    assert permissions.cache[3]["test1"] == "filter"