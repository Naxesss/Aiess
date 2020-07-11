import sys
sys.path.append('..')

from typing import List
import discord
from discord import TextChannel

from aiess import Event

from bot.subscriptions import Subscription
from bot.database import Database, BOT_DB_NAME
from bot.filterer import passes_filter

DEFAULT_DB_NAME = BOT_DB_NAME

cache: List[Subscription] = []

def load() -> None:
    """Retrieves all subscriptions from the database and appends them to the internal list."""
    global cache
    cache = []

    for sub in Database(DEFAULT_DB_NAME).retrieve_subscriptions():
        cache.append(sub)

def guild_id_or_none(channel: TextChannel):
    """Returns the id of the guild this channel belongs in, or None if the channel is a DM channel."""
    return channel.guild.id if hasattr(channel, "guild") else None

def subscribe(channel: TextChannel, _filter: str) -> None:
    """Inserts a channel and filter into the subscription table of the database and updates the cache.
    Causes any new events passing the filter to be sent to the channel."""
    sub = Subscription(guild_id_or_none(channel), channel.id, _filter)
    add_subscription(sub)

def add_subscription(sub: Subscription) -> None:
    """Inserts a subscription into the subscription table of the database and reloads the cache.
    Causes any new events passing the filter to be sent to the channel."""
    if sub.guild_id is None:
        # Prevents excessive discord rate limiting (5 DMs per second globally).
        raise ValueError("Cannot subscribe in DM channels.")

    Database(DEFAULT_DB_NAME).insert_subscription(sub)
    load()

def unsubscribe(channel: TextChannel) -> None:
    """Deletes a channel and its filter from the subscription table of the database and reloads the cache."""
    sub = Subscription(guild_id_or_none(channel), channel.id, None)
    remove_subscription(sub)

def remove_subscription(sub: Subscription) -> None:
    """Deletes a subscription from the subscription table of the database and reloads the cache."""
    Database(DEFAULT_DB_NAME).delete_subscription(sub)
    load()


async def forward(event: Event, client: discord.Client) -> None:
    """Attempts to forward an event through all subscription filters."""
    for sub in cache:
        if passes_filter(sub.filter, event):
            await client.send_event(event, sub)