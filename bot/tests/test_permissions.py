import sys
sys.path.append('..')

import pytest
import mock

from bot.tests.commands.mock_command import MockMessage, MockChannel, MockDMChannel, MockGuild, MockUser, MockRole, MockCommand
from bot.objects import CommandPermission
from bot.commands import register, get_wrapper
from bot.commands import FunctionWrapper, Command
from bot.database import Database, BOT_TEST_DB_NAME
from bot import permissions
from bot.permissions import set_permission_filter, get_permission_filter

def setup_module():
    register(
        category = None,
        names    = ["test1", "test2", "test3"]
    )(None)
    register(
        category = None,
        names    = ["wip1", "wip2"],
        wip      = True
    )(None)

def setup_function():
    permissions.DEFAULT_DB_NAME = BOT_TEST_DB_NAME
    Database(BOT_TEST_DB_NAME).clear_table_data("permissions")
    permissions.cache = {}

def test_set_permission_filter():
    command_wrapper = FunctionWrapper(category=None, names=["test1", "test2", "test3"], execute=None)

    set_permission_filter(guild_id=3, command_wrapper=command_wrapper, permission_filter="filter")

    assert "test1" in permissions.cache[3]
    assert "test2" not in permissions.cache[3]
    assert permissions.cache[3]["test1"] == "filter"

def test_set_permission_filter_multiple():
    command_wrapper = FunctionWrapper(category=None, names=["test1", "test2", "test3"], execute=None)
    command_wrapper2 = FunctionWrapper(category=None, names=["test4", "test5", "test6"], execute=None)

    set_permission_filter(guild_id=3, command_wrapper=command_wrapper, permission_filter="filter")
    set_permission_filter(guild_id=3, command_wrapper=command_wrapper2, permission_filter="filter2")

    assert "test1" in permissions.cache[3]
    assert "test2" not in permissions.cache[3]
    assert "test4" in permissions.cache[3]
    assert permissions.cache[3]["test1"] == "filter"
    assert permissions.cache[3]["test4"] == "filter2"

def test_set_permission_filter_none():
    command_wrapper = FunctionWrapper(category=None, names=["test1", "test2", "test3"], execute=None)

    set_permission_filter(guild_id=3, command_wrapper=command_wrapper, permission_filter="filter")
    set_permission_filter(guild_id=3, command_wrapper=command_wrapper, permission_filter=None)

    # The guild no longer has any permission filters, so it should be discarded together with the filter.
    assert 3 not in permissions.cache

def test_set_permission_filter_none_keep_guild():
    command_wrapper = FunctionWrapper(category=None, names=["test1", "test2", "test3"], execute=None)
    command_wrapper2 = FunctionWrapper(category=None, names=["test4", "test5", "test6"], execute=None)

    set_permission_filter(guild_id=3, command_wrapper=command_wrapper, permission_filter="filter")
    set_permission_filter(guild_id=3, command_wrapper=command_wrapper2, permission_filter="filter2")
    set_permission_filter(guild_id=3, command_wrapper=command_wrapper, permission_filter=None)

    assert "test4" in permissions.cache[3]
    assert "test1" not in permissions.cache[3]

def test_get_permission_filter():
    command_wrapper = FunctionWrapper(category=None, names=["test1", "test2", "test3"], execute=None)

    set_permission_filter(guild_id=3, command_wrapper=command_wrapper, permission_filter="filter")
    permission_filter = get_permission_filter(guild_id=3, command_wrapper=command_wrapper)

    assert permission_filter == "filter"

def test_load():
    permissions.load()
    assert not permissions.cache

    Database(BOT_TEST_DB_NAME).insert_permission(CommandPermission(guild_id=3, command_name="test1", permission_filter="filter"))

    permissions.load()
    assert permissions.cache
    assert permissions.cache[3]["test1"] == "filter"

@pytest.mark.asyncio
async def test_can_execute_channel_perm():
    command_wrapper = get_wrapper(name="test1")
    mock_message = MockMessage(
        channel = MockChannel(_id=44, guild=MockGuild(_id=3)),
        author  = MockUser(_id=2, is_admin=False)
    )
    command = Command(name="test2", context=mock_message)

    set_permission_filter(guild_id=3, command_wrapper=command_wrapper, permission_filter="channel:<#44>")
    
    assert await permissions.can_execute(command)

@pytest.mark.asyncio
async def test_can_execute_channel_perm_fail():
    command_wrapper = get_wrapper(name="test1")
    mock_message = MockMessage(
        channel = MockChannel(_id=9, guild=MockGuild(_id=3)),
        author  = MockUser(_id=2, is_admin=False)
    )
    command = Command(name="test2", context=mock_message)

    set_permission_filter(guild_id=3, command_wrapper=command_wrapper, permission_filter="channel:<#44>")
    
    assert not await permissions.can_execute(command)

@pytest.mark.asyncio
async def test_can_execute_role_perm():
    command_wrapper = get_wrapper(name="test1")
    mock_message = MockMessage(
        channel = MockChannel(_id=44, guild=MockGuild(_id=3)),
        author  = MockUser(_id=2, roles=[MockRole(_id=66)], is_admin=False)
    )
    command = Command(name="test2", context=mock_message)

    set_permission_filter(guild_id=3, command_wrapper=command_wrapper, permission_filter="role:<@&66>")
    
    assert await permissions.can_execute(command)

@pytest.mark.asyncio
async def test_can_execute_role_perm_fail():
    command_wrapper = get_wrapper(name="test1")
    mock_message = MockMessage(
        channel = MockChannel(_id=44, guild=MockGuild(_id=3)),
        author  = MockUser(_id=2, roles=[MockRole(_id=3)], is_admin=False)
    )
    command = Command(name="test2", context=mock_message)

    set_permission_filter(guild_id=3, command_wrapper=command_wrapper, permission_filter="role:<@&66>")
    
    assert not await permissions.can_execute(command)

@pytest.mark.asyncio
async def test_can_execute_user_perm():
    command_wrapper = get_wrapper(name="test1")
    mock_message = MockMessage(
        channel = MockChannel(_id=44, guild=MockGuild(_id=3)),
        author  = MockUser(_id=88, is_admin=False)
    )
    command = Command(name="test2", context=mock_message)

    set_permission_filter(guild_id=3, command_wrapper=command_wrapper, permission_filter="user:<@88>")
    
    assert await permissions.can_execute(command)

@pytest.mark.asyncio
async def test_can_execute_user_perm_fail():
    command_wrapper = get_wrapper(name="test1")
    mock_message = MockMessage(
        channel = MockChannel(_id=44, guild=MockGuild(_id=3)),
        author  = MockUser(_id=2, is_admin=False)
    )
    command = Command(name="test2", context=mock_message)

    set_permission_filter(guild_id=3, command_wrapper=command_wrapper, permission_filter="user:<@88>")
    
    assert not await permissions.can_execute(command)

@pytest.mark.asyncio
async def test_can_execute_default():
    mock_message = MockMessage(
        channel = MockChannel(_id=44, guild=MockGuild(_id=3)),
        author  = MockUser(_id=2, is_admin=False)
    )
    command = Command(name="test2", context=mock_message)
    
    assert not await permissions.can_execute(command)

@pytest.mark.asyncio
async def test_can_execute_admin():
    mock_message = MockMessage(
        channel = MockChannel(_id=44, guild=MockGuild(_id=3)),
        author  = MockUser(_id=2, is_admin=True)
    )
    command = Command(name="test2", context=mock_message)
    
    assert await permissions.can_execute(command)

@pytest.mark.asyncio
async def test_can_execute_dm():
    mock_message = MockMessage(
        channel = MockDMChannel(_id=44),
        author  = MockUser(_id=2, is_dm=True)
    )
    command = Command(name="test2", context=mock_message)
    
    assert await permissions.can_execute(command)



async def application_info():
    app_info_mock = mock.MagicMock()
    app_info_mock.owner = mock.MagicMock()
    app_info_mock.owner.id = 4
    return app_info_mock

async def application_info_owner():
    app_info_mock = mock.MagicMock()
    app_info_mock.owner = mock.MagicMock()
    app_info_mock.owner.id = 2
    return app_info_mock

@pytest.mark.asyncio
async def test_can_execute_wip():
    mock_message = MockMessage(
        channel = MockChannel(_id=44, guild=MockGuild(_id=3)),
        author  = MockUser(_id=2, is_admin=False)
    )
    mock_client = mock.MagicMock()
    mock_client.application_info = application_info
    command = MockCommand(name="wip2", context=mock_message, client=mock_client)
    
    assert not await permissions.can_execute(command)

@pytest.mark.asyncio
async def test_can_execute_wip_admin():
    mock_message = MockMessage(
        channel = MockChannel(_id=44, guild=MockGuild(_id=3)),
        author  = MockUser(_id=2, is_admin=True)
    )
    mock_client = mock.MagicMock()
    mock_client.application_info = application_info
    command = MockCommand(name="wip2", context=mock_message, client=mock_client)
    
    assert not await permissions.can_execute(command)

@pytest.mark.asyncio
async def test_can_execute_wip_dm():
    mock_message = MockMessage(
        channel = MockDMChannel(_id=44),
        author  = MockUser(_id=2, is_dm=True)
    )
    mock_client = mock.MagicMock()
    mock_client.application_info = application_info
    command = MockCommand(name="wip2", context=mock_message, client=mock_client)
    
    assert not await permissions.can_execute(command)

@pytest.mark.asyncio
async def test_can_execute_wip_dev():
    mock_message = MockMessage(
        channel = MockChannel(_id=44, guild=MockGuild(_id=3)),
        author  = MockUser(_id=2, is_admin=False)
    )
    mock_client = mock.MagicMock()
    mock_client.application_info = application_info_owner
    command = MockCommand(name="wip2", context=mock_message, client=mock_client)
    
    assert await permissions.can_execute(command)