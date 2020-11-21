![](https://i.imgur.com/RR3937R.jpg)
# Aiess
![tests](https://github.com/Naxesss/Aiess/workflows/tests/badge.svg) [![codecov](https://codecov.io/gh/Naxesss/Aiess/branch/master/graph/badge.svg)](https://codecov.io/gh/Naxesss/Aiess) [![CodeFactor](https://www.codefactor.io/repository/github/naxesss/aiess/badge)](https://www.codefactor.io/repository/github/naxesss/aiess) [![Discord](https://img.shields.io/discord/420015424365789184.svg?label=&logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)](https://discord.gg/2XV5dcW)

## Discord Bot `/bot` | [Invite](https://discord.com/api/oauth2/authorize?client_id=680467769573244928&permissions=0&scope=bot)
Provides subscriptions for mapping-related events in osu! (e.g. ranks, qualifications, nominations, suggestions, newsposts, group changes, etc). Written in [discord.py](https://discordpy.readthedocs.io/). Example commands:
- `+recent [filter]` Retrieves the latest event data, optionally matching a specific filter (e.g. `+recent type:nominate`).
- `+sub [filter]` Show current subscription, or subscribe to new events matching the given filter (e.g. `+sub user:ephemeral`)

Filtering supports logical operators (`and`/`or`/`not` case insensitive), parentheses (e.g. `type:(nominate or qualify)`), and aliases for types and groups (e.g. `type:nomination-reset` = `type:reset`). Here's a few useful filters:
- **#mapfeed** `type:(nom or qual or dq or pop or rank or love) and not user:banchobot`
- **#mapfeed-osu** `type:(nom or qual or dq or pop or rank or love) and not user:banchobot and mode:osu`
- **#groupfeed** `type:(add or remove)`
- **#groupfeed-bns** `group:bns`
- **#newsfeed** `type:news`
- **#newsfeed-fa** `type:news and news-title:"%featured artist%"`

All commands are admin-only by default. This can be changed using `+enable` and `+disable`, which also supports filtering to certain roles/channels/users, similarly to events (e.g. `+enable recent channel:#bot`).

## Web Scraper `/scraper`
Gathers event data from the [osu! website](https://osu.ppy.sh) into a MySQL database. Rate limited at 1 page / 60 s, and 1 osu!api request / 1 s.
| Page(s) scraped | Event type(s) yielded |
|-----------------|-----------------------|
|**[/beatmapsets/events](https://osu.ppy.sh/beatmapsets/events)**|`Nominated` `Qualified` `Nomination Reset` `Disqualified` `Ranked` `Loved` `Resolved` `Reopened` `Kudosu Given` `Kudosu Removed` `Kudosu Allowed` `Kudosu Denied` `Genre Edit` `Language Edit`|
|**[/beatmapsets/beatmap-discussions](https://osu.ppy.sh/beatmapsets/beatmap-discussions)**|`Suggestion` `Problem` `Note` `Praise` `Hype`|
|**[/beatmapsets/beatmap-discussion-posts](https://osu.ppy.sh/beatmapsets/beatmap-discussion-posts)**|`Reply`|
|**[/home/news](https://osu.ppy.sh/home/news)**|`News`|
|**[/groups/28](https://osu.ppy.sh/groups/28)** (full bns), **[/groups/32](https://osu.ppy.sh/groups/32)** (probo bns), **[/groups/7](https://osu.ppy.sh/groups/7)** (nat), **[/groups/4](https://osu.ppy.sh/groups/4)** (gmt), **[/groups/16](https://osu.ppy.sh/groups/16)** (alumni), **[/groups/11](https://osu.ppy.sh/groups/11)** (devs), **[/groups/22](https://osu.ppy.sh/groups/22)** (support)|`Added` `Removed`|

## BN Website MongoDB Interface `/bnsite` | [bn.mappersguild.com](https://bn.mappersguild.com/) | [github.com/pishifat/qat/](https://github.com/pishifat/qat/)
Reads `Nominated`, `Qualified`, `Nomination Reset`, `Disqualified` and `Ranked` events from the local database, and inserts them into a 3rd-party mongodb database used by the website. This enables the [Nomination Assessment Team](https://osu.ppy.sh/help/wiki/People/The_Team/Nomination_Assessment_Team) to conduct activity and performance evaluations of [Beatmap Nominators](https://osu.ppy.sh/help/wiki/People/The_Team/Beatmap_Nominators). Evaluation data is then requested to populate group events with additional information.

## BN Stats Interface `/bnstats` | [bnstats.rorre.xyz](https://bnstats.rorre.xyz/) | [github.com/rorre/BNStats/](https://github.com/rorre/BNStats/)
Reads `Nominated`, `Qualified`, `Nomination Reset`, and `Disqualified` events from the local database, and sends POST requests with the event data in json format to the website. This enables statistical analysis of [Beatmap Nominator](https://osu.ppy.sh/help/wiki/People/The_Team/Beatmap_Nominators) activity, including individual performance metrics.
