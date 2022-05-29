import sys
sys.path.append('..')

from discord import Embed

from bot.filterer import expand, get_invalid_gates, get_invalid_keys, get_invalid_filters, get_invalid_words, get_missing_gate
from bot.filterer import FilterContext
from bot.formatter import format_dotted_list

async def validate_filter(ctx, _filter: str, filter_context: FilterContext) -> bool:
    """Returns whether the filter was considered valid. If invalid, an appropriate response is sent
    where the command was called. Requires a filter context to determine filter validity."""
    try:
        expansion = expand(_filter)
    except ValueError as err:
        # E.g. parenthesis inequality.
        await ctx.respond(f"{str(err)}", embed=filters_embed(filter_context), ephemeral=True)
        return False

    invalid_gates = set(get_invalid_gates(_filter))
    if invalid_gates:
        invalids_formatted = "`" + "`, `".join(invalid_gates) + "`"
        await ctx.respond(f"✗ Invalid positioning of gate(s) {invalids_formatted} in expansion `{expansion}`.", embed=filters_embed(filter_context), ephemeral=True)
        return False

    invalid_keys = set(get_invalid_keys(_filter, filter_context))
    if invalid_keys:
        invalids_formatted = "`" + "`, `".join(invalid_keys) + "`"
        await ctx.respond(f"✗ Invalid key(s) {invalids_formatted} in expansion `{expansion}`.", embed=filters_embed(filter_context), ephemeral=True)
        return False

    invalid_filters = set(get_invalid_filters(_filter, filter_context))
    if invalid_filters:
        keys = []
        invalids_strs = []
        for key, value in invalid_filters:
            invalids_strs.append(f"{key}:{value}")
            keys.append(key)
        invalids_formatted = "`" + "`, `".join(invalids_strs) + "`"
        # `keys` will have at least one element, else `invalid_filters` would be falsy.
        await ctx.respond(f"✗ Invalid value(s) for key(s) {invalids_formatted} in expansion `{expansion}`.", embed=filter_embed(keys[0], filter_context), ephemeral=True)
        return False

    invalid_words = set(get_invalid_words(_filter))
    if invalid_words:
        invalids_formatted = "`" + "`, `".join(invalid_words) + "`"
        await ctx.respond(f"✗ Invalid word(s) {invalids_formatted} in expansion `{expansion}`.", embed=filters_embed(filter_context), ephemeral=True)
        return False
    
    parts = get_missing_gate(_filter)
    if parts:
        left_part, right_part = parts
        await ctx.respond(f"✗ Missing gate between `{left_part}` and `{right_part}` in expansion `{expansion}`.", embed=filters_embed(filter_context), ephemeral=True)
        return False

    if not hasattr(ctx.channel, "guild"):
        # Prevents excessive discord rate limiting (5 DMs per second globally).
        await ctx.respond("✗ Cannot subscribe in DM channels.", ephemeral=True)
        return False
    
    return True

def filters_embed(filter_context: FilterContext) -> Embed:
    """Returns an embed representing the given filter context; showing all tag names and examples."""
    embed = Embed()
    embed.title = f"Filter ({filter_context.name})"
    embed.description = """
            A string of key:value pairs (e.g. `key1:(value1 or value2) and key2:value3`).
            Keys and values are always case insensitive. Gates are `and`, `or`, and `not`.
            """
    
    keys = "\u2000".join("**`" + ("/".join(f"{name}" for name in tag.names) + "`**") for tag in filter_context.tags)
    embed.add_field(
        name   = "Keys" + (" (`/` denotes aliases)" if "/" in keys else ""),
        value  = keys,
        inline = True
    )
    embed.add_field(
        name   = "Example(s)",
        value  = format_dotted_list(filter_context.examples),
        inline = True
    )
    return embed

def filter_embed(key: str, filter_context: FilterContext) -> Embed:
    """Returns an embed representing the tag with the given name `key`, for this context.
    Goes more in detail regarding how to use this specific tag."""
    key = key.lower().strip()
    tag = filter_context.get_tag(key)
    keys = filter_context.get_tag(key).names

    embed = Embed()
    embed.add_field(
        name   = "/".join(f"**`{key}`**" for key in keys),
        value  = tag.description,
        inline = True
    )
    embed.add_field(
        name   = "Value(s)",
        value  = tag.value_hint,
        inline = True
    )
    embed.add_field(
        name   = "Example(s)",
        value  = format_dotted_list(f"`{key}:{value}`" for value in tag.example_values),
        inline = True
    )
    return embed