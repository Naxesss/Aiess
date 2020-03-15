from typing import List
from discord import TextChannel

from aiess import Event

from database import Database, database
from subscriptions import Subscription

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
    """Subscribes a channel to events passing the given filter."""
    sub = Subscription(channel.guild.id, channel.id, _filter)

    database.insert_subscription(sub)
    load()

async def forward(event: Event, client) -> None:
    """Attempts to forward an event through all subscription filters."""
    for sub in cache:
        if passes_filter(event, sub.filter):
            await client.send_event(event, sub)

def passes_filter(event: Event, filter: str) -> bool:
    # TODO: Implement filtering
    return True