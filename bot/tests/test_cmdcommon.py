import sys
sys.path.append('..')

import pytest

from bot.filterers.event_filterer import filter_context

from bot.cmdcommon import validate_filter
from bot.cmdcommon import filters_embed
from bot.cmdcommon import filter_embed

class MockChannel:
    def __init__(self, has_guild=True):
        if has_guild:
            self.guild = True

class MockContext:
    def __init__(self, has_guild=True):
        self.text = None
        self.embed = None
        self.ephemeral = False

        self.channel = MockChannel(has_guild)

    async def respond(self, text, embed=None, ephemeral=False):
        self.text = text
        self.embed = embed
        self.ephemeral = ephemeral

@pytest.mark.asyncio
async def test_validate_filter():
    ctx = MockContext()
    assert await validate_filter(ctx, _filter="type:nominate", filter_context=filter_context)

@pytest.mark.asyncio
async def test_validate_filter_complex():
    ctx = MockContext()
    assert await validate_filter(
        ctx            = ctx,
        _filter        = "type:(nom or qual or reset or dq) and not user:(banchobot or peppy)",
        filter_context = filter_context
    )

@pytest.mark.asyncio
async def test_validate_filter_invalid_key():
    ctx = MockContext()
    assert not await validate_filter(ctx, _filter="undefined:undefined", filter_context=filter_context)
    assert "✗" in ctx.text
    assert "invalid key" in ctx.text.lower()

    embed = filters_embed(filter_context=filter_context)
    assert ctx.embed.title == embed.title
    assert ctx.embed.description == embed.description
    assert ctx.embed.fields[0].name == embed.fields[0].name
    assert ctx.embed.fields[0].value == embed.fields[0].value
    assert ctx.embed.fields[1].name == embed.fields[1].name
    assert ctx.embed.fields[1].value == embed.fields[1].value

@pytest.mark.asyncio
async def test_validate_filter_invalid_value():
    ctx = MockContext()
    assert not await validate_filter(ctx, _filter="type:undefined", filter_context=filter_context)
    assert "✗" in ctx.text
    assert "invalid value" in ctx.text.lower()

    embed = filter_embed(key="type", filter_context=filter_context)
    assert ctx.embed.fields[0].name == embed.fields[0].name
    assert ctx.embed.fields[0].value == embed.fields[0].value
    assert ctx.embed.fields[1].name == embed.fields[1].name
    assert ctx.embed.fields[1].value == embed.fields[1].value
    assert ctx.embed.fields[2].name == embed.fields[2].name
    assert ctx.embed.fields[2].value == embed.fields[2].value

@pytest.mark.asyncio
async def test_validate_filter_invalid_word():
    ctx = MockContext()
    assert not await validate_filter(ctx, _filter="user:sometwo annd type:qualify", filter_context=filter_context)
    assert "✗" in ctx.text
    assert "invalid word" in ctx.text.lower()

    embed = filters_embed(filter_context=filter_context)
    assert ctx.embed.title == embed.title
    assert ctx.embed.description == embed.description
    assert ctx.embed.fields[0].name == embed.fields[0].name
    assert ctx.embed.fields[0].value == embed.fields[0].value
    assert ctx.embed.fields[1].name == embed.fields[1].name
    assert ctx.embed.fields[1].value == embed.fields[1].value

@pytest.mark.asyncio
async def test_validate_filter_missing_gate():
    ctx = MockContext()
    assert not await validate_filter(ctx, _filter="user:sometwo type:qualify", filter_context=filter_context)
    assert "✗" in ctx.text
    assert "missing gate" in ctx.text.lower()
    assert "between `user:sometwo` and `type:qualify`" in ctx.text.lower()

    embed = filters_embed(filter_context=filter_context)
    assert ctx.embed.title == embed.title
    assert ctx.embed.description == embed.description
    assert ctx.embed.fields[0].name == embed.fields[0].name
    assert ctx.embed.fields[0].value == embed.fields[0].value
    assert ctx.embed.fields[1].name == embed.fields[1].name
    assert ctx.embed.fields[1].value == embed.fields[1].value

@pytest.mark.asyncio
async def test_validate_filter_no_guild():
    ctx = MockContext(has_guild=False)
    assert not await validate_filter(ctx, _filter="type:nominate", filter_context=filter_context)