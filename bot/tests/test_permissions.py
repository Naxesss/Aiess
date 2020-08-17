import sys
sys.path.append('..')

import mock

from bot.tests.commands.mock_command import MockMessage, MockChannel, MockDMChannel, MockGuild, MockUser, MockRole
from bot.objects import CommandPermission
from bot.commands import register, get_wrapper
from bot.commands import FunctionWrapper, Command
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

def test_set_permission_filter_none():
    command_wrapper = FunctionWrapper(category=None, names=["test1", "test2", "test3"], execute=None)

    with mock.patch("bot.permissions.BOT_DB_NAME", BOT_TEST_DB_NAME):
        set_permission_filter(guild_id=3, command_wrapper=command_wrapper, permission_filter="filter")
        set_permission_filter(guild_id=3, command_wrapper=command_wrapper, permission_filter=None)

    # The guild no longer has any permission filters, so it should be discarded together with the filter.
    assert 3 not in permissions.cache

def test_set_permission_filter_none_keep_guild():
    command_wrapper = FunctionWrapper(category=None, names=["test1", "test2", "test3"], execute=None)
    command_wrapper2 = FunctionWrapper(category=None, names=["test4", "test5", "test6"], execute=None)

    with mock.patch("bot.permissions.BOT_DB_NAME", BOT_TEST_DB_NAME):
        set_permission_filter(guild_id=3, command_wrapper=command_wrapper, permission_filter="filter")
        set_permission_filter(guild_id=3, command_wrapper=command_wrapper2, permission_filter="filter2")
        set_permission_filter(guild_id=3, command_wrapper=command_wrapper, permission_filter=None)

    assert "test4" in permissions.cache[3]
    assert "test1" not in permissions.cache[3]

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

def test_can_execute_channel_perm():
    register(
        category = None, names = ["test1", "test2", "test3"]
    )(None)
    command_wrapper = get_wrapper(name="test1")
    mock_message = MockMessage(
        channel = MockChannel(_id=44, guild=MockGuild(_id=3)),
        author  = MockUser(_id=2, is_admin=False)
    )
    command = Command(name="test2", context=mock_message)

    with mock.patch("bot.permissions.BOT_DB_NAME", BOT_TEST_DB_NAME):
        set_permission_filter(guild_id=3, command_wrapper=command_wrapper, permission_filter="channel:<#44>")
    
    assert permissions.can_execute(command)

def test_can_execute_channel_perm_fail():
    register(
        category = None, names = ["test1", "test2", "test3"]
    )(None)
    command_wrapper = get_wrapper(name="test1")
    mock_message = MockMessage(
        channel = MockChannel(_id=9, guild=MockGuild(_id=3)),
        author  = MockUser(_id=2, is_admin=False)
    )
    command = Command(name="test2", context=mock_message)

    with mock.patch("bot.permissions.BOT_DB_NAME", BOT_TEST_DB_NAME):
        set_permission_filter(guild_id=3, command_wrapper=command_wrapper, permission_filter="channel:<#44>")
    
    assert not permissions.can_execute(command)

def test_can_execute_role_perm():
    register(
        category = None, names = ["test1", "test2", "test3"]
    )(None)
    command_wrapper = get_wrapper(name="test1")
    mock_message = MockMessage(
        channel = MockChannel(_id=44, guild=MockGuild(_id=3)),
        author  = MockUser(_id=2, roles=[MockRole(_id=66)], is_admin=False)
    )
    command = Command(name="test2", context=mock_message)

    with mock.patch("bot.permissions.BOT_DB_NAME", BOT_TEST_DB_NAME):
        set_permission_filter(guild_id=3, command_wrapper=command_wrapper, permission_filter="role:<@&66>")
    
    assert permissions.can_execute(command)

def test_can_execute_role_perm_fail():
    register(
        category = None, names = ["test1", "test2", "test3"]
    )(None)
    command_wrapper = get_wrapper(name="test1")
    mock_message = MockMessage(
        channel = MockChannel(_id=44, guild=MockGuild(_id=3)),
        author  = MockUser(_id=2, roles=[MockRole(_id=3)], is_admin=False)
    )
    command = Command(name="test2", context=mock_message)

    with mock.patch("bot.permissions.BOT_DB_NAME", BOT_TEST_DB_NAME):
        set_permission_filter(guild_id=3, command_wrapper=command_wrapper, permission_filter="role:<@&66>")
    
    assert not permissions.can_execute(command)

def test_can_execute_user_perm():
    register(
        category = None, names = ["test1", "test2", "test3"]
    )(None)
    command_wrapper = get_wrapper(name="test1")
    mock_message = MockMessage(
        channel = MockChannel(_id=44, guild=MockGuild(_id=3)),
        author  = MockUser(_id=88, is_admin=False)
    )
    command = Command(name="test2", context=mock_message)

    with mock.patch("bot.permissions.BOT_DB_NAME", BOT_TEST_DB_NAME):
        set_permission_filter(guild_id=3, command_wrapper=command_wrapper, permission_filter="user:<@88>")
    
    assert permissions.can_execute(command)

def test_can_execute_user_perm_fail():
    register(
        category = None, names = ["test1", "test2", "test3"]
    )(None)
    command_wrapper = get_wrapper(name="test1")
    mock_message = MockMessage(
        channel = MockChannel(_id=44, guild=MockGuild(_id=3)),
        author  = MockUser(_id=2, is_admin=False)
    )
    command = Command(name="test2", context=mock_message)

    with mock.patch("bot.permissions.BOT_DB_NAME", BOT_TEST_DB_NAME):
        set_permission_filter(guild_id=3, command_wrapper=command_wrapper, permission_filter="user:<@88>")
    
    assert not permissions.can_execute(command)

def test_can_execute_default():
    register(
        category = None, names = ["test1", "test2", "test3"]
    )(None)
    mock_message = MockMessage(
        channel = MockChannel(_id=44, guild=MockGuild(_id=3)),
        author  = MockUser(_id=2, is_admin=False)
    )
    command = Command(name="test2", context=mock_message)
    
    assert not permissions.can_execute(command)

def test_can_execute_admin():
    register(
        category = None, names = ["test1", "test2", "test3"]
    )(None)
    mock_message = MockMessage(
        channel = MockChannel(_id=44, guild=MockGuild(_id=3)),
        author  = MockUser(_id=2, is_admin=True)
    )
    command = Command(name="test2", context=mock_message)
    
    assert permissions.can_execute(command)

def test_can_execute_dm():
    register(
        category = None, names = ["test1", "test2", "test3"]
    )(None)
    mock_message = MockMessage(
        channel = MockDMChannel(_id=44),
        author  = MockUser(_id=2, is_dm=True)
    )
    command = Command(name="test2", context=mock_message)
    
    assert permissions.can_execute(command)