import sys
sys.path.append('..')

from typing import List
from discord import TextChannel

from aiess import Event

from bot.subscriptions import Subscription
from bot.database import Database, BOT_DB_NAME
from bot.filterer import passes_filter, dissect

cache: List[Subscription] = []

def load(database: Database=None) -> None:
    """Retrieves all subscriptions from the database and appends them to the internal list."""
    if not database:
        database = Database(BOT_DB_NAME)

    global cache
    cache = []

    for sub in database.retrieve_subscriptions():
        cache.append(sub)

def subscribe(channel: TextChannel, _filter: str) -> None:
    """Inserts a channel and filter into the subscription table of the database and updates the cache.
    Causes any new events passing the filter to be sent to the channel."""
    sub = Subscription(channel.guild.id, channel.id, _filter)
    add_subscription(sub)

def add_subscription(sub: Subscription, database: Database=None) -> None:
    """Inserts a subscription into the subscription table of the database and reloads the cache.
    Causes any new events passing the filter to be sent to the channel."""
    if not database:
        database = Database(BOT_DB_NAME)

    database.insert_subscription(sub)
    load(database)

def unsubscribe(channel: TextChannel) -> None:
    """Deletes a channel and its filter from the subscription table of the database and reloads the cache."""
    sub = Subscription(channel.guild.id, channel.id, None)
    remove_subscription(sub)

def remove_subscription(sub: Subscription, database: Database=None) -> None:
    """Deletes a subscription from the subscription table of the database and reloads the cache."""
    if not database:
        database = Database(BOT_DB_NAME)

    database.delete_subscription(sub)
    load(database)

async def forward(event: Event, client) -> None:
    """Attempts to forward an event through all subscription filters."""
    for sub in cache:
        if passes_filter(sub.filter, dissect(event)):
            await client.send_event(event, sub)