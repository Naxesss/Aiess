import sys
sys.path.append('..')

from discord import Embed

from aiess.database import SCRAPER_DB_NAME

from bot.commands import Command, register
from bot.commands import GENERAL_CATEGORY
from bot.database import Database, BOT_DB_NAME
from bot.formatter import format_timeago

@register(
    category      = GENERAL_CATEGORY,
    names         = ["info", "about", "invite", "source"],
    description   = "Returns general information about the bot."
)
async def cmd_info(command: Command, key: str=None):
    app_info = await command.client.application_info()

    info_embed = Embed()
    info_embed.set_author(name=command.client.user.name, icon_url=command.client.user.avatar_url)
    info_embed.description = app_info.description

    created_at      = command.client.user.created_at
    guilds_n        = len(command.client.guilds)
    subscriptions_n = retrieve_subscription_count()
    events_n        = retrieve_event_count()
    events_today_n  = retrieve_event_count_today()
    first_event_at  = retrieve_first_event_at()

    info_embed.add_field(name="Created at",     value=f"**{created_at.date()}**\n({format_timeago(created_at)})")
    info_embed.add_field(name="Author",         value=f"{app_info.owner}")
    info_embed.add_field(name="Source",         value="https://github.com/Naxesss/Aiess")
    info_embed.add_field(name="Events",         value=f"**{events_n}** in total, **{events_today_n}** in past 24h")
    info_embed.add_field(name="Subscriptions",  value=f"**{subscriptions_n}** in total across **{guilds_n}** server" + ("s" if guilds_n != 1 else ""))
    info_embed.add_field(name="First event at", value=f"**{first_event_at.date()}**\n({format_timeago(first_event_at)})")

    info_embed.set_image(url="https://i.imgur.com/RR3937R.jpg")

    await command.respond(
        response = f"https://discord.com/api/oauth2/authorize?client_id={app_info.id}&permissions=0&scope=bot",
        embed    = info_embed
    )

def retrieve_event_count():
    return retrieve_with_timeout(
        db_name      = SCRAPER_DB_NAME,
        table        = "events",
        where        = "TRUE ORDER BY id DESC LIMIT 1",
        selection    = "id"
    )

def retrieve_event_count_today():
    return retrieve_with_timeout(
        db_name      = SCRAPER_DB_NAME,
        table        = "events",
        where        = "time >= NOW() - INTERVAL 24 HOUR",
        selection    = "COUNT(*)"
    )

def retrieve_subscription_count():
    return retrieve_with_timeout(
        db_name      = BOT_DB_NAME,
        table        = "subscriptions",
        selection    = "COUNT(*)"
    )

def retrieve_first_event_at():
    return retrieve_with_timeout(
        db_name      = SCRAPER_DB_NAME,
        table        = "events",
        where        = "TRUE ORDER BY time ASC LIMIT 1",
        selection    = "time"
    )

def retrieve_with_timeout(db_name, table, where="TRUE", selection="*"):
    try:
        return Database(db_name).retrieve_table_data(
            table        = table,
            where        = where,
            selection    = selection
        )[0][0]
    except TimeoutError:
        return "(timed out)"