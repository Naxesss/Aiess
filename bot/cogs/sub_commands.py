from discord.ext import commands
from discord import Embed, Colour
from discord.commands import Option

from aiess.database import SCRAPER_DB_NAME

from bot.cmdcommon import validate_filter
from bot.subscriber import get_subscription
from bot.subscriber import subscribe
from bot.subscriber import unsubscribe
from bot.filterer import expand
from bot.formatter import escape_markdown
from bot.formatter import format_link, format_embed
from bot.cmdcommon import filters_embed, filter_embed
from bot.filterers.event_filterer import filter_to_sql
from bot.filterers.event_filterer import filter_context
from bot.database import Database

class Subscription(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def show_subscription(self, ctx):
        """Shows the current channel subscription."""
        subscription = get_subscription(ctx.channel)

        embed = Embed()
        embed.colour = Colour.from_rgb(255, 170, 50)
        embed.add_field(
            name="🔔\u2000Current Subscription",
            value=f"""
                {escape_markdown(subscription.filter)}
                `{expand(subscription.filter)}`
                """ if subscription else "None"
        )

        await ctx.respond(embed=embed, ephemeral=True)

    @commands.slash_command()
    async def subscribe(self, ctx, filter: Option(str, "Any event matching this will be sent in the channel.", required=True)):
        """Subscribes this channel to events matching `filter`."""
        if ctx.author.bot:
            return

        if not ctx.channel.guild:
            await ctx.respond("✗ This command can only be used in a server.", ephemeral=True)
            return

        if not ctx.channel.permissions_for(ctx.author).manage_channels:
            await ctx.respond("✗ You need the `Manage Channels` permission here to use this command.", ephemeral=True)
            return

        if not await validate_filter(ctx, filter, filter_context):
            return  # `validate_filter` will respond for us.

        subscribe(ctx.channel, filter)

        embed = Embed()
        embed.colour = Colour.from_rgb(255, 170, 50)
        embed.add_field(
            name="🔔\u2000Subscribed to",
            value=f"""
                {escape_markdown(filter)}
                `{expand(filter)}`
                """
        )

        await ctx.respond("✓", embed=embed)
    
    @commands.slash_command()
    async def unsubscribe(self, ctx):
        """Unsubscribes this channel from any event subscriptions."""
        if ctx.author.bot:
            return

        if not ctx.channel.guild:
            await ctx.respond("✗ This command can only be used in a server.", ephemeral=True)
            return

        if not ctx.channel.permissions_for(ctx.author).manage_channels:
            await ctx.respond("✗ You need the `Manage Channels` permission here to use this command.", ephemeral=True)
            return
        
        subscription = get_subscription(ctx.channel)
        if not subscription:
            await ctx.respond("✗ This channel has no subscriptions.", ephemeral=True)
            return

        unsubscribe(subscription)

        embed = Embed()
        embed.colour = Colour.from_rgb(255, 170, 50)
        embed.add_field(
            name="🔕\u2000Unsubscribed from",
            value=f"""
                {escape_markdown(subscription.filter)}
                `{expand(subscription.filter)}`
                """
        )

        await ctx.respond("✓", embed=embed)
    
    @commands.slash_command()
    async def recent(self, ctx, filter: Option(str, "The first event matching this will be sent in the channel.", required=False, default=None)):
        """Returns the most recent event gathered, optionally matching `filter`."""

        if filter and not await validate_filter(ctx, filter, filter_context):
            return  # `validate_filter` will respond for us.

        await ctx.defer(ephemeral=False)

        matching_filter_str = f" matching `{filter}`" if filter else ""

        filter_query, filter_values = filter_to_sql(filter)
        database = Database(SCRAPER_DB_NAME)
        try:
            event = await database.retrieve_event(
                where        = filter_query,
                where_values = filter_values,
                order_by     = "time DESC",
                extensive    = True if filter else False
            )
        except TimeoutError:
            await ctx.followup.send(f"✗ Took too long to find an event{matching_filter_str}.")
            return

        if not event:
            await ctx.followup.send(f"✗ No event{matching_filter_str} could be found.")
            return

        await ctx.followup.send(f"✓ Most recent event{matching_filter_str}:\r\n{format_link(event)}", embed=await format_embed(event))
    
    @commands.slash_command()
    async def filters(self, ctx, key: Option(str, "Explains how this specific filter key works (e.g. `creator`).", required=False, default=None)):
        """Explains how filters work with examples."""
        if key:
            key = key.lower().strip()
            tag = filter_context.get_tag(key)
            keys = tag.names if tag else None

            if not tag or not keys:
                await ctx.respond(f"✗ No filter key `{key}` exists.", ephemeral=True)
                return

            await ctx.respond("Type `/filters` for a list of keys and gates.", embed=filter_embed(key, filter_context), ephemeral=True)
            return

        await ctx.respond("Type `/filters <key>` for usage.", embed=filters_embed(filter_context), ephemeral=True)

def setup(bot):
    bot.add_cog(Subscription(bot))