import sys
sys.path.append('..')

import pytest

from bot.commands import register
from bot.commands import Command
from bot.tests.commands.mock_command import MockMessage, MockChannel, MockUser, MockGuild
from bot.filterers.event_filterer import filter_context

from bot.cmdcommon import validate_filter
from bot.cmdcommon import filters_embed
from bot.cmdcommon import filter_embed
from bot.cmdcommon import get_command_wrappers

def setup_module():
    register(
        category=None, names=["test4"]
    )(None)
    register(
        category=None, names=["test5"]
    )(None)

@pytest.mark.asyncio
async def test_validate_filter():
    command = Command(name="test", context=MockMessage(channel=MockChannel()))
    assert await validate_filter(command=command, _filter="type:nominate", filter_context=filter_context)

@pytest.mark.asyncio
async def test_validate_filter_complex():
    command = Command(name="test", context=MockMessage(channel=MockChannel()))
    assert await validate_filter(
        command        = command,
        _filter        = "type:(nom or qual or reset or dq) and not user:(banchobot or peppy)",
        filter_context = filter_context
    )

@pytest.mark.asyncio
async def test_validate_filter_invalid_key():
    command = Command(name="test", context=MockMessage(channel=MockChannel()))
    assert not await validate_filter(command=command, _filter="undefined:undefined", filter_context=filter_context)
    assert "✗" in command.response
    assert "invalid key" in command.response.lower()

    embed = filters_embed(filter_context=filter_context)
    assert command.response_embed.title == embed.title
    assert command.response_embed.description == embed.description
    assert command.response_embed.fields[0].name == embed.fields[0].name
    assert command.response_embed.fields[0].value == embed.fields[0].value
    assert command.response_embed.fields[1].name == embed.fields[1].name
    assert command.response_embed.fields[1].value == embed.fields[1].value

@pytest.mark.asyncio
async def test_validate_filter_invalid_value():
    command = Command(name="test", context=MockMessage(channel=MockChannel()))
    assert not await validate_filter(command=command, _filter="type:undefined", filter_context=filter_context)
    assert "✗" in command.response
    assert "invalid value" in command.response.lower()

    embed = filter_embed(key="type", filter_context=filter_context)
    assert command.response_embed.fields[0].name == embed.fields[0].name
    assert command.response_embed.fields[0].value == embed.fields[0].value
    assert command.response_embed.fields[1].name == embed.fields[1].name
    assert command.response_embed.fields[1].value == embed.fields[1].value
    assert command.response_embed.fields[2].name == embed.fields[2].name
    assert command.response_embed.fields[2].value == embed.fields[2].value

@pytest.mark.asyncio
async def test_validate_filter_invalid_word():
    command = Command(name="test", context=MockMessage(channel=MockChannel()))
    assert not await validate_filter(command=command, _filter="user:sometwo annd type:qualify", filter_context=filter_context)
    assert "✗" in command.response
    assert "invalid word" in command.response.lower()

    embed = filters_embed(filter_context=filter_context)
    assert command.response_embed.title == embed.title
    assert command.response_embed.description == embed.description
    assert command.response_embed.fields[0].name == embed.fields[0].name
    assert command.response_embed.fields[0].value == embed.fields[0].value
    assert command.response_embed.fields[1].name == embed.fields[1].name
    assert command.response_embed.fields[1].value == embed.fields[1].value

def test_get_command_wrappers():
    assert len(get_command_wrappers("test4, test5")) == 2

def test_get_command_wrappers_plus():
    assert get_command_wrappers("+test5")

def test_get_command_wrappers_none():
    assert not get_command_wrappers("test6, test7")