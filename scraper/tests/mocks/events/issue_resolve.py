from bs4 import BeautifulSoup, Tag

from scraper import soupify

HTML = """
<div class="beatmapset-events__event">
    <div class="beatmapset-event">
        <a href="https://osu.ppy.sh/beatmapsets/1011055/discussion#/1294675" title="
            Tokyo's Starlight - HyuN
            (mapped by Heilia)
        ">
            <img class="beatmapset-activities__beatmapset-cover" src="https://assets.ppy.sh/beatmaps/1011055/covers/list.jpg?1575541706" srcset="https://assets.ppy.sh/beatmaps/1011055/covers/list.jpg?1575541706 1x, https://assets.ppy.sh/beatmaps/1011055/covers/list@2x.jpg?1575541706 2x">
        </a>
        <div class="beatmapset-event__icon beatmapset-event__icon--issue-resolve beatmapset-activities__event-icon-spacer"></div>
        <div>
            <div class="beatmapset-event__content">
                Issue <a href="https://osu.ppy.sh/beatmapsets/1011055/discussion#/1294675">#1294675</a> marked as resolved.
            </div>
            <div><time class="timeago" datetime="2019-12-05T10:26:54+00:00" title="December 5, 2019 at 10:26:54 AM UTC">about 7 hours ago</time></div>
        </div>
    </div>
</div>
"""
soup: BeautifulSoup = soupify(HTML)
tag: Tag = soup.find("div", {"class": "beatmapset-event"})