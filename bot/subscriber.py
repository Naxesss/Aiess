import sys
sys.path.append('..')

import asyncio
from typing import List, Union
from aiohttp.client_exceptions import ClientOSError
from aiohttp.client_exceptions import ServerDisconnectedError

import discord
from discord import TextChannel
from discord.errors import Forbidden, HTTPException

from aiess import Event
from aiess import logger

from bot.objects import Subscription
from bot.database import Database, BOT_DB_NAME
from bot.formatter import format_embed, format_link
from bot.filterers.event_filterer import filter_context

from aiess.web import ratelimiter

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

def unsubscribe(channel_or_subscription: Union[TextChannel, Subscription]) -> None:
    """Deletes a channel and its filter from the subscription table of the database and reloads the cache."""
    sub = channel_or_subscription
    if isinstance(channel_or_subscription, TextChannel):
        channel = channel_or_subscription
        sub = Subscription(guild_id_or_none(channel), channel.id, None)
    remove_subscription(sub)

def remove_subscription(sub: Subscription) -> None:
    """Deletes a subscription from the subscription table of the database and reloads the cache."""
    Database(DEFAULT_DB_NAME).delete_subscription(sub)
    load()

def get_subscription(channel: TextChannel) -> Subscription:
    """Returns the subscription associated with the given channel, if any, otherwise None."""
    return Database(DEFAULT_DB_NAME).retrieve_subscription("guild_id=%s AND channel_id=%s", (guild_id_or_none(channel), channel.id))

async def forward(event: Event, bot: discord.Bot) -> None:
    """Attempts to forward an event through all subscription filters."""
    pre_generated_embed = await format_embed(event, skip_timeago_if_recent=True)

    for sub in cache:
        await forward_sub(event, sub, bot, pre_generated_embed)

async def forward_sub(event: Event, sub: Subscription, bot: discord.Bot, pre_generated_embed: discord.Embed) -> None:
    """Attempts to forward an event through the filter of the given subscription."""
    if filter_context.test(sub.filter, event):
        await send_event(event, sub, bot, pre_generated_embed)

async def send_event(event: Event, subscription: Subscription, bot: discord.Bot, pre_generated_embed: discord.Embed):
    channel = bot.get_channel(subscription.channel_id)
    if not channel:
        # Ignore channels we no longer have access to (e.g. deleted / power outage).
        return

    while True:
        try:
            await ratelimiter.async_call_with_rate_limit(
                awaited_result_func = lambda: channel.send(
                    content = format_link(event),
                    embed   = pre_generated_embed
                ),
                is_result_invalid   = lambda result: result is None,
                rate_limit          = 0,
                rate_limit_id       = "bot_channel_send"
            )
            break
        except Forbidden as ex:
            break  # In case we're subscribed to a channel we don't have access to.
        except ClientOSError as ex:
            logger.log_err(f"WARNING | Encountered ClientOSError \"{ex}\" when sending to channel \"{channel}\", retrying...")
        except ServerDisconnectedError as ex:
            logger.log_err(f"WARNING | Encountered ServerDisconnectedError \"{ex}\" when sending to channel \"{channel}\", retrying...")
        except HTTPException as ex:
            if str(ex.status).startswith("5"):
                # 500-type codes are server-related (i.e. on Discord's end) and can be safely ignored.
                # Commonly "503: Service Unavailable" and "504: Gateway Time-out".
                logger.log_err(f"WARNING | Encountered HTTPException \"{ex}\" when sending to channel \"{channel}\", retrying...")
            if ex.status == 429:
                # We are being ratelimited by Discord and should back off our next attempt.
                ratelimiter.back_off("bot_channel_send")
        except asyncio.TimeoutError as ex:
            logger.log_err(f"WARNING | Encountered asyncio.TimeoutError \"{ex}\" when sending to channel \"{channel}\", retrying...")