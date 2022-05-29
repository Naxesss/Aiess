from discord.ext import commands
from discord import Embed

from aiess.database import SCRAPER_DB_NAME

from bot.formatter import format_timeago
from bot.database import Database, BOT_DB_NAME

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def ping(self, ctx):
        """Returns the bot latency (e.g. "134 ms")."""
        await ctx.respond(f"Pong! ({ctx.bot.latency * 1000:.0f} ms)", ephemeral=True)
    
    @commands.slash_command()
    async def info(self, ctx):
        """Returns general information about the bot (e.g. creator and source code)."""
        await ctx.defer(ephemeral=True)

        app_info = await self.bot.application_info()

        info_embed = Embed()
        info_embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar.url)
        info_embed.description = app_info.description

        created_at      = self.bot.user.created_at
        guilds_n        = len(self.bot.guilds)
        subscriptions_n = retrieve_subscription_count()
        events_n        = retrieve_event_count()
        events_today_n  = retrieve_event_count_today()
        first_event_at  = retrieve_first_event_at()

        info_embed.add_field(name="Created",     value=f"**{created_at.date()}**\n({format_timeago(created_at)})")
        info_embed.add_field(name="Author",         value=f"{app_info.owner}")
        info_embed.add_field(name="Source",         value="https://github.com/Naxesss/Aiess")
        info_embed.add_field(name="Events",         value=f"**{events_n}** in total, **{events_today_n}** in past 24h")
        info_embed.add_field(name="Subscriptions",  value=f"**{subscriptions_n}** in total across **{guilds_n}** server" + ("s" if guilds_n != 1 else ""))
        info_embed.add_field(name="First event", value=f"**{first_event_at.date()}**\n({format_timeago(first_event_at)})")

        info_embed.set_image(url="https://i.imgur.com/RR3937R.jpg")

        await ctx.followup.send(f"https://discord.com/api/oauth2/authorize?client_id={app_info.id}&permissions=0&scope=bot%20applications.commands", embed=info_embed)

def retrieve_event_count():
    return retrieve_with_timeout(
        db_name      = SCRAPER_DB_NAME,
        table        = "events",
        where        = "TRUE",
        selection    = "id",
        order_by     = "id DESC",
        limit        = 1
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
        where        = "TRUE",
        selection    = "time",
        order_by     = "time ASC",
        limit        = 1
    )

def retrieve_with_timeout(
        db_name, table, where="TRUE", selection="*",
        group_by: str=None, order_by: str=None, limit: int=None
    ):
    try:
        db = Database(db_name)
        return db.retrieve_table_data(
            table        = table,
            where        = where,
            selection    = selection,
            group_by     = group_by,
            order_by     = order_by,
            limit        = limit
        )[0][0]
    except TimeoutError:
        return "(timed out)"

def setup(bot):
    bot.add_cog(General(bot))