import sys
sys.path.append('..')

from bs4 import BeautifulSoup, Tag

from scraper.requester import soupify

HTML = """
<script id="json-index" type="application/json">
    {
        "news_posts": [
            {
                "id": 812,
                "author": " -Mo- &amp; Ephemeral",
                "edit_url": "https://github.com/ppy/osu-wiki/tree/master/news/2020-07-21-aspire-v-finals-stage-voting.md",
                "first_image": "https://assets.ppy.sh/contests/94/header.jpg",
                "published_at": "2020-07-22T21:00:00+00:00",
                "updated_at": "2020-07-22T21:51:50+00:00",
                "slug": "2020-07-21-aspire-v-finals-stage-voting",
                "title": "Aspire V - Finals Stage Voting",
                "preview": "You've chosen your favourite beatmaps from the Aspire V categories, now it's time to pick the best of the best!"
            },
            {
                "id": 811,
                "author": "Ephemeral",
                "edit_url": "https://github.com/ppy/osu-wiki/tree/master/news/2020-07-22-new-featured-artist-receptor.md",
                "first_image": "https://assets.ppy.sh/artists/91/header.jpg",
                "published_at": "2020-07-22T08:00:00+00:00",
                "updated_at": "2020-07-22T11:00:04+00:00",
                "slug": "2020-07-22-new-featured-artist-receptor",
                "title": "New Featured Artist: Receptor",
                "preview": "We're excited to welcome Receptor aboard as our latest Featured Artist!"
            },
            {
                "id": 810,
                "author": "WalterToro",
                "edit_url": "https://github.com/ppy/osu-wiki/tree/master/news/2020-07-17-mwc-4k-2020-registrations-open.md",
                "first_image": "/help/wiki/shared/news/banners/MWC4k2020.jpg",
                "published_at": "2020-07-17T14:00:00+00:00",
                "updated_at": "2020-07-17T15:13:49+00:00",
                "slug": "2020-07-17-mwc-4k-2020-registrations-open",
                "title": "osu!mania 4K World Cup 2020: Registrations now open!",
                "preview": "Oh boy, here we go again. The osu!mania 4K World Cup registration phase is now open!"
            },
            {
                "id": 809,
                "author": "Ephemeral",
                "edit_url": "https://github.com/ppy/osu-wiki/tree/master/news/2020-07-16-summer-theme-park-2020-voting-open.md",
                "first_image": "https://assets.ppy.sh/contests/107/header.jpg",
                "published_at": "2020-07-16T10:00:00+00:00",
                "updated_at": "2020-07-16T10:13:08+00:00",
                "slug": "2020-07-16-summer-theme-park-2020-voting-open",
                "title": "Summer Theme Park 2020 Fanart Contest Voting Open",
                "preview": "10 votes, 116 entries — help us decide which fanart pieces are tall enough to ride the victory rollercoaster!"
            },
            {
                "id": 808,
                "author": "clayton",
                "edit_url": "https://github.com/ppy/osu-wiki/tree/master/news/2020-07-16-project-loved-july-2020.md",
                "first_image": "/help/wiki/shared/news/banners/project-loved.jpg",
                "published_at": "2020-07-16T09:00:00+00:00",
                "updated_at": "2020-07-16T09:00:47+00:00",
                "slug": "2020-07-16-project-loved-july-2020",
                "title": "Project Loved: July 2020",
                "preview": "Project Loved is back for the monthly routine of finding out which maps you want to see in Loved. Check out the picks and cast your votes!"
            },
            {
                "id": 807,
                "author": "Ephemeral",
                "edit_url": "https://github.com/ppy/osu-wiki/tree/master/news/2020-07-15-new-featured-artist-numtack05.md",
                "first_image": "https://assets.ppy.sh/artists/90/header.jpg",
                "published_at": "2020-07-15T08:00:00+00:00",
                "updated_at": "2020-07-15T11:59:39+00:00",
                "slug": "2020-07-15-new-featured-artist-numtack05",
                "title": "New Featured Artist: Numtack05",
                "preview": "Numtack05 joins the lineup as our latest Featured Artist!"
            }
        ],
        "search": {
            "cursor": null,
            "limit": 6
        },
        "cursor": {
            "published_at": "2020-07-15T08:00:00.000000Z",
            "id": 807
        }
    }
</script>
"""

soup: BeautifulSoup = soupify(HTML)
tag: Tag = soup.find("div", {"class": "news-card"})