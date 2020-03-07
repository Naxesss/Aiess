from bs4 import BeautifulSoup, Tag

from requester import soupify

HTML = """
<div class="beatmapset-events__event">
    <div class="beatmapset-event">
        <span>Something isn't right here...</span>
    </div>
</div>
"""
soup: BeautifulSoup = soupify(HTML)
tag: Tag = soup.find("div", {"class": "beatmapset-event"})