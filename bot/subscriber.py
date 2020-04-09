from typing import List
from discord import TextChannel

from aiess import Event

from database import Database, database
from subscriptions import Subscription
from filterer import passes_filter, dissect

cache: List[Subscription] = []

def load(_database: Database=None) -> None:
    """Retrieves all subscriptions from the database and appends them to the internal list."""
    if not _database:
        _database = database

    global cache
    cache = []

    for sub in _database.retrieve_subscriptions():
        cache.append(sub)

def subscribe(channel: TextChannel, _filter: str) -> None:
    """Inserts a channel and filter into the subscription table of the database and updates the cache.
    Causes any new events passing the filter to be sent to the channel."""
    sub = Subscription(channel.guild.id, channel.id, _filter)
    add_subscription(sub)

def add_subscription(sub: Subscription, _database: Database=None) -> None:
    """Inserts a subscription into the subscription table of the database and reloads the cache.
    Causes any new events passing the filter to be sent to the channel."""
    if not _database:
        _database = database

    _database.insert_subscription(sub)
    load(_database)

def unsubscribe(channel: TextChannel) -> None:
    """Deletes a channel and its filter from the subscription table of the database and reloads the cache."""
    sub = Subscription(channel.guild.id, channel.id, None)
    remove_subscription(sub)

def remove_subscription(sub: Subscription, _database: Database=None) -> None:
    """Deletes a subscription from the subscription table of the database and reloads the cache."""
    if not _database:
        _database = database

    _database.delete_subscription(sub)
    load(_database)

async def forward(event: Event, client) -> None:
    """Attempts to forward an event through all subscription filters."""
    for sub in cache:
        if passes_filter(sub.filter, dissect(event)):
            await client.send_event(event, sub)