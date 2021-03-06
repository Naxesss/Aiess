import sys
sys.path.append('..')

from bs4 import BeautifulSoup

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
				<a class="page-mode-link " href="https://osu.ppy.sh/beatmapsets/1111383/discussion/2322092/general" data-mode="general">
					<div>General 
						<span class="page-mode-link__subtitle">(This difficulty)</span>
					</div>
					<span class="page-mode-link__badge">6</span>
					<span class="page-mode-link__stripe"></span>
				</a>
			</li>
			<li class="page-mode__item">
				<a class="page-mode-link page-mode-link--is-active" href="https://osu.ppy.sh/beatmapsets/1111383/discussion/2322092/timeline" data-mode="timeline">
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

<div class="beatmap-discussions__discussion">
    <div class="beatmap-discussions__discussion beatmapset-activities__discussion-post">
        <div class="beatmap-discussion beatmapset-activities__post-grow">
            <div class="beatmap-discussion-timestamp__icons-container">
                <div class="beatmap-discussion-timestamp__icons">
                    <a href="https://osu.ppy.sh/beatmapsets/1094899/discussion#/1367171">
                        <img class="beatmapset-activities__beatmapset-cover" src="https://assets.ppy.sh/beatmaps/1094899/covers/list.jpg?1579725281" srcset="https://assets.ppy.sh/beatmaps/1094899/covers/list.jpg?1579725281 1x, https://assets.ppy.sh/beatmaps/1094899/covers/list@2x.jpg?1579725281 2x">
                    </a>
                    <div class="beatmap-discussion-timestamp__icon beatmapset-activities__timeline-icon-margin">
                        <span class="beatmap-discussion-message-type beatmap-discussion-message-type--suggestion">
                            <span class="far fa-circle"></span>
                        </span>
                    </div>
                </div>
            </div>
            <div class="beatmap-discussion__discussion">
                <div class="beatmap-discussion__top">
                    <div class="beatmap-discussion-post beatmap-discussion-post--discussion">
                        <div class="beatmap-discussion-post__content">
                            <div class="beatmap-discussion-user-card beatmap-discussion-user-card--{&quot;group_id&quot;:32,&quot;group_type&quot;:1,&quot;group_founder_manage&quot;:0,&quot;group_name&quot;:&quot;Beatmap Nominators (Probationary)&quot;,&quot;group_desc&quot;:&quot;&quot;,&quot;group_desc_bitfield&quot;:&quot;&quot;,&quot;group_desc_options&quot;:7,&quot;group_desc_uid&quot;:&quot;&quot;,&quot;group_display&quot;:0,&quot;group_avatar&quot;:&quot;&quot;,&quot;group_avatar_type&quot;:0,&quot;group_avatar_width&quot;:0,&quot;group_avatar_height&quot;:0,&quot;group_rank&quot;:0,&quot;group_colour&quot;:&quot;#6B3FA0&quot;,&quot;group_sig_chars&quot;:0,&quot;group_receive_pm&quot;:0,&quot;group_message_limit&quot;:0,&quot;group_legend&quot;:1,&quot;identifier&quot;:&quot;bng_limited&quot;,&quot;short_name&quot;:&quot;BN&quot;,&quot;display_order&quot;:5,&quot;colour&quot;:&quot;A347EB&quot;}">
                                <div class="beatmap-discussion-user-card__avatar">
                                    <a class="beatmap-discussion-user-card__user-link" href="https://osu.ppy.sh/users/9327302">
                                        <div class="avatar avatar--full-rounded" style="background-image: url(https://a.ppy.sh/9327302?1578169305.jpeg)"></div>
                                    </a>
                                </div>
                                <div class="beatmap-discussion-user-card__user">
                                    <div class="beatmap-discussion-user-card__user-row">
                                        <a class="beatmap-discussion-user-card__user-link" href="https://osu.ppy.sh/users/9327302">
                                            <span class="beatmap-discussion-user-card__user-text u-ellipsis-overflow">SMOKELIND</span>
                                        </a>
                                        <a class="beatmap-discussion-user-card__user-modding-history-link" href="https://osu.ppy.sh/users/9327302/modding" title="View modding history">
                                            <i class="fas fa-align-left"></i>
                                        </a>
                                    </div>
                                    <div class="beatmap-discussion-user-card__user-badge">
                                        <div class="user-group-badge user-group-badge--{&quot;group_id&quot;:32,&quot;group_type&quot;:1,&quot;group_founder_manage&quot;:0,&quot;group_name&quot;:&quot;Beatmap Nominators (Probationary)&quot;,&quot;group_desc&quot;:&quot;&quot;,&quot;group_desc_bitfield&quot;:&quot;&quot;,&quot;group_desc_options&quot;:7,&quot;group_desc_uid&quot;:&quot;&quot;,&quot;group_display&quot;:0,&quot;group_avatar&quot;:&quot;&quot;,&quot;group_avatar_type&quot;:0,&quot;group_avatar_width&quot;:0,&quot;group_avatar_height&quot;:0,&quot;group_rank&quot;:0,&quot;group_colour&quot;:&quot;#6B3FA0&quot;,&quot;group_sig_chars&quot;:0,&quot;group_receive_pm&quot;:0,&quot;group_message_limit&quot;:0,&quot;group_legend&quot;:1,&quot;identifier&quot;:&quot;bng_limited&quot;,&quot;short_name&quot;:&quot;BN&quot;,&quot;display_order&quot;:5,&quot;colour&quot;:&quot;A347EB&quot;}"></div>
                                    </div>
                                </div>
                                <div class="beatmap-discussion-user-card__user-stripe"></div>
                            </div>

                            <div class="beatmap-discussion-post__message-container">
                                <div class="beatmap-discussion-post__message">
                                    if you decided to your svs in the diff, could change some values a bit to fit different sections nicer
                                    Considering overall intensity parts like 
                                    00:02:313 - 00:23:411
                                    00:44:510 - 01:05:609
                                    01:16:159 - 01:21:433
                                    Deserve to have slightly lower value, 0.8 or smth, so the difference can be more clear in comparison with other stuff which is more intense in some way 00:23:411, 01:05:609 etc.
                                </div>
                                <div class="beatmap-discussion-post__info-container">
                                    <span class="beatmap-discussion-post__info"><time class="js-timeago" datetime="2020-01-24T11:17:51+00:00" title="January 24, 2020 at 11:17:51 AM UTC">about a minute ago</time></span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="beatmap-discussions__discussion beatmapset-activities__discussion-post">
        <div class="beatmap-discussion beatmapset-activities__post-grow">
            <div class="beatmap-discussion-timestamp__icons-container">
                <div class="beatmap-discussion-timestamp__icons">
                    <a href="https://osu.ppy.sh/beatmapsets/2/discussion#/1295203">
                        <img class="beatmapset-activities__beatmapset-cover" src="https://assets.ppy.sh/beatmaps/2/covers/list.jpg?1575564822" srcset="https://assets.ppy.sh/beatmaps/2/covers/list.jpg?1575564822 1x, https://assets.ppy.sh/beatmaps/2/covers/list@2x.jpg?1575564822 2x">
                    </a>
                    <div class="beatmap-discussion-timestamp__icon beatmapset-activities__timeline-icon-margin">
                        <span class="beatmap-discussion-message-type beatmap-discussion-message-type--problem">
                            <span class="fas fa-exclamation-circle"></span>
                        </span>
                    </div>
                </div>
            </div>
            <div class="beatmap-discussion__discussion">
                <div class="beatmap-discussion__top">
                    <div class="beatmap-discussion-post beatmap-discussion-post--discussion">
                        <div class="beatmap-discussion-post__content">
                            <div class="beatmap-discussion-user-card beatmap-discussion-user-card--alumni">
                                <div class="beatmap-discussion-user-card__avatar">
                                    <a class="beatmap-discussion-user-card__user-link" href="https://osu.ppy.sh/users/197805">
                                        <div class="avatar avatar--full-rounded" style="background-image: url(https://a.ppy.sh/197805?1531219665.jpeg)"></div>
                                    </a>
                                </div>
                                <div class="beatmap-discussion-user-card__user">
                                    <div class="beatmap-discussion-user-card__user-row">
                                        <a class="beatmap-discussion-user-card__user-link" href="https://osu.ppy.sh/users/197805">
                                            <span class="beatmap-discussion-user-card__user-text u-ellipsis-overflow">Niva</span>
                                        </a>
                                        <a class="beatmap-discussion-user-card__user-modding-history-link" href="https://osu.ppy.sh/users/197805/modding" title="View modding history">
                                            <i class="fas fa-align-left"></i>
                                        </a>
                                    </div>
                                    <div class="beatmap-discussion-user-card__user-badge">
                                        <div class="user-group-badge user-group-badge--alumni"></div>
                                    </div>
                                </div>
                                <div class="beatmap-discussion-user-card__user-stripe"></div>
                            </div>

                            <div class="beatmap-discussion-post__message-container">
                                <div class="beatmap-discussion-post__message">((in a more serious note tho : 04:05:694 (1) - aimod tells that this slider's end is not snapped properly))</div>
                                <div class="beatmap-discussion-post__info-container">
                                    <span class="beatmap-discussion-post__info"><time class="js-timeago" datetime="2019-12-05T16:50:10+00:00" title="December 5, 2019 at 4:50:10 PM UTC">about 2 hours ago</time></span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="beatmap-discussion__line beatmap-discussion__line--resolved"></div>
            </div>
        </div>
    </div>
</div>
"""
soup: BeautifulSoup = soupify(HTML)