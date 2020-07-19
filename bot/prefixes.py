import sys
sys.path.append('..')

from bot.database import Database, BOT_DB_NAME
from bot.objects import Prefix

DEFAULT_DB_NAME = BOT_DB_NAME

DEFAULT_PREFIX = "+"
cache = {}

def load():
    """Loads guild-specific prefixes from the database into the cache."""
    cache.clear()
    for prefix_obj in Database(DEFAULT_DB_NAME).retrieve_prefixes():
        cache[prefix_obj.guild_id] = prefix_obj.prefix

def get_prefix(guild_id: int):
    """Returns the command prefix for the given guild id."""
    if guild_id in cache:
        return cache[guild_id]
    return DEFAULT_PREFIX

def set_prefix(guild_id: int, prefix: str):
    """Sets the command prefix for this guild id to the given prefix.
    Instead deletes if prefix is None."""
    if prefix is None:
        Database(DEFAULT_DB_NAME).delete_prefix(guild_id)
    else:
        Database(DEFAULT_DB_NAME).insert_prefix(Prefix(guild_id, prefix))
    load()