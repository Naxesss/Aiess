import sys
sys.path.append('..')

from bot.commands import Command, register
from bot.subscriber import subscribe
from bot.filterer import expand, get_invalid_keys, get_invalid_filters, get_invalid_words

@register("sub", required_args=["filter"])
async def cmd_sub(command: Command, _filter: str):

    try:
        expand(_filter)
    except ValueError as err:
        # E.g. parenthesis inequality.
        await command.respond(f"✗ {str(err)}")
        return

    invalid_keys = set(get_invalid_keys(_filter))
    if invalid_keys:
        invalids_formatted = "`" + "`, `".join(invalid_keys) + "`"
        await command.respond(f"✗ Invalid key(s) {invalids_formatted}.")
        return

    invalid_filters = set(get_invalid_filters(_filter))
    if invalid_filters:
        invalids_strs = (f"{key}:{value}" for key, value in invalid_filters)
        invalids_formatted = "`" + "`, `".join(invalids_strs) + "`"
        await command.respond(f"✗ Invalid value(s) for key(s) {invalids_formatted}.") # TODO: Show valid values.
        return

    invalid_words = set(get_invalid_words(_filter))
    if invalid_words:
        invalids_formatted = "`" + "`, `".join(invalid_words) + "`"
        await command.respond(f"✗ Invalid word(s) {invalids_formatted}.") # TODO: Show valid values.
        return

    subscribe(command.context.channel, _filter)
    
    # TODO: Improve feedback by ecapsulating our input and its expansion in an embed.
    await command.respond("✓ Subscribed")