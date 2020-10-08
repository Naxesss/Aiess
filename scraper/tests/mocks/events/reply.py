import sys
sys.path.append('..')

from bs4 import BeautifulSoup, Tag

from scraper.requester import soupify

HTML = """
<div class="beatmap-discussions-header-top__filter-group">
	<div class="beatmap-list undefined">
		<div class="beatmap-list__body">
			<a href="https://osu.ppy.sh/beatmapsets/1111383/discussion/2322092/timeline" class="beatmap-list__item beatmap-list__item--selected beatmap-list__item--large js-beatmap-list-selector">
				<div class="beatmap-list-item beatmap-list-item--large">
					<div class="beatmap-list-item__col">
						<div class="beatmap-icon beatmap-icon--large beatmap-icon--with-hover js-beatmap-tooltip" data-beatmap-title="Expert" data-stars="5.18" data-difficulty="insane" style="--diff:var(--diff-insane);" data-hasqtip="0">
							<i class="fal fa-extra-mode-osu"></i>
						</div>
					</div>
					<div class="beatmap-list-item__col beatmap-list-item__col--main">
						<div class="u-ellipsis-overflow">Expert</div>
					</div>
					<div class="beatmap-list-item__col">
						<i class="fas fa-chevron-down"></i>
					</div>
				</div>
			</a>
			<div class="beatmap-list__selector">
				<a href="https://osu.ppy.sh/beatmapsets/1111383/discussion/2342266/timeline" class="beatmap-list__item" data-id="2342266">
					<div class="beatmap-list-item">
						<div class="beatmap-list-item__col">
							<div class="beatmap-icon beatmap-icon--undefined beatmap-icon--with-hover js-beatmap-tooltip" data-beatmap-title="Tatsuo's Normal" data-stars="2.24" data-difficulty="normal" style="--diff:var(--diff-normal);">
								<i class="fal fa-extra-mode-osu"></i>
							</div>
						</div>
						<div class="beatmap-list-item__col beatmap-list-item__col--main">
							<div class="u-ellipsis-overflow">Tatsuo's Normal</div>
						</div>
						<div class="beatmap-list-item__col">
							<div class="beatmap-list-item__counter">3</div>
						</div>
					</div>
				</a>
				<a href="https://osu.ppy.sh/beatmapsets/1111383/discussion/2336411/timeline" class="beatmap-list__item" data-id="2336411">
					<div class="beatmap-list-item">
						<div class="beatmap-list-item__col">
							<div class="beatmap-icon beatmap-icon--undefined beatmap-icon--with-hover js-beatmap-tooltip" data-beatmap-title="Hard" data-stars="3.5" data-difficulty="hard" style="--diff:var(--diff-hard);">
								<i class="fal fa-extra-mode-osu"></i>
							</div>
						</div>
						<div class="beatmap-list-item__col beatmap-list-item__col--main">
							<div class="u-ellipsis-overflow">Hard</div>
						</div>
						<div class="beatmap-list-item__col">
							<div class="beatmap-list-item__counter">6</div>
						</div>
					</div>
				</a>
				<a href="https://osu.ppy.sh/beatmapsets/1111383/discussion/2333030/timeline" class="beatmap-list__item" data-id="2333030">
					<div class="beatmap-list-item">
						<div class="beatmap-list-item__col">
							<div class="beatmap-icon beatmap-icon--undefined beatmap-icon--with-hover js-beatmap-tooltip" data-beatmap-title="Insane" data-stars="4.55" data-difficulty="insane" style="--diff:var(--diff-insane);">
								<i class="fal fa-extra-mode-osu"></i>
							</div>
						</div>
						<div class="beatmap-list-item__col beatmap-list-item__col--main">
							<div class="u-ellipsis-overflow">Insane</div>
						</div>
						<div class="beatmap-list-item__col">
							<div class="beatmap-list-item__counter">3</div>
						</div>
					</div>
				</a>
				<a href="https://osu.ppy.sh/beatmapsets/1111383/discussion/2322092/timeline" class="beatmap-list__item beatmap-list__item--current" data-id="2322092">
					<div class="beatmap-list-item">
						<div class="beatmap-list-item__col">
							<div class="beatmap-icon beatmap-icon--undefined beatmap-icon--with-hover js-beatmap-tooltip" data-beatmap-title="Expert" data-stars="5.18" data-difficulty="insane" style="--diff:var(--diff-insane);">
								<i class="fal fa-extra-mode-osu"></i>
							</div>
						</div>
						<div class="beatmap-list-item__col beatmap-list-item__col--main">
							<div class="u-ellipsis-overflow">Expert</div>
						</div>
						<div class="beatmap-list-item__col">
							<div class="beatmap-list-item__counter">2</div>
						</div>
					</div>
				</a>
			</div>
		</div>
	</div>
</div>

<div class="page-extra-tabs">
	<div class="osu-page osu-page--small">
		<ul class="page-mode page-mode--page-extra-tabs">
			<li class="page-mode__item">
				<a class="page-mode-link " href="https://osu.ppy.sh/beatmapsets/1111383/discussion/-/reviews" data-mode="reviews">
					<div>Reviews</div>
					<span class="page-mode-link__badge">0</span>
					<span class="page-mode-link__stripe"></span>
				</a>
			</li>
			<li class="page-mode__item">
				<a class="page-mode-link " href="https://osu.ppy.sh/beatmapsets/1111383/discussion/-/generalAll" data-mode="generalAll">
					<div>General 
						<span class="page-mode-link__subtitle">(All difficulties)</span>
					</div>
					<span class="page-mode-link__badge">22</span>
					<span class="page-mode-link__stripe"></span>
				</a>
			</li>
			<li class="page-mode__item">
				<a class="page-mode-link page-mode-link--is-active" href="https://osu.ppy.sh/beatmapsets/1111383/discussion/2322092/general" data-mode="general">
					<div>General 
						<span class="page-mode-link__subtitle">(This difficulty)</span>
					</div>
					<span class="page-mode-link__badge">6</span>
					<span class="page-mode-link__stripe"></span>
				</a>
			</li>
			<li class="page-mode__item">
				<a class="page-mode-link " href="https://osu.ppy.sh/beatmapsets/1111383/discussion/2322092/timeline" data-mode="timeline">
					<div>Timeline</div>
					<span class="page-mode-link__badge">35</span>
					<span class="page-mode-link__stripe"></span>
				</a>
			</li>
			<li class="page-mode__item">
				<a class="page-mode-link " href="https://osu.ppy.sh/beatmapsets/1111383/discussion/-/events" data-mode="events">
					<div>History</div>
					<span class="page-mode-link__stripe"></span>
				</a>
			</li>
		</ul>
	</div>
</div>

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