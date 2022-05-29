![](https://i.imgur.com/RR3937R.jpg)
# Aiess
![tests](https://github.com/Naxesss/Aiess/workflows/tests/badge.svg) [![codecov](https://codecov.io/gh/Naxesss/Aiess/branch/master/graph/badge.svg)](https://codecov.io/gh/Naxesss/Aiess) [![CodeFactor](https://www.codefactor.io/repository/github/naxesss/aiess/badge)](https://www.codefactor.io/repository/github/naxesss/aiess) [![Discord](https://img.shields.io/discord/420015424365789184.svg?label=&logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)](https://discord.gg/2XV5dcW)

Aiess gathers mapping-related events in osu! (e.g. ranks, qualifications, nominations, suggestions, newsposts, group changes, etc), and provides the ability to subscribe to these events through a Discord bot.

## Discord Bot (`./bot`) | **[Invite](https://discord.com/api/oauth2/authorize?client_id=680467769573244928&permissions=0&scope=bot%20applications.commands)**
Written in [Python](https://www.python.org/) using [Pycord](https://docs.pycord.dev/en/master/).

### **Example Commands**
- `/subscribe <filter>` Subscribes this channel to events matching `<filter>`
  - e.g. `/subscribe type:ranked`
  
    ![](https://i.imgur.com/VDgSBPu.png)
- `/recent [filter]` Returns the most recent event gathered, optionally matching `[filter]`
  - e.g. `/recent type:ranked and creator:vinxis`
  
    ![](https://i.imgur.com/gNzQTgn.png)

### **Filtering**
Supports
- logical operators (`and`/`or`/`not` case insensitive).
- parentheses (e.g. `type:(nominate or qualify)`).
- aliases for types and groups (e.g. `type:nomination-reset` = `type:reset`).
- quoting to escape spaces (e.g. `user:"name with spaces"`).
- basic wildcards (e.g. `content:%needle%` for any event with "needle" in its text).


Here's a few useful filters:
- **#mapfeed** `type:(nom or qual or dq or pop or rank or love) and not user:banchobot`
- **#mapfeed-osu** `type:(nom or qual or dq or pop or rank or love) and not user:banchobot and mode:osu`
- **#groupfeed** `type:(add or remove)`
- **#groupfeed-bns** `group:bns`
- **#newsfeed** `type:news`
- **#newsfeed-fa** `type:news and news-title:"%featured artist%"`

### **Permissions**
Commands can be disabled in **Server Settings > Integrations > Aiess**. By default:
- `/subscribe` and `/unsubscribe` requires the `Manage Channel` permission.
- `/info`, `/ping`, etc. are public, but only visible to the caller.

  ![](https://i.imgur.com/lqmIQp0.png)
- `/recent` is public.

## Event Gatherer (`./scraper`)
Gathers event data from [osu!apiv2](https://osu.ppy.sh/docs/index.html) and the [osu! website](https://osu.ppy.sh) into a [MySQL](https://www.mysql.com/) database.

### **Rate Limits**
| Request | Rate Limit |
|:-|:-
| Page | 1 / 60 seconds |
| API | 1 / 1 second |

### **Scraping**
| Route(s) | Event type(s) yielded |
|-----------------|-----------------------|
|**[/beatmapsets/events](https://osu.ppy.sh/beatmapsets/events)**|`Nominated`, `Qualified`, `Nomination Reset`, `Disqualified`, `Ranked`, `Loved`, `Unloved`, `Resolved`, `Reopened`, `Kudosu Given`, `Kudosu Removed`, `Kudosu Allowed`, `Kudosu Denied`, `Genre Edit`, `Language Edit`|
|**[/beatmapsets/discussions](https://osu.ppy.sh/beatmapsets/discussions)**|`Suggestion`, `Problem`, `Note`, `Praise`, `Hype`|
|**[/beatmapsets/discussions/posts](https://osu.ppy.sh/beatmapsets/discussions/posts)**|`Reply`|
|**[/home/news](https://osu.ppy.sh/home/news)**|`News`|
|**[/groups/28](https://osu.ppy.sh/groups/28)** (full bns), **[/groups/32](https://osu.ppy.sh/groups/32)** (probation bns), **[/groups/7](https://osu.ppy.sh/groups/7)** (nat), **[/groups/4](https://osu.ppy.sh/groups/4)** (gmt), **[/groups/16](https://osu.ppy.sh/groups/16)** (alumni), **[/groups/11](https://osu.ppy.sh/groups/11)** (devs), **[/groups/22](https://osu.ppy.sh/groups/22)** (support), **[/groups/31](https://osu.ppy.sh/groups/31)** (project loved)|`Added`, `Removed`|

## [BN Website]((https://github.com/pishifat/qat/)) Interface (`./bnsite`) | [bn.mappersguild.com](https://bn.mappersguild.com/)

Handles activity, performance, and application evaluations of [Beatmap Nominators](https://osu.ppy.sh/help/wiki/People/The_Team/Beatmap_Nominators).

| Events | Types |
|:-|:-
| Forwarded | `Nominated`, `Qualified`, `Nomination Reset`, `Disqualified`, `Ranked` |
| Retrieved | `SEV`, `Added`, `Removed`

## [BN Planner](https://github.com/Darius-Wattimena/bnplanner) Interface (`./bnplanner`)

Handles planning of nominations for [Beatmap Nominators](https://osu.ppy.sh/help/wiki/People/The_Team/Beatmap_Nominators) in osu!catch.

| Events | Types |
|:-|:-
| Forwarded | `Nominated`, `Qualified`, `Nomination Reset`, `Disqualified`, `Ranked`, `Add`, `Remove` |