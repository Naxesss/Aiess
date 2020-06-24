import sys
sys.path.append('..')

from bot.commands import Command
from bot.filterer import expand, get_invalid_keys, get_invalid_filters, get_invalid_words

def validate_filter(command: Command, _filter: str):
    """Returns whether the filter was considered valid. If invalid, an appropriate response is sent
    where the command was called."""
    try:
        expand(_filter)
    except ValueError as err:
        # E.g. parenthesis inequality.
        await command.respond_err(f"{str(err)}")
        return False

    invalid_keys = set(get_invalid_keys(_filter))
    if invalid_keys:
        invalids_formatted = "`" + "`, `".join(invalid_keys) + "`"
        await command.respond_err(f"Invalid key(s) {invalids_formatted}.")
        return False

    invalid_filters = set(get_invalid_filters(_filter))
    if invalid_filters:
        invalids_strs = (f"{key}:{value}" for key, value in invalid_filters)
        invalids_formatted = "`" + "`, `".join(invalids_strs) + "`"
        await command.respond_err(f"Invalid value(s) for key(s) {invalids_formatted}.") # TODO: Show valid values.
        return False

    invalid_words = set(get_invalid_words(_filter))
    if invalid_words:
        invalids_formatted = "`" + "`, `".join(invalid_words) + "`"
        await command.respond_err(f"Invalid word(s) {invalids_formatted}.")
        return False

    if not hasattr(command.context.channel, "guild"):
        # Prevents excessive discord rate limiting (5 DMs per second globally).
        await command.respond_err(f"Cannot subscribe in DM channels.")
        return False
    
    return True