import sys
sys.path.append('..')

from bs4 import BeautifulSoup, Tag

from scraper.requester import soupify

HTML = """
<div class="beatmap-discussions__discussion beatmapset-activities__discussion-post">
    <div class="beatmap-discussion beatmapset-activities__post-grow">
        <div class="beatmap-discussion-timestamp__icons-container">
            <div class="beatmap-discussion-timestamp__icons">
                <a href="https://osu.ppy.sh/beatmapsets/759587/discussion#/1396395">
                    <img class="beatmapset-activities__beatmapset-cover" src="https://assets.ppy.sh/beatmaps/759587/covers/list.jpg?1580846389" srcset="https://assets.ppy.sh/beatmaps/759587/covers/list.jpg?1580846389 1x, https://assets.ppy.sh/beatmaps/759587/covers/list@2x.jpg?1580846389 2x">
                </a>
                <div class="beatmap-discussion-timestamp__icon beatmapset-activities__timeline-icon-margin">
                    <span class="beatmap-discussion-message-type">
                        <span class="fas fa-reply"></span>
                    </span>
                </div>
            </div>
        </div>
        <div class="beatmap-discussion__discussion">
            <div class="beatmap-discussion__top">
                <div class="beatmap-discussion-post beatmap-discussion-post--discussion">
                    <div class="beatmap-discussion-post__content">
                        <div class="beatmap-discussion-user-card" style="--group-colour: initial">
                            <div class="beatmap-discussion-user-card__avatar">
                                <a class="beatmap-discussion-user-card__user-link" href="https://osu.ppy.sh/users/6751666">
                                    <div class="avatar avatar--full-rounded" style="background-image: url(https://a.ppy.sh/6751666?1568406376.png)"></div>
                                </a>
                            </div>
                            <div class="beatmap-discussion-user-card__user">
                                <div class="beatmap-discussion-user-card__user-row">
                                    <a class="beatmap-discussion-user-card__user-link" href="https://osu.ppy.sh/users/6751666">
                                        <span class="beatmap-discussion-user-card__user-text u-ellipsis-overflow">Tailsdk</span>
                                    </a>
                                    <a class="beatmap-discussion-user-card__user-modding-history-link" href="https://osu.ppy.sh/users/6751666/modding" title="View modding history">
                                        <i class="fas fa-align-left"></i>
                                    </a>
                                </div>
                                <div class="beatmap-discussion-user-card__user-badge"></div>
                            </div>
                            <div class="beatmap-discussion-user-card__user-stripe"></div>
                        </div>
                        <div class="beatmap-discussion-post__message-container">
                            <div class="beatmap-discussion-post__message">its for the vocal</div>
                            <div class="beatmap-discussion-post__info-container">
                                <span class="beatmap-discussion-post__info">
                                    <time class="js-timeago" datetime="2020-02-14T17:35:47+00:00" title="February 14, 2020 at 5:35:47 PM UTC">12 minutes ago</time>
                                </span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
"""
CONTENT = "its for the vocal"
soup: BeautifulSoup = soupify(HTML)
tag: Tag = soup.find("div", {"class": "beatmapset-activities__discussion-post"})