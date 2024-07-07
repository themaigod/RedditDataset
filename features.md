## user

- user_id: user id in reddit

- user_created_utc: the created time of the user

- user_premium: the user is premium or not
## instance

- time_end_time_stamp: the end time stamp of the time window
## comment

- num_of_all_awardings: the number of all awardings of the comment. it will be 0 if the comment has no awardings. it may show the popularity of the comment, but may leaking the information of the future related to the label.

- achieved: achieved or not of the comment, post will be achieved if it has been 180 days since the post was created

- stickied: if the post is stickied or not, it may be a post that the moderator wants to highlight

- collapsed: collapsed or not for the comment, it is judged by the reddit algorithm which may be related to the label

- controversiality: the controversiality of the comment, it may be a good feature, but may leaking the information of the future related to the label.

- gilded: the gilded of the comment, it means the author will get a month of Reddit Premium and 100 Coins, it may be a good feature, but may leaking the information of the future related to the label.

- edited: edited or not for the comment.

- num_of_guildings: the number of guildings of the comment, it may be a good feature, but may leaking the information of the future related to the label.

- locked: locked or not for the comment, it means the comment is locked by the moderator and no one can comment on it.

- no_follow: no follow or not for the comment, it means tell the search engines to not follow the link.

- body_length: the length of the body of the comment

- can_gild: can gild or not for the comment, it means the comment can be gilded or not.

- created_utc: the created time of the comment

- num_of_gildings: the number of gildings of the comment, it may be a good feature, but may leaking the information of the future related to the label.

- score: the score of the comment, it may be a good feature, but may leaking the information of the future related to the label.

- score_hidden: score hidden or not for the comment, it means the score of the comment is hidden or not.

- send_replies: send replies or not for the comment, it means the author will receive a notification when someone comments on the comment.

- is_submitter: the author is the submitter of the post or not

- have_unrepliable_reason: have unrepliable reason or not for the comment.

- post_level: the level of the whole post tree, it means the post is the i level leaves of the whole post tree. i.e. 0 means the post is the root of the whole post tree.

- comment_type: the type of the comment, mostly it is None

- num_of_comments: the number of comments of the comment in the observation period

- subreddit_subscribers: the number of subscribers of the subreddit of the comment

- subreddit_type: the type of the subreddit of the comment, mostly it is None

- subreddit_id: the id of the subreddit of the comment

- author_created_utc: the created time of the author

- author_premium: the author is premium or not
## submission

- num_of_all_awardings: the number of all awardings of the submission. it will be 0 if the submission has no awardings. it may show the popularity of the submission, but may leaking the information of the future related to the label.

- allow_live_comments: allow live comments or not for the submission, it means the submission can be commented on while it is live.

- archived: archived or not for the submission, it will be archived if it has been 180 days since the submission was created.

- num_of_awarders: the nums of awarders of the submission. it will be 0 if the submission has no awarders. it may show the popularity of the submission, but may leaking the information of the future related to the label.

- banned_by_someone: banned by someone or not for the submission

- can_gild: can gild or not for the submission, it means the submission can be gilded or not.

- can_mod_post: Whether the logged-in user can modify the post

- category: the category of the submission, mostly it is None

- num_of_comments: the number of comments of the submission in the observation period

- contest_mode: if the moderators choose to enable contest mode for the subreddit, it means the comment scores will be hidden and comments will be sorted randomly.

- created_utc: the created time of the submission

- content_categories: the content categories of the submission, mostly it is None

- discussion_type: the discussion type of the submission, mostly it is None

- distinguished: the distinguished of the submission, mostly it is None

- domain: the domain of the submission

- edited: edited or not for the submission.

- num_of_guildings: the number of guildings of the submission, it may be a good feature, but may leaking the information of the future related to the label.

- gilded: the gilded of the submission, it means the author will get a month of Reddit Premium and 100 Coins, it may be a good feature, but may leaking the information of the future related to the label.

- hidden: hidden or not for the submission, it means the submission is hidden or not.

- hide_score: hide score or not for the submission, it means the score of the submission is hidden or not.

- is_crosspostable: is a sharing post from another subreddit or not

- is_meta: is a meta post or not, it may be a post about the subreddit itself

- is_created_from_ads_ui: is created from ads ui or not

- is_original_content: is original content or not

- is_reddit_media_domain: is reddit media domain or not

- is_robot_indexable: is the post can be indexed by robots or not

- is_self: is self or not for the submission, it means the submission is a self post or not.

- is_video: is a video post or not

- link_flair_background_color: the link flair background color of the submission, mostly it is None

- link_flair_css_class: the link flair css class of the submission, mostly it is None

- link_flair_richtext: the link flair richtext of the submission, mostly it is None

- link_flair_template_id: the link flair template id of the submission, mostly it is None

- link_flair_text: the link flair text of the submission, mostly it is None

- link_flair_text_color: the link flair text color of the submission, mostly it is None

- link_flair_type: the link flair type of the submission, mostly it is None

- locked: locked or not for the submission, it means the submission is locked by the moderator and no one can comment on it.

- media_only: if the submission only contains media or not

- no_follow: no follow or not for the submission, it means tell the search engines to not follow the link.

- num_crossposts: the number of crossposts of the submission. it may be a good feature, but may leaking the information of the future related to the label.

- over_18: if the submission is visible only to users over 18 or not

- parent_whitelist_status: the parent whitelist status of the submission, mostly it is None

- pinned: pinned or not for the submission, it means the submission is pinned or not.

- pwls: the pwls of the submission

- quarantine: quarantine or not for the submission, it means the submission is quarantined or not.

- removed_by_someone: removed by someone or not for the submission

- score: the score of the submission, it may be a good feature, but may leaking the information of the future related to the label.

- length_of_selftext: the length of the selftext of the submission

- length_of_title: the length of the title of the submission

- send_replies: send replies or not for the submission, it means the author will receive a notification when someone comments on the submission.

- spoiler: if the submission is a spoiler or not, it may be a spoiler of a movie or a game

- stickied: if the submission is stickied or not, it may be a post that the moderator wants to highlight

- subreddit_subscribers: the number of subscribers of the subreddit of the submission

- suggested_sort: the suggested sort of the submission, mostly it is None

- subreddit_id: the id of the subreddit of the submission

- subreddit_type: the type of the subreddit of the submission, mostly it is None

- thumbnail: the thumbnail of the submission, mostly it is default

- top_awarded_type: the top awarded type of the submission, mostly it is None

- total_awards_received: the total awards received of the submission, it may be a good feature, but may leaking the information of the future related to the label.

- treatment_tags: the treatment tags of the submission, mostly it is None

- upvote_ratio: the upvote ratio of the submission, it may be a good feature, but may leaking the information of the future related to the label.

- whitelist_status: the whitelist status of the submission, mostly it is None

- wls: the wls of the submission, mostly it is 6

- num_of_all_comments: the number of all comments of the submission in the observation period, including the comments of the comments

- author_created_utc: the created time of the author

- author_premium: the author is premium or not
## label

- label: the label of the user, it means the user will be engaged or not in the prediction period
## sentiment

### post


- sentiment: the sentiment of the post

### whole_time_window


- sentiment_avg: the average sentiment of the whole time window


- sentiment_std: the standard deviation of the sentiment of the whole time window


- num_of_pos: the number of positive posts of the whole time window


- num_of_neg: the number of negative posts of the whole time window


- num_of_neu: the number of neutral posts of the whole time window


- num_of_pos_neg_ratio: the number of positive posts divided by the number of negative posts of the whole time window


- most_sentiment: the most sentiment of the whole time window


- times_of_most_sentiment: the times of the most sentiment of the whole time window


- times_of_sentiment_change: the times of the sentiment change of the whole time window


- times_of_sentiment_change_ratio: the times of the sentiment change divided by the number of posts of the whole time window


- times_of_sentiment_change_ratio_strong: the times of the sentiment change divided by the number of posts of the whole time window, but the sentiment change is only counted when the sentiment is changed from positive to negative or negative to positive


- times_of_sentiment_keep: the times of the sentiment keep of the whole time window


- times_of_sentiment_keep_ratio: the times of the sentiment keep divided by the number of posts of the whole time window


- times_of_sentiment_keep_ratio_strong: the times of the sentiment keep divided by the number of posts of the whole time window, but the sentiment keep is only counted when the sentiment is positive or negative


- times_of_sentiment_keep_ratio_weak: the times of the sentiment keep divided by the number of posts of the whole time window, but the sentiment keep is counted even when the sentiment is neutral


- the_first_sentiment: the first sentiment of the whole time window


- the_last_sentiment: the last sentiment of the whole time window


- the_first_sentiment_ratio: the first sentiment divided by the number of posts of the whole time window


- the_last_sentiment_ratio: the last sentiment divided by the number of posts of the whole time window


- the_first_sentiment_ratio_strong: the first sentiment divided by the number of posts of the whole time window, but the first sentiment is only counted when the sentiment is positive or negative


- the_last_sentiment_ratio_strong: the last sentiment divided by the number of posts of the whole time window, but the last sentiment is only counted when the sentiment is positive or negative

### seperate_days


- sentiment_avg_{i}_day: the average sentiment of the whole time window in the {i} day, i = 1, 2, ..., train_size, started from the prediction period


- sentiment_std_{i}_day: the standard deviation of the sentiment of the whole time window in the {i} day, i = 1, 2, ..., train_size, started from the prediction period


- num_of_pos_{i}_day: the number of positive posts of the whole time window in the {i} day, i = 1, 2, ..., train_size, started from the prediction period


- num_of_neg_{i}_day: the number of negative posts of the whole time window in the {i} day, i = 1, 2, ..., train_size, started from the prediction period


- num_of_neu_{i}_day: the number of neutral posts of the whole time window in the {i} day, i = 1, 2, ..., train_size, started from the prediction period


- num_of_pos_neg_ratio_{i}_day: the number of positive posts divided by the number of negative posts of the whole time window in the {i} day, i = 1, 2, ..., train_size, started from the prediction period


- most_sentiment_{i}_day: the most sentiment of the whole time window in the {i} day, i = 1, 2, ..., train_size, started from the prediction period


- times_of_most_sentiment_{i}_day: the times of the most sentiment of the whole time window in the {i} day, i = 1, 2, ..., train_size, started from the prediction period


- times_of_sentiment_change_{i}_day: the times of the sentiment change of the whole time window in the {i} day, i = 1, 2, ..., train_size, started from the prediction period


- times_of_sentiment_change_ratio_{i}_day: the times of the sentiment change divided by the number of posts of the whole time window in the {i} day, i = 1, 2, ..., train_size, started from the prediction period


- times_of_sentiment_change_ratio_strong_{i}_day: the times of the sentiment change divided by the number of posts of the whole time window, but the sentiment change is only counted when the sentiment is changed from positive to negative or negative to positive in the {i} day, i = 1, 2, ..., train_size, started from the prediction period


- times_of_sentiment_keep_{i}_day: the times of the sentiment keep of the whole time window in the {i} day, i = 1, 2, ..., train_size, started from the prediction period


- times_of_sentiment_keep_ratio_{i}_day: the times of the sentiment keep divided by the number of posts of the whole time window in the {i} day, i = 1, 2, ..., train_size, started from the prediction period


- times_of_sentiment_keep_ratio_strong_{i}_day: the times of the sentiment keep divided by the number of posts of the whole time window, but the sentiment keep is only counted when the sentiment is positive or negative in the {i} day, i = 1, 2, ..., train_size, started from the prediction period


- times_of_sentiment_keep_ratio_weak_{i}_day: the times of the sentiment keep divided by the number of posts of the whole time window, but the sentiment keep is counted even when the sentiment is neutral in the {i} day, i = 1, 2, ..., train_size, started from the prediction period


- the_first_sentiment_{i}_day: the first sentiment of the whole time window in the {i} day, i = 1, 2, ..., train_size, started from the prediction period


- the_last_sentiment_{i}_day: the last sentiment of the whole time window in the {i} day, i = 1, 2, ..., train_size, started from the prediction period


- the_first_sentiment_ratio_{i}_day: the first sentiment divided by the number of posts of the whole time window in the {i} day, i = 1, 2, ..., train_size, started from the prediction period


- the_last_sentiment_ratio_{i}_day: the last sentiment divided by the number of posts of the whole time window in the {i} day, i = 1, 2, ..., train_size, started from the prediction period


- the_first_sentiment_ratio_strong_{i}_day: the first sentiment divided by the number of posts of the whole time window, but the first sentiment is only counted when the sentiment is positive or negative in the {i} day, i = 1, 2, ..., train_size, started from the prediction period


- the_last_sentiment_ratio_strong_{i}_day: the last sentiment divided by the number of posts of the whole time window, but the last sentiment is only counted when the sentiment is positive or negative in the {i} day, i = 1, 2, ..., train_size, started from the prediction period

### single_post_in_a_post_tree


#### parent



- parent_sentiment_avg: the average sentiment of the parent of the post



- parent_sentiment_std: the standard deviation of the sentiment of the parent of the post



- parent_num_of_pos: the number of positive posts of the parent of the post



- parent_num_of_neg: the number of negative posts of the parent of the post



- parent_num_of_neu: the number of neutral posts of the parent of the post



- parent_num_of_pos_neg_ratio: the number of positive posts divided by the number of negative posts of the parent of the post



- parent_most_sentiment: the most sentiment of the parent of the post



- parent_times_of_most_sentiment: the times of the most sentiment of the parent of the post



- parent_times_of_sentiment_change: the times of the sentiment change of the parent of the post



- parent_times_of_sentiment_change_ratio: the times of the sentiment change divided by the number of posts of the parent of the post



- parent_times_of_sentiment_change_ratio_strong: the times of the sentiment change divided by the number of posts of the parent of the post, but the sentiment change is only counted when the sentiment is changed from positive to negative or negative to positive



- parent_times_of_sentiment_keep: the times of the sentiment keep of the parent of the post



- parent_times_of_sentiment_keep_ratio: the times of the sentiment keep divided by the number of posts of the parent of the post



- parent_times_of_sentiment_keep_ratio_strong: the times of the sentiment keep divided by the number of posts of the parent of the post, but the sentiment keep is only counted when the sentiment is positive or negative



- parent_times_of_sentiment_keep_ratio_weak: the times of the sentiment keep divided by the number of posts of the parent of the post, but the sentiment keep is counted even when the sentiment is neutral



- parent_the_first_sentiment: the first sentiment of the parent of the post



- parent_the_last_sentiment: the last sentiment of the parent of the post



- parent_the_first_sentiment_ratio: the first sentiment divided by the number of posts of the parent of the post



- parent_the_last_sentiment_ratio: the last sentiment divided by the number of posts of the parent of the post



- parent_the_first_sentiment_ratio_strong: the first sentiment divided by the number of posts of the parent of the post, but the first sentiment is only counted when the sentiment is positive or negative



- parent_the_last_sentiment_ratio_strong: the last sentiment divided by the number of posts of the parent of the post, but the last sentiment is only counted when the sentiment is positive or negative


#### children



- children_sentiment_avg: the average sentiment of the children of the post



- children_sentiment_std: the standard deviation of the sentiment of the children of the post



- children_num_of_pos: the number of positive posts of the children of the post



- children_num_of_neg: the number of negative posts of the children of the post



- children_num_of_neu: the number of neutral posts of the children of the post



- children_num_of_pos_neg_ratio: the number of positive posts divided by the number of negative posts of the children of the post



- children_most_sentiment: the most sentiment of the children of the post



- children_times_of_most_sentiment: the times of the most sentiment of the children of the post



- children_times_of_sentiment_change: the times of the sentiment change of the children of the post



- children_times_of_sentiment_change_ratio: the times of the sentiment change divided by the number of posts of the children of the post



- children_times_of_sentiment_change_ratio_strong: the times of the sentiment change divided by the number of posts of the children of the post, but the sentiment change is only counted when the sentiment is changed from positive to negative or negative to positive



- children_times_of_sentiment_keep: the times of the sentiment keep of the children of the post



- children_times_of_sentiment_keep_ratio: the times of the sentiment keep divided by the number of posts of the children of the post



- children_times_of_sentiment_keep_ratio_strong: the times of the sentiment keep divided by the number of posts of the children of the post, but the sentiment keep is only counted when the sentiment is positive or negative



- children_times_of_sentiment_keep_ratio_weak: the times of the sentiment keep divided by the number of posts of the children of the post, but the sentiment keep is counted even when the sentiment is neutral



- children_the_first_sentiment: the first sentiment of the children of the post



- children_the_last_sentiment: the last sentiment of the children of the post



- children_the_first_sentiment_ratio: the first sentiment divided by the number of posts of the children of the post



- children_the_last_sentiment_ratio: the last sentiment divided by the number of posts of the children of the post



- children_the_first_sentiment_ratio_strong: the first sentiment divided by the number of posts of the children of the post, but the first sentiment is only counted when the sentiment is positive or negative



- children_the_last_sentiment_ratio_strong: the last sentiment divided by the number of posts of the children of the post, but the last sentiment is only counted when the sentiment is positive or negative


#### all_children



- controversiality: the controversiality of the post, it means the ratio of childrens (including the current post) which are controversial to the root of the post tree



- all_children_sentiment_avg: the average sentiment of the all children of the post, including the children of the children



- all_children_sentiment_std: the standard deviation of the sentiment of the all children of the post, including the children of the children



- all_children_num_of_pos: the number of positive posts of the all children of the post, including the children of the children



- all_children_num_of_neg: the number of negative posts of the all children of the post, including the children of the children



- all_children_num_of_neu: the number of neutral posts of the all children of the post, including the children of the children



- all_children_num_of_pos_neg_ratio: the number of positive posts divided by the number of negative posts of the all children of the post, including the children of the children



- all_children_most_sentiment: the most sentiment of the all children of the post, including the children of the children



- all_children_times_of_most_sentiment: the times of the most sentiment of the all children of the post, including the children of the children



- all_children_the_first_sentiment: the first sentiment of the all children of the post, including the children of the children



- all_children_the_last_sentiment: the last sentiment of the all children of the post, including the children of the children



- all_children_the_first_sentiment_ratio: the first sentiment divided by the number of posts of the all children of the post, including the children of the children



- all_children_the_last_sentiment_ratio: the last sentiment divided by the number of posts of the all children of the post, including the children of the children



- all_children_the_first_sentiment_ratio_strong: the first sentiment divided by the number of posts of the all children of the post, including the children of the children, but the first sentiment is only counted when the sentiment is positive or negative



- all_children_the_last_sentiment_ratio_strong: the last sentiment divided by the number of posts of the all children of the post, including the children of the children, but the last sentiment is only counted when the sentiment is positive or negative



- all_children_num_of_pos_tree: the number of positive posts of the all children of the post, including the children of the children, but the positive posts are only counted when the sentiment is positive or negative



- all_children_num_of_neg_tree: the number of negative posts of the all children of the post, including the children of the children, but the negative posts are only counted when the sentiment is positive or negative



- all_children_num_of_neu_tree: the number of neutral posts of the all children of the post, including the children of the children, but the neutral posts are only counted when the sentiment is positive or negative



- all_children_num_of_pos_neg_ratio_tree: the number of positive posts divided by the number of negative posts of the all children of the post, including the children of the children, but the positive posts and negative posts are only counted when the sentiment is positive or negative



- all_children_most_sentiment_tree: the most sentiment of the all children of the post, including the children of the children, but the most sentiment is only counted when the sentiment is positive or negative



- all_children_times_of_most_sentiment_tree: the times of the most sentiment of the all children of the post, including the children of the children, but the most sentiment is only counted when the sentiment is positive or negative



- all_children_the_first_sentiment_tree: the first sentiment of the all children of the post, including the children of the children, but the first sentiment is only counted when the sentiment is positive or negative



- all_children_the_last_sentiment_tree: the last sentiment of the all children of the post, including the children of the children, but the last sentiment is only counted when the sentiment is positive or negative



- all_children_the_first_sentiment_ratio_tree: the first sentiment divided by the number of posts of the all children of the post, including the children of the children, but the first sentiment is only counted when the sentiment is positive or negative



- all_children_the_last_sentiment_ratio_tree: the last sentiment divided by the number of posts of the all children of the post, including the children of the children, but the last sentiment is only counted when the sentiment is positive or negative



- all_children_num_of_controversiality_tree: the number of post trees which are controversiality. it means the controversal sentiment of the root of the post tree is more than 0.5 in the all children of the post, including the children of the children



- all_children_num_of_controversiality_ratio_tree: the number of post trees which are controversiality divided by the number of post trees in the all children of the post, including the children of the children



- all_children_the_most_attractive_tree_sentiment: the most attractive sentiment of the all children of the post, including the children of the children, but the most attractive sentiment is only counted when the sentiment is positive or negative



- all_children_the_most_attractive_tree_controrversiality: the most attractive controversiality of the all children of the post, including the children of the children, but the most attractive controversiality is only counted when the sentiment is positive or negative



- all_children_controversiality_avg_tree: the average controversiality of the all children of the post, including the children of the children, but the controversiality is only counted when the sentiment is positive or negative



- all_children_controversiality_std_tree: the standard deviation of the controversiality of the all children of the post, including the children of the children, but the controversiality is only counted when the sentiment is positive or negative



- all_children_controversiality_max_tree: the max controversiality of the all children of the post, including the children of the children, but the controversiality is only counted when the sentiment is positive or negative



- all_children_controversiality_min_tree: the min controversiality of the all children of the post, including the children of the children, but the controversiality is only counted when the sentiment is positive or negative



- all_children_controversiality_max_min_ratio_tree: the max controversiality divided by the min controversiality of the all children of the post, including the children of the children, but the controversiality is only counted when the sentiment is positive or negative



- all_children_controversiality_max_tree_sentiment: the max controversiality sentiment of the all children of the post, including the children of the children, but the controversiality sentiment is only counted when the sentiment is positive or negative



- all_children_controversiality_min_tree_sentiment: the min controversiality sentiment of the all children of the post, including the children of the children, but the controversiality sentiment is only counted when the sentiment is positive or negative



- all_children_controversiality_max_tree_attraction: the max controversiality attraction of the all children of the post, including the children of the children, but the controversiality attraction is only counted when the sentiment is positive or negative



- all_children_controversiality_min_tree_attraction: the min controversiality attraction of the all children of the post, including the children of the children, but the controversiality attraction is only counted when the sentiment is positive or negative



- all_children_more_than_sentiment_avg_tree: the number of posts which are more than the average sentiment of the all children of the post, including the children of the children, but the sentiment is only counted when the sentiment is positive or negative



- all_children_more_than_sentiment_avg_ratio_tree: the number of posts which are more than the average sentiment divided by the number of posts of the all children of the post, including the children of the children, but the sentiment is only counted when the sentiment is positive or negative



- all_children_more_than_attraction_of_controversiality_max_tree: the number of posts which are more than the controversiality max attraction of the all children of the post, including the children of the children, but the controversiality attraction is only counted when the sentiment is positive or negative



- all_children_more_than_attraction_of_controversiality_max_ratio_tree: the number of posts which are more than the controversiality max attraction divided by the number of posts of the all children of the post, including the children of the children, but the controversiality attraction is only counted when the sentiment is positive or negative



- all_children_more_than_attraction_of_controversiality_min_tree: the number of posts which are more than the controversiality min attraction of the all children of the post, including the children of the children, but the controversiality attraction is only counted when the sentiment is positive or negative



- all_children_more_than_attraction_of_controversiality_min_ratio_tree: the number of posts which are more than the controversiality min attraction divided by the number of posts of the all children of the post, including the children of the children, but the controversiality attraction is only counted when the sentiment is positive or negative
## user_feature_from_post

### comment


- num_of_all_awardings_avg: the number of all awardings of the comment. it will be 0 if the comment has no awardings. it may show the popularity of the comment, but may leaking the information of the future related to the label. avg of the comment


- num_of_all_awardings_avg_parent: the number of all awardings of the comment. it will be 0 if the comment has no awardings. it may show the popularity of the comment, but may leaking the information of the future related to the label. avg of the comment_parent


- num_of_all_awardings_avg_children: the number of all awardings of the comment. it will be 0 if the comment has no awardings. it may show the popularity of the comment, but may leaking the information of the future related to the label. avg of the comment_children


- num_of_all_awardings_avg_all_children: the number of all awardings of the comment. it will be 0 if the comment has no awardings. it may show the popularity of the comment, but may leaking the information of the future related to the label. avg of the comment_all_children


- num_of_all_awardings_std: the number of all awardings of the comment. it will be 0 if the comment has no awardings. it may show the popularity of the comment, but may leaking the information of the future related to the label. std of the comment


- num_of_all_awardings_std_parent: the number of all awardings of the comment. it will be 0 if the comment has no awardings. it may show the popularity of the comment, but may leaking the information of the future related to the label. std of the comment_parent


- num_of_all_awardings_std_children: the number of all awardings of the comment. it will be 0 if the comment has no awardings. it may show the popularity of the comment, but may leaking the information of the future related to the label. std of the comment_children


- num_of_all_awardings_std_all_children: the number of all awardings of the comment. it will be 0 if the comment has no awardings. it may show the popularity of the comment, but may leaking the information of the future related to the label. std of the comment_all_children


- num_of_all_awardings_max: the number of all awardings of the comment. it will be 0 if the comment has no awardings. it may show the popularity of the comment, but may leaking the information of the future related to the label. max of the comment


- num_of_all_awardings_max_parent: the number of all awardings of the comment. it will be 0 if the comment has no awardings. it may show the popularity of the comment, but may leaking the information of the future related to the label. max of the comment_parent


- num_of_all_awardings_max_children: the number of all awardings of the comment. it will be 0 if the comment has no awardings. it may show the popularity of the comment, but may leaking the information of the future related to the label. max of the comment_children


- num_of_all_awardings_max_all_children: the number of all awardings of the comment. it will be 0 if the comment has no awardings. it may show the popularity of the comment, but may leaking the information of the future related to the label. max of the comment_all_children


- num_of_all_awardings_min: the number of all awardings of the comment. it will be 0 if the comment has no awardings. it may show the popularity of the comment, but may leaking the information of the future related to the label. min of the comment


- num_of_all_awardings_min_parent: the number of all awardings of the comment. it will be 0 if the comment has no awardings. it may show the popularity of the comment, but may leaking the information of the future related to the label. min of the comment_parent


- num_of_all_awardings_min_children: the number of all awardings of the comment. it will be 0 if the comment has no awardings. it may show the popularity of the comment, but may leaking the information of the future related to the label. min of the comment_children


- num_of_all_awardings_min_all_children: the number of all awardings of the comment. it will be 0 if the comment has no awardings. it may show the popularity of the comment, but may leaking the information of the future related to the label. min of the comment_all_children


- num_of_all_awardings_first: the number of all awardings of the comment. it will be 0 if the comment has no awardings. it may show the popularity of the comment, but may leaking the information of the future related to the label. first of the comment


- num_of_all_awardings_first_parent: the number of all awardings of the comment. it will be 0 if the comment has no awardings. it may show the popularity of the comment, but may leaking the information of the future related to the label. first of the comment_parent


- num_of_all_awardings_first_children: the number of all awardings of the comment. it will be 0 if the comment has no awardings. it may show the popularity of the comment, but may leaking the information of the future related to the label. first of the comment_children


- num_of_all_awardings_first_all_children: the number of all awardings of the comment. it will be 0 if the comment has no awardings. it may show the popularity of the comment, but may leaking the information of the future related to the label. first of the comment_all_children


- num_of_all_awardings_last: the number of all awardings of the comment. it will be 0 if the comment has no awardings. it may show the popularity of the comment, but may leaking the information of the future related to the label. last of the comment


- num_of_all_awardings_last_parent: the number of all awardings of the comment. it will be 0 if the comment has no awardings. it may show the popularity of the comment, but may leaking the information of the future related to the label. last of the comment_parent


- num_of_all_awardings_last_children: the number of all awardings of the comment. it will be 0 if the comment has no awardings. it may show the popularity of the comment, but may leaking the information of the future related to the label. last of the comment_children


- num_of_all_awardings_last_all_children: the number of all awardings of the comment. it will be 0 if the comment has no awardings. it may show the popularity of the comment, but may leaking the information of the future related to the label. last of the comment_all_children


- achieved_avg: achieved or not of the comment, post will be achieved if it has been 180 days since the post was created avg of the comment


- achieved_avg_parent: achieved or not of the comment, post will be achieved if it has been 180 days since the post was created avg of the comment_parent


- achieved_avg_children: achieved or not of the comment, post will be achieved if it has been 180 days since the post was created avg of the comment_children


- achieved_avg_all_children: achieved or not of the comment, post will be achieved if it has been 180 days since the post was created avg of the comment_all_children


- achieved_std: achieved or not of the comment, post will be achieved if it has been 180 days since the post was created std of the comment


- achieved_std_parent: achieved or not of the comment, post will be achieved if it has been 180 days since the post was created std of the comment_parent


- achieved_std_children: achieved or not of the comment, post will be achieved if it has been 180 days since the post was created std of the comment_children


- achieved_std_all_children: achieved or not of the comment, post will be achieved if it has been 180 days since the post was created std of the comment_all_children


- achieved_max: achieved or not of the comment, post will be achieved if it has been 180 days since the post was created max of the comment


- achieved_max_parent: achieved or not of the comment, post will be achieved if it has been 180 days since the post was created max of the comment_parent


- achieved_max_children: achieved or not of the comment, post will be achieved if it has been 180 days since the post was created max of the comment_children


- achieved_max_all_children: achieved or not of the comment, post will be achieved if it has been 180 days since the post was created max of the comment_all_children


- achieved_min: achieved or not of the comment, post will be achieved if it has been 180 days since the post was created min of the comment


- achieved_min_parent: achieved or not of the comment, post will be achieved if it has been 180 days since the post was created min of the comment_parent


- achieved_min_children: achieved or not of the comment, post will be achieved if it has been 180 days since the post was created min of the comment_children


- achieved_min_all_children: achieved or not of the comment, post will be achieved if it has been 180 days since the post was created min of the comment_all_children


- achieved_first: achieved or not of the comment, post will be achieved if it has been 180 days since the post was created first of the comment


- achieved_first_parent: achieved or not of the comment, post will be achieved if it has been 180 days since the post was created first of the comment_parent


- achieved_first_children: achieved or not of the comment, post will be achieved if it has been 180 days since the post was created first of the comment_children


- achieved_first_all_children: achieved or not of the comment, post will be achieved if it has been 180 days since the post was created first of the comment_all_children


- achieved_last: achieved or not of the comment, post will be achieved if it has been 180 days since the post was created last of the comment


- achieved_last_parent: achieved or not of the comment, post will be achieved if it has been 180 days since the post was created last of the comment_parent


- achieved_last_children: achieved or not of the comment, post will be achieved if it has been 180 days since the post was created last of the comment_children


- achieved_last_all_children: achieved or not of the comment, post will be achieved if it has been 180 days since the post was created last of the comment_all_children


- stickied_avg: if the post is stickied or not, it may be a post that the moderator wants to highlight avg of the comment


- stickied_avg_parent: if the post is stickied or not, it may be a post that the moderator wants to highlight avg of the comment_parent


- stickied_avg_children: if the post is stickied or not, it may be a post that the moderator wants to highlight avg of the comment_children


- stickied_avg_all_children: if the post is stickied or not, it may be a post that the moderator wants to highlight avg of the comment_all_children


- stickied_std: if the post is stickied or not, it may be a post that the moderator wants to highlight std of the comment


- stickied_std_parent: if the post is stickied or not, it may be a post that the moderator wants to highlight std of the comment_parent


- stickied_std_children: if the post is stickied or not, it may be a post that the moderator wants to highlight std of the comment_children


- stickied_std_all_children: if the post is stickied or not, it may be a post that the moderator wants to highlight std of the comment_all_children


- stickied_max: if the post is stickied or not, it may be a post that the moderator wants to highlight max of the comment


- stickied_max_parent: if the post is stickied or not, it may be a post that the moderator wants to highlight max of the comment_parent


- stickied_max_children: if the post is stickied or not, it may be a post that the moderator wants to highlight max of the comment_children


- stickied_max_all_children: if the post is stickied or not, it may be a post that the moderator wants to highlight max of the comment_all_children


- stickied_min: if the post is stickied or not, it may be a post that the moderator wants to highlight min of the comment


- stickied_min_parent: if the post is stickied or not, it may be a post that the moderator wants to highlight min of the comment_parent


- stickied_min_children: if the post is stickied or not, it may be a post that the moderator wants to highlight min of the comment_children


- stickied_min_all_children: if the post is stickied or not, it may be a post that the moderator wants to highlight min of the comment_all_children


- stickied_first: if the post is stickied or not, it may be a post that the moderator wants to highlight first of the comment


- stickied_first_parent: if the post is stickied or not, it may be a post that the moderator wants to highlight first of the comment_parent


- stickied_first_children: if the post is stickied or not, it may be a post that the moderator wants to highlight first of the comment_children


- stickied_first_all_children: if the post is stickied or not, it may be a post that the moderator wants to highlight first of the comment_all_children


- stickied_last: if the post is stickied or not, it may be a post that the moderator wants to highlight last of the comment


- stickied_last_parent: if the post is stickied or not, it may be a post that the moderator wants to highlight last of the comment_parent


- stickied_last_children: if the post is stickied or not, it may be a post that the moderator wants to highlight last of the comment_children


- stickied_last_all_children: if the post is stickied or not, it may be a post that the moderator wants to highlight last of the comment_all_children


- collapsed_avg: collapsed or not for the comment, it is judged by the reddit algorithm which may be related to the label avg of the comment


- collapsed_avg_parent: collapsed or not for the comment, it is judged by the reddit algorithm which may be related to the label avg of the comment_parent


- collapsed_avg_children: collapsed or not for the comment, it is judged by the reddit algorithm which may be related to the label avg of the comment_children


- collapsed_avg_all_children: collapsed or not for the comment, it is judged by the reddit algorithm which may be related to the label avg of the comment_all_children


- collapsed_std: collapsed or not for the comment, it is judged by the reddit algorithm which may be related to the label std of the comment


- collapsed_std_parent: collapsed or not for the comment, it is judged by the reddit algorithm which may be related to the label std of the comment_parent


- collapsed_std_children: collapsed or not for the comment, it is judged by the reddit algorithm which may be related to the label std of the comment_children


- collapsed_std_all_children: collapsed or not for the comment, it is judged by the reddit algorithm which may be related to the label std of the comment_all_children


- collapsed_max: collapsed or not for the comment, it is judged by the reddit algorithm which may be related to the label max of the comment


- collapsed_max_parent: collapsed or not for the comment, it is judged by the reddit algorithm which may be related to the label max of the comment_parent


- collapsed_max_children: collapsed or not for the comment, it is judged by the reddit algorithm which may be related to the label max of the comment_children


- collapsed_max_all_children: collapsed or not for the comment, it is judged by the reddit algorithm which may be related to the label max of the comment_all_children


- collapsed_min: collapsed or not for the comment, it is judged by the reddit algorithm which may be related to the label min of the comment


- collapsed_min_parent: collapsed or not for the comment, it is judged by the reddit algorithm which may be related to the label min of the comment_parent


- collapsed_min_children: collapsed or not for the comment, it is judged by the reddit algorithm which may be related to the label min of the comment_children


- collapsed_min_all_children: collapsed or not for the comment, it is judged by the reddit algorithm which may be related to the label min of the comment_all_children


- collapsed_first: collapsed or not for the comment, it is judged by the reddit algorithm which may be related to the label first of the comment


- collapsed_first_parent: collapsed or not for the comment, it is judged by the reddit algorithm which may be related to the label first of the comment_parent


- collapsed_first_children: collapsed or not for the comment, it is judged by the reddit algorithm which may be related to the label first of the comment_children


- collapsed_first_all_children: collapsed or not for the comment, it is judged by the reddit algorithm which may be related to the label first of the comment_all_children


- collapsed_last: collapsed or not for the comment, it is judged by the reddit algorithm which may be related to the label last of the comment


- collapsed_last_parent: collapsed or not for the comment, it is judged by the reddit algorithm which may be related to the label last of the comment_parent


- collapsed_last_children: collapsed or not for the comment, it is judged by the reddit algorithm which may be related to the label last of the comment_children


- collapsed_last_all_children: collapsed or not for the comment, it is judged by the reddit algorithm which may be related to the label last of the comment_all_children


- controversiality_avg: the controversiality of the comment, it may be a good feature, but may leaking the information of the future related to the label. avg of the comment


- controversiality_avg_parent: the controversiality of the comment, it may be a good feature, but may leaking the information of the future related to the label. avg of the comment_parent


- controversiality_avg_children: the controversiality of the comment, it may be a good feature, but may leaking the information of the future related to the label. avg of the comment_children


- controversiality_avg_all_children: the controversiality of the comment, it may be a good feature, but may leaking the information of the future related to the label. avg of the comment_all_children


- controversiality_std: the controversiality of the comment, it may be a good feature, but may leaking the information of the future related to the label. std of the comment


- controversiality_std_parent: the controversiality of the comment, it may be a good feature, but may leaking the information of the future related to the label. std of the comment_parent


- controversiality_std_children: the controversiality of the comment, it may be a good feature, but may leaking the information of the future related to the label. std of the comment_children


- controversiality_std_all_children: the controversiality of the comment, it may be a good feature, but may leaking the information of the future related to the label. std of the comment_all_children


- controversiality_max: the controversiality of the comment, it may be a good feature, but may leaking the information of the future related to the label. max of the comment


- controversiality_max_parent: the controversiality of the comment, it may be a good feature, but may leaking the information of the future related to the label. max of the comment_parent


- controversiality_max_children: the controversiality of the comment, it may be a good feature, but may leaking the information of the future related to the label. max of the comment_children


- controversiality_max_all_children: the controversiality of the comment, it may be a good feature, but may leaking the information of the future related to the label. max of the comment_all_children


- controversiality_min: the controversiality of the comment, it may be a good feature, but may leaking the information of the future related to the label. min of the comment


- controversiality_min_parent: the controversiality of the comment, it may be a good feature, but may leaking the information of the future related to the label. min of the comment_parent


- controversiality_min_children: the controversiality of the comment, it may be a good feature, but may leaking the information of the future related to the label. min of the comment_children


- controversiality_min_all_children: the controversiality of the comment, it may be a good feature, but may leaking the information of the future related to the label. min of the comment_all_children


- controversiality_first: the controversiality of the comment, it may be a good feature, but may leaking the information of the future related to the label. first of the comment


- controversiality_first_parent: the controversiality of the comment, it may be a good feature, but may leaking the information of the future related to the label. first of the comment_parent


- controversiality_first_children: the controversiality of the comment, it may be a good feature, but may leaking the information of the future related to the label. first of the comment_children


- controversiality_first_all_children: the controversiality of the comment, it may be a good feature, but may leaking the information of the future related to the label. first of the comment_all_children


- controversiality_last: the controversiality of the comment, it may be a good feature, but may leaking the information of the future related to the label. last of the comment


- controversiality_last_parent: the controversiality of the comment, it may be a good feature, but may leaking the information of the future related to the label. last of the comment_parent


- controversiality_last_children: the controversiality of the comment, it may be a good feature, but may leaking the information of the future related to the label. last of the comment_children


- controversiality_last_all_children: the controversiality of the comment, it may be a good feature, but may leaking the information of the future related to the label. last of the comment_all_children


- gilded_avg: the gilded of the comment, it means the author will get a month of Reddit Premium and 100 Coins, it may be a good feature, but may leaking the information of the future related to the label. avg of the comment


- gilded_avg_parent: the gilded of the comment, it means the author will get a month of Reddit Premium and 100 Coins, it may be a good feature, but may leaking the information of the future related to the label. avg of the comment_parent


- gilded_avg_children: the gilded of the comment, it means the author will get a month of Reddit Premium and 100 Coins, it may be a good feature, but may leaking the information of the future related to the label. avg of the comment_children


- gilded_avg_all_children: the gilded of the comment, it means the author will get a month of Reddit Premium and 100 Coins, it may be a good feature, but may leaking the information of the future related to the label. avg of the comment_all_children


- gilded_std: the gilded of the comment, it means the author will get a month of Reddit Premium and 100 Coins, it may be a good feature, but may leaking the information of the future related to the label. std of the comment


- gilded_std_parent: the gilded of the comment, it means the author will get a month of Reddit Premium and 100 Coins, it may be a good feature, but may leaking the information of the future related to the label. std of the comment_parent


- gilded_std_children: the gilded of the comment, it means the author will get a month of Reddit Premium and 100 Coins, it may be a good feature, but may leaking the information of the future related to the label. std of the comment_children


- gilded_std_all_children: the gilded of the comment, it means the author will get a month of Reddit Premium and 100 Coins, it may be a good feature, but may leaking the information of the future related to the label. std of the comment_all_children


- gilded_max: the gilded of the comment, it means the author will get a month of Reddit Premium and 100 Coins, it may be a good feature, but may leaking the information of the future related to the label. max of the comment


- gilded_max_parent: the gilded of the comment, it means the author will get a month of Reddit Premium and 100 Coins, it may be a good feature, but may leaking the information of the future related to the label. max of the comment_parent


- gilded_max_children: the gilded of the comment, it means the author will get a month of Reddit Premium and 100 Coins, it may be a good feature, but may leaking the information of the future related to the label. max of the comment_children


- gilded_max_all_children: the gilded of the comment, it means the author will get a month of Reddit Premium and 100 Coins, it may be a good feature, but may leaking the information of the future related to the label. max of the comment_all_children


- gilded_min: the gilded of the comment, it means the author will get a month of Reddit Premium and 100 Coins, it may be a good feature, but may leaking the information of the future related to the label. min of the comment


- gilded_min_parent: the gilded of the comment, it means the author will get a month of Reddit Premium and 100 Coins, it may be a good feature, but may leaking the information of the future related to the label. min of the comment_parent


- gilded_min_children: the gilded of the comment, it means the author will get a month of Reddit Premium and 100 Coins, it may be a good feature, but may leaking the information of the future related to the label. min of the comment_children


- gilded_min_all_children: the gilded of the comment, it means the author will get a month of Reddit Premium and 100 Coins, it may be a good feature, but may leaking the information of the future related to the label. min of the comment_all_children


- gilded_first: the gilded of the comment, it means the author will get a month of Reddit Premium and 100 Coins, it may be a good feature, but may leaking the information of the future related to the label. first of the comment


- gilded_first_parent: the gilded of the comment, it means the author will get a month of Reddit Premium and 100 Coins, it may be a good feature, but may leaking the information of the future related to the label. first of the comment_parent


- gilded_first_children: the gilded of the comment, it means the author will get a month of Reddit Premium and 100 Coins, it may be a good feature, but may leaking the information of the future related to the label. first of the comment_children


- gilded_first_all_children: the gilded of the comment, it means the author will get a month of Reddit Premium and 100 Coins, it may be a good feature, but may leaking the information of the future related to the label. first of the comment_all_children


- gilded_last: the gilded of the comment, it means the author will get a month of Reddit Premium and 100 Coins, it may be a good feature, but may leaking the information of the future related to the label. last of the comment


- gilded_last_parent: the gilded of the comment, it means the author will get a month of Reddit Premium and 100 Coins, it may be a good feature, but may leaking the information of the future related to the label. last of the comment_parent


- gilded_last_children: the gilded of the comment, it means the author will get a month of Reddit Premium and 100 Coins, it may be a good feature, but may leaking the information of the future related to the label. last of the comment_children


- gilded_last_all_children: the gilded of the comment, it means the author will get a month of Reddit Premium and 100 Coins, it may be a good feature, but may leaking the information of the future related to the label. last of the comment_all_children


- edited_avg: edited or not for the comment. avg of the comment


- edited_avg_parent: edited or not for the comment. avg of the comment_parent


- edited_avg_children: edited or not for the comment. avg of the comment_children


- edited_avg_all_children: edited or not for the comment. avg of the comment_all_children


- edited_std: edited or not for the comment. std of the comment


- edited_std_parent: edited or not for the comment. std of the comment_parent


- edited_std_children: edited or not for the comment. std of the comment_children


- edited_std_all_children: edited or not for the comment. std of the comment_all_children


- edited_max: edited or not for the comment. max of the comment


- edited_max_parent: edited or not for the comment. max of the comment_parent


- edited_max_children: edited or not for the comment. max of the comment_children


- edited_max_all_children: edited or not for the comment. max of the comment_all_children


- edited_min: edited or not for the comment. min of the comment


- edited_min_parent: edited or not for the comment. min of the comment_parent


- edited_min_children: edited or not for the comment. min of the comment_children


- edited_min_all_children: edited or not for the comment. min of the comment_all_children


- edited_first: edited or not for the comment. first of the comment


- edited_first_parent: edited or not for the comment. first of the comment_parent


- edited_first_children: edited or not for the comment. first of the comment_children


- edited_first_all_children: edited or not for the comment. first of the comment_all_children


- edited_last: edited or not for the comment. last of the comment


- edited_last_parent: edited or not for the comment. last of the comment_parent


- edited_last_children: edited or not for the comment. last of the comment_children


- edited_last_all_children: edited or not for the comment. last of the comment_all_children


- num_of_guildings_avg: the number of guildings of the comment, it may be a good feature, but may leaking the information of the future related to the label. avg of the comment


- num_of_guildings_avg_parent: the number of guildings of the comment, it may be a good feature, but may leaking the information of the future related to the label. avg of the comment_parent


- num_of_guildings_avg_children: the number of guildings of the comment, it may be a good feature, but may leaking the information of the future related to the label. avg of the comment_children


- num_of_guildings_avg_all_children: the number of guildings of the comment, it may be a good feature, but may leaking the information of the future related to the label. avg of the comment_all_children


- num_of_guildings_std: the number of guildings of the comment, it may be a good feature, but may leaking the information of the future related to the label. std of the comment


- num_of_guildings_std_parent: the number of guildings of the comment, it may be a good feature, but may leaking the information of the future related to the label. std of the comment_parent


- num_of_guildings_std_children: the number of guildings of the comment, it may be a good feature, but may leaking the information of the future related to the label. std of the comment_children


- num_of_guildings_std_all_children: the number of guildings of the comment, it may be a good feature, but may leaking the information of the future related to the label. std of the comment_all_children


- num_of_guildings_max: the number of guildings of the comment, it may be a good feature, but may leaking the information of the future related to the label. max of the comment


- num_of_guildings_max_parent: the number of guildings of the comment, it may be a good feature, but may leaking the information of the future related to the label. max of the comment_parent


- num_of_guildings_max_children: the number of guildings of the comment, it may be a good feature, but may leaking the information of the future related to the label. max of the comment_children


- num_of_guildings_max_all_children: the number of guildings of the comment, it may be a good feature, but may leaking the information of the future related to the label. max of the comment_all_children


- num_of_guildings_min: the number of guildings of the comment, it may be a good feature, but may leaking the information of the future related to the label. min of the comment


- num_of_guildings_min_parent: the number of guildings of the comment, it may be a good feature, but may leaking the information of the future related to the label. min of the comment_parent


- num_of_guildings_min_children: the number of guildings of the comment, it may be a good feature, but may leaking the information of the future related to the label. min of the comment_children


- num_of_guildings_min_all_children: the number of guildings of the comment, it may be a good feature, but may leaking the information of the future related to the label. min of the comment_all_children


- num_of_guildings_first: the number of guildings of the comment, it may be a good feature, but may leaking the information of the future related to the label. first of the comment


- num_of_guildings_first_parent: the number of guildings of the comment, it may be a good feature, but may leaking the information of the future related to the label. first of the comment_parent


- num_of_guildings_first_children: the number of guildings of the comment, it may be a good feature, but may leaking the information of the future related to the label. first of the comment_children


- num_of_guildings_first_all_children: the number of guildings of the comment, it may be a good feature, but may leaking the information of the future related to the label. first of the comment_all_children


- num_of_guildings_last: the number of guildings of the comment, it may be a good feature, but may leaking the information of the future related to the label. last of the comment


- num_of_guildings_last_parent: the number of guildings of the comment, it may be a good feature, but may leaking the information of the future related to the label. last of the comment_parent


- num_of_guildings_last_children: the number of guildings of the comment, it may be a good feature, but may leaking the information of the future related to the label. last of the comment_children


- num_of_guildings_last_all_children: the number of guildings of the comment, it may be a good feature, but may leaking the information of the future related to the label. last of the comment_all_children


- locked_avg: locked or not for the comment, it means the comment is locked by the moderator and no one can comment on it. avg of the comment


- locked_avg_parent: locked or not for the comment, it means the comment is locked by the moderator and no one can comment on it. avg of the comment_parent


- locked_avg_children: locked or not for the comment, it means the comment is locked by the moderator and no one can comment on it. avg of the comment_children


- locked_avg_all_children: locked or not for the comment, it means the comment is locked by the moderator and no one can comment on it. avg of the comment_all_children


- locked_std: locked or not for the comment, it means the comment is locked by the moderator and no one can comment on it. std of the comment


- locked_std_parent: locked or not for the comment, it means the comment is locked by the moderator and no one can comment on it. std of the comment_parent


- locked_std_children: locked or not for the comment, it means the comment is locked by the moderator and no one can comment on it. std of the comment_children


- locked_std_all_children: locked or not for the comment, it means the comment is locked by the moderator and no one can comment on it. std of the comment_all_children


- locked_max: locked or not for the comment, it means the comment is locked by the moderator and no one can comment on it. max of the comment


- locked_max_parent: locked or not for the comment, it means the comment is locked by the moderator and no one can comment on it. max of the comment_parent


- locked_max_children: locked or not for the comment, it means the comment is locked by the moderator and no one can comment on it. max of the comment_children


- locked_max_all_children: locked or not for the comment, it means the comment is locked by the moderator and no one can comment on it. max of the comment_all_children


- locked_min: locked or not for the comment, it means the comment is locked by the moderator and no one can comment on it. min of the comment


- locked_min_parent: locked or not for the comment, it means the comment is locked by the moderator and no one can comment on it. min of the comment_parent


- locked_min_children: locked or not for the comment, it means the comment is locked by the moderator and no one can comment on it. min of the comment_children


- locked_min_all_children: locked or not for the comment, it means the comment is locked by the moderator and no one can comment on it. min of the comment_all_children


- locked_first: locked or not for the comment, it means the comment is locked by the moderator and no one can comment on it. first of the comment


- locked_first_parent: locked or not for the comment, it means the comment is locked by the moderator and no one can comment on it. first of the comment_parent


- locked_first_children: locked or not for the comment, it means the comment is locked by the moderator and no one can comment on it. first of the comment_children


- locked_first_all_children: locked or not for the comment, it means the comment is locked by the moderator and no one can comment on it. first of the comment_all_children


- locked_last: locked or not for the comment, it means the comment is locked by the moderator and no one can comment on it. last of the comment


- locked_last_parent: locked or not for the comment, it means the comment is locked by the moderator and no one can comment on it. last of the comment_parent


- locked_last_children: locked or not for the comment, it means the comment is locked by the moderator and no one can comment on it. last of the comment_children


- locked_last_all_children: locked or not for the comment, it means the comment is locked by the moderator and no one can comment on it. last of the comment_all_children


- no_follow_avg: no follow or not for the comment, it means tell the search engines to not follow the link. avg of the comment


- no_follow_avg_parent: no follow or not for the comment, it means tell the search engines to not follow the link. avg of the comment_parent


- no_follow_avg_children: no follow or not for the comment, it means tell the search engines to not follow the link. avg of the comment_children


- no_follow_avg_all_children: no follow or not for the comment, it means tell the search engines to not follow the link. avg of the comment_all_children


- no_follow_std: no follow or not for the comment, it means tell the search engines to not follow the link. std of the comment


- no_follow_std_parent: no follow or not for the comment, it means tell the search engines to not follow the link. std of the comment_parent


- no_follow_std_children: no follow or not for the comment, it means tell the search engines to not follow the link. std of the comment_children


- no_follow_std_all_children: no follow or not for the comment, it means tell the search engines to not follow the link. std of the comment_all_children


- no_follow_max: no follow or not for the comment, it means tell the search engines to not follow the link. max of the comment


- no_follow_max_parent: no follow or not for the comment, it means tell the search engines to not follow the link. max of the comment_parent


- no_follow_max_children: no follow or not for the comment, it means tell the search engines to not follow the link. max of the comment_children


- no_follow_max_all_children: no follow or not for the comment, it means tell the search engines to not follow the link. max of the comment_all_children


- no_follow_min: no follow or not for the comment, it means tell the search engines to not follow the link. min of the comment


- no_follow_min_parent: no follow or not for the comment, it means tell the search engines to not follow the link. min of the comment_parent


- no_follow_min_children: no follow or not for the comment, it means tell the search engines to not follow the link. min of the comment_children


- no_follow_min_all_children: no follow or not for the comment, it means tell the search engines to not follow the link. min of the comment_all_children


- no_follow_first: no follow or not for the comment, it means tell the search engines to not follow the link. first of the comment


- no_follow_first_parent: no follow or not for the comment, it means tell the search engines to not follow the link. first of the comment_parent


- no_follow_first_children: no follow or not for the comment, it means tell the search engines to not follow the link. first of the comment_children


- no_follow_first_all_children: no follow or not for the comment, it means tell the search engines to not follow the link. first of the comment_all_children


- no_follow_last: no follow or not for the comment, it means tell the search engines to not follow the link. last of the comment


- no_follow_last_parent: no follow or not for the comment, it means tell the search engines to not follow the link. last of the comment_parent


- no_follow_last_children: no follow or not for the comment, it means tell the search engines to not follow the link. last of the comment_children


- no_follow_last_all_children: no follow or not for the comment, it means tell the search engines to not follow the link. last of the comment_all_children


- body_length_avg: the length of the body of the comment avg of the comment


- body_length_avg_parent: the length of the body of the comment avg of the comment_parent


- body_length_avg_children: the length of the body of the comment avg of the comment_children


- body_length_avg_all_children: the length of the body of the comment avg of the comment_all_children


- body_length_std: the length of the body of the comment std of the comment


- body_length_std_parent: the length of the body of the comment std of the comment_parent


- body_length_std_children: the length of the body of the comment std of the comment_children


- body_length_std_all_children: the length of the body of the comment std of the comment_all_children


- body_length_max: the length of the body of the comment max of the comment


- body_length_max_parent: the length of the body of the comment max of the comment_parent


- body_length_max_children: the length of the body of the comment max of the comment_children


- body_length_max_all_children: the length of the body of the comment max of the comment_all_children


- body_length_min: the length of the body of the comment min of the comment


- body_length_min_parent: the length of the body of the comment min of the comment_parent


- body_length_min_children: the length of the body of the comment min of the comment_children


- body_length_min_all_children: the length of the body of the comment min of the comment_all_children


- body_length_first: the length of the body of the comment first of the comment


- body_length_first_parent: the length of the body of the comment first of the comment_parent


- body_length_first_children: the length of the body of the comment first of the comment_children


- body_length_first_all_children: the length of the body of the comment first of the comment_all_children


- body_length_last: the length of the body of the comment last of the comment


- body_length_last_parent: the length of the body of the comment last of the comment_parent


- body_length_last_children: the length of the body of the comment last of the comment_children


- body_length_last_all_children: the length of the body of the comment last of the comment_all_children


- can_gild_avg: can gild or not for the comment, it means the comment can be gilded or not. avg of the comment


- can_gild_avg_parent: can gild or not for the comment, it means the comment can be gilded or not. avg of the comment_parent


- can_gild_avg_children: can gild or not for the comment, it means the comment can be gilded or not. avg of the comment_children


- can_gild_avg_all_children: can gild or not for the comment, it means the comment can be gilded or not. avg of the comment_all_children


- can_gild_std: can gild or not for the comment, it means the comment can be gilded or not. std of the comment


- can_gild_std_parent: can gild or not for the comment, it means the comment can be gilded or not. std of the comment_parent


- can_gild_std_children: can gild or not for the comment, it means the comment can be gilded or not. std of the comment_children


- can_gild_std_all_children: can gild or not for the comment, it means the comment can be gilded or not. std of the comment_all_children


- can_gild_max: can gild or not for the comment, it means the comment can be gilded or not. max of the comment


- can_gild_max_parent: can gild or not for the comment, it means the comment can be gilded or not. max of the comment_parent


- can_gild_max_children: can gild or not for the comment, it means the comment can be gilded or not. max of the comment_children


- can_gild_max_all_children: can gild or not for the comment, it means the comment can be gilded or not. max of the comment_all_children


- can_gild_min: can gild or not for the comment, it means the comment can be gilded or not. min of the comment


- can_gild_min_parent: can gild or not for the comment, it means the comment can be gilded or not. min of the comment_parent


- can_gild_min_children: can gild or not for the comment, it means the comment can be gilded or not. min of the comment_children


- can_gild_min_all_children: can gild or not for the comment, it means the comment can be gilded or not. min of the comment_all_children


- can_gild_first: can gild or not for the comment, it means the comment can be gilded or not. first of the comment


- can_gild_first_parent: can gild or not for the comment, it means the comment can be gilded or not. first of the comment_parent


- can_gild_first_children: can gild or not for the comment, it means the comment can be gilded or not. first of the comment_children


- can_gild_first_all_children: can gild or not for the comment, it means the comment can be gilded or not. first of the comment_all_children


- can_gild_last: can gild or not for the comment, it means the comment can be gilded or not. last of the comment


- can_gild_last_parent: can gild or not for the comment, it means the comment can be gilded or not. last of the comment_parent


- can_gild_last_children: can gild or not for the comment, it means the comment can be gilded or not. last of the comment_children


- can_gild_last_all_children: can gild or not for the comment, it means the comment can be gilded or not. last of the comment_all_children


- created_utc_avg: the created time of the comment avg of the comment


- created_utc_avg_parent: the created time of the comment avg of the comment_parent


- created_utc_avg_children: the created time of the comment avg of the comment_children


- created_utc_avg_all_children: the created time of the comment avg of the comment_all_children


- created_utc_std: the created time of the comment std of the comment


- created_utc_std_parent: the created time of the comment std of the comment_parent


- created_utc_std_children: the created time of the comment std of the comment_children


- created_utc_std_all_children: the created time of the comment std of the comment_all_children


- created_utc_max: the created time of the comment max of the comment


- created_utc_max_parent: the created time of the comment max of the comment_parent


- created_utc_max_children: the created time of the comment max of the comment_children


- created_utc_max_all_children: the created time of the comment max of the comment_all_children


- created_utc_min: the created time of the comment min of the comment


- created_utc_min_parent: the created time of the comment min of the comment_parent


- created_utc_min_children: the created time of the comment min of the comment_children


- created_utc_min_all_children: the created time of the comment min of the comment_all_children


- created_utc_first: the created time of the comment first of the comment


- created_utc_first_parent: the created time of the comment first of the comment_parent


- created_utc_first_children: the created time of the comment first of the comment_children


- created_utc_first_all_children: the created time of the comment first of the comment_all_children


- created_utc_last: the created time of the comment last of the comment


- created_utc_last_parent: the created time of the comment last of the comment_parent


- created_utc_last_children: the created time of the comment last of the comment_children


- created_utc_last_all_children: the created time of the comment last of the comment_all_children


- num_of_gildings_avg: the number of gildings of the comment, it may be a good feature, but may leaking the information of the future related to the label. avg of the comment


- num_of_gildings_avg_parent: the number of gildings of the comment, it may be a good feature, but may leaking the information of the future related to the label. avg of the comment_parent


- num_of_gildings_avg_children: the number of gildings of the comment, it may be a good feature, but may leaking the information of the future related to the label. avg of the comment_children


- num_of_gildings_avg_all_children: the number of gildings of the comment, it may be a good feature, but may leaking the information of the future related to the label. avg of the comment_all_children


- num_of_gildings_std: the number of gildings of the comment, it may be a good feature, but may leaking the information of the future related to the label. std of the comment


- num_of_gildings_std_parent: the number of gildings of the comment, it may be a good feature, but may leaking the information of the future related to the label. std of the comment_parent


- num_of_gildings_std_children: the number of gildings of the comment, it may be a good feature, but may leaking the information of the future related to the label. std of the comment_children


- num_of_gildings_std_all_children: the number of gildings of the comment, it may be a good feature, but may leaking the information of the future related to the label. std of the comment_all_children


- num_of_gildings_max: the number of gildings of the comment, it may be a good feature, but may leaking the information of the future related to the label. max of the comment


- num_of_gildings_max_parent: the number of gildings of the comment, it may be a good feature, but may leaking the information of the future related to the label. max of the comment_parent


- num_of_gildings_max_children: the number of gildings of the comment, it may be a good feature, but may leaking the information of the future related to the label. max of the comment_children


- num_of_gildings_max_all_children: the number of gildings of the comment, it may be a good feature, but may leaking the information of the future related to the label. max of the comment_all_children


- num_of_gildings_min: the number of gildings of the comment, it may be a good feature, but may leaking the information of the future related to the label. min of the comment


- num_of_gildings_min_parent: the number of gildings of the comment, it may be a good feature, but may leaking the information of the future related to the label. min of the comment_parent


- num_of_gildings_min_children: the number of gildings of the comment, it may be a good feature, but may leaking the information of the future related to the label. min of the comment_children


- num_of_gildings_min_all_children: the number of gildings of the comment, it may be a good feature, but may leaking the information of the future related to the label. min of the comment_all_children


- num_of_gildings_first: the number of gildings of the comment, it may be a good feature, but may leaking the information of the future related to the label. first of the comment


- num_of_gildings_first_parent: the number of gildings of the comment, it may be a good feature, but may leaking the information of the future related to the label. first of the comment_parent


- num_of_gildings_first_children: the number of gildings of the comment, it may be a good feature, but may leaking the information of the future related to the label. first of the comment_children


- num_of_gildings_first_all_children: the number of gildings of the comment, it may be a good feature, but may leaking the information of the future related to the label. first of the comment_all_children


- num_of_gildings_last: the number of gildings of the comment, it may be a good feature, but may leaking the information of the future related to the label. last of the comment


- num_of_gildings_last_parent: the number of gildings of the comment, it may be a good feature, but may leaking the information of the future related to the label. last of the comment_parent


- num_of_gildings_last_children: the number of gildings of the comment, it may be a good feature, but may leaking the information of the future related to the label. last of the comment_children


- num_of_gildings_last_all_children: the number of gildings of the comment, it may be a good feature, but may leaking the information of the future related to the label. last of the comment_all_children


- score_avg: the score of the comment, it may be a good feature, but may leaking the information of the future related to the label. avg of the comment


- score_avg_parent: the score of the comment, it may be a good feature, but may leaking the information of the future related to the label. avg of the comment_parent


- score_avg_children: the score of the comment, it may be a good feature, but may leaking the information of the future related to the label. avg of the comment_children


- score_avg_all_children: the score of the comment, it may be a good feature, but may leaking the information of the future related to the label. avg of the comment_all_children


- score_std: the score of the comment, it may be a good feature, but may leaking the information of the future related to the label. std of the comment


- score_std_parent: the score of the comment, it may be a good feature, but may leaking the information of the future related to the label. std of the comment_parent


- score_std_children: the score of the comment, it may be a good feature, but may leaking the information of the future related to the label. std of the comment_children


- score_std_all_children: the score of the comment, it may be a good feature, but may leaking the information of the future related to the label. std of the comment_all_children


- score_max: the score of the comment, it may be a good feature, but may leaking the information of the future related to the label. max of the comment


- score_max_parent: the score of the comment, it may be a good feature, but may leaking the information of the future related to the label. max of the comment_parent


- score_max_children: the score of the comment, it may be a good feature, but may leaking the information of the future related to the label. max of the comment_children


- score_max_all_children: the score of the comment, it may be a good feature, but may leaking the information of the future related to the label. max of the comment_all_children


- score_min: the score of the comment, it may be a good feature, but may leaking the information of the future related to the label. min of the comment


- score_min_parent: the score of the comment, it may be a good feature, but may leaking the information of the future related to the label. min of the comment_parent


- score_min_children: the score of the comment, it may be a good feature, but may leaking the information of the future related to the label. min of the comment_children


- score_min_all_children: the score of the comment, it may be a good feature, but may leaking the information of the future related to the label. min of the comment_all_children


- score_first: the score of the comment, it may be a good feature, but may leaking the information of the future related to the label. first of the comment


- score_first_parent: the score of the comment, it may be a good feature, but may leaking the information of the future related to the label. first of the comment_parent


- score_first_children: the score of the comment, it may be a good feature, but may leaking the information of the future related to the label. first of the comment_children


- score_first_all_children: the score of the comment, it may be a good feature, but may leaking the information of the future related to the label. first of the comment_all_children


- score_last: the score of the comment, it may be a good feature, but may leaking the information of the future related to the label. last of the comment


- score_last_parent: the score of the comment, it may be a good feature, but may leaking the information of the future related to the label. last of the comment_parent


- score_last_children: the score of the comment, it may be a good feature, but may leaking the information of the future related to the label. last of the comment_children


- score_last_all_children: the score of the comment, it may be a good feature, but may leaking the information of the future related to the label. last of the comment_all_children


- score_hidden_avg: score hidden or not for the comment, it means the score of the comment is hidden or not. avg of the comment


- score_hidden_avg_parent: score hidden or not for the comment, it means the score of the comment is hidden or not. avg of the comment_parent


- score_hidden_avg_children: score hidden or not for the comment, it means the score of the comment is hidden or not. avg of the comment_children


- score_hidden_avg_all_children: score hidden or not for the comment, it means the score of the comment is hidden or not. avg of the comment_all_children


- score_hidden_std: score hidden or not for the comment, it means the score of the comment is hidden or not. std of the comment


- score_hidden_std_parent: score hidden or not for the comment, it means the score of the comment is hidden or not. std of the comment_parent


- score_hidden_std_children: score hidden or not for the comment, it means the score of the comment is hidden or not. std of the comment_children


- score_hidden_std_all_children: score hidden or not for the comment, it means the score of the comment is hidden or not. std of the comment_all_children


- score_hidden_max: score hidden or not for the comment, it means the score of the comment is hidden or not. max of the comment


- score_hidden_max_parent: score hidden or not for the comment, it means the score of the comment is hidden or not. max of the comment_parent


- score_hidden_max_children: score hidden or not for the comment, it means the score of the comment is hidden or not. max of the comment_children


- score_hidden_max_all_children: score hidden or not for the comment, it means the score of the comment is hidden or not. max of the comment_all_children


- score_hidden_min: score hidden or not for the comment, it means the score of the comment is hidden or not. min of the comment


- score_hidden_min_parent: score hidden or not for the comment, it means the score of the comment is hidden or not. min of the comment_parent


- score_hidden_min_children: score hidden or not for the comment, it means the score of the comment is hidden or not. min of the comment_children


- score_hidden_min_all_children: score hidden or not for the comment, it means the score of the comment is hidden or not. min of the comment_all_children


- score_hidden_first: score hidden or not for the comment, it means the score of the comment is hidden or not. first of the comment


- score_hidden_first_parent: score hidden or not for the comment, it means the score of the comment is hidden or not. first of the comment_parent


- score_hidden_first_children: score hidden or not for the comment, it means the score of the comment is hidden or not. first of the comment_children


- score_hidden_first_all_children: score hidden or not for the comment, it means the score of the comment is hidden or not. first of the comment_all_children


- score_hidden_last: score hidden or not for the comment, it means the score of the comment is hidden or not. last of the comment


- score_hidden_last_parent: score hidden or not for the comment, it means the score of the comment is hidden or not. last of the comment_parent


- score_hidden_last_children: score hidden or not for the comment, it means the score of the comment is hidden or not. last of the comment_children


- score_hidden_last_all_children: score hidden or not for the comment, it means the score of the comment is hidden or not. last of the comment_all_children


- send_replies_avg: send replies or not for the comment, it means the author will receive a notification when someone comments on the comment. avg of the comment


- send_replies_avg_parent: send replies or not for the comment, it means the author will receive a notification when someone comments on the comment. avg of the comment_parent


- send_replies_avg_children: send replies or not for the comment, it means the author will receive a notification when someone comments on the comment. avg of the comment_children


- send_replies_avg_all_children: send replies or not for the comment, it means the author will receive a notification when someone comments on the comment. avg of the comment_all_children


- send_replies_std: send replies or not for the comment, it means the author will receive a notification when someone comments on the comment. std of the comment


- send_replies_std_parent: send replies or not for the comment, it means the author will receive a notification when someone comments on the comment. std of the comment_parent


- send_replies_std_children: send replies or not for the comment, it means the author will receive a notification when someone comments on the comment. std of the comment_children


- send_replies_std_all_children: send replies or not for the comment, it means the author will receive a notification when someone comments on the comment. std of the comment_all_children


- send_replies_max: send replies or not for the comment, it means the author will receive a notification when someone comments on the comment. max of the comment


- send_replies_max_parent: send replies or not for the comment, it means the author will receive a notification when someone comments on the comment. max of the comment_parent


- send_replies_max_children: send replies or not for the comment, it means the author will receive a notification when someone comments on the comment. max of the comment_children


- send_replies_max_all_children: send replies or not for the comment, it means the author will receive a notification when someone comments on the comment. max of the comment_all_children


- send_replies_min: send replies or not for the comment, it means the author will receive a notification when someone comments on the comment. min of the comment


- send_replies_min_parent: send replies or not for the comment, it means the author will receive a notification when someone comments on the comment. min of the comment_parent


- send_replies_min_children: send replies or not for the comment, it means the author will receive a notification when someone comments on the comment. min of the comment_children


- send_replies_min_all_children: send replies or not for the comment, it means the author will receive a notification when someone comments on the comment. min of the comment_all_children


- send_replies_first: send replies or not for the comment, it means the author will receive a notification when someone comments on the comment. first of the comment


- send_replies_first_parent: send replies or not for the comment, it means the author will receive a notification when someone comments on the comment. first of the comment_parent


- send_replies_first_children: send replies or not for the comment, it means the author will receive a notification when someone comments on the comment. first of the comment_children


- send_replies_first_all_children: send replies or not for the comment, it means the author will receive a notification when someone comments on the comment. first of the comment_all_children


- send_replies_last: send replies or not for the comment, it means the author will receive a notification when someone comments on the comment. last of the comment


- send_replies_last_parent: send replies or not for the comment, it means the author will receive a notification when someone comments on the comment. last of the comment_parent


- send_replies_last_children: send replies or not for the comment, it means the author will receive a notification when someone comments on the comment. last of the comment_children


- send_replies_last_all_children: send replies or not for the comment, it means the author will receive a notification when someone comments on the comment. last of the comment_all_children


- is_submitter_avg: the author is the submitter of the post or not avg of the comment


- is_submitter_avg_parent: the author is the submitter of the post or not avg of the comment_parent


- is_submitter_avg_children: the author is the submitter of the post or not avg of the comment_children


- is_submitter_avg_all_children: the author is the submitter of the post or not avg of the comment_all_children


- is_submitter_std: the author is the submitter of the post or not std of the comment


- is_submitter_std_parent: the author is the submitter of the post or not std of the comment_parent


- is_submitter_std_children: the author is the submitter of the post or not std of the comment_children


- is_submitter_std_all_children: the author is the submitter of the post or not std of the comment_all_children


- is_submitter_max: the author is the submitter of the post or not max of the comment


- is_submitter_max_parent: the author is the submitter of the post or not max of the comment_parent


- is_submitter_max_children: the author is the submitter of the post or not max of the comment_children


- is_submitter_max_all_children: the author is the submitter of the post or not max of the comment_all_children


- is_submitter_min: the author is the submitter of the post or not min of the comment


- is_submitter_min_parent: the author is the submitter of the post or not min of the comment_parent


- is_submitter_min_children: the author is the submitter of the post or not min of the comment_children


- is_submitter_min_all_children: the author is the submitter of the post or not min of the comment_all_children


- is_submitter_first: the author is the submitter of the post or not first of the comment


- is_submitter_first_parent: the author is the submitter of the post or not first of the comment_parent


- is_submitter_first_children: the author is the submitter of the post or not first of the comment_children


- is_submitter_first_all_children: the author is the submitter of the post or not first of the comment_all_children


- is_submitter_last: the author is the submitter of the post or not last of the comment


- is_submitter_last_parent: the author is the submitter of the post or not last of the comment_parent


- is_submitter_last_children: the author is the submitter of the post or not last of the comment_children


- is_submitter_last_all_children: the author is the submitter of the post or not last of the comment_all_children


- have_unrepliable_reason_avg: have unrepliable reason or not for the comment. avg of the comment


- have_unrepliable_reason_avg_parent: have unrepliable reason or not for the comment. avg of the comment_parent


- have_unrepliable_reason_avg_children: have unrepliable reason or not for the comment. avg of the comment_children


- have_unrepliable_reason_avg_all_children: have unrepliable reason or not for the comment. avg of the comment_all_children


- have_unrepliable_reason_std: have unrepliable reason or not for the comment. std of the comment


- have_unrepliable_reason_std_parent: have unrepliable reason or not for the comment. std of the comment_parent


- have_unrepliable_reason_std_children: have unrepliable reason or not for the comment. std of the comment_children


- have_unrepliable_reason_std_all_children: have unrepliable reason or not for the comment. std of the comment_all_children


- have_unrepliable_reason_max: have unrepliable reason or not for the comment. max of the comment


- have_unrepliable_reason_max_parent: have unrepliable reason or not for the comment. max of the comment_parent


- have_unrepliable_reason_max_children: have unrepliable reason or not for the comment. max of the comment_children


- have_unrepliable_reason_max_all_children: have unrepliable reason or not for the comment. max of the comment_all_children


- have_unrepliable_reason_min: have unrepliable reason or not for the comment. min of the comment


- have_unrepliable_reason_min_parent: have unrepliable reason or not for the comment. min of the comment_parent


- have_unrepliable_reason_min_children: have unrepliable reason or not for the comment. min of the comment_children


- have_unrepliable_reason_min_all_children: have unrepliable reason or not for the comment. min of the comment_all_children


- have_unrepliable_reason_first: have unrepliable reason or not for the comment. first of the comment


- have_unrepliable_reason_first_parent: have unrepliable reason or not for the comment. first of the comment_parent


- have_unrepliable_reason_first_children: have unrepliable reason or not for the comment. first of the comment_children


- have_unrepliable_reason_first_all_children: have unrepliable reason or not for the comment. first of the comment_all_children


- have_unrepliable_reason_last: have unrepliable reason or not for the comment. last of the comment


- have_unrepliable_reason_last_parent: have unrepliable reason or not for the comment. last of the comment_parent


- have_unrepliable_reason_last_children: have unrepliable reason or not for the comment. last of the comment_children


- have_unrepliable_reason_last_all_children: have unrepliable reason or not for the comment. last of the comment_all_children


- post_level_avg: the level of the whole post tree, it means the post is the i level leaves of the whole post tree. i.e. 0 means the post is the root of the whole post tree. avg of the comment


- post_level_avg_parent: the level of the whole post tree, it means the post is the i level leaves of the whole post tree. i.e. 0 means the post is the root of the whole post tree. avg of the comment_parent


- post_level_avg_children: the level of the whole post tree, it means the post is the i level leaves of the whole post tree. i.e. 0 means the post is the root of the whole post tree. avg of the comment_children


- post_level_avg_all_children: the level of the whole post tree, it means the post is the i level leaves of the whole post tree. i.e. 0 means the post is the root of the whole post tree. avg of the comment_all_children


- post_level_std: the level of the whole post tree, it means the post is the i level leaves of the whole post tree. i.e. 0 means the post is the root of the whole post tree. std of the comment


- post_level_std_parent: the level of the whole post tree, it means the post is the i level leaves of the whole post tree. i.e. 0 means the post is the root of the whole post tree. std of the comment_parent


- post_level_std_children: the level of the whole post tree, it means the post is the i level leaves of the whole post tree. i.e. 0 means the post is the root of the whole post tree. std of the comment_children


- post_level_std_all_children: the level of the whole post tree, it means the post is the i level leaves of the whole post tree. i.e. 0 means the post is the root of the whole post tree. std of the comment_all_children


- post_level_max: the level of the whole post tree, it means the post is the i level leaves of the whole post tree. i.e. 0 means the post is the root of the whole post tree. max of the comment


- post_level_max_parent: the level of the whole post tree, it means the post is the i level leaves of the whole post tree. i.e. 0 means the post is the root of the whole post tree. max of the comment_parent


- post_level_max_children: the level of the whole post tree, it means the post is the i level leaves of the whole post tree. i.e. 0 means the post is the root of the whole post tree. max of the comment_children


- post_level_max_all_children: the level of the whole post tree, it means the post is the i level leaves of the whole post tree. i.e. 0 means the post is the root of the whole post tree. max of the comment_all_children


- post_level_min: the level of the whole post tree, it means the post is the i level leaves of the whole post tree. i.e. 0 means the post is the root of the whole post tree. min of the comment


- post_level_min_parent: the level of the whole post tree, it means the post is the i level leaves of the whole post tree. i.e. 0 means the post is the root of the whole post tree. min of the comment_parent


- post_level_min_children: the level of the whole post tree, it means the post is the i level leaves of the whole post tree. i.e. 0 means the post is the root of the whole post tree. min of the comment_children


- post_level_min_all_children: the level of the whole post tree, it means the post is the i level leaves of the whole post tree. i.e. 0 means the post is the root of the whole post tree. min of the comment_all_children


- post_level_first: the level of the whole post tree, it means the post is the i level leaves of the whole post tree. i.e. 0 means the post is the root of the whole post tree. first of the comment


- post_level_first_parent: the level of the whole post tree, it means the post is the i level leaves of the whole post tree. i.e. 0 means the post is the root of the whole post tree. first of the comment_parent


- post_level_first_children: the level of the whole post tree, it means the post is the i level leaves of the whole post tree. i.e. 0 means the post is the root of the whole post tree. first of the comment_children


- post_level_first_all_children: the level of the whole post tree, it means the post is the i level leaves of the whole post tree. i.e. 0 means the post is the root of the whole post tree. first of the comment_all_children


- post_level_last: the level of the whole post tree, it means the post is the i level leaves of the whole post tree. i.e. 0 means the post is the root of the whole post tree. last of the comment


- post_level_last_parent: the level of the whole post tree, it means the post is the i level leaves of the whole post tree. i.e. 0 means the post is the root of the whole post tree. last of the comment_parent


- post_level_last_children: the level of the whole post tree, it means the post is the i level leaves of the whole post tree. i.e. 0 means the post is the root of the whole post tree. last of the comment_children


- post_level_last_all_children: the level of the whole post tree, it means the post is the i level leaves of the whole post tree. i.e. 0 means the post is the root of the whole post tree. last of the comment_all_children


- comment_type_avg: the type of the comment, mostly it is None avg of the comment


- comment_type_avg_parent: the type of the comment, mostly it is None avg of the comment_parent


- comment_type_avg_children: the type of the comment, mostly it is None avg of the comment_children


- comment_type_avg_all_children: the type of the comment, mostly it is None avg of the comment_all_children


- comment_type_std: the type of the comment, mostly it is None std of the comment


- comment_type_std_parent: the type of the comment, mostly it is None std of the comment_parent


- comment_type_std_children: the type of the comment, mostly it is None std of the comment_children


- comment_type_std_all_children: the type of the comment, mostly it is None std of the comment_all_children


- comment_type_max: the type of the comment, mostly it is None max of the comment


- comment_type_max_parent: the type of the comment, mostly it is None max of the comment_parent


- comment_type_max_children: the type of the comment, mostly it is None max of the comment_children


- comment_type_max_all_children: the type of the comment, mostly it is None max of the comment_all_children


- comment_type_min: the type of the comment, mostly it is None min of the comment


- comment_type_min_parent: the type of the comment, mostly it is None min of the comment_parent


- comment_type_min_children: the type of the comment, mostly it is None min of the comment_children


- comment_type_min_all_children: the type of the comment, mostly it is None min of the comment_all_children


- comment_type_first: the type of the comment, mostly it is None first of the comment


- comment_type_first_parent: the type of the comment, mostly it is None first of the comment_parent


- comment_type_first_children: the type of the comment, mostly it is None first of the comment_children


- comment_type_first_all_children: the type of the comment, mostly it is None first of the comment_all_children


- comment_type_last: the type of the comment, mostly it is None last of the comment


- comment_type_last_parent: the type of the comment, mostly it is None last of the comment_parent


- comment_type_last_children: the type of the comment, mostly it is None last of the comment_children


- comment_type_last_all_children: the type of the comment, mostly it is None last of the comment_all_children


- num_of_comments_avg: the number of comments of the comment in the observation period avg of the comment


- num_of_comments_avg_parent: the number of comments of the comment in the observation period avg of the comment_parent


- num_of_comments_avg_children: the number of comments of the comment in the observation period avg of the comment_children


- num_of_comments_avg_all_children: the number of comments of the comment in the observation period avg of the comment_all_children


- num_of_comments_std: the number of comments of the comment in the observation period std of the comment


- num_of_comments_std_parent: the number of comments of the comment in the observation period std of the comment_parent


- num_of_comments_std_children: the number of comments of the comment in the observation period std of the comment_children


- num_of_comments_std_all_children: the number of comments of the comment in the observation period std of the comment_all_children


- num_of_comments_max: the number of comments of the comment in the observation period max of the comment


- num_of_comments_max_parent: the number of comments of the comment in the observation period max of the comment_parent


- num_of_comments_max_children: the number of comments of the comment in the observation period max of the comment_children


- num_of_comments_max_all_children: the number of comments of the comment in the observation period max of the comment_all_children


- num_of_comments_min: the number of comments of the comment in the observation period min of the comment


- num_of_comments_min_parent: the number of comments of the comment in the observation period min of the comment_parent


- num_of_comments_min_children: the number of comments of the comment in the observation period min of the comment_children


- num_of_comments_min_all_children: the number of comments of the comment in the observation period min of the comment_all_children


- num_of_comments_first: the number of comments of the comment in the observation period first of the comment


- num_of_comments_first_parent: the number of comments of the comment in the observation period first of the comment_parent


- num_of_comments_first_children: the number of comments of the comment in the observation period first of the comment_children


- num_of_comments_first_all_children: the number of comments of the comment in the observation period first of the comment_all_children


- num_of_comments_last: the number of comments of the comment in the observation period last of the comment


- num_of_comments_last_parent: the number of comments of the comment in the observation period last of the comment_parent


- num_of_comments_last_children: the number of comments of the comment in the observation period last of the comment_children


- num_of_comments_last_all_children: the number of comments of the comment in the observation period last of the comment_all_children


- subreddit_subscribers_avg: the number of subscribers of the subreddit of the comment avg of the comment


- subreddit_subscribers_avg_parent: the number of subscribers of the subreddit of the comment avg of the comment_parent


- subreddit_subscribers_avg_children: the number of subscribers of the subreddit of the comment avg of the comment_children


- subreddit_subscribers_avg_all_children: the number of subscribers of the subreddit of the comment avg of the comment_all_children


- subreddit_subscribers_std: the number of subscribers of the subreddit of the comment std of the comment


- subreddit_subscribers_std_parent: the number of subscribers of the subreddit of the comment std of the comment_parent


- subreddit_subscribers_std_children: the number of subscribers of the subreddit of the comment std of the comment_children


- subreddit_subscribers_std_all_children: the number of subscribers of the subreddit of the comment std of the comment_all_children


- subreddit_subscribers_max: the number of subscribers of the subreddit of the comment max of the comment


- subreddit_subscribers_max_parent: the number of subscribers of the subreddit of the comment max of the comment_parent


- subreddit_subscribers_max_children: the number of subscribers of the subreddit of the comment max of the comment_children


- subreddit_subscribers_max_all_children: the number of subscribers of the subreddit of the comment max of the comment_all_children


- subreddit_subscribers_min: the number of subscribers of the subreddit of the comment min of the comment


- subreddit_subscribers_min_parent: the number of subscribers of the subreddit of the comment min of the comment_parent


- subreddit_subscribers_min_children: the number of subscribers of the subreddit of the comment min of the comment_children


- subreddit_subscribers_min_all_children: the number of subscribers of the subreddit of the comment min of the comment_all_children


- subreddit_subscribers_first: the number of subscribers of the subreddit of the comment first of the comment


- subreddit_subscribers_first_parent: the number of subscribers of the subreddit of the comment first of the comment_parent


- subreddit_subscribers_first_children: the number of subscribers of the subreddit of the comment first of the comment_children


- subreddit_subscribers_first_all_children: the number of subscribers of the subreddit of the comment first of the comment_all_children


- subreddit_subscribers_last: the number of subscribers of the subreddit of the comment last of the comment


- subreddit_subscribers_last_parent: the number of subscribers of the subreddit of the comment last of the comment_parent


- subreddit_subscribers_last_children: the number of subscribers of the subreddit of the comment last of the comment_children


- subreddit_subscribers_last_all_children: the number of subscribers of the subreddit of the comment last of the comment_all_children


- subreddit_type_avg: the type of the subreddit of the comment, mostly it is None avg of the comment


- subreddit_type_avg_parent: the type of the subreddit of the comment, mostly it is None avg of the comment_parent


- subreddit_type_avg_children: the type of the subreddit of the comment, mostly it is None avg of the comment_children


- subreddit_type_avg_all_children: the type of the subreddit of the comment, mostly it is None avg of the comment_all_children


- subreddit_type_std: the type of the subreddit of the comment, mostly it is None std of the comment


- subreddit_type_std_parent: the type of the subreddit of the comment, mostly it is None std of the comment_parent


- subreddit_type_std_children: the type of the subreddit of the comment, mostly it is None std of the comment_children


- subreddit_type_std_all_children: the type of the subreddit of the comment, mostly it is None std of the comment_all_children


- subreddit_type_max: the type of the subreddit of the comment, mostly it is None max of the comment


- subreddit_type_max_parent: the type of the subreddit of the comment, mostly it is None max of the comment_parent


- subreddit_type_max_children: the type of the subreddit of the comment, mostly it is None max of the comment_children


- subreddit_type_max_all_children: the type of the subreddit of the comment, mostly it is None max of the comment_all_children


- subreddit_type_min: the type of the subreddit of the comment, mostly it is None min of the comment


- subreddit_type_min_parent: the type of the subreddit of the comment, mostly it is None min of the comment_parent


- subreddit_type_min_children: the type of the subreddit of the comment, mostly it is None min of the comment_children


- subreddit_type_min_all_children: the type of the subreddit of the comment, mostly it is None min of the comment_all_children


- subreddit_type_first: the type of the subreddit of the comment, mostly it is None first of the comment


- subreddit_type_first_parent: the type of the subreddit of the comment, mostly it is None first of the comment_parent


- subreddit_type_first_children: the type of the subreddit of the comment, mostly it is None first of the comment_children


- subreddit_type_first_all_children: the type of the subreddit of the comment, mostly it is None first of the comment_all_children


- subreddit_type_last: the type of the subreddit of the comment, mostly it is None last of the comment


- subreddit_type_last_parent: the type of the subreddit of the comment, mostly it is None last of the comment_parent


- subreddit_type_last_children: the type of the subreddit of the comment, mostly it is None last of the comment_children


- subreddit_type_last_all_children: the type of the subreddit of the comment, mostly it is None last of the comment_all_children


- subreddit_id_avg: the id of the subreddit of the comment avg of the comment


- subreddit_id_avg_parent: the id of the subreddit of the comment avg of the comment_parent


- subreddit_id_avg_children: the id of the subreddit of the comment avg of the comment_children


- subreddit_id_avg_all_children: the id of the subreddit of the comment avg of the comment_all_children


- subreddit_id_std: the id of the subreddit of the comment std of the comment


- subreddit_id_std_parent: the id of the subreddit of the comment std of the comment_parent


- subreddit_id_std_children: the id of the subreddit of the comment std of the comment_children


- subreddit_id_std_all_children: the id of the subreddit of the comment std of the comment_all_children


- subreddit_id_max: the id of the subreddit of the comment max of the comment


- subreddit_id_max_parent: the id of the subreddit of the comment max of the comment_parent


- subreddit_id_max_children: the id of the subreddit of the comment max of the comment_children


- subreddit_id_max_all_children: the id of the subreddit of the comment max of the comment_all_children


- subreddit_id_min: the id of the subreddit of the comment min of the comment


- subreddit_id_min_parent: the id of the subreddit of the comment min of the comment_parent


- subreddit_id_min_children: the id of the subreddit of the comment min of the comment_children


- subreddit_id_min_all_children: the id of the subreddit of the comment min of the comment_all_children


- subreddit_id_first: the id of the subreddit of the comment first of the comment


- subreddit_id_first_parent: the id of the subreddit of the comment first of the comment_parent


- subreddit_id_first_children: the id of the subreddit of the comment first of the comment_children


- subreddit_id_first_all_children: the id of the subreddit of the comment first of the comment_all_children


- subreddit_id_last: the id of the subreddit of the comment last of the comment


- subreddit_id_last_parent: the id of the subreddit of the comment last of the comment_parent


- subreddit_id_last_children: the id of the subreddit of the comment last of the comment_children


- subreddit_id_last_all_children: the id of the subreddit of the comment last of the comment_all_children


- author_created_utc_avg: the created time of the author avg of the comment


- author_created_utc_avg_parent: the created time of the author avg of the comment_parent


- author_created_utc_avg_children: the created time of the author avg of the comment_children


- author_created_utc_avg_all_children: the created time of the author avg of the comment_all_children


- author_created_utc_std: the created time of the author std of the comment


- author_created_utc_std_parent: the created time of the author std of the comment_parent


- author_created_utc_std_children: the created time of the author std of the comment_children


- author_created_utc_std_all_children: the created time of the author std of the comment_all_children


- author_created_utc_max: the created time of the author max of the comment


- author_created_utc_max_parent: the created time of the author max of the comment_parent


- author_created_utc_max_children: the created time of the author max of the comment_children


- author_created_utc_max_all_children: the created time of the author max of the comment_all_children


- author_created_utc_min: the created time of the author min of the comment


- author_created_utc_min_parent: the created time of the author min of the comment_parent


- author_created_utc_min_children: the created time of the author min of the comment_children


- author_created_utc_min_all_children: the created time of the author min of the comment_all_children


- author_created_utc_first: the created time of the author first of the comment


- author_created_utc_first_parent: the created time of the author first of the comment_parent


- author_created_utc_first_children: the created time of the author first of the comment_children


- author_created_utc_first_all_children: the created time of the author first of the comment_all_children


- author_created_utc_last: the created time of the author last of the comment


- author_created_utc_last_parent: the created time of the author last of the comment_parent


- author_created_utc_last_children: the created time of the author last of the comment_children


- author_created_utc_last_all_children: the created time of the author last of the comment_all_children


- author_premium_avg: the author is premium or not avg of the comment


- author_premium_avg_parent: the author is premium or not avg of the comment_parent


- author_premium_avg_children: the author is premium or not avg of the comment_children


- author_premium_avg_all_children: the author is premium or not avg of the comment_all_children


- author_premium_std: the author is premium or not std of the comment


- author_premium_std_parent: the author is premium or not std of the comment_parent


- author_premium_std_children: the author is premium or not std of the comment_children


- author_premium_std_all_children: the author is premium or not std of the comment_all_children


- author_premium_max: the author is premium or not max of the comment


- author_premium_max_parent: the author is premium or not max of the comment_parent


- author_premium_max_children: the author is premium or not max of the comment_children


- author_premium_max_all_children: the author is premium or not max of the comment_all_children


- author_premium_min: the author is premium or not min of the comment


- author_premium_min_parent: the author is premium or not min of the comment_parent


- author_premium_min_children: the author is premium or not min of the comment_children


- author_premium_min_all_children: the author is premium or not min of the comment_all_children


- author_premium_first: the author is premium or not first of the comment


- author_premium_first_parent: the author is premium or not first of the comment_parent


- author_premium_first_children: the author is premium or not first of the comment_children


- author_premium_first_all_children: the author is premium or not first of the comment_all_children


- author_premium_last: the author is premium or not last of the comment


- author_premium_last_parent: the author is premium or not last of the comment_parent


- author_premium_last_children: the author is premium or not last of the comment_children


- author_premium_last_all_children: the author is premium or not last of the comment_all_children

### submission


- num_of_all_awardings_avg: the number of all awardings of the submission. it will be 0 if the submission has no awardings. it may show the popularity of the submission, but may leaking the information of the future related to the label. avg of the submission


- num_of_all_awardings_avg_children: the number of all awardings of the submission. it will be 0 if the submission has no awardings. it may show the popularity of the submission, but may leaking the information of the future related to the label. avg of the submission_children


- num_of_all_awardings_avg_all_children: the number of all awardings of the submission. it will be 0 if the submission has no awardings. it may show the popularity of the submission, but may leaking the information of the future related to the label. avg of the submission_all_children


- num_of_all_awardings_std: the number of all awardings of the submission. it will be 0 if the submission has no awardings. it may show the popularity of the submission, but may leaking the information of the future related to the label. std of the submission


- num_of_all_awardings_std_children: the number of all awardings of the submission. it will be 0 if the submission has no awardings. it may show the popularity of the submission, but may leaking the information of the future related to the label. std of the submission_children


- num_of_all_awardings_std_all_children: the number of all awardings of the submission. it will be 0 if the submission has no awardings. it may show the popularity of the submission, but may leaking the information of the future related to the label. std of the submission_all_children


- num_of_all_awardings_max: the number of all awardings of the submission. it will be 0 if the submission has no awardings. it may show the popularity of the submission, but may leaking the information of the future related to the label. max of the submission


- num_of_all_awardings_max_children: the number of all awardings of the submission. it will be 0 if the submission has no awardings. it may show the popularity of the submission, but may leaking the information of the future related to the label. max of the submission_children


- num_of_all_awardings_max_all_children: the number of all awardings of the submission. it will be 0 if the submission has no awardings. it may show the popularity of the submission, but may leaking the information of the future related to the label. max of the submission_all_children


- num_of_all_awardings_min: the number of all awardings of the submission. it will be 0 if the submission has no awardings. it may show the popularity of the submission, but may leaking the information of the future related to the label. min of the submission


- num_of_all_awardings_min_children: the number of all awardings of the submission. it will be 0 if the submission has no awardings. it may show the popularity of the submission, but may leaking the information of the future related to the label. min of the submission_children


- num_of_all_awardings_min_all_children: the number of all awardings of the submission. it will be 0 if the submission has no awardings. it may show the popularity of the submission, but may leaking the information of the future related to the label. min of the submission_all_children


- num_of_all_awardings_first: the number of all awardings of the submission. it will be 0 if the submission has no awardings. it may show the popularity of the submission, but may leaking the information of the future related to the label. first of the submission


- num_of_all_awardings_first_children: the number of all awardings of the submission. it will be 0 if the submission has no awardings. it may show the popularity of the submission, but may leaking the information of the future related to the label. first of the submission_children


- num_of_all_awardings_first_all_children: the number of all awardings of the submission. it will be 0 if the submission has no awardings. it may show the popularity of the submission, but may leaking the information of the future related to the label. first of the submission_all_children


- num_of_all_awardings_last: the number of all awardings of the submission. it will be 0 if the submission has no awardings. it may show the popularity of the submission, but may leaking the information of the future related to the label. last of the submission


- num_of_all_awardings_last_children: the number of all awardings of the submission. it will be 0 if the submission has no awardings. it may show the popularity of the submission, but may leaking the information of the future related to the label. last of the submission_children


- num_of_all_awardings_last_all_children: the number of all awardings of the submission. it will be 0 if the submission has no awardings. it may show the popularity of the submission, but may leaking the information of the future related to the label. last of the submission_all_children


- allow_live_comments_avg: allow live comments or not for the submission, it means the submission can be commented on while it is live. avg of the submission


- allow_live_comments_avg_children: allow live comments or not for the submission, it means the submission can be commented on while it is live. avg of the submission_children


- allow_live_comments_avg_all_children: allow live comments or not for the submission, it means the submission can be commented on while it is live. avg of the submission_all_children


- allow_live_comments_std: allow live comments or not for the submission, it means the submission can be commented on while it is live. std of the submission


- allow_live_comments_std_children: allow live comments or not for the submission, it means the submission can be commented on while it is live. std of the submission_children


- allow_live_comments_std_all_children: allow live comments or not for the submission, it means the submission can be commented on while it is live. std of the submission_all_children


- allow_live_comments_max: allow live comments or not for the submission, it means the submission can be commented on while it is live. max of the submission


- allow_live_comments_max_children: allow live comments or not for the submission, it means the submission can be commented on while it is live. max of the submission_children


- allow_live_comments_max_all_children: allow live comments or not for the submission, it means the submission can be commented on while it is live. max of the submission_all_children


- allow_live_comments_min: allow live comments or not for the submission, it means the submission can be commented on while it is live. min of the submission


- allow_live_comments_min_children: allow live comments or not for the submission, it means the submission can be commented on while it is live. min of the submission_children


- allow_live_comments_min_all_children: allow live comments or not for the submission, it means the submission can be commented on while it is live. min of the submission_all_children


- allow_live_comments_first: allow live comments or not for the submission, it means the submission can be commented on while it is live. first of the submission


- allow_live_comments_first_children: allow live comments or not for the submission, it means the submission can be commented on while it is live. first of the submission_children


- allow_live_comments_first_all_children: allow live comments or not for the submission, it means the submission can be commented on while it is live. first of the submission_all_children


- allow_live_comments_last: allow live comments or not for the submission, it means the submission can be commented on while it is live. last of the submission


- allow_live_comments_last_children: allow live comments or not for the submission, it means the submission can be commented on while it is live. last of the submission_children


- allow_live_comments_last_all_children: allow live comments or not for the submission, it means the submission can be commented on while it is live. last of the submission_all_children


- archived_avg: archived or not for the submission, it will be archived if it has been 180 days since the submission was created. avg of the submission


- archived_avg_children: archived or not for the submission, it will be archived if it has been 180 days since the submission was created. avg of the submission_children


- archived_avg_all_children: archived or not for the submission, it will be archived if it has been 180 days since the submission was created. avg of the submission_all_children


- archived_std: archived or not for the submission, it will be archived if it has been 180 days since the submission was created. std of the submission


- archived_std_children: archived or not for the submission, it will be archived if it has been 180 days since the submission was created. std of the submission_children


- archived_std_all_children: archived or not for the submission, it will be archived if it has been 180 days since the submission was created. std of the submission_all_children


- archived_max: archived or not for the submission, it will be archived if it has been 180 days since the submission was created. max of the submission


- archived_max_children: archived or not for the submission, it will be archived if it has been 180 days since the submission was created. max of the submission_children


- archived_max_all_children: archived or not for the submission, it will be archived if it has been 180 days since the submission was created. max of the submission_all_children


- archived_min: archived or not for the submission, it will be archived if it has been 180 days since the submission was created. min of the submission


- archived_min_children: archived or not for the submission, it will be archived if it has been 180 days since the submission was created. min of the submission_children


- archived_min_all_children: archived or not for the submission, it will be archived if it has been 180 days since the submission was created. min of the submission_all_children


- archived_first: archived or not for the submission, it will be archived if it has been 180 days since the submission was created. first of the submission


- archived_first_children: archived or not for the submission, it will be archived if it has been 180 days since the submission was created. first of the submission_children


- archived_first_all_children: archived or not for the submission, it will be archived if it has been 180 days since the submission was created. first of the submission_all_children


- archived_last: archived or not for the submission, it will be archived if it has been 180 days since the submission was created. last of the submission


- archived_last_children: archived or not for the submission, it will be archived if it has been 180 days since the submission was created. last of the submission_children


- archived_last_all_children: archived or not for the submission, it will be archived if it has been 180 days since the submission was created. last of the submission_all_children


- num_of_awarders_avg: the nums of awarders of the submission. it will be 0 if the submission has no awarders. it may show the popularity of the submission, but may leaking the information of the future related to the label. avg of the submission


- num_of_awarders_avg_children: the nums of awarders of the submission. it will be 0 if the submission has no awarders. it may show the popularity of the submission, but may leaking the information of the future related to the label. avg of the submission_children


- num_of_awarders_avg_all_children: the nums of awarders of the submission. it will be 0 if the submission has no awarders. it may show the popularity of the submission, but may leaking the information of the future related to the label. avg of the submission_all_children


- num_of_awarders_std: the nums of awarders of the submission. it will be 0 if the submission has no awarders. it may show the popularity of the submission, but may leaking the information of the future related to the label. std of the submission


- num_of_awarders_std_children: the nums of awarders of the submission. it will be 0 if the submission has no awarders. it may show the popularity of the submission, but may leaking the information of the future related to the label. std of the submission_children


- num_of_awarders_std_all_children: the nums of awarders of the submission. it will be 0 if the submission has no awarders. it may show the popularity of the submission, but may leaking the information of the future related to the label. std of the submission_all_children


- num_of_awarders_max: the nums of awarders of the submission. it will be 0 if the submission has no awarders. it may show the popularity of the submission, but may leaking the information of the future related to the label. max of the submission


- num_of_awarders_max_children: the nums of awarders of the submission. it will be 0 if the submission has no awarders. it may show the popularity of the submission, but may leaking the information of the future related to the label. max of the submission_children


- num_of_awarders_max_all_children: the nums of awarders of the submission. it will be 0 if the submission has no awarders. it may show the popularity of the submission, but may leaking the information of the future related to the label. max of the submission_all_children


- num_of_awarders_min: the nums of awarders of the submission. it will be 0 if the submission has no awarders. it may show the popularity of the submission, but may leaking the information of the future related to the label. min of the submission


- num_of_awarders_min_children: the nums of awarders of the submission. it will be 0 if the submission has no awarders. it may show the popularity of the submission, but may leaking the information of the future related to the label. min of the submission_children


- num_of_awarders_min_all_children: the nums of awarders of the submission. it will be 0 if the submission has no awarders. it may show the popularity of the submission, but may leaking the information of the future related to the label. min of the submission_all_children


- num_of_awarders_first: the nums of awarders of the submission. it will be 0 if the submission has no awarders. it may show the popularity of the submission, but may leaking the information of the future related to the label. first of the submission


- num_of_awarders_first_children: the nums of awarders of the submission. it will be 0 if the submission has no awarders. it may show the popularity of the submission, but may leaking the information of the future related to the label. first of the submission_children


- num_of_awarders_first_all_children: the nums of awarders of the submission. it will be 0 if the submission has no awarders. it may show the popularity of the submission, but may leaking the information of the future related to the label. first of the submission_all_children


- num_of_awarders_last: the nums of awarders of the submission. it will be 0 if the submission has no awarders. it may show the popularity of the submission, but may leaking the information of the future related to the label. last of the submission


- num_of_awarders_last_children: the nums of awarders of the submission. it will be 0 if the submission has no awarders. it may show the popularity of the submission, but may leaking the information of the future related to the label. last of the submission_children


- num_of_awarders_last_all_children: the nums of awarders of the submission. it will be 0 if the submission has no awarders. it may show the popularity of the submission, but may leaking the information of the future related to the label. last of the submission_all_children


- banned_by_someone_avg: banned by someone or not for the submission avg of the submission


- banned_by_someone_avg_children: banned by someone or not for the submission avg of the submission_children


- banned_by_someone_avg_all_children: banned by someone or not for the submission avg of the submission_all_children


- banned_by_someone_std: banned by someone or not for the submission std of the submission


- banned_by_someone_std_children: banned by someone or not for the submission std of the submission_children


- banned_by_someone_std_all_children: banned by someone or not for the submission std of the submission_all_children


- banned_by_someone_max: banned by someone or not for the submission max of the submission


- banned_by_someone_max_children: banned by someone or not for the submission max of the submission_children


- banned_by_someone_max_all_children: banned by someone or not for the submission max of the submission_all_children


- banned_by_someone_min: banned by someone or not for the submission min of the submission


- banned_by_someone_min_children: banned by someone or not for the submission min of the submission_children


- banned_by_someone_min_all_children: banned by someone or not for the submission min of the submission_all_children


- banned_by_someone_first: banned by someone or not for the submission first of the submission


- banned_by_someone_first_children: banned by someone or not for the submission first of the submission_children


- banned_by_someone_first_all_children: banned by someone or not for the submission first of the submission_all_children


- banned_by_someone_last: banned by someone or not for the submission last of the submission


- banned_by_someone_last_children: banned by someone or not for the submission last of the submission_children


- banned_by_someone_last_all_children: banned by someone or not for the submission last of the submission_all_children


- can_gild_avg: can gild or not for the submission, it means the submission can be gilded or not. avg of the submission


- can_gild_avg_children: can gild or not for the submission, it means the submission can be gilded or not. avg of the submission_children


- can_gild_avg_all_children: can gild or not for the submission, it means the submission can be gilded or not. avg of the submission_all_children


- can_gild_std: can gild or not for the submission, it means the submission can be gilded or not. std of the submission


- can_gild_std_children: can gild or not for the submission, it means the submission can be gilded or not. std of the submission_children


- can_gild_std_all_children: can gild or not for the submission, it means the submission can be gilded or not. std of the submission_all_children


- can_gild_max: can gild or not for the submission, it means the submission can be gilded or not. max of the submission


- can_gild_max_children: can gild or not for the submission, it means the submission can be gilded or not. max of the submission_children


- can_gild_max_all_children: can gild or not for the submission, it means the submission can be gilded or not. max of the submission_all_children


- can_gild_min: can gild or not for the submission, it means the submission can be gilded or not. min of the submission


- can_gild_min_children: can gild or not for the submission, it means the submission can be gilded or not. min of the submission_children


- can_gild_min_all_children: can gild or not for the submission, it means the submission can be gilded or not. min of the submission_all_children


- can_gild_first: can gild or not for the submission, it means the submission can be gilded or not. first of the submission


- can_gild_first_children: can gild or not for the submission, it means the submission can be gilded or not. first of the submission_children


- can_gild_first_all_children: can gild or not for the submission, it means the submission can be gilded or not. first of the submission_all_children


- can_gild_last: can gild or not for the submission, it means the submission can be gilded or not. last of the submission


- can_gild_last_children: can gild or not for the submission, it means the submission can be gilded or not. last of the submission_children


- can_gild_last_all_children: can gild or not for the submission, it means the submission can be gilded or not. last of the submission_all_children


- can_mod_post_avg: Whether the logged-in user can modify the post avg of the submission


- can_mod_post_avg_children: Whether the logged-in user can modify the post avg of the submission_children


- can_mod_post_avg_all_children: Whether the logged-in user can modify the post avg of the submission_all_children


- can_mod_post_std: Whether the logged-in user can modify the post std of the submission


- can_mod_post_std_children: Whether the logged-in user can modify the post std of the submission_children


- can_mod_post_std_all_children: Whether the logged-in user can modify the post std of the submission_all_children


- can_mod_post_max: Whether the logged-in user can modify the post max of the submission


- can_mod_post_max_children: Whether the logged-in user can modify the post max of the submission_children


- can_mod_post_max_all_children: Whether the logged-in user can modify the post max of the submission_all_children


- can_mod_post_min: Whether the logged-in user can modify the post min of the submission


- can_mod_post_min_children: Whether the logged-in user can modify the post min of the submission_children


- can_mod_post_min_all_children: Whether the logged-in user can modify the post min of the submission_all_children


- can_mod_post_first: Whether the logged-in user can modify the post first of the submission


- can_mod_post_first_children: Whether the logged-in user can modify the post first of the submission_children


- can_mod_post_first_all_children: Whether the logged-in user can modify the post first of the submission_all_children


- can_mod_post_last: Whether the logged-in user can modify the post last of the submission


- can_mod_post_last_children: Whether the logged-in user can modify the post last of the submission_children


- can_mod_post_last_all_children: Whether the logged-in user can modify the post last of the submission_all_children


- category_avg: the category of the submission, mostly it is None avg of the submission


- category_avg_children: the category of the submission, mostly it is None avg of the submission_children


- category_avg_all_children: the category of the submission, mostly it is None avg of the submission_all_children


- category_std: the category of the submission, mostly it is None std of the submission


- category_std_children: the category of the submission, mostly it is None std of the submission_children


- category_std_all_children: the category of the submission, mostly it is None std of the submission_all_children


- category_max: the category of the submission, mostly it is None max of the submission


- category_max_children: the category of the submission, mostly it is None max of the submission_children


- category_max_all_children: the category of the submission, mostly it is None max of the submission_all_children


- category_min: the category of the submission, mostly it is None min of the submission


- category_min_children: the category of the submission, mostly it is None min of the submission_children


- category_min_all_children: the category of the submission, mostly it is None min of the submission_all_children


- category_first: the category of the submission, mostly it is None first of the submission


- category_first_children: the category of the submission, mostly it is None first of the submission_children


- category_first_all_children: the category of the submission, mostly it is None first of the submission_all_children


- category_last: the category of the submission, mostly it is None last of the submission


- category_last_children: the category of the submission, mostly it is None last of the submission_children


- category_last_all_children: the category of the submission, mostly it is None last of the submission_all_children


- num_of_comments_avg: the number of comments of the submission in the observation period avg of the submission


- num_of_comments_avg_children: the number of comments of the submission in the observation period avg of the submission_children


- num_of_comments_avg_all_children: the number of comments of the submission in the observation period avg of the submission_all_children


- num_of_comments_std: the number of comments of the submission in the observation period std of the submission


- num_of_comments_std_children: the number of comments of the submission in the observation period std of the submission_children


- num_of_comments_std_all_children: the number of comments of the submission in the observation period std of the submission_all_children


- num_of_comments_max: the number of comments of the submission in the observation period max of the submission


- num_of_comments_max_children: the number of comments of the submission in the observation period max of the submission_children


- num_of_comments_max_all_children: the number of comments of the submission in the observation period max of the submission_all_children


- num_of_comments_min: the number of comments of the submission in the observation period min of the submission


- num_of_comments_min_children: the number of comments of the submission in the observation period min of the submission_children


- num_of_comments_min_all_children: the number of comments of the submission in the observation period min of the submission_all_children


- num_of_comments_first: the number of comments of the submission in the observation period first of the submission


- num_of_comments_first_children: the number of comments of the submission in the observation period first of the submission_children


- num_of_comments_first_all_children: the number of comments of the submission in the observation period first of the submission_all_children


- num_of_comments_last: the number of comments of the submission in the observation period last of the submission


- num_of_comments_last_children: the number of comments of the submission in the observation period last of the submission_children


- num_of_comments_last_all_children: the number of comments of the submission in the observation period last of the submission_all_children


- contest_mode_avg: if the moderators choose to enable contest mode for the subreddit, it means the comment scores will be hidden and comments will be sorted randomly. avg of the submission


- contest_mode_avg_children: if the moderators choose to enable contest mode for the subreddit, it means the comment scores will be hidden and comments will be sorted randomly. avg of the submission_children


- contest_mode_avg_all_children: if the moderators choose to enable contest mode for the subreddit, it means the comment scores will be hidden and comments will be sorted randomly. avg of the submission_all_children


- contest_mode_std: if the moderators choose to enable contest mode for the subreddit, it means the comment scores will be hidden and comments will be sorted randomly. std of the submission


- contest_mode_std_children: if the moderators choose to enable contest mode for the subreddit, it means the comment scores will be hidden and comments will be sorted randomly. std of the submission_children


- contest_mode_std_all_children: if the moderators choose to enable contest mode for the subreddit, it means the comment scores will be hidden and comments will be sorted randomly. std of the submission_all_children


- contest_mode_max: if the moderators choose to enable contest mode for the subreddit, it means the comment scores will be hidden and comments will be sorted randomly. max of the submission


- contest_mode_max_children: if the moderators choose to enable contest mode for the subreddit, it means the comment scores will be hidden and comments will be sorted randomly. max of the submission_children


- contest_mode_max_all_children: if the moderators choose to enable contest mode for the subreddit, it means the comment scores will be hidden and comments will be sorted randomly. max of the submission_all_children


- contest_mode_min: if the moderators choose to enable contest mode for the subreddit, it means the comment scores will be hidden and comments will be sorted randomly. min of the submission


- contest_mode_min_children: if the moderators choose to enable contest mode for the subreddit, it means the comment scores will be hidden and comments will be sorted randomly. min of the submission_children


- contest_mode_min_all_children: if the moderators choose to enable contest mode for the subreddit, it means the comment scores will be hidden and comments will be sorted randomly. min of the submission_all_children


- contest_mode_first: if the moderators choose to enable contest mode for the subreddit, it means the comment scores will be hidden and comments will be sorted randomly. first of the submission


- contest_mode_first_children: if the moderators choose to enable contest mode for the subreddit, it means the comment scores will be hidden and comments will be sorted randomly. first of the submission_children


- contest_mode_first_all_children: if the moderators choose to enable contest mode for the subreddit, it means the comment scores will be hidden and comments will be sorted randomly. first of the submission_all_children


- contest_mode_last: if the moderators choose to enable contest mode for the subreddit, it means the comment scores will be hidden and comments will be sorted randomly. last of the submission


- contest_mode_last_children: if the moderators choose to enable contest mode for the subreddit, it means the comment scores will be hidden and comments will be sorted randomly. last of the submission_children


- contest_mode_last_all_children: if the moderators choose to enable contest mode for the subreddit, it means the comment scores will be hidden and comments will be sorted randomly. last of the submission_all_children


- created_utc_avg: the created time of the submission avg of the submission


- created_utc_avg_children: the created time of the submission avg of the submission_children


- created_utc_avg_all_children: the created time of the submission avg of the submission_all_children


- created_utc_std: the created time of the submission std of the submission


- created_utc_std_children: the created time of the submission std of the submission_children


- created_utc_std_all_children: the created time of the submission std of the submission_all_children


- created_utc_max: the created time of the submission max of the submission


- created_utc_max_children: the created time of the submission max of the submission_children


- created_utc_max_all_children: the created time of the submission max of the submission_all_children


- created_utc_min: the created time of the submission min of the submission


- created_utc_min_children: the created time of the submission min of the submission_children


- created_utc_min_all_children: the created time of the submission min of the submission_all_children


- created_utc_first: the created time of the submission first of the submission


- created_utc_first_children: the created time of the submission first of the submission_children


- created_utc_first_all_children: the created time of the submission first of the submission_all_children


- created_utc_last: the created time of the submission last of the submission


- created_utc_last_children: the created time of the submission last of the submission_children


- created_utc_last_all_children: the created time of the submission last of the submission_all_children


- content_categories_avg: the content categories of the submission, mostly it is None avg of the submission


- content_categories_avg_children: the content categories of the submission, mostly it is None avg of the submission_children


- content_categories_avg_all_children: the content categories of the submission, mostly it is None avg of the submission_all_children


- content_categories_std: the content categories of the submission, mostly it is None std of the submission


- content_categories_std_children: the content categories of the submission, mostly it is None std of the submission_children


- content_categories_std_all_children: the content categories of the submission, mostly it is None std of the submission_all_children


- content_categories_max: the content categories of the submission, mostly it is None max of the submission


- content_categories_max_children: the content categories of the submission, mostly it is None max of the submission_children


- content_categories_max_all_children: the content categories of the submission, mostly it is None max of the submission_all_children


- content_categories_min: the content categories of the submission, mostly it is None min of the submission


- content_categories_min_children: the content categories of the submission, mostly it is None min of the submission_children


- content_categories_min_all_children: the content categories of the submission, mostly it is None min of the submission_all_children


- content_categories_first: the content categories of the submission, mostly it is None first of the submission


- content_categories_first_children: the content categories of the submission, mostly it is None first of the submission_children


- content_categories_first_all_children: the content categories of the submission, mostly it is None first of the submission_all_children


- content_categories_last: the content categories of the submission, mostly it is None last of the submission


- content_categories_last_children: the content categories of the submission, mostly it is None last of the submission_children


- content_categories_last_all_children: the content categories of the submission, mostly it is None last of the submission_all_children


- discussion_type_avg: the discussion type of the submission, mostly it is None avg of the submission


- discussion_type_avg_children: the discussion type of the submission, mostly it is None avg of the submission_children


- discussion_type_avg_all_children: the discussion type of the submission, mostly it is None avg of the submission_all_children


- discussion_type_std: the discussion type of the submission, mostly it is None std of the submission


- discussion_type_std_children: the discussion type of the submission, mostly it is None std of the submission_children


- discussion_type_std_all_children: the discussion type of the submission, mostly it is None std of the submission_all_children


- discussion_type_max: the discussion type of the submission, mostly it is None max of the submission


- discussion_type_max_children: the discussion type of the submission, mostly it is None max of the submission_children


- discussion_type_max_all_children: the discussion type of the submission, mostly it is None max of the submission_all_children


- discussion_type_min: the discussion type of the submission, mostly it is None min of the submission


- discussion_type_min_children: the discussion type of the submission, mostly it is None min of the submission_children


- discussion_type_min_all_children: the discussion type of the submission, mostly it is None min of the submission_all_children


- discussion_type_first: the discussion type of the submission, mostly it is None first of the submission


- discussion_type_first_children: the discussion type of the submission, mostly it is None first of the submission_children


- discussion_type_first_all_children: the discussion type of the submission, mostly it is None first of the submission_all_children


- discussion_type_last: the discussion type of the submission, mostly it is None last of the submission


- discussion_type_last_children: the discussion type of the submission, mostly it is None last of the submission_children


- discussion_type_last_all_children: the discussion type of the submission, mostly it is None last of the submission_all_children


- distinguished_avg: the distinguished of the submission, mostly it is None avg of the submission


- distinguished_avg_children: the distinguished of the submission, mostly it is None avg of the submission_children


- distinguished_avg_all_children: the distinguished of the submission, mostly it is None avg of the submission_all_children


- distinguished_std: the distinguished of the submission, mostly it is None std of the submission


- distinguished_std_children: the distinguished of the submission, mostly it is None std of the submission_children


- distinguished_std_all_children: the distinguished of the submission, mostly it is None std of the submission_all_children


- distinguished_max: the distinguished of the submission, mostly it is None max of the submission


- distinguished_max_children: the distinguished of the submission, mostly it is None max of the submission_children


- distinguished_max_all_children: the distinguished of the submission, mostly it is None max of the submission_all_children


- distinguished_min: the distinguished of the submission, mostly it is None min of the submission


- distinguished_min_children: the distinguished of the submission, mostly it is None min of the submission_children


- distinguished_min_all_children: the distinguished of the submission, mostly it is None min of the submission_all_children


- distinguished_first: the distinguished of the submission, mostly it is None first of the submission


- distinguished_first_children: the distinguished of the submission, mostly it is None first of the submission_children


- distinguished_first_all_children: the distinguished of the submission, mostly it is None first of the submission_all_children


- distinguished_last: the distinguished of the submission, mostly it is None last of the submission


- distinguished_last_children: the distinguished of the submission, mostly it is None last of the submission_children


- distinguished_last_all_children: the distinguished of the submission, mostly it is None last of the submission_all_children


- domain_avg: the domain of the submission avg of the submission


- domain_avg_children: the domain of the submission avg of the submission_children


- domain_avg_all_children: the domain of the submission avg of the submission_all_children


- domain_std: the domain of the submission std of the submission


- domain_std_children: the domain of the submission std of the submission_children


- domain_std_all_children: the domain of the submission std of the submission_all_children


- domain_max: the domain of the submission max of the submission


- domain_max_children: the domain of the submission max of the submission_children


- domain_max_all_children: the domain of the submission max of the submission_all_children


- domain_min: the domain of the submission min of the submission


- domain_min_children: the domain of the submission min of the submission_children


- domain_min_all_children: the domain of the submission min of the submission_all_children


- domain_first: the domain of the submission first of the submission


- domain_first_children: the domain of the submission first of the submission_children


- domain_first_all_children: the domain of the submission first of the submission_all_children


- domain_last: the domain of the submission last of the submission


- domain_last_children: the domain of the submission last of the submission_children


- domain_last_all_children: the domain of the submission last of the submission_all_children


- edited_avg: edited or not for the submission. avg of the submission


- edited_avg_children: edited or not for the submission. avg of the submission_children


- edited_avg_all_children: edited or not for the submission. avg of the submission_all_children


- edited_std: edited or not for the submission. std of the submission


- edited_std_children: edited or not for the submission. std of the submission_children


- edited_std_all_children: edited or not for the submission. std of the submission_all_children


- edited_max: edited or not for the submission. max of the submission


- edited_max_children: edited or not for the submission. max of the submission_children


- edited_max_all_children: edited or not for the submission. max of the submission_all_children


- edited_min: edited or not for the submission. min of the submission


- edited_min_children: edited or not for the submission. min of the submission_children


- edited_min_all_children: edited or not for the submission. min of the submission_all_children


- edited_first: edited or not for the submission. first of the submission


- edited_first_children: edited or not for the submission. first of the submission_children


- edited_first_all_children: edited or not for the submission. first of the submission_all_children


- edited_last: edited or not for the submission. last of the submission


- edited_last_children: edited or not for the submission. last of the submission_children


- edited_last_all_children: edited or not for the submission. last of the submission_all_children


- num_of_guildings_avg: the number of guildings of the submission, it may be a good feature, but may leaking the information of the future related to the label. avg of the submission


- num_of_guildings_avg_children: the number of guildings of the submission, it may be a good feature, but may leaking the information of the future related to the label. avg of the submission_children


- num_of_guildings_avg_all_children: the number of guildings of the submission, it may be a good feature, but may leaking the information of the future related to the label. avg of the submission_all_children


- num_of_guildings_std: the number of guildings of the submission, it may be a good feature, but may leaking the information of the future related to the label. std of the submission


- num_of_guildings_std_children: the number of guildings of the submission, it may be a good feature, but may leaking the information of the future related to the label. std of the submission_children


- num_of_guildings_std_all_children: the number of guildings of the submission, it may be a good feature, but may leaking the information of the future related to the label. std of the submission_all_children


- num_of_guildings_max: the number of guildings of the submission, it may be a good feature, but may leaking the information of the future related to the label. max of the submission


- num_of_guildings_max_children: the number of guildings of the submission, it may be a good feature, but may leaking the information of the future related to the label. max of the submission_children


- num_of_guildings_max_all_children: the number of guildings of the submission, it may be a good feature, but may leaking the information of the future related to the label. max of the submission_all_children


- num_of_guildings_min: the number of guildings of the submission, it may be a good feature, but may leaking the information of the future related to the label. min of the submission


- num_of_guildings_min_children: the number of guildings of the submission, it may be a good feature, but may leaking the information of the future related to the label. min of the submission_children


- num_of_guildings_min_all_children: the number of guildings of the submission, it may be a good feature, but may leaking the information of the future related to the label. min of the submission_all_children


- num_of_guildings_first: the number of guildings of the submission, it may be a good feature, but may leaking the information of the future related to the label. first of the submission


- num_of_guildings_first_children: the number of guildings of the submission, it may be a good feature, but may leaking the information of the future related to the label. first of the submission_children


- num_of_guildings_first_all_children: the number of guildings of the submission, it may be a good feature, but may leaking the information of the future related to the label. first of the submission_all_children


- num_of_guildings_last: the number of guildings of the submission, it may be a good feature, but may leaking the information of the future related to the label. last of the submission


- num_of_guildings_last_children: the number of guildings of the submission, it may be a good feature, but may leaking the information of the future related to the label. last of the submission_children


- num_of_guildings_last_all_children: the number of guildings of the submission, it may be a good feature, but may leaking the information of the future related to the label. last of the submission_all_children


- gilded_avg: the gilded of the submission, it means the author will get a month of Reddit Premium and 100 Coins, it may be a good feature, but may leaking the information of the future related to the label. avg of the submission


- gilded_avg_children: the gilded of the submission, it means the author will get a month of Reddit Premium and 100 Coins, it may be a good feature, but may leaking the information of the future related to the label. avg of the submission_children


- gilded_avg_all_children: the gilded of the submission, it means the author will get a month of Reddit Premium and 100 Coins, it may be a good feature, but may leaking the information of the future related to the label. avg of the submission_all_children


- gilded_std: the gilded of the submission, it means the author will get a month of Reddit Premium and 100 Coins, it may be a good feature, but may leaking the information of the future related to the label. std of the submission


- gilded_std_children: the gilded of the submission, it means the author will get a month of Reddit Premium and 100 Coins, it may be a good feature, but may leaking the information of the future related to the label. std of the submission_children


- gilded_std_all_children: the gilded of the submission, it means the author will get a month of Reddit Premium and 100 Coins, it may be a good feature, but may leaking the information of the future related to the label. std of the submission_all_children


- gilded_max: the gilded of the submission, it means the author will get a month of Reddit Premium and 100 Coins, it may be a good feature, but may leaking the information of the future related to the label. max of the submission


- gilded_max_children: the gilded of the submission, it means the author will get a month of Reddit Premium and 100 Coins, it may be a good feature, but may leaking the information of the future related to the label. max of the submission_children


- gilded_max_all_children: the gilded of the submission, it means the author will get a month of Reddit Premium and 100 Coins, it may be a good feature, but may leaking the information of the future related to the label. max of the submission_all_children


- gilded_min: the gilded of the submission, it means the author will get a month of Reddit Premium and 100 Coins, it may be a good feature, but may leaking the information of the future related to the label. min of the submission


- gilded_min_children: the gilded of the submission, it means the author will get a month of Reddit Premium and 100 Coins, it may be a good feature, but may leaking the information of the future related to the label. min of the submission_children


- gilded_min_all_children: the gilded of the submission, it means the author will get a month of Reddit Premium and 100 Coins, it may be a good feature, but may leaking the information of the future related to the label. min of the submission_all_children


- gilded_first: the gilded of the submission, it means the author will get a month of Reddit Premium and 100 Coins, it may be a good feature, but may leaking the information of the future related to the label. first of the submission


- gilded_first_children: the gilded of the submission, it means the author will get a month of Reddit Premium and 100 Coins, it may be a good feature, but may leaking the information of the future related to the label. first of the submission_children


- gilded_first_all_children: the gilded of the submission, it means the author will get a month of Reddit Premium and 100 Coins, it may be a good feature, but may leaking the information of the future related to the label. first of the submission_all_children


- gilded_last: the gilded of the submission, it means the author will get a month of Reddit Premium and 100 Coins, it may be a good feature, but may leaking the information of the future related to the label. last of the submission


- gilded_last_children: the gilded of the submission, it means the author will get a month of Reddit Premium and 100 Coins, it may be a good feature, but may leaking the information of the future related to the label. last of the submission_children


- gilded_last_all_children: the gilded of the submission, it means the author will get a month of Reddit Premium and 100 Coins, it may be a good feature, but may leaking the information of the future related to the label. last of the submission_all_children


- hidden_avg: hidden or not for the submission, it means the submission is hidden or not. avg of the submission


- hidden_avg_children: hidden or not for the submission, it means the submission is hidden or not. avg of the submission_children


- hidden_avg_all_children: hidden or not for the submission, it means the submission is hidden or not. avg of the submission_all_children


- hidden_std: hidden or not for the submission, it means the submission is hidden or not. std of the submission


- hidden_std_children: hidden or not for the submission, it means the submission is hidden or not. std of the submission_children


- hidden_std_all_children: hidden or not for the submission, it means the submission is hidden or not. std of the submission_all_children


- hidden_max: hidden or not for the submission, it means the submission is hidden or not. max of the submission


- hidden_max_children: hidden or not for the submission, it means the submission is hidden or not. max of the submission_children


- hidden_max_all_children: hidden or not for the submission, it means the submission is hidden or not. max of the submission_all_children


- hidden_min: hidden or not for the submission, it means the submission is hidden or not. min of the submission


- hidden_min_children: hidden or not for the submission, it means the submission is hidden or not. min of the submission_children


- hidden_min_all_children: hidden or not for the submission, it means the submission is hidden or not. min of the submission_all_children


- hidden_first: hidden or not for the submission, it means the submission is hidden or not. first of the submission


- hidden_first_children: hidden or not for the submission, it means the submission is hidden or not. first of the submission_children


- hidden_first_all_children: hidden or not for the submission, it means the submission is hidden or not. first of the submission_all_children


- hidden_last: hidden or not for the submission, it means the submission is hidden or not. last of the submission


- hidden_last_children: hidden or not for the submission, it means the submission is hidden or not. last of the submission_children


- hidden_last_all_children: hidden or not for the submission, it means the submission is hidden or not. last of the submission_all_children


- hide_score_avg: hide score or not for the submission, it means the score of the submission is hidden or not. avg of the submission


- hide_score_avg_children: hide score or not for the submission, it means the score of the submission is hidden or not. avg of the submission_children


- hide_score_avg_all_children: hide score or not for the submission, it means the score of the submission is hidden or not. avg of the submission_all_children


- hide_score_std: hide score or not for the submission, it means the score of the submission is hidden or not. std of the submission


- hide_score_std_children: hide score or not for the submission, it means the score of the submission is hidden or not. std of the submission_children


- hide_score_std_all_children: hide score or not for the submission, it means the score of the submission is hidden or not. std of the submission_all_children


- hide_score_max: hide score or not for the submission, it means the score of the submission is hidden or not. max of the submission


- hide_score_max_children: hide score or not for the submission, it means the score of the submission is hidden or not. max of the submission_children


- hide_score_max_all_children: hide score or not for the submission, it means the score of the submission is hidden or not. max of the submission_all_children


- hide_score_min: hide score or not for the submission, it means the score of the submission is hidden or not. min of the submission


- hide_score_min_children: hide score or not for the submission, it means the score of the submission is hidden or not. min of the submission_children


- hide_score_min_all_children: hide score or not for the submission, it means the score of the submission is hidden or not. min of the submission_all_children


- hide_score_first: hide score or not for the submission, it means the score of the submission is hidden or not. first of the submission


- hide_score_first_children: hide score or not for the submission, it means the score of the submission is hidden or not. first of the submission_children


- hide_score_first_all_children: hide score or not for the submission, it means the score of the submission is hidden or not. first of the submission_all_children


- hide_score_last: hide score or not for the submission, it means the score of the submission is hidden or not. last of the submission


- hide_score_last_children: hide score or not for the submission, it means the score of the submission is hidden or not. last of the submission_children


- hide_score_last_all_children: hide score or not for the submission, it means the score of the submission is hidden or not. last of the submission_all_children


- is_crosspostable_avg: is a sharing post from another subreddit or not avg of the submission


- is_crosspostable_avg_children: is a sharing post from another subreddit or not avg of the submission_children


- is_crosspostable_avg_all_children: is a sharing post from another subreddit or not avg of the submission_all_children


- is_crosspostable_std: is a sharing post from another subreddit or not std of the submission


- is_crosspostable_std_children: is a sharing post from another subreddit or not std of the submission_children


- is_crosspostable_std_all_children: is a sharing post from another subreddit or not std of the submission_all_children


- is_crosspostable_max: is a sharing post from another subreddit or not max of the submission


- is_crosspostable_max_children: is a sharing post from another subreddit or not max of the submission_children


- is_crosspostable_max_all_children: is a sharing post from another subreddit or not max of the submission_all_children


- is_crosspostable_min: is a sharing post from another subreddit or not min of the submission


- is_crosspostable_min_children: is a sharing post from another subreddit or not min of the submission_children


- is_crosspostable_min_all_children: is a sharing post from another subreddit or not min of the submission_all_children


- is_crosspostable_first: is a sharing post from another subreddit or not first of the submission


- is_crosspostable_first_children: is a sharing post from another subreddit or not first of the submission_children


- is_crosspostable_first_all_children: is a sharing post from another subreddit or not first of the submission_all_children


- is_crosspostable_last: is a sharing post from another subreddit or not last of the submission


- is_crosspostable_last_children: is a sharing post from another subreddit or not last of the submission_children


- is_crosspostable_last_all_children: is a sharing post from another subreddit or not last of the submission_all_children


- is_meta_avg: is a meta post or not, it may be a post about the subreddit itself avg of the submission


- is_meta_avg_children: is a meta post or not, it may be a post about the subreddit itself avg of the submission_children


- is_meta_avg_all_children: is a meta post or not, it may be a post about the subreddit itself avg of the submission_all_children


- is_meta_std: is a meta post or not, it may be a post about the subreddit itself std of the submission


- is_meta_std_children: is a meta post or not, it may be a post about the subreddit itself std of the submission_children


- is_meta_std_all_children: is a meta post or not, it may be a post about the subreddit itself std of the submission_all_children


- is_meta_max: is a meta post or not, it may be a post about the subreddit itself max of the submission


- is_meta_max_children: is a meta post or not, it may be a post about the subreddit itself max of the submission_children


- is_meta_max_all_children: is a meta post or not, it may be a post about the subreddit itself max of the submission_all_children


- is_meta_min: is a meta post or not, it may be a post about the subreddit itself min of the submission


- is_meta_min_children: is a meta post or not, it may be a post about the subreddit itself min of the submission_children


- is_meta_min_all_children: is a meta post or not, it may be a post about the subreddit itself min of the submission_all_children


- is_meta_first: is a meta post or not, it may be a post about the subreddit itself first of the submission


- is_meta_first_children: is a meta post or not, it may be a post about the subreddit itself first of the submission_children


- is_meta_first_all_children: is a meta post or not, it may be a post about the subreddit itself first of the submission_all_children


- is_meta_last: is a meta post or not, it may be a post about the subreddit itself last of the submission


- is_meta_last_children: is a meta post or not, it may be a post about the subreddit itself last of the submission_children


- is_meta_last_all_children: is a meta post or not, it may be a post about the subreddit itself last of the submission_all_children


- is_created_from_ads_ui_avg: is created from ads ui or not avg of the submission


- is_created_from_ads_ui_avg_children: is created from ads ui or not avg of the submission_children


- is_created_from_ads_ui_avg_all_children: is created from ads ui or not avg of the submission_all_children


- is_created_from_ads_ui_std: is created from ads ui or not std of the submission


- is_created_from_ads_ui_std_children: is created from ads ui or not std of the submission_children


- is_created_from_ads_ui_std_all_children: is created from ads ui or not std of the submission_all_children


- is_created_from_ads_ui_max: is created from ads ui or not max of the submission


- is_created_from_ads_ui_max_children: is created from ads ui or not max of the submission_children


- is_created_from_ads_ui_max_all_children: is created from ads ui or not max of the submission_all_children


- is_created_from_ads_ui_min: is created from ads ui or not min of the submission


- is_created_from_ads_ui_min_children: is created from ads ui or not min of the submission_children


- is_created_from_ads_ui_min_all_children: is created from ads ui or not min of the submission_all_children


- is_created_from_ads_ui_first: is created from ads ui or not first of the submission


- is_created_from_ads_ui_first_children: is created from ads ui or not first of the submission_children


- is_created_from_ads_ui_first_all_children: is created from ads ui or not first of the submission_all_children


- is_created_from_ads_ui_last: is created from ads ui or not last of the submission


- is_created_from_ads_ui_last_children: is created from ads ui or not last of the submission_children


- is_created_from_ads_ui_last_all_children: is created from ads ui or not last of the submission_all_children


- is_original_content_avg: is original content or not avg of the submission


- is_original_content_avg_children: is original content or not avg of the submission_children


- is_original_content_avg_all_children: is original content or not avg of the submission_all_children


- is_original_content_std: is original content or not std of the submission


- is_original_content_std_children: is original content or not std of the submission_children


- is_original_content_std_all_children: is original content or not std of the submission_all_children


- is_original_content_max: is original content or not max of the submission


- is_original_content_max_children: is original content or not max of the submission_children


- is_original_content_max_all_children: is original content or not max of the submission_all_children


- is_original_content_min: is original content or not min of the submission


- is_original_content_min_children: is original content or not min of the submission_children


- is_original_content_min_all_children: is original content or not min of the submission_all_children


- is_original_content_first: is original content or not first of the submission


- is_original_content_first_children: is original content or not first of the submission_children


- is_original_content_first_all_children: is original content or not first of the submission_all_children


- is_original_content_last: is original content or not last of the submission


- is_original_content_last_children: is original content or not last of the submission_children


- is_original_content_last_all_children: is original content or not last of the submission_all_children


- is_reddit_media_domain_avg: is reddit media domain or not avg of the submission


- is_reddit_media_domain_avg_children: is reddit media domain or not avg of the submission_children


- is_reddit_media_domain_avg_all_children: is reddit media domain or not avg of the submission_all_children


- is_reddit_media_domain_std: is reddit media domain or not std of the submission


- is_reddit_media_domain_std_children: is reddit media domain or not std of the submission_children


- is_reddit_media_domain_std_all_children: is reddit media domain or not std of the submission_all_children


- is_reddit_media_domain_max: is reddit media domain or not max of the submission


- is_reddit_media_domain_max_children: is reddit media domain or not max of the submission_children


- is_reddit_media_domain_max_all_children: is reddit media domain or not max of the submission_all_children


- is_reddit_media_domain_min: is reddit media domain or not min of the submission


- is_reddit_media_domain_min_children: is reddit media domain or not min of the submission_children


- is_reddit_media_domain_min_all_children: is reddit media domain or not min of the submission_all_children


- is_reddit_media_domain_first: is reddit media domain or not first of the submission


- is_reddit_media_domain_first_children: is reddit media domain or not first of the submission_children


- is_reddit_media_domain_first_all_children: is reddit media domain or not first of the submission_all_children


- is_reddit_media_domain_last: is reddit media domain or not last of the submission


- is_reddit_media_domain_last_children: is reddit media domain or not last of the submission_children


- is_reddit_media_domain_last_all_children: is reddit media domain or not last of the submission_all_children


- is_robot_indexable_avg: is the post can be indexed by robots or not avg of the submission


- is_robot_indexable_avg_children: is the post can be indexed by robots or not avg of the submission_children


- is_robot_indexable_avg_all_children: is the post can be indexed by robots or not avg of the submission_all_children


- is_robot_indexable_std: is the post can be indexed by robots or not std of the submission


- is_robot_indexable_std_children: is the post can be indexed by robots or not std of the submission_children


- is_robot_indexable_std_all_children: is the post can be indexed by robots or not std of the submission_all_children


- is_robot_indexable_max: is the post can be indexed by robots or not max of the submission


- is_robot_indexable_max_children: is the post can be indexed by robots or not max of the submission_children


- is_robot_indexable_max_all_children: is the post can be indexed by robots or not max of the submission_all_children


- is_robot_indexable_min: is the post can be indexed by robots or not min of the submission


- is_robot_indexable_min_children: is the post can be indexed by robots or not min of the submission_children


- is_robot_indexable_min_all_children: is the post can be indexed by robots or not min of the submission_all_children


- is_robot_indexable_first: is the post can be indexed by robots or not first of the submission


- is_robot_indexable_first_children: is the post can be indexed by robots or not first of the submission_children


- is_robot_indexable_first_all_children: is the post can be indexed by robots or not first of the submission_all_children


- is_robot_indexable_last: is the post can be indexed by robots or not last of the submission


- is_robot_indexable_last_children: is the post can be indexed by robots or not last of the submission_children


- is_robot_indexable_last_all_children: is the post can be indexed by robots or not last of the submission_all_children


- is_self_avg: is self or not for the submission, it means the submission is a self post or not. avg of the submission


- is_self_avg_children: is self or not for the submission, it means the submission is a self post or not. avg of the submission_children


- is_self_avg_all_children: is self or not for the submission, it means the submission is a self post or not. avg of the submission_all_children


- is_self_std: is self or not for the submission, it means the submission is a self post or not. std of the submission


- is_self_std_children: is self or not for the submission, it means the submission is a self post or not. std of the submission_children


- is_self_std_all_children: is self or not for the submission, it means the submission is a self post or not. std of the submission_all_children


- is_self_max: is self or not for the submission, it means the submission is a self post or not. max of the submission


- is_self_max_children: is self or not for the submission, it means the submission is a self post or not. max of the submission_children


- is_self_max_all_children: is self or not for the submission, it means the submission is a self post or not. max of the submission_all_children


- is_self_min: is self or not for the submission, it means the submission is a self post or not. min of the submission


- is_self_min_children: is self or not for the submission, it means the submission is a self post or not. min of the submission_children


- is_self_min_all_children: is self or not for the submission, it means the submission is a self post or not. min of the submission_all_children


- is_self_first: is self or not for the submission, it means the submission is a self post or not. first of the submission


- is_self_first_children: is self or not for the submission, it means the submission is a self post or not. first of the submission_children


- is_self_first_all_children: is self or not for the submission, it means the submission is a self post or not. first of the submission_all_children


- is_self_last: is self or not for the submission, it means the submission is a self post or not. last of the submission


- is_self_last_children: is self or not for the submission, it means the submission is a self post or not. last of the submission_children


- is_self_last_all_children: is self or not for the submission, it means the submission is a self post or not. last of the submission_all_children


- is_video_avg: is a video post or not avg of the submission


- is_video_avg_children: is a video post or not avg of the submission_children


- is_video_avg_all_children: is a video post or not avg of the submission_all_children


- is_video_std: is a video post or not std of the submission


- is_video_std_children: is a video post or not std of the submission_children


- is_video_std_all_children: is a video post or not std of the submission_all_children


- is_video_max: is a video post or not max of the submission


- is_video_max_children: is a video post or not max of the submission_children


- is_video_max_all_children: is a video post or not max of the submission_all_children


- is_video_min: is a video post or not min of the submission


- is_video_min_children: is a video post or not min of the submission_children


- is_video_min_all_children: is a video post or not min of the submission_all_children


- is_video_first: is a video post or not first of the submission


- is_video_first_children: is a video post or not first of the submission_children


- is_video_first_all_children: is a video post or not first of the submission_all_children


- is_video_last: is a video post or not last of the submission


- is_video_last_children: is a video post or not last of the submission_children


- is_video_last_all_children: is a video post or not last of the submission_all_children


- link_flair_background_color_avg: the link flair background color of the submission, mostly it is None avg of the submission


- link_flair_background_color_avg_children: the link flair background color of the submission, mostly it is None avg of the submission_children


- link_flair_background_color_avg_all_children: the link flair background color of the submission, mostly it is None avg of the submission_all_children


- link_flair_background_color_std: the link flair background color of the submission, mostly it is None std of the submission


- link_flair_background_color_std_children: the link flair background color of the submission, mostly it is None std of the submission_children


- link_flair_background_color_std_all_children: the link flair background color of the submission, mostly it is None std of the submission_all_children


- link_flair_background_color_max: the link flair background color of the submission, mostly it is None max of the submission


- link_flair_background_color_max_children: the link flair background color of the submission, mostly it is None max of the submission_children


- link_flair_background_color_max_all_children: the link flair background color of the submission, mostly it is None max of the submission_all_children


- link_flair_background_color_min: the link flair background color of the submission, mostly it is None min of the submission


- link_flair_background_color_min_children: the link flair background color of the submission, mostly it is None min of the submission_children


- link_flair_background_color_min_all_children: the link flair background color of the submission, mostly it is None min of the submission_all_children


- link_flair_background_color_first: the link flair background color of the submission, mostly it is None first of the submission


- link_flair_background_color_first_children: the link flair background color of the submission, mostly it is None first of the submission_children


- link_flair_background_color_first_all_children: the link flair background color of the submission, mostly it is None first of the submission_all_children


- link_flair_background_color_last: the link flair background color of the submission, mostly it is None last of the submission


- link_flair_background_color_last_children: the link flair background color of the submission, mostly it is None last of the submission_children


- link_flair_background_color_last_all_children: the link flair background color of the submission, mostly it is None last of the submission_all_children


- link_flair_css_class_avg: the link flair css class of the submission, mostly it is None avg of the submission


- link_flair_css_class_avg_children: the link flair css class of the submission, mostly it is None avg of the submission_children


- link_flair_css_class_avg_all_children: the link flair css class of the submission, mostly it is None avg of the submission_all_children


- link_flair_css_class_std: the link flair css class of the submission, mostly it is None std of the submission


- link_flair_css_class_std_children: the link flair css class of the submission, mostly it is None std of the submission_children


- link_flair_css_class_std_all_children: the link flair css class of the submission, mostly it is None std of the submission_all_children


- link_flair_css_class_max: the link flair css class of the submission, mostly it is None max of the submission


- link_flair_css_class_max_children: the link flair css class of the submission, mostly it is None max of the submission_children


- link_flair_css_class_max_all_children: the link flair css class of the submission, mostly it is None max of the submission_all_children


- link_flair_css_class_min: the link flair css class of the submission, mostly it is None min of the submission


- link_flair_css_class_min_children: the link flair css class of the submission, mostly it is None min of the submission_children


- link_flair_css_class_min_all_children: the link flair css class of the submission, mostly it is None min of the submission_all_children


- link_flair_css_class_first: the link flair css class of the submission, mostly it is None first of the submission


- link_flair_css_class_first_children: the link flair css class of the submission, mostly it is None first of the submission_children


- link_flair_css_class_first_all_children: the link flair css class of the submission, mostly it is None first of the submission_all_children


- link_flair_css_class_last: the link flair css class of the submission, mostly it is None last of the submission


- link_flair_css_class_last_children: the link flair css class of the submission, mostly it is None last of the submission_children


- link_flair_css_class_last_all_children: the link flair css class of the submission, mostly it is None last of the submission_all_children


- link_flair_richtext_avg: the link flair richtext of the submission, mostly it is None avg of the submission


- link_flair_richtext_avg_children: the link flair richtext of the submission, mostly it is None avg of the submission_children


- link_flair_richtext_avg_all_children: the link flair richtext of the submission, mostly it is None avg of the submission_all_children


- link_flair_richtext_std: the link flair richtext of the submission, mostly it is None std of the submission


- link_flair_richtext_std_children: the link flair richtext of the submission, mostly it is None std of the submission_children


- link_flair_richtext_std_all_children: the link flair richtext of the submission, mostly it is None std of the submission_all_children


- link_flair_richtext_max: the link flair richtext of the submission, mostly it is None max of the submission


- link_flair_richtext_max_children: the link flair richtext of the submission, mostly it is None max of the submission_children


- link_flair_richtext_max_all_children: the link flair richtext of the submission, mostly it is None max of the submission_all_children


- link_flair_richtext_min: the link flair richtext of the submission, mostly it is None min of the submission


- link_flair_richtext_min_children: the link flair richtext of the submission, mostly it is None min of the submission_children


- link_flair_richtext_min_all_children: the link flair richtext of the submission, mostly it is None min of the submission_all_children


- link_flair_richtext_first: the link flair richtext of the submission, mostly it is None first of the submission


- link_flair_richtext_first_children: the link flair richtext of the submission, mostly it is None first of the submission_children


- link_flair_richtext_first_all_children: the link flair richtext of the submission, mostly it is None first of the submission_all_children


- link_flair_richtext_last: the link flair richtext of the submission, mostly it is None last of the submission


- link_flair_richtext_last_children: the link flair richtext of the submission, mostly it is None last of the submission_children


- link_flair_richtext_last_all_children: the link flair richtext of the submission, mostly it is None last of the submission_all_children


- link_flair_template_id_avg: the link flair template id of the submission, mostly it is None avg of the submission


- link_flair_template_id_avg_children: the link flair template id of the submission, mostly it is None avg of the submission_children


- link_flair_template_id_avg_all_children: the link flair template id of the submission, mostly it is None avg of the submission_all_children


- link_flair_template_id_std: the link flair template id of the submission, mostly it is None std of the submission


- link_flair_template_id_std_children: the link flair template id of the submission, mostly it is None std of the submission_children


- link_flair_template_id_std_all_children: the link flair template id of the submission, mostly it is None std of the submission_all_children


- link_flair_template_id_max: the link flair template id of the submission, mostly it is None max of the submission


- link_flair_template_id_max_children: the link flair template id of the submission, mostly it is None max of the submission_children


- link_flair_template_id_max_all_children: the link flair template id of the submission, mostly it is None max of the submission_all_children


- link_flair_template_id_min: the link flair template id of the submission, mostly it is None min of the submission


- link_flair_template_id_min_children: the link flair template id of the submission, mostly it is None min of the submission_children


- link_flair_template_id_min_all_children: the link flair template id of the submission, mostly it is None min of the submission_all_children


- link_flair_template_id_first: the link flair template id of the submission, mostly it is None first of the submission


- link_flair_template_id_first_children: the link flair template id of the submission, mostly it is None first of the submission_children


- link_flair_template_id_first_all_children: the link flair template id of the submission, mostly it is None first of the submission_all_children


- link_flair_template_id_last: the link flair template id of the submission, mostly it is None last of the submission


- link_flair_template_id_last_children: the link flair template id of the submission, mostly it is None last of the submission_children


- link_flair_template_id_last_all_children: the link flair template id of the submission, mostly it is None last of the submission_all_children


- link_flair_text_avg: the link flair text of the submission, mostly it is None avg of the submission


- link_flair_text_avg_children: the link flair text of the submission, mostly it is None avg of the submission_children


- link_flair_text_avg_all_children: the link flair text of the submission, mostly it is None avg of the submission_all_children


- link_flair_text_std: the link flair text of the submission, mostly it is None std of the submission


- link_flair_text_std_children: the link flair text of the submission, mostly it is None std of the submission_children


- link_flair_text_std_all_children: the link flair text of the submission, mostly it is None std of the submission_all_children


- link_flair_text_max: the link flair text of the submission, mostly it is None max of the submission


- link_flair_text_max_children: the link flair text of the submission, mostly it is None max of the submission_children


- link_flair_text_max_all_children: the link flair text of the submission, mostly it is None max of the submission_all_children


- link_flair_text_min: the link flair text of the submission, mostly it is None min of the submission


- link_flair_text_min_children: the link flair text of the submission, mostly it is None min of the submission_children


- link_flair_text_min_all_children: the link flair text of the submission, mostly it is None min of the submission_all_children


- link_flair_text_first: the link flair text of the submission, mostly it is None first of the submission


- link_flair_text_first_children: the link flair text of the submission, mostly it is None first of the submission_children


- link_flair_text_first_all_children: the link flair text of the submission, mostly it is None first of the submission_all_children


- link_flair_text_last: the link flair text of the submission, mostly it is None last of the submission


- link_flair_text_last_children: the link flair text of the submission, mostly it is None last of the submission_children


- link_flair_text_last_all_children: the link flair text of the submission, mostly it is None last of the submission_all_children


- link_flair_text_color_avg: the link flair text color of the submission, mostly it is None avg of the submission


- link_flair_text_color_avg_children: the link flair text color of the submission, mostly it is None avg of the submission_children


- link_flair_text_color_avg_all_children: the link flair text color of the submission, mostly it is None avg of the submission_all_children


- link_flair_text_color_std: the link flair text color of the submission, mostly it is None std of the submission


- link_flair_text_color_std_children: the link flair text color of the submission, mostly it is None std of the submission_children


- link_flair_text_color_std_all_children: the link flair text color of the submission, mostly it is None std of the submission_all_children


- link_flair_text_color_max: the link flair text color of the submission, mostly it is None max of the submission


- link_flair_text_color_max_children: the link flair text color of the submission, mostly it is None max of the submission_children


- link_flair_text_color_max_all_children: the link flair text color of the submission, mostly it is None max of the submission_all_children


- link_flair_text_color_min: the link flair text color of the submission, mostly it is None min of the submission


- link_flair_text_color_min_children: the link flair text color of the submission, mostly it is None min of the submission_children


- link_flair_text_color_min_all_children: the link flair text color of the submission, mostly it is None min of the submission_all_children


- link_flair_text_color_first: the link flair text color of the submission, mostly it is None first of the submission


- link_flair_text_color_first_children: the link flair text color of the submission, mostly it is None first of the submission_children


- link_flair_text_color_first_all_children: the link flair text color of the submission, mostly it is None first of the submission_all_children


- link_flair_text_color_last: the link flair text color of the submission, mostly it is None last of the submission


- link_flair_text_color_last_children: the link flair text color of the submission, mostly it is None last of the submission_children


- link_flair_text_color_last_all_children: the link flair text color of the submission, mostly it is None last of the submission_all_children


- link_flair_type_avg: the link flair type of the submission, mostly it is None avg of the submission


- link_flair_type_avg_children: the link flair type of the submission, mostly it is None avg of the submission_children


- link_flair_type_avg_all_children: the link flair type of the submission, mostly it is None avg of the submission_all_children


- link_flair_type_std: the link flair type of the submission, mostly it is None std of the submission


- link_flair_type_std_children: the link flair type of the submission, mostly it is None std of the submission_children


- link_flair_type_std_all_children: the link flair type of the submission, mostly it is None std of the submission_all_children


- link_flair_type_max: the link flair type of the submission, mostly it is None max of the submission


- link_flair_type_max_children: the link flair type of the submission, mostly it is None max of the submission_children


- link_flair_type_max_all_children: the link flair type of the submission, mostly it is None max of the submission_all_children


- link_flair_type_min: the link flair type of the submission, mostly it is None min of the submission


- link_flair_type_min_children: the link flair type of the submission, mostly it is None min of the submission_children


- link_flair_type_min_all_children: the link flair type of the submission, mostly it is None min of the submission_all_children


- link_flair_type_first: the link flair type of the submission, mostly it is None first of the submission


- link_flair_type_first_children: the link flair type of the submission, mostly it is None first of the submission_children


- link_flair_type_first_all_children: the link flair type of the submission, mostly it is None first of the submission_all_children


- link_flair_type_last: the link flair type of the submission, mostly it is None last of the submission


- link_flair_type_last_children: the link flair type of the submission, mostly it is None last of the submission_children


- link_flair_type_last_all_children: the link flair type of the submission, mostly it is None last of the submission_all_children


- locked_avg: locked or not for the submission, it means the submission is locked by the moderator and no one can comment on it. avg of the submission


- locked_avg_children: locked or not for the submission, it means the submission is locked by the moderator and no one can comment on it. avg of the submission_children


- locked_avg_all_children: locked or not for the submission, it means the submission is locked by the moderator and no one can comment on it. avg of the submission_all_children


- locked_std: locked or not for the submission, it means the submission is locked by the moderator and no one can comment on it. std of the submission


- locked_std_children: locked or not for the submission, it means the submission is locked by the moderator and no one can comment on it. std of the submission_children


- locked_std_all_children: locked or not for the submission, it means the submission is locked by the moderator and no one can comment on it. std of the submission_all_children


- locked_max: locked or not for the submission, it means the submission is locked by the moderator and no one can comment on it. max of the submission


- locked_max_children: locked or not for the submission, it means the submission is locked by the moderator and no one can comment on it. max of the submission_children


- locked_max_all_children: locked or not for the submission, it means the submission is locked by the moderator and no one can comment on it. max of the submission_all_children


- locked_min: locked or not for the submission, it means the submission is locked by the moderator and no one can comment on it. min of the submission


- locked_min_children: locked or not for the submission, it means the submission is locked by the moderator and no one can comment on it. min of the submission_children


- locked_min_all_children: locked or not for the submission, it means the submission is locked by the moderator and no one can comment on it. min of the submission_all_children


- locked_first: locked or not for the submission, it means the submission is locked by the moderator and no one can comment on it. first of the submission


- locked_first_children: locked or not for the submission, it means the submission is locked by the moderator and no one can comment on it. first of the submission_children


- locked_first_all_children: locked or not for the submission, it means the submission is locked by the moderator and no one can comment on it. first of the submission_all_children


- locked_last: locked or not for the submission, it means the submission is locked by the moderator and no one can comment on it. last of the submission


- locked_last_children: locked or not for the submission, it means the submission is locked by the moderator and no one can comment on it. last of the submission_children


- locked_last_all_children: locked or not for the submission, it means the submission is locked by the moderator and no one can comment on it. last of the submission_all_children


- media_only_avg: if the submission only contains media or not avg of the submission


- media_only_avg_children: if the submission only contains media or not avg of the submission_children


- media_only_avg_all_children: if the submission only contains media or not avg of the submission_all_children


- media_only_std: if the submission only contains media or not std of the submission


- media_only_std_children: if the submission only contains media or not std of the submission_children


- media_only_std_all_children: if the submission only contains media or not std of the submission_all_children


- media_only_max: if the submission only contains media or not max of the submission


- media_only_max_children: if the submission only contains media or not max of the submission_children


- media_only_max_all_children: if the submission only contains media or not max of the submission_all_children


- media_only_min: if the submission only contains media or not min of the submission


- media_only_min_children: if the submission only contains media or not min of the submission_children


- media_only_min_all_children: if the submission only contains media or not min of the submission_all_children


- media_only_first: if the submission only contains media or not first of the submission


- media_only_first_children: if the submission only contains media or not first of the submission_children


- media_only_first_all_children: if the submission only contains media or not first of the submission_all_children


- media_only_last: if the submission only contains media or not last of the submission


- media_only_last_children: if the submission only contains media or not last of the submission_children


- media_only_last_all_children: if the submission only contains media or not last of the submission_all_children


- no_follow_avg: no follow or not for the submission, it means tell the search engines to not follow the link. avg of the submission


- no_follow_avg_children: no follow or not for the submission, it means tell the search engines to not follow the link. avg of the submission_children


- no_follow_avg_all_children: no follow or not for the submission, it means tell the search engines to not follow the link. avg of the submission_all_children


- no_follow_std: no follow or not for the submission, it means tell the search engines to not follow the link. std of the submission


- no_follow_std_children: no follow or not for the submission, it means tell the search engines to not follow the link. std of the submission_children


- no_follow_std_all_children: no follow or not for the submission, it means tell the search engines to not follow the link. std of the submission_all_children


- no_follow_max: no follow or not for the submission, it means tell the search engines to not follow the link. max of the submission


- no_follow_max_children: no follow or not for the submission, it means tell the search engines to not follow the link. max of the submission_children


- no_follow_max_all_children: no follow or not for the submission, it means tell the search engines to not follow the link. max of the submission_all_children


- no_follow_min: no follow or not for the submission, it means tell the search engines to not follow the link. min of the submission


- no_follow_min_children: no follow or not for the submission, it means tell the search engines to not follow the link. min of the submission_children


- no_follow_min_all_children: no follow or not for the submission, it means tell the search engines to not follow the link. min of the submission_all_children


- no_follow_first: no follow or not for the submission, it means tell the search engines to not follow the link. first of the submission


- no_follow_first_children: no follow or not for the submission, it means tell the search engines to not follow the link. first of the submission_children


- no_follow_first_all_children: no follow or not for the submission, it means tell the search engines to not follow the link. first of the submission_all_children


- no_follow_last: no follow or not for the submission, it means tell the search engines to not follow the link. last of the submission


- no_follow_last_children: no follow or not for the submission, it means tell the search engines to not follow the link. last of the submission_children


- no_follow_last_all_children: no follow or not for the submission, it means tell the search engines to not follow the link. last of the submission_all_children


- num_crossposts_avg: the number of crossposts of the submission. it may be a good feature, but may leaking the information of the future related to the label. avg of the submission


- num_crossposts_avg_children: the number of crossposts of the submission. it may be a good feature, but may leaking the information of the future related to the label. avg of the submission_children


- num_crossposts_avg_all_children: the number of crossposts of the submission. it may be a good feature, but may leaking the information of the future related to the label. avg of the submission_all_children


- num_crossposts_std: the number of crossposts of the submission. it may be a good feature, but may leaking the information of the future related to the label. std of the submission


- num_crossposts_std_children: the number of crossposts of the submission. it may be a good feature, but may leaking the information of the future related to the label. std of the submission_children


- num_crossposts_std_all_children: the number of crossposts of the submission. it may be a good feature, but may leaking the information of the future related to the label. std of the submission_all_children


- num_crossposts_max: the number of crossposts of the submission. it may be a good feature, but may leaking the information of the future related to the label. max of the submission


- num_crossposts_max_children: the number of crossposts of the submission. it may be a good feature, but may leaking the information of the future related to the label. max of the submission_children


- num_crossposts_max_all_children: the number of crossposts of the submission. it may be a good feature, but may leaking the information of the future related to the label. max of the submission_all_children


- num_crossposts_min: the number of crossposts of the submission. it may be a good feature, but may leaking the information of the future related to the label. min of the submission


- num_crossposts_min_children: the number of crossposts of the submission. it may be a good feature, but may leaking the information of the future related to the label. min of the submission_children


- num_crossposts_min_all_children: the number of crossposts of the submission. it may be a good feature, but may leaking the information of the future related to the label. min of the submission_all_children


- num_crossposts_first: the number of crossposts of the submission. it may be a good feature, but may leaking the information of the future related to the label. first of the submission


- num_crossposts_first_children: the number of crossposts of the submission. it may be a good feature, but may leaking the information of the future related to the label. first of the submission_children


- num_crossposts_first_all_children: the number of crossposts of the submission. it may be a good feature, but may leaking the information of the future related to the label. first of the submission_all_children


- num_crossposts_last: the number of crossposts of the submission. it may be a good feature, but may leaking the information of the future related to the label. last of the submission


- num_crossposts_last_children: the number of crossposts of the submission. it may be a good feature, but may leaking the information of the future related to the label. last of the submission_children


- num_crossposts_last_all_children: the number of crossposts of the submission. it may be a good feature, but may leaking the information of the future related to the label. last of the submission_all_children


- over_18_avg: if the submission is visible only to users over 18 or not avg of the submission


- over_18_avg_children: if the submission is visible only to users over 18 or not avg of the submission_children


- over_18_avg_all_children: if the submission is visible only to users over 18 or not avg of the submission_all_children


- over_18_std: if the submission is visible only to users over 18 or not std of the submission


- over_18_std_children: if the submission is visible only to users over 18 or not std of the submission_children


- over_18_std_all_children: if the submission is visible only to users over 18 or not std of the submission_all_children


- over_18_max: if the submission is visible only to users over 18 or not max of the submission


- over_18_max_children: if the submission is visible only to users over 18 or not max of the submission_children


- over_18_max_all_children: if the submission is visible only to users over 18 or not max of the submission_all_children


- over_18_min: if the submission is visible only to users over 18 or not min of the submission


- over_18_min_children: if the submission is visible only to users over 18 or not min of the submission_children


- over_18_min_all_children: if the submission is visible only to users over 18 or not min of the submission_all_children


- over_18_first: if the submission is visible only to users over 18 or not first of the submission


- over_18_first_children: if the submission is visible only to users over 18 or not first of the submission_children


- over_18_first_all_children: if the submission is visible only to users over 18 or not first of the submission_all_children


- over_18_last: if the submission is visible only to users over 18 or not last of the submission


- over_18_last_children: if the submission is visible only to users over 18 or not last of the submission_children


- over_18_last_all_children: if the submission is visible only to users over 18 or not last of the submission_all_children


- parent_whitelist_status_avg: the parent whitelist status of the submission, mostly it is None avg of the submission


- parent_whitelist_status_avg_children: the parent whitelist status of the submission, mostly it is None avg of the submission_children


- parent_whitelist_status_avg_all_children: the parent whitelist status of the submission, mostly it is None avg of the submission_all_children


- parent_whitelist_status_std: the parent whitelist status of the submission, mostly it is None std of the submission


- parent_whitelist_status_std_children: the parent whitelist status of the submission, mostly it is None std of the submission_children


- parent_whitelist_status_std_all_children: the parent whitelist status of the submission, mostly it is None std of the submission_all_children


- parent_whitelist_status_max: the parent whitelist status of the submission, mostly it is None max of the submission


- parent_whitelist_status_max_children: the parent whitelist status of the submission, mostly it is None max of the submission_children


- parent_whitelist_status_max_all_children: the parent whitelist status of the submission, mostly it is None max of the submission_all_children


- parent_whitelist_status_min: the parent whitelist status of the submission, mostly it is None min of the submission


- parent_whitelist_status_min_children: the parent whitelist status of the submission, mostly it is None min of the submission_children


- parent_whitelist_status_min_all_children: the parent whitelist status of the submission, mostly it is None min of the submission_all_children


- parent_whitelist_status_first: the parent whitelist status of the submission, mostly it is None first of the submission


- parent_whitelist_status_first_children: the parent whitelist status of the submission, mostly it is None first of the submission_children


- parent_whitelist_status_first_all_children: the parent whitelist status of the submission, mostly it is None first of the submission_all_children


- parent_whitelist_status_last: the parent whitelist status of the submission, mostly it is None last of the submission


- parent_whitelist_status_last_children: the parent whitelist status of the submission, mostly it is None last of the submission_children


- parent_whitelist_status_last_all_children: the parent whitelist status of the submission, mostly it is None last of the submission_all_children


- pinned_avg: pinned or not for the submission, it means the submission is pinned or not. avg of the submission


- pinned_avg_children: pinned or not for the submission, it means the submission is pinned or not. avg of the submission_children


- pinned_avg_all_children: pinned or not for the submission, it means the submission is pinned or not. avg of the submission_all_children


- pinned_std: pinned or not for the submission, it means the submission is pinned or not. std of the submission


- pinned_std_children: pinned or not for the submission, it means the submission is pinned or not. std of the submission_children


- pinned_std_all_children: pinned or not for the submission, it means the submission is pinned or not. std of the submission_all_children


- pinned_max: pinned or not for the submission, it means the submission is pinned or not. max of the submission


- pinned_max_children: pinned or not for the submission, it means the submission is pinned or not. max of the submission_children


- pinned_max_all_children: pinned or not for the submission, it means the submission is pinned or not. max of the submission_all_children


- pinned_min: pinned or not for the submission, it means the submission is pinned or not. min of the submission


- pinned_min_children: pinned or not for the submission, it means the submission is pinned or not. min of the submission_children


- pinned_min_all_children: pinned or not for the submission, it means the submission is pinned or not. min of the submission_all_children


- pinned_first: pinned or not for the submission, it means the submission is pinned or not. first of the submission


- pinned_first_children: pinned or not for the submission, it means the submission is pinned or not. first of the submission_children


- pinned_first_all_children: pinned or not for the submission, it means the submission is pinned or not. first of the submission_all_children


- pinned_last: pinned or not for the submission, it means the submission is pinned or not. last of the submission


- pinned_last_children: pinned or not for the submission, it means the submission is pinned or not. last of the submission_children


- pinned_last_all_children: pinned or not for the submission, it means the submission is pinned or not. last of the submission_all_children


- pwls_avg: the pwls of the submission avg of the submission


- pwls_avg_children: the pwls of the submission avg of the submission_children


- pwls_avg_all_children: the pwls of the submission avg of the submission_all_children


- pwls_std: the pwls of the submission std of the submission


- pwls_std_children: the pwls of the submission std of the submission_children


- pwls_std_all_children: the pwls of the submission std of the submission_all_children


- pwls_max: the pwls of the submission max of the submission


- pwls_max_children: the pwls of the submission max of the submission_children


- pwls_max_all_children: the pwls of the submission max of the submission_all_children


- pwls_min: the pwls of the submission min of the submission


- pwls_min_children: the pwls of the submission min of the submission_children


- pwls_min_all_children: the pwls of the submission min of the submission_all_children


- pwls_first: the pwls of the submission first of the submission


- pwls_first_children: the pwls of the submission first of the submission_children


- pwls_first_all_children: the pwls of the submission first of the submission_all_children


- pwls_last: the pwls of the submission last of the submission


- pwls_last_children: the pwls of the submission last of the submission_children


- pwls_last_all_children: the pwls of the submission last of the submission_all_children


- quarantine_avg: quarantine or not for the submission, it means the submission is quarantined or not. avg of the submission


- quarantine_avg_children: quarantine or not for the submission, it means the submission is quarantined or not. avg of the submission_children


- quarantine_avg_all_children: quarantine or not for the submission, it means the submission is quarantined or not. avg of the submission_all_children


- quarantine_std: quarantine or not for the submission, it means the submission is quarantined or not. std of the submission


- quarantine_std_children: quarantine or not for the submission, it means the submission is quarantined or not. std of the submission_children


- quarantine_std_all_children: quarantine or not for the submission, it means the submission is quarantined or not. std of the submission_all_children


- quarantine_max: quarantine or not for the submission, it means the submission is quarantined or not. max of the submission


- quarantine_max_children: quarantine or not for the submission, it means the submission is quarantined or not. max of the submission_children


- quarantine_max_all_children: quarantine or not for the submission, it means the submission is quarantined or not. max of the submission_all_children


- quarantine_min: quarantine or not for the submission, it means the submission is quarantined or not. min of the submission


- quarantine_min_children: quarantine or not for the submission, it means the submission is quarantined or not. min of the submission_children


- quarantine_min_all_children: quarantine or not for the submission, it means the submission is quarantined or not. min of the submission_all_children


- quarantine_first: quarantine or not for the submission, it means the submission is quarantined or not. first of the submission


- quarantine_first_children: quarantine or not for the submission, it means the submission is quarantined or not. first of the submission_children


- quarantine_first_all_children: quarantine or not for the submission, it means the submission is quarantined or not. first of the submission_all_children


- quarantine_last: quarantine or not for the submission, it means the submission is quarantined or not. last of the submission


- quarantine_last_children: quarantine or not for the submission, it means the submission is quarantined or not. last of the submission_children


- quarantine_last_all_children: quarantine or not for the submission, it means the submission is quarantined or not. last of the submission_all_children


- removed_by_someone_avg: removed by someone or not for the submission avg of the submission


- removed_by_someone_avg_children: removed by someone or not for the submission avg of the submission_children


- removed_by_someone_avg_all_children: removed by someone or not for the submission avg of the submission_all_children


- removed_by_someone_std: removed by someone or not for the submission std of the submission


- removed_by_someone_std_children: removed by someone or not for the submission std of the submission_children


- removed_by_someone_std_all_children: removed by someone or not for the submission std of the submission_all_children


- removed_by_someone_max: removed by someone or not for the submission max of the submission


- removed_by_someone_max_children: removed by someone or not for the submission max of the submission_children


- removed_by_someone_max_all_children: removed by someone or not for the submission max of the submission_all_children


- removed_by_someone_min: removed by someone or not for the submission min of the submission


- removed_by_someone_min_children: removed by someone or not for the submission min of the submission_children


- removed_by_someone_min_all_children: removed by someone or not for the submission min of the submission_all_children


- removed_by_someone_first: removed by someone or not for the submission first of the submission


- removed_by_someone_first_children: removed by someone or not for the submission first of the submission_children


- removed_by_someone_first_all_children: removed by someone or not for the submission first of the submission_all_children


- removed_by_someone_last: removed by someone or not for the submission last of the submission


- removed_by_someone_last_children: removed by someone or not for the submission last of the submission_children


- removed_by_someone_last_all_children: removed by someone or not for the submission last of the submission_all_children


- score_avg: the score of the submission, it may be a good feature, but may leaking the information of the future related to the label. avg of the submission


- score_avg_children: the score of the submission, it may be a good feature, but may leaking the information of the future related to the label. avg of the submission_children


- score_avg_all_children: the score of the submission, it may be a good feature, but may leaking the information of the future related to the label. avg of the submission_all_children


- score_std: the score of the submission, it may be a good feature, but may leaking the information of the future related to the label. std of the submission


- score_std_children: the score of the submission, it may be a good feature, but may leaking the information of the future related to the label. std of the submission_children


- score_std_all_children: the score of the submission, it may be a good feature, but may leaking the information of the future related to the label. std of the submission_all_children


- score_max: the score of the submission, it may be a good feature, but may leaking the information of the future related to the label. max of the submission


- score_max_children: the score of the submission, it may be a good feature, but may leaking the information of the future related to the label. max of the submission_children


- score_max_all_children: the score of the submission, it may be a good feature, but may leaking the information of the future related to the label. max of the submission_all_children


- score_min: the score of the submission, it may be a good feature, but may leaking the information of the future related to the label. min of the submission


- score_min_children: the score of the submission, it may be a good feature, but may leaking the information of the future related to the label. min of the submission_children


- score_min_all_children: the score of the submission, it may be a good feature, but may leaking the information of the future related to the label. min of the submission_all_children


- score_first: the score of the submission, it may be a good feature, but may leaking the information of the future related to the label. first of the submission


- score_first_children: the score of the submission, it may be a good feature, but may leaking the information of the future related to the label. first of the submission_children


- score_first_all_children: the score of the submission, it may be a good feature, but may leaking the information of the future related to the label. first of the submission_all_children


- score_last: the score of the submission, it may be a good feature, but may leaking the information of the future related to the label. last of the submission


- score_last_children: the score of the submission, it may be a good feature, but may leaking the information of the future related to the label. last of the submission_children


- score_last_all_children: the score of the submission, it may be a good feature, but may leaking the information of the future related to the label. last of the submission_all_children


- length_of_selftext_avg: the length of the selftext of the submission avg of the submission


- length_of_selftext_avg_children: the length of the selftext of the submission avg of the submission_children


- length_of_selftext_avg_all_children: the length of the selftext of the submission avg of the submission_all_children


- length_of_selftext_std: the length of the selftext of the submission std of the submission


- length_of_selftext_std_children: the length of the selftext of the submission std of the submission_children


- length_of_selftext_std_all_children: the length of the selftext of the submission std of the submission_all_children


- length_of_selftext_max: the length of the selftext of the submission max of the submission


- length_of_selftext_max_children: the length of the selftext of the submission max of the submission_children


- length_of_selftext_max_all_children: the length of the selftext of the submission max of the submission_all_children


- length_of_selftext_min: the length of the selftext of the submission min of the submission


- length_of_selftext_min_children: the length of the selftext of the submission min of the submission_children


- length_of_selftext_min_all_children: the length of the selftext of the submission min of the submission_all_children


- length_of_selftext_first: the length of the selftext of the submission first of the submission


- length_of_selftext_first_children: the length of the selftext of the submission first of the submission_children


- length_of_selftext_first_all_children: the length of the selftext of the submission first of the submission_all_children


- length_of_selftext_last: the length of the selftext of the submission last of the submission


- length_of_selftext_last_children: the length of the selftext of the submission last of the submission_children


- length_of_selftext_last_all_children: the length of the selftext of the submission last of the submission_all_children


- length_of_title_avg: the length of the title of the submission avg of the submission


- length_of_title_avg_children: the length of the title of the submission avg of the submission_children


- length_of_title_avg_all_children: the length of the title of the submission avg of the submission_all_children


- length_of_title_std: the length of the title of the submission std of the submission


- length_of_title_std_children: the length of the title of the submission std of the submission_children


- length_of_title_std_all_children: the length of the title of the submission std of the submission_all_children


- length_of_title_max: the length of the title of the submission max of the submission


- length_of_title_max_children: the length of the title of the submission max of the submission_children


- length_of_title_max_all_children: the length of the title of the submission max of the submission_all_children


- length_of_title_min: the length of the title of the submission min of the submission


- length_of_title_min_children: the length of the title of the submission min of the submission_children


- length_of_title_min_all_children: the length of the title of the submission min of the submission_all_children


- length_of_title_first: the length of the title of the submission first of the submission


- length_of_title_first_children: the length of the title of the submission first of the submission_children


- length_of_title_first_all_children: the length of the title of the submission first of the submission_all_children


- length_of_title_last: the length of the title of the submission last of the submission


- length_of_title_last_children: the length of the title of the submission last of the submission_children


- length_of_title_last_all_children: the length of the title of the submission last of the submission_all_children


- send_replies_avg: send replies or not for the submission, it means the author will receive a notification when someone comments on the submission. avg of the submission


- send_replies_avg_children: send replies or not for the submission, it means the author will receive a notification when someone comments on the submission. avg of the submission_children


- send_replies_avg_all_children: send replies or not for the submission, it means the author will receive a notification when someone comments on the submission. avg of the submission_all_children


- send_replies_std: send replies or not for the submission, it means the author will receive a notification when someone comments on the submission. std of the submission


- send_replies_std_children: send replies or not for the submission, it means the author will receive a notification when someone comments on the submission. std of the submission_children


- send_replies_std_all_children: send replies or not for the submission, it means the author will receive a notification when someone comments on the submission. std of the submission_all_children


- send_replies_max: send replies or not for the submission, it means the author will receive a notification when someone comments on the submission. max of the submission


- send_replies_max_children: send replies or not for the submission, it means the author will receive a notification when someone comments on the submission. max of the submission_children


- send_replies_max_all_children: send replies or not for the submission, it means the author will receive a notification when someone comments on the submission. max of the submission_all_children


- send_replies_min: send replies or not for the submission, it means the author will receive a notification when someone comments on the submission. min of the submission


- send_replies_min_children: send replies or not for the submission, it means the author will receive a notification when someone comments on the submission. min of the submission_children


- send_replies_min_all_children: send replies or not for the submission, it means the author will receive a notification when someone comments on the submission. min of the submission_all_children


- send_replies_first: send replies or not for the submission, it means the author will receive a notification when someone comments on the submission. first of the submission


- send_replies_first_children: send replies or not for the submission, it means the author will receive a notification when someone comments on the submission. first of the submission_children


- send_replies_first_all_children: send replies or not for the submission, it means the author will receive a notification when someone comments on the submission. first of the submission_all_children


- send_replies_last: send replies or not for the submission, it means the author will receive a notification when someone comments on the submission. last of the submission


- send_replies_last_children: send replies or not for the submission, it means the author will receive a notification when someone comments on the submission. last of the submission_children


- send_replies_last_all_children: send replies or not for the submission, it means the author will receive a notification when someone comments on the submission. last of the submission_all_children


- spoiler_avg: if the submission is a spoiler or not, it may be a spoiler of a movie or a game avg of the submission


- spoiler_avg_children: if the submission is a spoiler or not, it may be a spoiler of a movie or a game avg of the submission_children


- spoiler_avg_all_children: if the submission is a spoiler or not, it may be a spoiler of a movie or a game avg of the submission_all_children


- spoiler_std: if the submission is a spoiler or not, it may be a spoiler of a movie or a game std of the submission


- spoiler_std_children: if the submission is a spoiler or not, it may be a spoiler of a movie or a game std of the submission_children


- spoiler_std_all_children: if the submission is a spoiler or not, it may be a spoiler of a movie or a game std of the submission_all_children


- spoiler_max: if the submission is a spoiler or not, it may be a spoiler of a movie or a game max of the submission


- spoiler_max_children: if the submission is a spoiler or not, it may be a spoiler of a movie or a game max of the submission_children


- spoiler_max_all_children: if the submission is a spoiler or not, it may be a spoiler of a movie or a game max of the submission_all_children


- spoiler_min: if the submission is a spoiler or not, it may be a spoiler of a movie or a game min of the submission


- spoiler_min_children: if the submission is a spoiler or not, it may be a spoiler of a movie or a game min of the submission_children


- spoiler_min_all_children: if the submission is a spoiler or not, it may be a spoiler of a movie or a game min of the submission_all_children


- spoiler_first: if the submission is a spoiler or not, it may be a spoiler of a movie or a game first of the submission


- spoiler_first_children: if the submission is a spoiler or not, it may be a spoiler of a movie or a game first of the submission_children


- spoiler_first_all_children: if the submission is a spoiler or not, it may be a spoiler of a movie or a game first of the submission_all_children


- spoiler_last: if the submission is a spoiler or not, it may be a spoiler of a movie or a game last of the submission


- spoiler_last_children: if the submission is a spoiler or not, it may be a spoiler of a movie or a game last of the submission_children


- spoiler_last_all_children: if the submission is a spoiler or not, it may be a spoiler of a movie or a game last of the submission_all_children


- stickied_avg: if the submission is stickied or not, it may be a post that the moderator wants to highlight avg of the submission


- stickied_avg_children: if the submission is stickied or not, it may be a post that the moderator wants to highlight avg of the submission_children


- stickied_avg_all_children: if the submission is stickied or not, it may be a post that the moderator wants to highlight avg of the submission_all_children


- stickied_std: if the submission is stickied or not, it may be a post that the moderator wants to highlight std of the submission


- stickied_std_children: if the submission is stickied or not, it may be a post that the moderator wants to highlight std of the submission_children


- stickied_std_all_children: if the submission is stickied or not, it may be a post that the moderator wants to highlight std of the submission_all_children


- stickied_max: if the submission is stickied or not, it may be a post that the moderator wants to highlight max of the submission


- stickied_max_children: if the submission is stickied or not, it may be a post that the moderator wants to highlight max of the submission_children


- stickied_max_all_children: if the submission is stickied or not, it may be a post that the moderator wants to highlight max of the submission_all_children


- stickied_min: if the submission is stickied or not, it may be a post that the moderator wants to highlight min of the submission


- stickied_min_children: if the submission is stickied or not, it may be a post that the moderator wants to highlight min of the submission_children


- stickied_min_all_children: if the submission is stickied or not, it may be a post that the moderator wants to highlight min of the submission_all_children


- stickied_first: if the submission is stickied or not, it may be a post that the moderator wants to highlight first of the submission


- stickied_first_children: if the submission is stickied or not, it may be a post that the moderator wants to highlight first of the submission_children


- stickied_first_all_children: if the submission is stickied or not, it may be a post that the moderator wants to highlight first of the submission_all_children


- stickied_last: if the submission is stickied or not, it may be a post that the moderator wants to highlight last of the submission


- stickied_last_children: if the submission is stickied or not, it may be a post that the moderator wants to highlight last of the submission_children


- stickied_last_all_children: if the submission is stickied or not, it may be a post that the moderator wants to highlight last of the submission_all_children


- subreddit_subscribers_avg: the number of subscribers of the subreddit of the submission avg of the submission


- subreddit_subscribers_avg_children: the number of subscribers of the subreddit of the submission avg of the submission_children


- subreddit_subscribers_avg_all_children: the number of subscribers of the subreddit of the submission avg of the submission_all_children


- subreddit_subscribers_std: the number of subscribers of the subreddit of the submission std of the submission


- subreddit_subscribers_std_children: the number of subscribers of the subreddit of the submission std of the submission_children


- subreddit_subscribers_std_all_children: the number of subscribers of the subreddit of the submission std of the submission_all_children


- subreddit_subscribers_max: the number of subscribers of the subreddit of the submission max of the submission


- subreddit_subscribers_max_children: the number of subscribers of the subreddit of the submission max of the submission_children


- subreddit_subscribers_max_all_children: the number of subscribers of the subreddit of the submission max of the submission_all_children


- subreddit_subscribers_min: the number of subscribers of the subreddit of the submission min of the submission


- subreddit_subscribers_min_children: the number of subscribers of the subreddit of the submission min of the submission_children


- subreddit_subscribers_min_all_children: the number of subscribers of the subreddit of the submission min of the submission_all_children


- subreddit_subscribers_first: the number of subscribers of the subreddit of the submission first of the submission


- subreddit_subscribers_first_children: the number of subscribers of the subreddit of the submission first of the submission_children


- subreddit_subscribers_first_all_children: the number of subscribers of the subreddit of the submission first of the submission_all_children


- subreddit_subscribers_last: the number of subscribers of the subreddit of the submission last of the submission


- subreddit_subscribers_last_children: the number of subscribers of the subreddit of the submission last of the submission_children


- subreddit_subscribers_last_all_children: the number of subscribers of the subreddit of the submission last of the submission_all_children


- suggested_sort_avg: the suggested sort of the submission, mostly it is None avg of the submission


- suggested_sort_avg_children: the suggested sort of the submission, mostly it is None avg of the submission_children


- suggested_sort_avg_all_children: the suggested sort of the submission, mostly it is None avg of the submission_all_children


- suggested_sort_std: the suggested sort of the submission, mostly it is None std of the submission


- suggested_sort_std_children: the suggested sort of the submission, mostly it is None std of the submission_children


- suggested_sort_std_all_children: the suggested sort of the submission, mostly it is None std of the submission_all_children


- suggested_sort_max: the suggested sort of the submission, mostly it is None max of the submission


- suggested_sort_max_children: the suggested sort of the submission, mostly it is None max of the submission_children


- suggested_sort_max_all_children: the suggested sort of the submission, mostly it is None max of the submission_all_children


- suggested_sort_min: the suggested sort of the submission, mostly it is None min of the submission


- suggested_sort_min_children: the suggested sort of the submission, mostly it is None min of the submission_children


- suggested_sort_min_all_children: the suggested sort of the submission, mostly it is None min of the submission_all_children


- suggested_sort_first: the suggested sort of the submission, mostly it is None first of the submission


- suggested_sort_first_children: the suggested sort of the submission, mostly it is None first of the submission_children


- suggested_sort_first_all_children: the suggested sort of the submission, mostly it is None first of the submission_all_children


- suggested_sort_last: the suggested sort of the submission, mostly it is None last of the submission


- suggested_sort_last_children: the suggested sort of the submission, mostly it is None last of the submission_children


- suggested_sort_last_all_children: the suggested sort of the submission, mostly it is None last of the submission_all_children


- subreddit_id_avg: the id of the subreddit of the submission avg of the submission


- subreddit_id_avg_children: the id of the subreddit of the submission avg of the submission_children


- subreddit_id_avg_all_children: the id of the subreddit of the submission avg of the submission_all_children


- subreddit_id_std: the id of the subreddit of the submission std of the submission


- subreddit_id_std_children: the id of the subreddit of the submission std of the submission_children


- subreddit_id_std_all_children: the id of the subreddit of the submission std of the submission_all_children


- subreddit_id_max: the id of the subreddit of the submission max of the submission


- subreddit_id_max_children: the id of the subreddit of the submission max of the submission_children


- subreddit_id_max_all_children: the id of the subreddit of the submission max of the submission_all_children


- subreddit_id_min: the id of the subreddit of the submission min of the submission


- subreddit_id_min_children: the id of the subreddit of the submission min of the submission_children


- subreddit_id_min_all_children: the id of the subreddit of the submission min of the submission_all_children


- subreddit_id_first: the id of the subreddit of the submission first of the submission


- subreddit_id_first_children: the id of the subreddit of the submission first of the submission_children


- subreddit_id_first_all_children: the id of the subreddit of the submission first of the submission_all_children


- subreddit_id_last: the id of the subreddit of the submission last of the submission


- subreddit_id_last_children: the id of the subreddit of the submission last of the submission_children


- subreddit_id_last_all_children: the id of the subreddit of the submission last of the submission_all_children


- subreddit_type_avg: the type of the subreddit of the submission, mostly it is None avg of the submission


- subreddit_type_avg_children: the type of the subreddit of the submission, mostly it is None avg of the submission_children


- subreddit_type_avg_all_children: the type of the subreddit of the submission, mostly it is None avg of the submission_all_children


- subreddit_type_std: the type of the subreddit of the submission, mostly it is None std of the submission


- subreddit_type_std_children: the type of the subreddit of the submission, mostly it is None std of the submission_children


- subreddit_type_std_all_children: the type of the subreddit of the submission, mostly it is None std of the submission_all_children


- subreddit_type_max: the type of the subreddit of the submission, mostly it is None max of the submission


- subreddit_type_max_children: the type of the subreddit of the submission, mostly it is None max of the submission_children


- subreddit_type_max_all_children: the type of the subreddit of the submission, mostly it is None max of the submission_all_children


- subreddit_type_min: the type of the subreddit of the submission, mostly it is None min of the submission


- subreddit_type_min_children: the type of the subreddit of the submission, mostly it is None min of the submission_children


- subreddit_type_min_all_children: the type of the subreddit of the submission, mostly it is None min of the submission_all_children


- subreddit_type_first: the type of the subreddit of the submission, mostly it is None first of the submission


- subreddit_type_first_children: the type of the subreddit of the submission, mostly it is None first of the submission_children


- subreddit_type_first_all_children: the type of the subreddit of the submission, mostly it is None first of the submission_all_children


- subreddit_type_last: the type of the subreddit of the submission, mostly it is None last of the submission


- subreddit_type_last_children: the type of the subreddit of the submission, mostly it is None last of the submission_children


- subreddit_type_last_all_children: the type of the subreddit of the submission, mostly it is None last of the submission_all_children


- thumbnail_avg: the thumbnail of the submission, mostly it is default avg of the submission


- thumbnail_avg_children: the thumbnail of the submission, mostly it is default avg of the submission_children


- thumbnail_avg_all_children: the thumbnail of the submission, mostly it is default avg of the submission_all_children


- thumbnail_std: the thumbnail of the submission, mostly it is default std of the submission


- thumbnail_std_children: the thumbnail of the submission, mostly it is default std of the submission_children


- thumbnail_std_all_children: the thumbnail of the submission, mostly it is default std of the submission_all_children


- thumbnail_max: the thumbnail of the submission, mostly it is default max of the submission


- thumbnail_max_children: the thumbnail of the submission, mostly it is default max of the submission_children


- thumbnail_max_all_children: the thumbnail of the submission, mostly it is default max of the submission_all_children


- thumbnail_min: the thumbnail of the submission, mostly it is default min of the submission


- thumbnail_min_children: the thumbnail of the submission, mostly it is default min of the submission_children


- thumbnail_min_all_children: the thumbnail of the submission, mostly it is default min of the submission_all_children


- thumbnail_first: the thumbnail of the submission, mostly it is default first of the submission


- thumbnail_first_children: the thumbnail of the submission, mostly it is default first of the submission_children


- thumbnail_first_all_children: the thumbnail of the submission, mostly it is default first of the submission_all_children


- thumbnail_last: the thumbnail of the submission, mostly it is default last of the submission


- thumbnail_last_children: the thumbnail of the submission, mostly it is default last of the submission_children


- thumbnail_last_all_children: the thumbnail of the submission, mostly it is default last of the submission_all_children


- top_awarded_type_avg: the top awarded type of the submission, mostly it is None avg of the submission


- top_awarded_type_avg_children: the top awarded type of the submission, mostly it is None avg of the submission_children


- top_awarded_type_avg_all_children: the top awarded type of the submission, mostly it is None avg of the submission_all_children


- top_awarded_type_std: the top awarded type of the submission, mostly it is None std of the submission


- top_awarded_type_std_children: the top awarded type of the submission, mostly it is None std of the submission_children


- top_awarded_type_std_all_children: the top awarded type of the submission, mostly it is None std of the submission_all_children


- top_awarded_type_max: the top awarded type of the submission, mostly it is None max of the submission


- top_awarded_type_max_children: the top awarded type of the submission, mostly it is None max of the submission_children


- top_awarded_type_max_all_children: the top awarded type of the submission, mostly it is None max of the submission_all_children


- top_awarded_type_min: the top awarded type of the submission, mostly it is None min of the submission


- top_awarded_type_min_children: the top awarded type of the submission, mostly it is None min of the submission_children


- top_awarded_type_min_all_children: the top awarded type of the submission, mostly it is None min of the submission_all_children


- top_awarded_type_first: the top awarded type of the submission, mostly it is None first of the submission


- top_awarded_type_first_children: the top awarded type of the submission, mostly it is None first of the submission_children


- top_awarded_type_first_all_children: the top awarded type of the submission, mostly it is None first of the submission_all_children


- top_awarded_type_last: the top awarded type of the submission, mostly it is None last of the submission


- top_awarded_type_last_children: the top awarded type of the submission, mostly it is None last of the submission_children


- top_awarded_type_last_all_children: the top awarded type of the submission, mostly it is None last of the submission_all_children


- total_awards_received_avg: the total awards received of the submission, it may be a good feature, but may leaking the information of the future related to the label. avg of the submission


- total_awards_received_avg_children: the total awards received of the submission, it may be a good feature, but may leaking the information of the future related to the label. avg of the submission_children


- total_awards_received_avg_all_children: the total awards received of the submission, it may be a good feature, but may leaking the information of the future related to the label. avg of the submission_all_children


- total_awards_received_std: the total awards received of the submission, it may be a good feature, but may leaking the information of the future related to the label. std of the submission


- total_awards_received_std_children: the total awards received of the submission, it may be a good feature, but may leaking the information of the future related to the label. std of the submission_children


- total_awards_received_std_all_children: the total awards received of the submission, it may be a good feature, but may leaking the information of the future related to the label. std of the submission_all_children


- total_awards_received_max: the total awards received of the submission, it may be a good feature, but may leaking the information of the future related to the label. max of the submission


- total_awards_received_max_children: the total awards received of the submission, it may be a good feature, but may leaking the information of the future related to the label. max of the submission_children


- total_awards_received_max_all_children: the total awards received of the submission, it may be a good feature, but may leaking the information of the future related to the label. max of the submission_all_children


- total_awards_received_min: the total awards received of the submission, it may be a good feature, but may leaking the information of the future related to the label. min of the submission


- total_awards_received_min_children: the total awards received of the submission, it may be a good feature, but may leaking the information of the future related to the label. min of the submission_children


- total_awards_received_min_all_children: the total awards received of the submission, it may be a good feature, but may leaking the information of the future related to the label. min of the submission_all_children


- total_awards_received_first: the total awards received of the submission, it may be a good feature, but may leaking the information of the future related to the label. first of the submission


- total_awards_received_first_children: the total awards received of the submission, it may be a good feature, but may leaking the information of the future related to the label. first of the submission_children


- total_awards_received_first_all_children: the total awards received of the submission, it may be a good feature, but may leaking the information of the future related to the label. first of the submission_all_children


- total_awards_received_last: the total awards received of the submission, it may be a good feature, but may leaking the information of the future related to the label. last of the submission


- total_awards_received_last_children: the total awards received of the submission, it may be a good feature, but may leaking the information of the future related to the label. last of the submission_children


- total_awards_received_last_all_children: the total awards received of the submission, it may be a good feature, but may leaking the information of the future related to the label. last of the submission_all_children


- treatment_tags_avg: the treatment tags of the submission, mostly it is None avg of the submission


- treatment_tags_avg_children: the treatment tags of the submission, mostly it is None avg of the submission_children


- treatment_tags_avg_all_children: the treatment tags of the submission, mostly it is None avg of the submission_all_children


- treatment_tags_std: the treatment tags of the submission, mostly it is None std of the submission


- treatment_tags_std_children: the treatment tags of the submission, mostly it is None std of the submission_children


- treatment_tags_std_all_children: the treatment tags of the submission, mostly it is None std of the submission_all_children


- treatment_tags_max: the treatment tags of the submission, mostly it is None max of the submission


- treatment_tags_max_children: the treatment tags of the submission, mostly it is None max of the submission_children


- treatment_tags_max_all_children: the treatment tags of the submission, mostly it is None max of the submission_all_children


- treatment_tags_min: the treatment tags of the submission, mostly it is None min of the submission


- treatment_tags_min_children: the treatment tags of the submission, mostly it is None min of the submission_children


- treatment_tags_min_all_children: the treatment tags of the submission, mostly it is None min of the submission_all_children


- treatment_tags_first: the treatment tags of the submission, mostly it is None first of the submission


- treatment_tags_first_children: the treatment tags of the submission, mostly it is None first of the submission_children


- treatment_tags_first_all_children: the treatment tags of the submission, mostly it is None first of the submission_all_children


- treatment_tags_last: the treatment tags of the submission, mostly it is None last of the submission


- treatment_tags_last_children: the treatment tags of the submission, mostly it is None last of the submission_children


- treatment_tags_last_all_children: the treatment tags of the submission, mostly it is None last of the submission_all_children


- upvote_ratio_avg: the upvote ratio of the submission, it may be a good feature, but may leaking the information of the future related to the label. avg of the submission


- upvote_ratio_avg_children: the upvote ratio of the submission, it may be a good feature, but may leaking the information of the future related to the label. avg of the submission_children


- upvote_ratio_avg_all_children: the upvote ratio of the submission, it may be a good feature, but may leaking the information of the future related to the label. avg of the submission_all_children


- upvote_ratio_std: the upvote ratio of the submission, it may be a good feature, but may leaking the information of the future related to the label. std of the submission


- upvote_ratio_std_children: the upvote ratio of the submission, it may be a good feature, but may leaking the information of the future related to the label. std of the submission_children


- upvote_ratio_std_all_children: the upvote ratio of the submission, it may be a good feature, but may leaking the information of the future related to the label. std of the submission_all_children


- upvote_ratio_max: the upvote ratio of the submission, it may be a good feature, but may leaking the information of the future related to the label. max of the submission


- upvote_ratio_max_children: the upvote ratio of the submission, it may be a good feature, but may leaking the information of the future related to the label. max of the submission_children


- upvote_ratio_max_all_children: the upvote ratio of the submission, it may be a good feature, but may leaking the information of the future related to the label. max of the submission_all_children


- upvote_ratio_min: the upvote ratio of the submission, it may be a good feature, but may leaking the information of the future related to the label. min of the submission


- upvote_ratio_min_children: the upvote ratio of the submission, it may be a good feature, but may leaking the information of the future related to the label. min of the submission_children


- upvote_ratio_min_all_children: the upvote ratio of the submission, it may be a good feature, but may leaking the information of the future related to the label. min of the submission_all_children


- upvote_ratio_first: the upvote ratio of the submission, it may be a good feature, but may leaking the information of the future related to the label. first of the submission


- upvote_ratio_first_children: the upvote ratio of the submission, it may be a good feature, but may leaking the information of the future related to the label. first of the submission_children


- upvote_ratio_first_all_children: the upvote ratio of the submission, it may be a good feature, but may leaking the information of the future related to the label. first of the submission_all_children


- upvote_ratio_last: the upvote ratio of the submission, it may be a good feature, but may leaking the information of the future related to the label. last of the submission


- upvote_ratio_last_children: the upvote ratio of the submission, it may be a good feature, but may leaking the information of the future related to the label. last of the submission_children


- upvote_ratio_last_all_children: the upvote ratio of the submission, it may be a good feature, but may leaking the information of the future related to the label. last of the submission_all_children


- whitelist_status_avg: the whitelist status of the submission, mostly it is None avg of the submission


- whitelist_status_avg_children: the whitelist status of the submission, mostly it is None avg of the submission_children


- whitelist_status_avg_all_children: the whitelist status of the submission, mostly it is None avg of the submission_all_children


- whitelist_status_std: the whitelist status of the submission, mostly it is None std of the submission


- whitelist_status_std_children: the whitelist status of the submission, mostly it is None std of the submission_children


- whitelist_status_std_all_children: the whitelist status of the submission, mostly it is None std of the submission_all_children


- whitelist_status_max: the whitelist status of the submission, mostly it is None max of the submission


- whitelist_status_max_children: the whitelist status of the submission, mostly it is None max of the submission_children


- whitelist_status_max_all_children: the whitelist status of the submission, mostly it is None max of the submission_all_children


- whitelist_status_min: the whitelist status of the submission, mostly it is None min of the submission


- whitelist_status_min_children: the whitelist status of the submission, mostly it is None min of the submission_children


- whitelist_status_min_all_children: the whitelist status of the submission, mostly it is None min of the submission_all_children


- whitelist_status_first: the whitelist status of the submission, mostly it is None first of the submission


- whitelist_status_first_children: the whitelist status of the submission, mostly it is None first of the submission_children


- whitelist_status_first_all_children: the whitelist status of the submission, mostly it is None first of the submission_all_children


- whitelist_status_last: the whitelist status of the submission, mostly it is None last of the submission


- whitelist_status_last_children: the whitelist status of the submission, mostly it is None last of the submission_children


- whitelist_status_last_all_children: the whitelist status of the submission, mostly it is None last of the submission_all_children


- wls_avg: the wls of the submission, mostly it is 6 avg of the submission


- wls_avg_children: the wls of the submission, mostly it is 6 avg of the submission_children


- wls_avg_all_children: the wls of the submission, mostly it is 6 avg of the submission_all_children


- wls_std: the wls of the submission, mostly it is 6 std of the submission


- wls_std_children: the wls of the submission, mostly it is 6 std of the submission_children


- wls_std_all_children: the wls of the submission, mostly it is 6 std of the submission_all_children


- wls_max: the wls of the submission, mostly it is 6 max of the submission


- wls_max_children: the wls of the submission, mostly it is 6 max of the submission_children


- wls_max_all_children: the wls of the submission, mostly it is 6 max of the submission_all_children


- wls_min: the wls of the submission, mostly it is 6 min of the submission


- wls_min_children: the wls of the submission, mostly it is 6 min of the submission_children


- wls_min_all_children: the wls of the submission, mostly it is 6 min of the submission_all_children


- wls_first: the wls of the submission, mostly it is 6 first of the submission


- wls_first_children: the wls of the submission, mostly it is 6 first of the submission_children


- wls_first_all_children: the wls of the submission, mostly it is 6 first of the submission_all_children


- wls_last: the wls of the submission, mostly it is 6 last of the submission


- wls_last_children: the wls of the submission, mostly it is 6 last of the submission_children


- wls_last_all_children: the wls of the submission, mostly it is 6 last of the submission_all_children


- num_of_all_comments_avg: the number of all comments of the submission in the observation period, including the comments of the comments avg of the submission


- num_of_all_comments_avg_children: the number of all comments of the submission in the observation period, including the comments of the comments avg of the submission_children


- num_of_all_comments_avg_all_children: the number of all comments of the submission in the observation period, including the comments of the comments avg of the submission_all_children


- num_of_all_comments_std: the number of all comments of the submission in the observation period, including the comments of the comments std of the submission


- num_of_all_comments_std_children: the number of all comments of the submission in the observation period, including the comments of the comments std of the submission_children


- num_of_all_comments_std_all_children: the number of all comments of the submission in the observation period, including the comments of the comments std of the submission_all_children


- num_of_all_comments_max: the number of all comments of the submission in the observation period, including the comments of the comments max of the submission


- num_of_all_comments_max_children: the number of all comments of the submission in the observation period, including the comments of the comments max of the submission_children


- num_of_all_comments_max_all_children: the number of all comments of the submission in the observation period, including the comments of the comments max of the submission_all_children


- num_of_all_comments_min: the number of all comments of the submission in the observation period, including the comments of the comments min of the submission


- num_of_all_comments_min_children: the number of all comments of the submission in the observation period, including the comments of the comments min of the submission_children


- num_of_all_comments_min_all_children: the number of all comments of the submission in the observation period, including the comments of the comments min of the submission_all_children


- num_of_all_comments_first: the number of all comments of the submission in the observation period, including the comments of the comments first of the submission


- num_of_all_comments_first_children: the number of all comments of the submission in the observation period, including the comments of the comments first of the submission_children


- num_of_all_comments_first_all_children: the number of all comments of the submission in the observation period, including the comments of the comments first of the submission_all_children


- num_of_all_comments_last: the number of all comments of the submission in the observation period, including the comments of the comments last of the submission


- num_of_all_comments_last_children: the number of all comments of the submission in the observation period, including the comments of the comments last of the submission_children


- num_of_all_comments_last_all_children: the number of all comments of the submission in the observation period, including the comments of the comments last of the submission_all_children


- author_created_utc_avg: the created time of the author avg of the submission


- author_created_utc_avg_children: the created time of the author avg of the submission_children


- author_created_utc_avg_all_children: the created time of the author avg of the submission_all_children


- author_created_utc_std: the created time of the author std of the submission


- author_created_utc_std_children: the created time of the author std of the submission_children


- author_created_utc_std_all_children: the created time of the author std of the submission_all_children


- author_created_utc_max: the created time of the author max of the submission


- author_created_utc_max_children: the created time of the author max of the submission_children


- author_created_utc_max_all_children: the created time of the author max of the submission_all_children


- author_created_utc_min: the created time of the author min of the submission


- author_created_utc_min_children: the created time of the author min of the submission_children


- author_created_utc_min_all_children: the created time of the author min of the submission_all_children


- author_created_utc_first: the created time of the author first of the submission


- author_created_utc_first_children: the created time of the author first of the submission_children


- author_created_utc_first_all_children: the created time of the author first of the submission_all_children


- author_created_utc_last: the created time of the author last of the submission


- author_created_utc_last_children: the created time of the author last of the submission_children


- author_created_utc_last_all_children: the created time of the author last of the submission_all_children


- author_premium_avg: the author is premium or not avg of the submission


- author_premium_avg_children: the author is premium or not avg of the submission_children


- author_premium_avg_all_children: the author is premium or not avg of the submission_all_children


- author_premium_std: the author is premium or not std of the submission


- author_premium_std_children: the author is premium or not std of the submission_children


- author_premium_std_all_children: the author is premium or not std of the submission_all_children


- author_premium_max: the author is premium or not max of the submission


- author_premium_max_children: the author is premium or not max of the submission_children


- author_premium_max_all_children: the author is premium or not max of the submission_all_children


- author_premium_min: the author is premium or not min of the submission


- author_premium_min_children: the author is premium or not min of the submission_children


- author_premium_min_all_children: the author is premium or not min of the submission_all_children


- author_premium_first: the author is premium or not first of the submission


- author_premium_first_children: the author is premium or not first of the submission_children


- author_premium_first_all_children: the author is premium or not first of the submission_all_children


- author_premium_last: the author is premium or not last of the submission


- author_premium_last_children: the author is premium or not last of the submission_children


- author_premium_last_all_children: the author is premium or not last of the submission_all_children

### post


- is_created_from_ads_ui_avg: avg of the post for the feature is_created_from_ads_ui


- is_created_from_ads_ui_avg_parent: avg of the post_parent for the feature is_created_from_ads_ui


- is_created_from_ads_ui_avg_children: avg of the post_children for the feature is_created_from_ads_ui


- is_created_from_ads_ui_avg_all_children: avg of the post_all_children for the feature is_created_from_ads_ui


- is_created_from_ads_ui_std: std of the post for the feature is_created_from_ads_ui


- is_created_from_ads_ui_std_parent: std of the post_parent for the feature is_created_from_ads_ui


- is_created_from_ads_ui_std_children: std of the post_children for the feature is_created_from_ads_ui


- is_created_from_ads_ui_std_all_children: std of the post_all_children for the feature is_created_from_ads_ui


- is_created_from_ads_ui_max: max of the post for the feature is_created_from_ads_ui


- is_created_from_ads_ui_max_parent: max of the post_parent for the feature is_created_from_ads_ui


- is_created_from_ads_ui_max_children: max of the post_children for the feature is_created_from_ads_ui


- is_created_from_ads_ui_max_all_children: max of the post_all_children for the feature is_created_from_ads_ui


- is_created_from_ads_ui_min: min of the post for the feature is_created_from_ads_ui


- is_created_from_ads_ui_min_parent: min of the post_parent for the feature is_created_from_ads_ui


- is_created_from_ads_ui_min_children: min of the post_children for the feature is_created_from_ads_ui


- is_created_from_ads_ui_min_all_children: min of the post_all_children for the feature is_created_from_ads_ui


- is_created_from_ads_ui_first: first of the post for the feature is_created_from_ads_ui


- is_created_from_ads_ui_first_parent: first of the post_parent for the feature is_created_from_ads_ui


- is_created_from_ads_ui_first_children: first of the post_children for the feature is_created_from_ads_ui


- is_created_from_ads_ui_first_all_children: first of the post_all_children for the feature is_created_from_ads_ui


- is_created_from_ads_ui_last: last of the post for the feature is_created_from_ads_ui


- is_created_from_ads_ui_last_parent: last of the post_parent for the feature is_created_from_ads_ui


- is_created_from_ads_ui_last_children: last of the post_children for the feature is_created_from_ads_ui


- is_created_from_ads_ui_last_all_children: last of the post_all_children for the feature is_created_from_ads_ui


- send_replies_avg: avg of the post for the feature send_replies


- send_replies_avg_parent: avg of the post_parent for the feature send_replies


- send_replies_avg_children: avg of the post_children for the feature send_replies


- send_replies_avg_all_children: avg of the post_all_children for the feature send_replies


- send_replies_std: std of the post for the feature send_replies


- send_replies_std_parent: std of the post_parent for the feature send_replies


- send_replies_std_children: std of the post_children for the feature send_replies


- send_replies_std_all_children: std of the post_all_children for the feature send_replies


- send_replies_max: max of the post for the feature send_replies


- send_replies_max_parent: max of the post_parent for the feature send_replies


- send_replies_max_children: max of the post_children for the feature send_replies


- send_replies_max_all_children: max of the post_all_children for the feature send_replies


- send_replies_min: min of the post for the feature send_replies


- send_replies_min_parent: min of the post_parent for the feature send_replies


- send_replies_min_children: min of the post_children for the feature send_replies


- send_replies_min_all_children: min of the post_all_children for the feature send_replies


- send_replies_first: first of the post for the feature send_replies


- send_replies_first_parent: first of the post_parent for the feature send_replies


- send_replies_first_children: first of the post_children for the feature send_replies


- send_replies_first_all_children: first of the post_all_children for the feature send_replies


- send_replies_last: last of the post for the feature send_replies


- send_replies_last_parent: last of the post_parent for the feature send_replies


- send_replies_last_children: last of the post_children for the feature send_replies


- send_replies_last_all_children: last of the post_all_children for the feature send_replies


- contest_mode_avg: avg of the post for the feature contest_mode


- contest_mode_avg_parent: avg of the post_parent for the feature contest_mode


- contest_mode_avg_children: avg of the post_children for the feature contest_mode


- contest_mode_avg_all_children: avg of the post_all_children for the feature contest_mode


- contest_mode_std: std of the post for the feature contest_mode


- contest_mode_std_parent: std of the post_parent for the feature contest_mode


- contest_mode_std_children: std of the post_children for the feature contest_mode


- contest_mode_std_all_children: std of the post_all_children for the feature contest_mode


- contest_mode_max: max of the post for the feature contest_mode


- contest_mode_max_parent: max of the post_parent for the feature contest_mode


- contest_mode_max_children: max of the post_children for the feature contest_mode


- contest_mode_max_all_children: max of the post_all_children for the feature contest_mode


- contest_mode_min: min of the post for the feature contest_mode


- contest_mode_min_parent: min of the post_parent for the feature contest_mode


- contest_mode_min_children: min of the post_children for the feature contest_mode


- contest_mode_min_all_children: min of the post_all_children for the feature contest_mode


- contest_mode_first: first of the post for the feature contest_mode


- contest_mode_first_parent: first of the post_parent for the feature contest_mode


- contest_mode_first_children: first of the post_children for the feature contest_mode


- contest_mode_first_all_children: first of the post_all_children for the feature contest_mode


- contest_mode_last: last of the post for the feature contest_mode


- contest_mode_last_parent: last of the post_parent for the feature contest_mode


- contest_mode_last_children: last of the post_children for the feature contest_mode


- contest_mode_last_all_children: last of the post_all_children for the feature contest_mode


- link_flair_type_avg: avg of the post for the feature link_flair_type


- link_flair_type_avg_parent: avg of the post_parent for the feature link_flair_type


- link_flair_type_avg_children: avg of the post_children for the feature link_flair_type


- link_flair_type_avg_all_children: avg of the post_all_children for the feature link_flair_type


- link_flair_type_std: std of the post for the feature link_flair_type


- link_flair_type_std_parent: std of the post_parent for the feature link_flair_type


- link_flair_type_std_children: std of the post_children for the feature link_flair_type


- link_flair_type_std_all_children: std of the post_all_children for the feature link_flair_type


- link_flair_type_max: max of the post for the feature link_flair_type


- link_flair_type_max_parent: max of the post_parent for the feature link_flair_type


- link_flair_type_max_children: max of the post_children for the feature link_flair_type


- link_flair_type_max_all_children: max of the post_all_children for the feature link_flair_type


- link_flair_type_min: min of the post for the feature link_flair_type


- link_flair_type_min_parent: min of the post_parent for the feature link_flair_type


- link_flair_type_min_children: min of the post_children for the feature link_flair_type


- link_flair_type_min_all_children: min of the post_all_children for the feature link_flair_type


- link_flair_type_first: first of the post for the feature link_flair_type


- link_flair_type_first_parent: first of the post_parent for the feature link_flair_type


- link_flair_type_first_children: first of the post_children for the feature link_flair_type


- link_flair_type_first_all_children: first of the post_all_children for the feature link_flair_type


- link_flair_type_last: last of the post for the feature link_flair_type


- link_flair_type_last_parent: last of the post_parent for the feature link_flair_type


- link_flair_type_last_children: last of the post_children for the feature link_flair_type


- link_flair_type_last_all_children: last of the post_all_children for the feature link_flair_type


- is_reddit_media_domain_avg: avg of the post for the feature is_reddit_media_domain


- is_reddit_media_domain_avg_parent: avg of the post_parent for the feature is_reddit_media_domain


- is_reddit_media_domain_avg_children: avg of the post_children for the feature is_reddit_media_domain


- is_reddit_media_domain_avg_all_children: avg of the post_all_children for the feature is_reddit_media_domain


- is_reddit_media_domain_std: std of the post for the feature is_reddit_media_domain


- is_reddit_media_domain_std_parent: std of the post_parent for the feature is_reddit_media_domain


- is_reddit_media_domain_std_children: std of the post_children for the feature is_reddit_media_domain


- is_reddit_media_domain_std_all_children: std of the post_all_children for the feature is_reddit_media_domain


- is_reddit_media_domain_max: max of the post for the feature is_reddit_media_domain


- is_reddit_media_domain_max_parent: max of the post_parent for the feature is_reddit_media_domain


- is_reddit_media_domain_max_children: max of the post_children for the feature is_reddit_media_domain


- is_reddit_media_domain_max_all_children: max of the post_all_children for the feature is_reddit_media_domain


- is_reddit_media_domain_min: min of the post for the feature is_reddit_media_domain


- is_reddit_media_domain_min_parent: min of the post_parent for the feature is_reddit_media_domain


- is_reddit_media_domain_min_children: min of the post_children for the feature is_reddit_media_domain


- is_reddit_media_domain_min_all_children: min of the post_all_children for the feature is_reddit_media_domain


- is_reddit_media_domain_first: first of the post for the feature is_reddit_media_domain


- is_reddit_media_domain_first_parent: first of the post_parent for the feature is_reddit_media_domain


- is_reddit_media_domain_first_children: first of the post_children for the feature is_reddit_media_domain


- is_reddit_media_domain_first_all_children: first of the post_all_children for the feature is_reddit_media_domain


- is_reddit_media_domain_last: last of the post for the feature is_reddit_media_domain


- is_reddit_media_domain_last_parent: last of the post_parent for the feature is_reddit_media_domain


- is_reddit_media_domain_last_children: last of the post_children for the feature is_reddit_media_domain


- is_reddit_media_domain_last_all_children: last of the post_all_children for the feature is_reddit_media_domain


- no_follow_avg: avg of the post for the feature no_follow


- no_follow_avg_parent: avg of the post_parent for the feature no_follow


- no_follow_avg_children: avg of the post_children for the feature no_follow


- no_follow_avg_all_children: avg of the post_all_children for the feature no_follow


- no_follow_std: std of the post for the feature no_follow


- no_follow_std_parent: std of the post_parent for the feature no_follow


- no_follow_std_children: std of the post_children for the feature no_follow


- no_follow_std_all_children: std of the post_all_children for the feature no_follow


- no_follow_max: max of the post for the feature no_follow


- no_follow_max_parent: max of the post_parent for the feature no_follow


- no_follow_max_children: max of the post_children for the feature no_follow


- no_follow_max_all_children: max of the post_all_children for the feature no_follow


- no_follow_min: min of the post for the feature no_follow


- no_follow_min_parent: min of the post_parent for the feature no_follow


- no_follow_min_children: min of the post_children for the feature no_follow


- no_follow_min_all_children: min of the post_all_children for the feature no_follow


- no_follow_first: first of the post for the feature no_follow


- no_follow_first_parent: first of the post_parent for the feature no_follow


- no_follow_first_children: first of the post_children for the feature no_follow


- no_follow_first_all_children: first of the post_all_children for the feature no_follow


- no_follow_last: last of the post for the feature no_follow


- no_follow_last_parent: last of the post_parent for the feature no_follow


- no_follow_last_children: last of the post_children for the feature no_follow


- no_follow_last_all_children: last of the post_all_children for the feature no_follow


- edited_avg: avg of the post for the feature edited


- edited_avg_parent: avg of the post_parent for the feature edited


- edited_avg_children: avg of the post_children for the feature edited


- edited_avg_all_children: avg of the post_all_children for the feature edited


- edited_std: std of the post for the feature edited


- edited_std_parent: std of the post_parent for the feature edited


- edited_std_children: std of the post_children for the feature edited


- edited_std_all_children: std of the post_all_children for the feature edited


- edited_max: max of the post for the feature edited


- edited_max_parent: max of the post_parent for the feature edited


- edited_max_children: max of the post_children for the feature edited


- edited_max_all_children: max of the post_all_children for the feature edited


- edited_min: min of the post for the feature edited


- edited_min_parent: min of the post_parent for the feature edited


- edited_min_children: min of the post_children for the feature edited


- edited_min_all_children: min of the post_all_children for the feature edited


- edited_first: first of the post for the feature edited


- edited_first_parent: first of the post_parent for the feature edited


- edited_first_children: first of the post_children for the feature edited


- edited_first_all_children: first of the post_all_children for the feature edited


- edited_last: last of the post for the feature edited


- edited_last_parent: last of the post_parent for the feature edited


- edited_last_children: last of the post_children for the feature edited


- edited_last_all_children: last of the post_all_children for the feature edited


- num_of_comments_avg: avg of the post for the feature num_of_comments


- num_of_comments_avg_parent: avg of the post_parent for the feature num_of_comments


- num_of_comments_avg_children: avg of the post_children for the feature num_of_comments


- num_of_comments_avg_all_children: avg of the post_all_children for the feature num_of_comments


- num_of_comments_std: std of the post for the feature num_of_comments


- num_of_comments_std_parent: std of the post_parent for the feature num_of_comments


- num_of_comments_std_children: std of the post_children for the feature num_of_comments


- num_of_comments_std_all_children: std of the post_all_children for the feature num_of_comments


- num_of_comments_max: max of the post for the feature num_of_comments


- num_of_comments_max_parent: max of the post_parent for the feature num_of_comments


- num_of_comments_max_children: max of the post_children for the feature num_of_comments


- num_of_comments_max_all_children: max of the post_all_children for the feature num_of_comments


- num_of_comments_min: min of the post for the feature num_of_comments


- num_of_comments_min_parent: min of the post_parent for the feature num_of_comments


- num_of_comments_min_children: min of the post_children for the feature num_of_comments


- num_of_comments_min_all_children: min of the post_all_children for the feature num_of_comments


- num_of_comments_first: first of the post for the feature num_of_comments


- num_of_comments_first_parent: first of the post_parent for the feature num_of_comments


- num_of_comments_first_children: first of the post_children for the feature num_of_comments


- num_of_comments_first_all_children: first of the post_all_children for the feature num_of_comments


- num_of_comments_last: last of the post for the feature num_of_comments


- num_of_comments_last_parent: last of the post_parent for the feature num_of_comments


- num_of_comments_last_children: last of the post_children for the feature num_of_comments


- num_of_comments_last_all_children: last of the post_all_children for the feature num_of_comments


- link_flair_richtext_avg: avg of the post for the feature link_flair_richtext


- link_flair_richtext_avg_parent: avg of the post_parent for the feature link_flair_richtext


- link_flair_richtext_avg_children: avg of the post_children for the feature link_flair_richtext


- link_flair_richtext_avg_all_children: avg of the post_all_children for the feature link_flair_richtext


- link_flair_richtext_std: std of the post for the feature link_flair_richtext


- link_flair_richtext_std_parent: std of the post_parent for the feature link_flair_richtext


- link_flair_richtext_std_children: std of the post_children for the feature link_flair_richtext


- link_flair_richtext_std_all_children: std of the post_all_children for the feature link_flair_richtext


- link_flair_richtext_max: max of the post for the feature link_flair_richtext


- link_flair_richtext_max_parent: max of the post_parent for the feature link_flair_richtext


- link_flair_richtext_max_children: max of the post_children for the feature link_flair_richtext


- link_flair_richtext_max_all_children: max of the post_all_children for the feature link_flair_richtext


- link_flair_richtext_min: min of the post for the feature link_flair_richtext


- link_flair_richtext_min_parent: min of the post_parent for the feature link_flair_richtext


- link_flair_richtext_min_children: min of the post_children for the feature link_flair_richtext


- link_flair_richtext_min_all_children: min of the post_all_children for the feature link_flair_richtext


- link_flair_richtext_first: first of the post for the feature link_flair_richtext


- link_flair_richtext_first_parent: first of the post_parent for the feature link_flair_richtext


- link_flair_richtext_first_children: first of the post_children for the feature link_flair_richtext


- link_flair_richtext_first_all_children: first of the post_all_children for the feature link_flair_richtext


- link_flair_richtext_last: last of the post for the feature link_flair_richtext


- link_flair_richtext_last_parent: last of the post_parent for the feature link_flair_richtext


- link_flair_richtext_last_children: last of the post_children for the feature link_flair_richtext


- link_flair_richtext_last_all_children: last of the post_all_children for the feature link_flair_richtext


- archived_avg: avg of the post for the feature archived


- archived_avg_parent: avg of the post_parent for the feature archived


- archived_avg_children: avg of the post_children for the feature archived


- archived_avg_all_children: avg of the post_all_children for the feature archived


- archived_std: std of the post for the feature archived


- archived_std_parent: std of the post_parent for the feature archived


- archived_std_children: std of the post_children for the feature archived


- archived_std_all_children: std of the post_all_children for the feature archived


- archived_max: max of the post for the feature archived


- archived_max_parent: max of the post_parent for the feature archived


- archived_max_children: max of the post_children for the feature archived


- archived_max_all_children: max of the post_all_children for the feature archived


- archived_min: min of the post for the feature archived


- archived_min_parent: min of the post_parent for the feature archived


- archived_min_children: min of the post_children for the feature archived


- archived_min_all_children: min of the post_all_children for the feature archived


- archived_first: first of the post for the feature archived


- archived_first_parent: first of the post_parent for the feature archived


- archived_first_children: first of the post_children for the feature archived


- archived_first_all_children: first of the post_all_children for the feature archived


- archived_last: last of the post for the feature archived


- archived_last_parent: last of the post_parent for the feature archived


- archived_last_children: last of the post_children for the feature archived


- archived_last_all_children: last of the post_all_children for the feature archived


- pinned_avg: avg of the post for the feature pinned


- pinned_avg_parent: avg of the post_parent for the feature pinned


- pinned_avg_children: avg of the post_children for the feature pinned


- pinned_avg_all_children: avg of the post_all_children for the feature pinned


- pinned_std: std of the post for the feature pinned


- pinned_std_parent: std of the post_parent for the feature pinned


- pinned_std_children: std of the post_children for the feature pinned


- pinned_std_all_children: std of the post_all_children for the feature pinned


- pinned_max: max of the post for the feature pinned


- pinned_max_parent: max of the post_parent for the feature pinned


- pinned_max_children: max of the post_children for the feature pinned


- pinned_max_all_children: max of the post_all_children for the feature pinned


- pinned_min: min of the post for the feature pinned


- pinned_min_parent: min of the post_parent for the feature pinned


- pinned_min_children: min of the post_children for the feature pinned


- pinned_min_all_children: min of the post_all_children for the feature pinned


- pinned_first: first of the post for the feature pinned


- pinned_first_parent: first of the post_parent for the feature pinned


- pinned_first_children: first of the post_children for the feature pinned


- pinned_first_all_children: first of the post_all_children for the feature pinned


- pinned_last: last of the post for the feature pinned


- pinned_last_parent: last of the post_parent for the feature pinned


- pinned_last_children: last of the post_children for the feature pinned


- pinned_last_all_children: last of the post_all_children for the feature pinned


- subreddit_type_avg: avg of the post for the feature subreddit_type


- subreddit_type_avg_parent: avg of the post_parent for the feature subreddit_type


- subreddit_type_avg_children: avg of the post_children for the feature subreddit_type


- subreddit_type_avg_all_children: avg of the post_all_children for the feature subreddit_type


- subreddit_type_std: std of the post for the feature subreddit_type


- subreddit_type_std_parent: std of the post_parent for the feature subreddit_type


- subreddit_type_std_children: std of the post_children for the feature subreddit_type


- subreddit_type_std_all_children: std of the post_all_children for the feature subreddit_type


- subreddit_type_max: max of the post for the feature subreddit_type


- subreddit_type_max_parent: max of the post_parent for the feature subreddit_type


- subreddit_type_max_children: max of the post_children for the feature subreddit_type


- subreddit_type_max_all_children: max of the post_all_children for the feature subreddit_type


- subreddit_type_min: min of the post for the feature subreddit_type


- subreddit_type_min_parent: min of the post_parent for the feature subreddit_type


- subreddit_type_min_children: min of the post_children for the feature subreddit_type


- subreddit_type_min_all_children: min of the post_all_children for the feature subreddit_type


- subreddit_type_first: first of the post for the feature subreddit_type


- subreddit_type_first_parent: first of the post_parent for the feature subreddit_type


- subreddit_type_first_children: first of the post_children for the feature subreddit_type


- subreddit_type_first_all_children: first of the post_all_children for the feature subreddit_type


- subreddit_type_last: last of the post for the feature subreddit_type


- subreddit_type_last_parent: last of the post_parent for the feature subreddit_type


- subreddit_type_last_children: last of the post_children for the feature subreddit_type


- subreddit_type_last_all_children: last of the post_all_children for the feature subreddit_type


- controversiality_avg: avg of the post for the feature controversiality


- controversiality_avg_parent: avg of the post_parent for the feature controversiality


- controversiality_avg_children: avg of the post_children for the feature controversiality


- controversiality_avg_all_children: avg of the post_all_children for the feature controversiality


- controversiality_std: std of the post for the feature controversiality


- controversiality_std_parent: std of the post_parent for the feature controversiality


- controversiality_std_children: std of the post_children for the feature controversiality


- controversiality_std_all_children: std of the post_all_children for the feature controversiality


- controversiality_max: max of the post for the feature controversiality


- controversiality_max_parent: max of the post_parent for the feature controversiality


- controversiality_max_children: max of the post_children for the feature controversiality


- controversiality_max_all_children: max of the post_all_children for the feature controversiality


- controversiality_min: min of the post for the feature controversiality


- controversiality_min_parent: min of the post_parent for the feature controversiality


- controversiality_min_children: min of the post_children for the feature controversiality


- controversiality_min_all_children: min of the post_all_children for the feature controversiality


- controversiality_first: first of the post for the feature controversiality


- controversiality_first_parent: first of the post_parent for the feature controversiality


- controversiality_first_children: first of the post_children for the feature controversiality


- controversiality_first_all_children: first of the post_all_children for the feature controversiality


- controversiality_last: last of the post for the feature controversiality


- controversiality_last_parent: last of the post_parent for the feature controversiality


- controversiality_last_children: last of the post_children for the feature controversiality


- controversiality_last_all_children: last of the post_all_children for the feature controversiality


- parent_whitelist_status_avg: avg of the post for the feature parent_whitelist_status


- parent_whitelist_status_avg_parent: avg of the post_parent for the feature parent_whitelist_status


- parent_whitelist_status_avg_children: avg of the post_children for the feature parent_whitelist_status


- parent_whitelist_status_avg_all_children: avg of the post_all_children for the feature parent_whitelist_status


- parent_whitelist_status_std: std of the post for the feature parent_whitelist_status


- parent_whitelist_status_std_parent: std of the post_parent for the feature parent_whitelist_status


- parent_whitelist_status_std_children: std of the post_children for the feature parent_whitelist_status


- parent_whitelist_status_std_all_children: std of the post_all_children for the feature parent_whitelist_status


- parent_whitelist_status_max: max of the post for the feature parent_whitelist_status


- parent_whitelist_status_max_parent: max of the post_parent for the feature parent_whitelist_status


- parent_whitelist_status_max_children: max of the post_children for the feature parent_whitelist_status


- parent_whitelist_status_max_all_children: max of the post_all_children for the feature parent_whitelist_status


- parent_whitelist_status_min: min of the post for the feature parent_whitelist_status


- parent_whitelist_status_min_parent: min of the post_parent for the feature parent_whitelist_status


- parent_whitelist_status_min_children: min of the post_children for the feature parent_whitelist_status


- parent_whitelist_status_min_all_children: min of the post_all_children for the feature parent_whitelist_status


- parent_whitelist_status_first: first of the post for the feature parent_whitelist_status


- parent_whitelist_status_first_parent: first of the post_parent for the feature parent_whitelist_status


- parent_whitelist_status_first_children: first of the post_children for the feature parent_whitelist_status


- parent_whitelist_status_first_all_children: first of the post_all_children for the feature parent_whitelist_status


- parent_whitelist_status_last: last of the post for the feature parent_whitelist_status


- parent_whitelist_status_last_parent: last of the post_parent for the feature parent_whitelist_status


- parent_whitelist_status_last_children: last of the post_children for the feature parent_whitelist_status


- parent_whitelist_status_last_all_children: last of the post_all_children for the feature parent_whitelist_status


- link_flair_text_avg: avg of the post for the feature link_flair_text


- link_flair_text_avg_parent: avg of the post_parent for the feature link_flair_text


- link_flair_text_avg_children: avg of the post_children for the feature link_flair_text


- link_flair_text_avg_all_children: avg of the post_all_children for the feature link_flair_text


- link_flair_text_std: std of the post for the feature link_flair_text


- link_flair_text_std_parent: std of the post_parent for the feature link_flair_text


- link_flair_text_std_children: std of the post_children for the feature link_flair_text


- link_flair_text_std_all_children: std of the post_all_children for the feature link_flair_text


- link_flair_text_max: max of the post for the feature link_flair_text


- link_flair_text_max_parent: max of the post_parent for the feature link_flair_text


- link_flair_text_max_children: max of the post_children for the feature link_flair_text


- link_flair_text_max_all_children: max of the post_all_children for the feature link_flair_text


- link_flair_text_min: min of the post for the feature link_flair_text


- link_flair_text_min_parent: min of the post_parent for the feature link_flair_text


- link_flair_text_min_children: min of the post_children for the feature link_flair_text


- link_flair_text_min_all_children: min of the post_all_children for the feature link_flair_text


- link_flair_text_first: first of the post for the feature link_flair_text


- link_flair_text_first_parent: first of the post_parent for the feature link_flair_text


- link_flair_text_first_children: first of the post_children for the feature link_flair_text


- link_flair_text_first_all_children: first of the post_all_children for the feature link_flair_text


- link_flair_text_last: last of the post for the feature link_flair_text


- link_flair_text_last_parent: last of the post_parent for the feature link_flair_text


- link_flair_text_last_children: last of the post_children for the feature link_flair_text


- link_flair_text_last_all_children: last of the post_all_children for the feature link_flair_text


- spoiler_avg: avg of the post for the feature spoiler


- spoiler_avg_parent: avg of the post_parent for the feature spoiler


- spoiler_avg_children: avg of the post_children for the feature spoiler


- spoiler_avg_all_children: avg of the post_all_children for the feature spoiler


- spoiler_std: std of the post for the feature spoiler


- spoiler_std_parent: std of the post_parent for the feature spoiler


- spoiler_std_children: std of the post_children for the feature spoiler


- spoiler_std_all_children: std of the post_all_children for the feature spoiler


- spoiler_max: max of the post for the feature spoiler


- spoiler_max_parent: max of the post_parent for the feature spoiler


- spoiler_max_children: max of the post_children for the feature spoiler


- spoiler_max_all_children: max of the post_all_children for the feature spoiler


- spoiler_min: min of the post for the feature spoiler


- spoiler_min_parent: min of the post_parent for the feature spoiler


- spoiler_min_children: min of the post_children for the feature spoiler


- spoiler_min_all_children: min of the post_all_children for the feature spoiler


- spoiler_first: first of the post for the feature spoiler


- spoiler_first_parent: first of the post_parent for the feature spoiler


- spoiler_first_children: first of the post_children for the feature spoiler


- spoiler_first_all_children: first of the post_all_children for the feature spoiler


- spoiler_last: last of the post for the feature spoiler


- spoiler_last_parent: last of the post_parent for the feature spoiler


- spoiler_last_children: last of the post_children for the feature spoiler


- spoiler_last_all_children: last of the post_all_children for the feature spoiler


- category_avg: avg of the post for the feature category


- category_avg_parent: avg of the post_parent for the feature category


- category_avg_children: avg of the post_children for the feature category


- category_avg_all_children: avg of the post_all_children for the feature category


- category_std: std of the post for the feature category


- category_std_parent: std of the post_parent for the feature category


- category_std_children: std of the post_children for the feature category


- category_std_all_children: std of the post_all_children for the feature category


- category_max: max of the post for the feature category


- category_max_parent: max of the post_parent for the feature category


- category_max_children: max of the post_children for the feature category


- category_max_all_children: max of the post_all_children for the feature category


- category_min: min of the post for the feature category


- category_min_parent: min of the post_parent for the feature category


- category_min_children: min of the post_children for the feature category


- category_min_all_children: min of the post_all_children for the feature category


- category_first: first of the post for the feature category


- category_first_parent: first of the post_parent for the feature category


- category_first_children: first of the post_children for the feature category


- category_first_all_children: first of the post_all_children for the feature category


- category_last: last of the post for the feature category


- category_last_parent: last of the post_parent for the feature category


- category_last_children: last of the post_children for the feature category


- category_last_all_children: last of the post_all_children for the feature category


- score_avg: avg of the post for the feature score


- score_avg_parent: avg of the post_parent for the feature score


- score_avg_children: avg of the post_children for the feature score


- score_avg_all_children: avg of the post_all_children for the feature score


- score_std: std of the post for the feature score


- score_std_parent: std of the post_parent for the feature score


- score_std_children: std of the post_children for the feature score


- score_std_all_children: std of the post_all_children for the feature score


- score_max: max of the post for the feature score


- score_max_parent: max of the post_parent for the feature score


- score_max_children: max of the post_children for the feature score


- score_max_all_children: max of the post_all_children for the feature score


- score_min: min of the post for the feature score


- score_min_parent: min of the post_parent for the feature score


- score_min_children: min of the post_children for the feature score


- score_min_all_children: min of the post_all_children for the feature score


- score_first: first of the post for the feature score


- score_first_parent: first of the post_parent for the feature score


- score_first_children: first of the post_children for the feature score


- score_first_all_children: first of the post_all_children for the feature score


- score_last: last of the post for the feature score


- score_last_parent: last of the post_parent for the feature score


- score_last_children: last of the post_children for the feature score


- score_last_all_children: last of the post_all_children for the feature score


- over_18_avg: avg of the post for the feature over_18


- over_18_avg_parent: avg of the post_parent for the feature over_18


- over_18_avg_children: avg of the post_children for the feature over_18


- over_18_avg_all_children: avg of the post_all_children for the feature over_18


- over_18_std: std of the post for the feature over_18


- over_18_std_parent: std of the post_parent for the feature over_18


- over_18_std_children: std of the post_children for the feature over_18


- over_18_std_all_children: std of the post_all_children for the feature over_18


- over_18_max: max of the post for the feature over_18


- over_18_max_parent: max of the post_parent for the feature over_18


- over_18_max_children: max of the post_children for the feature over_18


- over_18_max_all_children: max of the post_all_children for the feature over_18


- over_18_min: min of the post for the feature over_18


- over_18_min_parent: min of the post_parent for the feature over_18


- over_18_min_children: min of the post_children for the feature over_18


- over_18_min_all_children: min of the post_all_children for the feature over_18


- over_18_first: first of the post for the feature over_18


- over_18_first_parent: first of the post_parent for the feature over_18


- over_18_first_children: first of the post_children for the feature over_18


- over_18_first_all_children: first of the post_all_children for the feature over_18


- over_18_last: last of the post for the feature over_18


- over_18_last_parent: last of the post_parent for the feature over_18


- over_18_last_children: last of the post_children for the feature over_18


- over_18_last_all_children: last of the post_all_children for the feature over_18


- pwls_avg: avg of the post for the feature pwls


- pwls_avg_parent: avg of the post_parent for the feature pwls


- pwls_avg_children: avg of the post_children for the feature pwls


- pwls_avg_all_children: avg of the post_all_children for the feature pwls


- pwls_std: std of the post for the feature pwls


- pwls_std_parent: std of the post_parent for the feature pwls


- pwls_std_children: std of the post_children for the feature pwls


- pwls_std_all_children: std of the post_all_children for the feature pwls


- pwls_max: max of the post for the feature pwls


- pwls_max_parent: max of the post_parent for the feature pwls


- pwls_max_children: max of the post_children for the feature pwls


- pwls_max_all_children: max of the post_all_children for the feature pwls


- pwls_min: min of the post for the feature pwls


- pwls_min_parent: min of the post_parent for the feature pwls


- pwls_min_children: min of the post_children for the feature pwls


- pwls_min_all_children: min of the post_all_children for the feature pwls


- pwls_first: first of the post for the feature pwls


- pwls_first_parent: first of the post_parent for the feature pwls


- pwls_first_children: first of the post_children for the feature pwls


- pwls_first_all_children: first of the post_all_children for the feature pwls


- pwls_last: last of the post for the feature pwls


- pwls_last_parent: last of the post_parent for the feature pwls


- pwls_last_children: last of the post_children for the feature pwls


- pwls_last_all_children: last of the post_all_children for the feature pwls


- collapsed_avg: avg of the post for the feature collapsed


- collapsed_avg_parent: avg of the post_parent for the feature collapsed


- collapsed_avg_children: avg of the post_children for the feature collapsed


- collapsed_avg_all_children: avg of the post_all_children for the feature collapsed


- collapsed_std: std of the post for the feature collapsed


- collapsed_std_parent: std of the post_parent for the feature collapsed


- collapsed_std_children: std of the post_children for the feature collapsed


- collapsed_std_all_children: std of the post_all_children for the feature collapsed


- collapsed_max: max of the post for the feature collapsed


- collapsed_max_parent: max of the post_parent for the feature collapsed


- collapsed_max_children: max of the post_children for the feature collapsed


- collapsed_max_all_children: max of the post_all_children for the feature collapsed


- collapsed_min: min of the post for the feature collapsed


- collapsed_min_parent: min of the post_parent for the feature collapsed


- collapsed_min_children: min of the post_children for the feature collapsed


- collapsed_min_all_children: min of the post_all_children for the feature collapsed


- collapsed_first: first of the post for the feature collapsed


- collapsed_first_parent: first of the post_parent for the feature collapsed


- collapsed_first_children: first of the post_children for the feature collapsed


- collapsed_first_all_children: first of the post_all_children for the feature collapsed


- collapsed_last: last of the post for the feature collapsed


- collapsed_last_parent: last of the post_parent for the feature collapsed


- collapsed_last_children: last of the post_children for the feature collapsed


- collapsed_last_all_children: last of the post_all_children for the feature collapsed


- achieved_avg: avg of the post for the feature achieved


- achieved_avg_parent: avg of the post_parent for the feature achieved


- achieved_avg_children: avg of the post_children for the feature achieved


- achieved_avg_all_children: avg of the post_all_children for the feature achieved


- achieved_std: std of the post for the feature achieved


- achieved_std_parent: std of the post_parent for the feature achieved


- achieved_std_children: std of the post_children for the feature achieved


- achieved_std_all_children: std of the post_all_children for the feature achieved


- achieved_max: max of the post for the feature achieved


- achieved_max_parent: max of the post_parent for the feature achieved


- achieved_max_children: max of the post_children for the feature achieved


- achieved_max_all_children: max of the post_all_children for the feature achieved


- achieved_min: min of the post for the feature achieved


- achieved_min_parent: min of the post_parent for the feature achieved


- achieved_min_children: min of the post_children for the feature achieved


- achieved_min_all_children: min of the post_all_children for the feature achieved


- achieved_first: first of the post for the feature achieved


- achieved_first_parent: first of the post_parent for the feature achieved


- achieved_first_children: first of the post_children for the feature achieved


- achieved_first_all_children: first of the post_all_children for the feature achieved


- achieved_last: last of the post for the feature achieved


- achieved_last_parent: last of the post_parent for the feature achieved


- achieved_last_children: last of the post_children for the feature achieved


- achieved_last_all_children: last of the post_all_children for the feature achieved


- is_robot_indexable_avg: avg of the post for the feature is_robot_indexable


- is_robot_indexable_avg_parent: avg of the post_parent for the feature is_robot_indexable


- is_robot_indexable_avg_children: avg of the post_children for the feature is_robot_indexable


- is_robot_indexable_avg_all_children: avg of the post_all_children for the feature is_robot_indexable


- is_robot_indexable_std: std of the post for the feature is_robot_indexable


- is_robot_indexable_std_parent: std of the post_parent for the feature is_robot_indexable


- is_robot_indexable_std_children: std of the post_children for the feature is_robot_indexable


- is_robot_indexable_std_all_children: std of the post_all_children for the feature is_robot_indexable


- is_robot_indexable_max: max of the post for the feature is_robot_indexable


- is_robot_indexable_max_parent: max of the post_parent for the feature is_robot_indexable


- is_robot_indexable_max_children: max of the post_children for the feature is_robot_indexable


- is_robot_indexable_max_all_children: max of the post_all_children for the feature is_robot_indexable


- is_robot_indexable_min: min of the post for the feature is_robot_indexable


- is_robot_indexable_min_parent: min of the post_parent for the feature is_robot_indexable


- is_robot_indexable_min_children: min of the post_children for the feature is_robot_indexable


- is_robot_indexable_min_all_children: min of the post_all_children for the feature is_robot_indexable


- is_robot_indexable_first: first of the post for the feature is_robot_indexable


- is_robot_indexable_first_parent: first of the post_parent for the feature is_robot_indexable


- is_robot_indexable_first_children: first of the post_children for the feature is_robot_indexable


- is_robot_indexable_first_all_children: first of the post_all_children for the feature is_robot_indexable


- is_robot_indexable_last: last of the post for the feature is_robot_indexable


- is_robot_indexable_last_parent: last of the post_parent for the feature is_robot_indexable


- is_robot_indexable_last_children: last of the post_children for the feature is_robot_indexable


- is_robot_indexable_last_all_children: last of the post_all_children for the feature is_robot_indexable


- length_of_title_avg: avg of the post for the feature length_of_title


- length_of_title_avg_parent: avg of the post_parent for the feature length_of_title


- length_of_title_avg_children: avg of the post_children for the feature length_of_title


- length_of_title_avg_all_children: avg of the post_all_children for the feature length_of_title


- length_of_title_std: std of the post for the feature length_of_title


- length_of_title_std_parent: std of the post_parent for the feature length_of_title


- length_of_title_std_children: std of the post_children for the feature length_of_title


- length_of_title_std_all_children: std of the post_all_children for the feature length_of_title


- length_of_title_max: max of the post for the feature length_of_title


- length_of_title_max_parent: max of the post_parent for the feature length_of_title


- length_of_title_max_children: max of the post_children for the feature length_of_title


- length_of_title_max_all_children: max of the post_all_children for the feature length_of_title


- length_of_title_min: min of the post for the feature length_of_title


- length_of_title_min_parent: min of the post_parent for the feature length_of_title


- length_of_title_min_children: min of the post_children for the feature length_of_title


- length_of_title_min_all_children: min of the post_all_children for the feature length_of_title


- length_of_title_first: first of the post for the feature length_of_title


- length_of_title_first_parent: first of the post_parent for the feature length_of_title


- length_of_title_first_children: first of the post_children for the feature length_of_title


- length_of_title_first_all_children: first of the post_all_children for the feature length_of_title


- length_of_title_last: last of the post for the feature length_of_title


- length_of_title_last_parent: last of the post_parent for the feature length_of_title


- length_of_title_last_children: last of the post_children for the feature length_of_title


- length_of_title_last_all_children: last of the post_all_children for the feature length_of_title


- content_categories_avg: avg of the post for the feature content_categories


- content_categories_avg_parent: avg of the post_parent for the feature content_categories


- content_categories_avg_children: avg of the post_children for the feature content_categories


- content_categories_avg_all_children: avg of the post_all_children for the feature content_categories


- content_categories_std: std of the post for the feature content_categories


- content_categories_std_parent: std of the post_parent for the feature content_categories


- content_categories_std_children: std of the post_children for the feature content_categories


- content_categories_std_all_children: std of the post_all_children for the feature content_categories


- content_categories_max: max of the post for the feature content_categories


- content_categories_max_parent: max of the post_parent for the feature content_categories


- content_categories_max_children: max of the post_children for the feature content_categories


- content_categories_max_all_children: max of the post_all_children for the feature content_categories


- content_categories_min: min of the post for the feature content_categories


- content_categories_min_parent: min of the post_parent for the feature content_categories


- content_categories_min_children: min of the post_children for the feature content_categories


- content_categories_min_all_children: min of the post_all_children for the feature content_categories


- content_categories_first: first of the post for the feature content_categories


- content_categories_first_parent: first of the post_parent for the feature content_categories


- content_categories_first_children: first of the post_children for the feature content_categories


- content_categories_first_all_children: first of the post_all_children for the feature content_categories


- content_categories_last: last of the post for the feature content_categories


- content_categories_last_parent: last of the post_parent for the feature content_categories


- content_categories_last_children: last of the post_children for the feature content_categories


- content_categories_last_all_children: last of the post_all_children for the feature content_categories


- num_of_all_comments_avg: avg of the post for the feature num_of_all_comments


- num_of_all_comments_avg_parent: avg of the post_parent for the feature num_of_all_comments


- num_of_all_comments_avg_children: avg of the post_children for the feature num_of_all_comments


- num_of_all_comments_avg_all_children: avg of the post_all_children for the feature num_of_all_comments


- num_of_all_comments_std: std of the post for the feature num_of_all_comments


- num_of_all_comments_std_parent: std of the post_parent for the feature num_of_all_comments


- num_of_all_comments_std_children: std of the post_children for the feature num_of_all_comments


- num_of_all_comments_std_all_children: std of the post_all_children for the feature num_of_all_comments


- num_of_all_comments_max: max of the post for the feature num_of_all_comments


- num_of_all_comments_max_parent: max of the post_parent for the feature num_of_all_comments


- num_of_all_comments_max_children: max of the post_children for the feature num_of_all_comments


- num_of_all_comments_max_all_children: max of the post_all_children for the feature num_of_all_comments


- num_of_all_comments_min: min of the post for the feature num_of_all_comments


- num_of_all_comments_min_parent: min of the post_parent for the feature num_of_all_comments


- num_of_all_comments_min_children: min of the post_children for the feature num_of_all_comments


- num_of_all_comments_min_all_children: min of the post_all_children for the feature num_of_all_comments


- num_of_all_comments_first: first of the post for the feature num_of_all_comments


- num_of_all_comments_first_parent: first of the post_parent for the feature num_of_all_comments


- num_of_all_comments_first_children: first of the post_children for the feature num_of_all_comments


- num_of_all_comments_first_all_children: first of the post_all_children for the feature num_of_all_comments


- num_of_all_comments_last: last of the post for the feature num_of_all_comments


- num_of_all_comments_last_parent: last of the post_parent for the feature num_of_all_comments


- num_of_all_comments_last_children: last of the post_children for the feature num_of_all_comments


- num_of_all_comments_last_all_children: last of the post_all_children for the feature num_of_all_comments


- post_level_avg: avg of the post for the feature post_level


- post_level_avg_parent: avg of the post_parent for the feature post_level


- post_level_avg_children: avg of the post_children for the feature post_level


- post_level_avg_all_children: avg of the post_all_children for the feature post_level


- post_level_std: std of the post for the feature post_level


- post_level_std_parent: std of the post_parent for the feature post_level


- post_level_std_children: std of the post_children for the feature post_level


- post_level_std_all_children: std of the post_all_children for the feature post_level


- post_level_max: max of the post for the feature post_level


- post_level_max_parent: max of the post_parent for the feature post_level


- post_level_max_children: max of the post_children for the feature post_level


- post_level_max_all_children: max of the post_all_children for the feature post_level


- post_level_min: min of the post for the feature post_level


- post_level_min_parent: min of the post_parent for the feature post_level


- post_level_min_children: min of the post_children for the feature post_level


- post_level_min_all_children: min of the post_all_children for the feature post_level


- post_level_first: first of the post for the feature post_level


- post_level_first_parent: first of the post_parent for the feature post_level


- post_level_first_children: first of the post_children for the feature post_level


- post_level_first_all_children: first of the post_all_children for the feature post_level


- post_level_last: last of the post for the feature post_level


- post_level_last_parent: last of the post_parent for the feature post_level


- post_level_last_children: last of the post_children for the feature post_level


- post_level_last_all_children: last of the post_all_children for the feature post_level


- is_self_avg: avg of the post for the feature is_self


- is_self_avg_parent: avg of the post_parent for the feature is_self


- is_self_avg_children: avg of the post_children for the feature is_self


- is_self_avg_all_children: avg of the post_all_children for the feature is_self


- is_self_std: std of the post for the feature is_self


- is_self_std_parent: std of the post_parent for the feature is_self


- is_self_std_children: std of the post_children for the feature is_self


- is_self_std_all_children: std of the post_all_children for the feature is_self


- is_self_max: max of the post for the feature is_self


- is_self_max_parent: max of the post_parent for the feature is_self


- is_self_max_children: max of the post_children for the feature is_self


- is_self_max_all_children: max of the post_all_children for the feature is_self


- is_self_min: min of the post for the feature is_self


- is_self_min_parent: min of the post_parent for the feature is_self


- is_self_min_children: min of the post_children for the feature is_self


- is_self_min_all_children: min of the post_all_children for the feature is_self


- is_self_first: first of the post for the feature is_self


- is_self_first_parent: first of the post_parent for the feature is_self


- is_self_first_children: first of the post_children for the feature is_self


- is_self_first_all_children: first of the post_all_children for the feature is_self


- is_self_last: last of the post for the feature is_self


- is_self_last_parent: last of the post_parent for the feature is_self


- is_self_last_children: last of the post_children for the feature is_self


- is_self_last_all_children: last of the post_all_children for the feature is_self


- top_awarded_type_avg: avg of the post for the feature top_awarded_type


- top_awarded_type_avg_parent: avg of the post_parent for the feature top_awarded_type


- top_awarded_type_avg_children: avg of the post_children for the feature top_awarded_type


- top_awarded_type_avg_all_children: avg of the post_all_children for the feature top_awarded_type


- top_awarded_type_std: std of the post for the feature top_awarded_type


- top_awarded_type_std_parent: std of the post_parent for the feature top_awarded_type


- top_awarded_type_std_children: std of the post_children for the feature top_awarded_type


- top_awarded_type_std_all_children: std of the post_all_children for the feature top_awarded_type


- top_awarded_type_max: max of the post for the feature top_awarded_type


- top_awarded_type_max_parent: max of the post_parent for the feature top_awarded_type


- top_awarded_type_max_children: max of the post_children for the feature top_awarded_type


- top_awarded_type_max_all_children: max of the post_all_children for the feature top_awarded_type


- top_awarded_type_min: min of the post for the feature top_awarded_type


- top_awarded_type_min_parent: min of the post_parent for the feature top_awarded_type


- top_awarded_type_min_children: min of the post_children for the feature top_awarded_type


- top_awarded_type_min_all_children: min of the post_all_children for the feature top_awarded_type


- top_awarded_type_first: first of the post for the feature top_awarded_type


- top_awarded_type_first_parent: first of the post_parent for the feature top_awarded_type


- top_awarded_type_first_children: first of the post_children for the feature top_awarded_type


- top_awarded_type_first_all_children: first of the post_all_children for the feature top_awarded_type


- top_awarded_type_last: last of the post for the feature top_awarded_type


- top_awarded_type_last_parent: last of the post_parent for the feature top_awarded_type


- top_awarded_type_last_children: last of the post_children for the feature top_awarded_type


- top_awarded_type_last_all_children: last of the post_all_children for the feature top_awarded_type


- subreddit_subscribers_avg: avg of the post for the feature subreddit_subscribers


- subreddit_subscribers_avg_parent: avg of the post_parent for the feature subreddit_subscribers


- subreddit_subscribers_avg_children: avg of the post_children for the feature subreddit_subscribers


- subreddit_subscribers_avg_all_children: avg of the post_all_children for the feature subreddit_subscribers


- subreddit_subscribers_std: std of the post for the feature subreddit_subscribers


- subreddit_subscribers_std_parent: std of the post_parent for the feature subreddit_subscribers


- subreddit_subscribers_std_children: std of the post_children for the feature subreddit_subscribers


- subreddit_subscribers_std_all_children: std of the post_all_children for the feature subreddit_subscribers


- subreddit_subscribers_max: max of the post for the feature subreddit_subscribers


- subreddit_subscribers_max_parent: max of the post_parent for the feature subreddit_subscribers


- subreddit_subscribers_max_children: max of the post_children for the feature subreddit_subscribers


- subreddit_subscribers_max_all_children: max of the post_all_children for the feature subreddit_subscribers


- subreddit_subscribers_min: min of the post for the feature subreddit_subscribers


- subreddit_subscribers_min_parent: min of the post_parent for the feature subreddit_subscribers


- subreddit_subscribers_min_children: min of the post_children for the feature subreddit_subscribers


- subreddit_subscribers_min_all_children: min of the post_all_children for the feature subreddit_subscribers


- subreddit_subscribers_first: first of the post for the feature subreddit_subscribers


- subreddit_subscribers_first_parent: first of the post_parent for the feature subreddit_subscribers


- subreddit_subscribers_first_children: first of the post_children for the feature subreddit_subscribers


- subreddit_subscribers_first_all_children: first of the post_all_children for the feature subreddit_subscribers


- subreddit_subscribers_last: last of the post for the feature subreddit_subscribers


- subreddit_subscribers_last_parent: last of the post_parent for the feature subreddit_subscribers


- subreddit_subscribers_last_children: last of the post_children for the feature subreddit_subscribers


- subreddit_subscribers_last_all_children: last of the post_all_children for the feature subreddit_subscribers


- link_flair_text_color_avg: avg of the post for the feature link_flair_text_color


- link_flair_text_color_avg_parent: avg of the post_parent for the feature link_flair_text_color


- link_flair_text_color_avg_children: avg of the post_children for the feature link_flair_text_color


- link_flair_text_color_avg_all_children: avg of the post_all_children for the feature link_flair_text_color


- link_flair_text_color_std: std of the post for the feature link_flair_text_color


- link_flair_text_color_std_parent: std of the post_parent for the feature link_flair_text_color


- link_flair_text_color_std_children: std of the post_children for the feature link_flair_text_color


- link_flair_text_color_std_all_children: std of the post_all_children for the feature link_flair_text_color


- link_flair_text_color_max: max of the post for the feature link_flair_text_color


- link_flair_text_color_max_parent: max of the post_parent for the feature link_flair_text_color


- link_flair_text_color_max_children: max of the post_children for the feature link_flair_text_color


- link_flair_text_color_max_all_children: max of the post_all_children for the feature link_flair_text_color


- link_flair_text_color_min: min of the post for the feature link_flair_text_color


- link_flair_text_color_min_parent: min of the post_parent for the feature link_flair_text_color


- link_flair_text_color_min_children: min of the post_children for the feature link_flair_text_color


- link_flair_text_color_min_all_children: min of the post_all_children for the feature link_flair_text_color


- link_flair_text_color_first: first of the post for the feature link_flair_text_color


- link_flair_text_color_first_parent: first of the post_parent for the feature link_flair_text_color


- link_flair_text_color_first_children: first of the post_children for the feature link_flair_text_color


- link_flair_text_color_first_all_children: first of the post_all_children for the feature link_flair_text_color


- link_flair_text_color_last: last of the post for the feature link_flair_text_color


- link_flair_text_color_last_parent: last of the post_parent for the feature link_flair_text_color


- link_flair_text_color_last_children: last of the post_children for the feature link_flair_text_color


- link_flair_text_color_last_all_children: last of the post_all_children for the feature link_flair_text_color


- wls_avg: avg of the post for the feature wls


- wls_avg_parent: avg of the post_parent for the feature wls


- wls_avg_children: avg of the post_children for the feature wls


- wls_avg_all_children: avg of the post_all_children for the feature wls


- wls_std: std of the post for the feature wls


- wls_std_parent: std of the post_parent for the feature wls


- wls_std_children: std of the post_children for the feature wls


- wls_std_all_children: std of the post_all_children for the feature wls


- wls_max: max of the post for the feature wls


- wls_max_parent: max of the post_parent for the feature wls


- wls_max_children: max of the post_children for the feature wls


- wls_max_all_children: max of the post_all_children for the feature wls


- wls_min: min of the post for the feature wls


- wls_min_parent: min of the post_parent for the feature wls


- wls_min_children: min of the post_children for the feature wls


- wls_min_all_children: min of the post_all_children for the feature wls


- wls_first: first of the post for the feature wls


- wls_first_parent: first of the post_parent for the feature wls


- wls_first_children: first of the post_children for the feature wls


- wls_first_all_children: first of the post_all_children for the feature wls


- wls_last: last of the post for the feature wls


- wls_last_parent: last of the post_parent for the feature wls


- wls_last_children: last of the post_children for the feature wls


- wls_last_all_children: last of the post_all_children for the feature wls


- num_of_all_awardings_avg: avg of the post for the feature num_of_all_awardings


- num_of_all_awardings_avg_parent: avg of the post_parent for the feature num_of_all_awardings


- num_of_all_awardings_avg_children: avg of the post_children for the feature num_of_all_awardings


- num_of_all_awardings_avg_all_children: avg of the post_all_children for the feature num_of_all_awardings


- num_of_all_awardings_std: std of the post for the feature num_of_all_awardings


- num_of_all_awardings_std_parent: std of the post_parent for the feature num_of_all_awardings


- num_of_all_awardings_std_children: std of the post_children for the feature num_of_all_awardings


- num_of_all_awardings_std_all_children: std of the post_all_children for the feature num_of_all_awardings


- num_of_all_awardings_max: max of the post for the feature num_of_all_awardings


- num_of_all_awardings_max_parent: max of the post_parent for the feature num_of_all_awardings


- num_of_all_awardings_max_children: max of the post_children for the feature num_of_all_awardings


- num_of_all_awardings_max_all_children: max of the post_all_children for the feature num_of_all_awardings


- num_of_all_awardings_min: min of the post for the feature num_of_all_awardings


- num_of_all_awardings_min_parent: min of the post_parent for the feature num_of_all_awardings


- num_of_all_awardings_min_children: min of the post_children for the feature num_of_all_awardings


- num_of_all_awardings_min_all_children: min of the post_all_children for the feature num_of_all_awardings


- num_of_all_awardings_first: first of the post for the feature num_of_all_awardings


- num_of_all_awardings_first_parent: first of the post_parent for the feature num_of_all_awardings


- num_of_all_awardings_first_children: first of the post_children for the feature num_of_all_awardings


- num_of_all_awardings_first_all_children: first of the post_all_children for the feature num_of_all_awardings


- num_of_all_awardings_last: last of the post for the feature num_of_all_awardings


- num_of_all_awardings_last_parent: last of the post_parent for the feature num_of_all_awardings


- num_of_all_awardings_last_children: last of the post_children for the feature num_of_all_awardings


- num_of_all_awardings_last_all_children: last of the post_all_children for the feature num_of_all_awardings


- distinguished_avg: avg of the post for the feature distinguished


- distinguished_avg_parent: avg of the post_parent for the feature distinguished


- distinguished_avg_children: avg of the post_children for the feature distinguished


- distinguished_avg_all_children: avg of the post_all_children for the feature distinguished


- distinguished_std: std of the post for the feature distinguished


- distinguished_std_parent: std of the post_parent for the feature distinguished


- distinguished_std_children: std of the post_children for the feature distinguished


- distinguished_std_all_children: std of the post_all_children for the feature distinguished


- distinguished_max: max of the post for the feature distinguished


- distinguished_max_parent: max of the post_parent for the feature distinguished


- distinguished_max_children: max of the post_children for the feature distinguished


- distinguished_max_all_children: max of the post_all_children for the feature distinguished


- distinguished_min: min of the post for the feature distinguished


- distinguished_min_parent: min of the post_parent for the feature distinguished


- distinguished_min_children: min of the post_children for the feature distinguished


- distinguished_min_all_children: min of the post_all_children for the feature distinguished


- distinguished_first: first of the post for the feature distinguished


- distinguished_first_parent: first of the post_parent for the feature distinguished


- distinguished_first_children: first of the post_children for the feature distinguished


- distinguished_first_all_children: first of the post_all_children for the feature distinguished


- distinguished_last: last of the post for the feature distinguished


- distinguished_last_parent: last of the post_parent for the feature distinguished


- distinguished_last_children: last of the post_children for the feature distinguished


- distinguished_last_all_children: last of the post_all_children for the feature distinguished


- num_crossposts_avg: avg of the post for the feature num_crossposts


- num_crossposts_avg_parent: avg of the post_parent for the feature num_crossposts


- num_crossposts_avg_children: avg of the post_children for the feature num_crossposts


- num_crossposts_avg_all_children: avg of the post_all_children for the feature num_crossposts


- num_crossposts_std: std of the post for the feature num_crossposts


- num_crossposts_std_parent: std of the post_parent for the feature num_crossposts


- num_crossposts_std_children: std of the post_children for the feature num_crossposts


- num_crossposts_std_all_children: std of the post_all_children for the feature num_crossposts


- num_crossposts_max: max of the post for the feature num_crossposts


- num_crossposts_max_parent: max of the post_parent for the feature num_crossposts


- num_crossposts_max_children: max of the post_children for the feature num_crossposts


- num_crossposts_max_all_children: max of the post_all_children for the feature num_crossposts


- num_crossposts_min: min of the post for the feature num_crossposts


- num_crossposts_min_parent: min of the post_parent for the feature num_crossposts


- num_crossposts_min_children: min of the post_children for the feature num_crossposts


- num_crossposts_min_all_children: min of the post_all_children for the feature num_crossposts


- num_crossposts_first: first of the post for the feature num_crossposts


- num_crossposts_first_parent: first of the post_parent for the feature num_crossposts


- num_crossposts_first_children: first of the post_children for the feature num_crossposts


- num_crossposts_first_all_children: first of the post_all_children for the feature num_crossposts


- num_crossposts_last: last of the post for the feature num_crossposts


- num_crossposts_last_parent: last of the post_parent for the feature num_crossposts


- num_crossposts_last_children: last of the post_children for the feature num_crossposts


- num_crossposts_last_all_children: last of the post_all_children for the feature num_crossposts


- author_created_utc_avg: avg of the post for the feature author_created_utc


- author_created_utc_avg_parent: avg of the post_parent for the feature author_created_utc


- author_created_utc_avg_children: avg of the post_children for the feature author_created_utc


- author_created_utc_avg_all_children: avg of the post_all_children for the feature author_created_utc


- author_created_utc_std: std of the post for the feature author_created_utc


- author_created_utc_std_parent: std of the post_parent for the feature author_created_utc


- author_created_utc_std_children: std of the post_children for the feature author_created_utc


- author_created_utc_std_all_children: std of the post_all_children for the feature author_created_utc


- author_created_utc_max: max of the post for the feature author_created_utc


- author_created_utc_max_parent: max of the post_parent for the feature author_created_utc


- author_created_utc_max_children: max of the post_children for the feature author_created_utc


- author_created_utc_max_all_children: max of the post_all_children for the feature author_created_utc


- author_created_utc_min: min of the post for the feature author_created_utc


- author_created_utc_min_parent: min of the post_parent for the feature author_created_utc


- author_created_utc_min_children: min of the post_children for the feature author_created_utc


- author_created_utc_min_all_children: min of the post_all_children for the feature author_created_utc


- author_created_utc_first: first of the post for the feature author_created_utc


- author_created_utc_first_parent: first of the post_parent for the feature author_created_utc


- author_created_utc_first_children: first of the post_children for the feature author_created_utc


- author_created_utc_first_all_children: first of the post_all_children for the feature author_created_utc


- author_created_utc_last: last of the post for the feature author_created_utc


- author_created_utc_last_parent: last of the post_parent for the feature author_created_utc


- author_created_utc_last_children: last of the post_children for the feature author_created_utc


- author_created_utc_last_all_children: last of the post_all_children for the feature author_created_utc


- link_flair_template_id_avg: avg of the post for the feature link_flair_template_id


- link_flair_template_id_avg_parent: avg of the post_parent for the feature link_flair_template_id


- link_flair_template_id_avg_children: avg of the post_children for the feature link_flair_template_id


- link_flair_template_id_avg_all_children: avg of the post_all_children for the feature link_flair_template_id


- link_flair_template_id_std: std of the post for the feature link_flair_template_id


- link_flair_template_id_std_parent: std of the post_parent for the feature link_flair_template_id


- link_flair_template_id_std_children: std of the post_children for the feature link_flair_template_id


- link_flair_template_id_std_all_children: std of the post_all_children for the feature link_flair_template_id


- link_flair_template_id_max: max of the post for the feature link_flair_template_id


- link_flair_template_id_max_parent: max of the post_parent for the feature link_flair_template_id


- link_flair_template_id_max_children: max of the post_children for the feature link_flair_template_id


- link_flair_template_id_max_all_children: max of the post_all_children for the feature link_flair_template_id


- link_flair_template_id_min: min of the post for the feature link_flair_template_id


- link_flair_template_id_min_parent: min of the post_parent for the feature link_flair_template_id


- link_flair_template_id_min_children: min of the post_children for the feature link_flair_template_id


- link_flair_template_id_min_all_children: min of the post_all_children for the feature link_flair_template_id


- link_flair_template_id_first: first of the post for the feature link_flair_template_id


- link_flair_template_id_first_parent: first of the post_parent for the feature link_flair_template_id


- link_flair_template_id_first_children: first of the post_children for the feature link_flair_template_id


- link_flair_template_id_first_all_children: first of the post_all_children for the feature link_flair_template_id


- link_flair_template_id_last: last of the post for the feature link_flair_template_id


- link_flair_template_id_last_parent: last of the post_parent for the feature link_flair_template_id


- link_flair_template_id_last_children: last of the post_children for the feature link_flair_template_id


- link_flair_template_id_last_all_children: last of the post_all_children for the feature link_flair_template_id


- is_video_avg: avg of the post for the feature is_video


- is_video_avg_parent: avg of the post_parent for the feature is_video


- is_video_avg_children: avg of the post_children for the feature is_video


- is_video_avg_all_children: avg of the post_all_children for the feature is_video


- is_video_std: std of the post for the feature is_video


- is_video_std_parent: std of the post_parent for the feature is_video


- is_video_std_children: std of the post_children for the feature is_video


- is_video_std_all_children: std of the post_all_children for the feature is_video


- is_video_max: max of the post for the feature is_video


- is_video_max_parent: max of the post_parent for the feature is_video


- is_video_max_children: max of the post_children for the feature is_video


- is_video_max_all_children: max of the post_all_children for the feature is_video


- is_video_min: min of the post for the feature is_video


- is_video_min_parent: min of the post_parent for the feature is_video


- is_video_min_children: min of the post_children for the feature is_video


- is_video_min_all_children: min of the post_all_children for the feature is_video


- is_video_first: first of the post for the feature is_video


- is_video_first_parent: first of the post_parent for the feature is_video


- is_video_first_children: first of the post_children for the feature is_video


- is_video_first_all_children: first of the post_all_children for the feature is_video


- is_video_last: last of the post for the feature is_video


- is_video_last_parent: last of the post_parent for the feature is_video


- is_video_last_children: last of the post_children for the feature is_video


- is_video_last_all_children: last of the post_all_children for the feature is_video


- domain_avg: avg of the post for the feature domain


- domain_avg_parent: avg of the post_parent for the feature domain


- domain_avg_children: avg of the post_children for the feature domain


- domain_avg_all_children: avg of the post_all_children for the feature domain


- domain_std: std of the post for the feature domain


- domain_std_parent: std of the post_parent for the feature domain


- domain_std_children: std of the post_children for the feature domain


- domain_std_all_children: std of the post_all_children for the feature domain


- domain_max: max of the post for the feature domain


- domain_max_parent: max of the post_parent for the feature domain


- domain_max_children: max of the post_children for the feature domain


- domain_max_all_children: max of the post_all_children for the feature domain


- domain_min: min of the post for the feature domain


- domain_min_parent: min of the post_parent for the feature domain


- domain_min_children: min of the post_children for the feature domain


- domain_min_all_children: min of the post_all_children for the feature domain


- domain_first: first of the post for the feature domain


- domain_first_parent: first of the post_parent for the feature domain


- domain_first_children: first of the post_children for the feature domain


- domain_first_all_children: first of the post_all_children for the feature domain


- domain_last: last of the post for the feature domain


- domain_last_parent: last of the post_parent for the feature domain


- domain_last_children: last of the post_children for the feature domain


- domain_last_all_children: last of the post_all_children for the feature domain


- body_length_avg: avg of the post for the feature body_length


- body_length_avg_parent: avg of the post_parent for the feature body_length


- body_length_avg_children: avg of the post_children for the feature body_length


- body_length_avg_all_children: avg of the post_all_children for the feature body_length


- body_length_std: std of the post for the feature body_length


- body_length_std_parent: std of the post_parent for the feature body_length


- body_length_std_children: std of the post_children for the feature body_length


- body_length_std_all_children: std of the post_all_children for the feature body_length


- body_length_max: max of the post for the feature body_length


- body_length_max_parent: max of the post_parent for the feature body_length


- body_length_max_children: max of the post_children for the feature body_length


- body_length_max_all_children: max of the post_all_children for the feature body_length


- body_length_min: min of the post for the feature body_length


- body_length_min_parent: min of the post_parent for the feature body_length


- body_length_min_children: min of the post_children for the feature body_length


- body_length_min_all_children: min of the post_all_children for the feature body_length


- body_length_first: first of the post for the feature body_length


- body_length_first_parent: first of the post_parent for the feature body_length


- body_length_first_children: first of the post_children for the feature body_length


- body_length_first_all_children: first of the post_all_children for the feature body_length


- body_length_last: last of the post for the feature body_length


- body_length_last_parent: last of the post_parent for the feature body_length


- body_length_last_children: last of the post_children for the feature body_length


- body_length_last_all_children: last of the post_all_children for the feature body_length


- suggested_sort_avg: avg of the post for the feature suggested_sort


- suggested_sort_avg_parent: avg of the post_parent for the feature suggested_sort


- suggested_sort_avg_children: avg of the post_children for the feature suggested_sort


- suggested_sort_avg_all_children: avg of the post_all_children for the feature suggested_sort


- suggested_sort_std: std of the post for the feature suggested_sort


- suggested_sort_std_parent: std of the post_parent for the feature suggested_sort


- suggested_sort_std_children: std of the post_children for the feature suggested_sort


- suggested_sort_std_all_children: std of the post_all_children for the feature suggested_sort


- suggested_sort_max: max of the post for the feature suggested_sort


- suggested_sort_max_parent: max of the post_parent for the feature suggested_sort


- suggested_sort_max_children: max of the post_children for the feature suggested_sort


- suggested_sort_max_all_children: max of the post_all_children for the feature suggested_sort


- suggested_sort_min: min of the post for the feature suggested_sort


- suggested_sort_min_parent: min of the post_parent for the feature suggested_sort


- suggested_sort_min_children: min of the post_children for the feature suggested_sort


- suggested_sort_min_all_children: min of the post_all_children for the feature suggested_sort


- suggested_sort_first: first of the post for the feature suggested_sort


- suggested_sort_first_parent: first of the post_parent for the feature suggested_sort


- suggested_sort_first_children: first of the post_children for the feature suggested_sort


- suggested_sort_first_all_children: first of the post_all_children for the feature suggested_sort


- suggested_sort_last: last of the post for the feature suggested_sort


- suggested_sort_last_parent: last of the post_parent for the feature suggested_sort


- suggested_sort_last_children: last of the post_children for the feature suggested_sort


- suggested_sort_last_all_children: last of the post_all_children for the feature suggested_sort


- length_of_selftext_avg: avg of the post for the feature length_of_selftext


- length_of_selftext_avg_parent: avg of the post_parent for the feature length_of_selftext


- length_of_selftext_avg_children: avg of the post_children for the feature length_of_selftext


- length_of_selftext_avg_all_children: avg of the post_all_children for the feature length_of_selftext


- length_of_selftext_std: std of the post for the feature length_of_selftext


- length_of_selftext_std_parent: std of the post_parent for the feature length_of_selftext


- length_of_selftext_std_children: std of the post_children for the feature length_of_selftext


- length_of_selftext_std_all_children: std of the post_all_children for the feature length_of_selftext


- length_of_selftext_max: max of the post for the feature length_of_selftext


- length_of_selftext_max_parent: max of the post_parent for the feature length_of_selftext


- length_of_selftext_max_children: max of the post_children for the feature length_of_selftext


- length_of_selftext_max_all_children: max of the post_all_children for the feature length_of_selftext


- length_of_selftext_min: min of the post for the feature length_of_selftext


- length_of_selftext_min_parent: min of the post_parent for the feature length_of_selftext


- length_of_selftext_min_children: min of the post_children for the feature length_of_selftext


- length_of_selftext_min_all_children: min of the post_all_children for the feature length_of_selftext


- length_of_selftext_first: first of the post for the feature length_of_selftext


- length_of_selftext_first_parent: first of the post_parent for the feature length_of_selftext


- length_of_selftext_first_children: first of the post_children for the feature length_of_selftext


- length_of_selftext_first_all_children: first of the post_all_children for the feature length_of_selftext


- length_of_selftext_last: last of the post for the feature length_of_selftext


- length_of_selftext_last_parent: last of the post_parent for the feature length_of_selftext


- length_of_selftext_last_children: last of the post_children for the feature length_of_selftext


- length_of_selftext_last_all_children: last of the post_all_children for the feature length_of_selftext


- num_of_awarders_avg: avg of the post for the feature num_of_awarders


- num_of_awarders_avg_parent: avg of the post_parent for the feature num_of_awarders


- num_of_awarders_avg_children: avg of the post_children for the feature num_of_awarders


- num_of_awarders_avg_all_children: avg of the post_all_children for the feature num_of_awarders


- num_of_awarders_std: std of the post for the feature num_of_awarders


- num_of_awarders_std_parent: std of the post_parent for the feature num_of_awarders


- num_of_awarders_std_children: std of the post_children for the feature num_of_awarders


- num_of_awarders_std_all_children: std of the post_all_children for the feature num_of_awarders


- num_of_awarders_max: max of the post for the feature num_of_awarders


- num_of_awarders_max_parent: max of the post_parent for the feature num_of_awarders


- num_of_awarders_max_children: max of the post_children for the feature num_of_awarders


- num_of_awarders_max_all_children: max of the post_all_children for the feature num_of_awarders


- num_of_awarders_min: min of the post for the feature num_of_awarders


- num_of_awarders_min_parent: min of the post_parent for the feature num_of_awarders


- num_of_awarders_min_children: min of the post_children for the feature num_of_awarders


- num_of_awarders_min_all_children: min of the post_all_children for the feature num_of_awarders


- num_of_awarders_first: first of the post for the feature num_of_awarders


- num_of_awarders_first_parent: first of the post_parent for the feature num_of_awarders


- num_of_awarders_first_children: first of the post_children for the feature num_of_awarders


- num_of_awarders_first_all_children: first of the post_all_children for the feature num_of_awarders


- num_of_awarders_last: last of the post for the feature num_of_awarders


- num_of_awarders_last_parent: last of the post_parent for the feature num_of_awarders


- num_of_awarders_last_children: last of the post_children for the feature num_of_awarders


- num_of_awarders_last_all_children: last of the post_all_children for the feature num_of_awarders


- stickied_avg: avg of the post for the feature stickied


- stickied_avg_parent: avg of the post_parent for the feature stickied


- stickied_avg_children: avg of the post_children for the feature stickied


- stickied_avg_all_children: avg of the post_all_children for the feature stickied


- stickied_std: std of the post for the feature stickied


- stickied_std_parent: std of the post_parent for the feature stickied


- stickied_std_children: std of the post_children for the feature stickied


- stickied_std_all_children: std of the post_all_children for the feature stickied


- stickied_max: max of the post for the feature stickied


- stickied_max_parent: max of the post_parent for the feature stickied


- stickied_max_children: max of the post_children for the feature stickied


- stickied_max_all_children: max of the post_all_children for the feature stickied


- stickied_min: min of the post for the feature stickied


- stickied_min_parent: min of the post_parent for the feature stickied


- stickied_min_children: min of the post_children for the feature stickied


- stickied_min_all_children: min of the post_all_children for the feature stickied


- stickied_first: first of the post for the feature stickied


- stickied_first_parent: first of the post_parent for the feature stickied


- stickied_first_children: first of the post_children for the feature stickied


- stickied_first_all_children: first of the post_all_children for the feature stickied


- stickied_last: last of the post for the feature stickied


- stickied_last_parent: last of the post_parent for the feature stickied


- stickied_last_children: last of the post_children for the feature stickied


- stickied_last_all_children: last of the post_all_children for the feature stickied


- total_awards_received_avg: avg of the post for the feature total_awards_received


- total_awards_received_avg_parent: avg of the post_parent for the feature total_awards_received


- total_awards_received_avg_children: avg of the post_children for the feature total_awards_received


- total_awards_received_avg_all_children: avg of the post_all_children for the feature total_awards_received


- total_awards_received_std: std of the post for the feature total_awards_received


- total_awards_received_std_parent: std of the post_parent for the feature total_awards_received


- total_awards_received_std_children: std of the post_children for the feature total_awards_received


- total_awards_received_std_all_children: std of the post_all_children for the feature total_awards_received


- total_awards_received_max: max of the post for the feature total_awards_received


- total_awards_received_max_parent: max of the post_parent for the feature total_awards_received


- total_awards_received_max_children: max of the post_children for the feature total_awards_received


- total_awards_received_max_all_children: max of the post_all_children for the feature total_awards_received


- total_awards_received_min: min of the post for the feature total_awards_received


- total_awards_received_min_parent: min of the post_parent for the feature total_awards_received


- total_awards_received_min_children: min of the post_children for the feature total_awards_received


- total_awards_received_min_all_children: min of the post_all_children for the feature total_awards_received


- total_awards_received_first: first of the post for the feature total_awards_received


- total_awards_received_first_parent: first of the post_parent for the feature total_awards_received


- total_awards_received_first_children: first of the post_children for the feature total_awards_received


- total_awards_received_first_all_children: first of the post_all_children for the feature total_awards_received


- total_awards_received_last: last of the post for the feature total_awards_received


- total_awards_received_last_parent: last of the post_parent for the feature total_awards_received


- total_awards_received_last_children: last of the post_children for the feature total_awards_received


- total_awards_received_last_all_children: last of the post_all_children for the feature total_awards_received


- thumbnail_avg: avg of the post for the feature thumbnail


- thumbnail_avg_parent: avg of the post_parent for the feature thumbnail


- thumbnail_avg_children: avg of the post_children for the feature thumbnail


- thumbnail_avg_all_children: avg of the post_all_children for the feature thumbnail


- thumbnail_std: std of the post for the feature thumbnail


- thumbnail_std_parent: std of the post_parent for the feature thumbnail


- thumbnail_std_children: std of the post_children for the feature thumbnail


- thumbnail_std_all_children: std of the post_all_children for the feature thumbnail


- thumbnail_max: max of the post for the feature thumbnail


- thumbnail_max_parent: max of the post_parent for the feature thumbnail


- thumbnail_max_children: max of the post_children for the feature thumbnail


- thumbnail_max_all_children: max of the post_all_children for the feature thumbnail


- thumbnail_min: min of the post for the feature thumbnail


- thumbnail_min_parent: min of the post_parent for the feature thumbnail


- thumbnail_min_children: min of the post_children for the feature thumbnail


- thumbnail_min_all_children: min of the post_all_children for the feature thumbnail


- thumbnail_first: first of the post for the feature thumbnail


- thumbnail_first_parent: first of the post_parent for the feature thumbnail


- thumbnail_first_children: first of the post_children for the feature thumbnail


- thumbnail_first_all_children: first of the post_all_children for the feature thumbnail


- thumbnail_last: last of the post for the feature thumbnail


- thumbnail_last_parent: last of the post_parent for the feature thumbnail


- thumbnail_last_children: last of the post_children for the feature thumbnail


- thumbnail_last_all_children: last of the post_all_children for the feature thumbnail


- discussion_type_avg: avg of the post for the feature discussion_type


- discussion_type_avg_parent: avg of the post_parent for the feature discussion_type


- discussion_type_avg_children: avg of the post_children for the feature discussion_type


- discussion_type_avg_all_children: avg of the post_all_children for the feature discussion_type


- discussion_type_std: std of the post for the feature discussion_type


- discussion_type_std_parent: std of the post_parent for the feature discussion_type


- discussion_type_std_children: std of the post_children for the feature discussion_type


- discussion_type_std_all_children: std of the post_all_children for the feature discussion_type


- discussion_type_max: max of the post for the feature discussion_type


- discussion_type_max_parent: max of the post_parent for the feature discussion_type


- discussion_type_max_children: max of the post_children for the feature discussion_type


- discussion_type_max_all_children: max of the post_all_children for the feature discussion_type


- discussion_type_min: min of the post for the feature discussion_type


- discussion_type_min_parent: min of the post_parent for the feature discussion_type


- discussion_type_min_children: min of the post_children for the feature discussion_type


- discussion_type_min_all_children: min of the post_all_children for the feature discussion_type


- discussion_type_first: first of the post for the feature discussion_type


- discussion_type_first_parent: first of the post_parent for the feature discussion_type


- discussion_type_first_children: first of the post_children for the feature discussion_type


- discussion_type_first_all_children: first of the post_all_children for the feature discussion_type


- discussion_type_last: last of the post for the feature discussion_type


- discussion_type_last_parent: last of the post_parent for the feature discussion_type


- discussion_type_last_children: last of the post_children for the feature discussion_type


- discussion_type_last_all_children: last of the post_all_children for the feature discussion_type


- removed_by_someone_avg: avg of the post for the feature removed_by_someone


- removed_by_someone_avg_parent: avg of the post_parent for the feature removed_by_someone


- removed_by_someone_avg_children: avg of the post_children for the feature removed_by_someone


- removed_by_someone_avg_all_children: avg of the post_all_children for the feature removed_by_someone


- removed_by_someone_std: std of the post for the feature removed_by_someone


- removed_by_someone_std_parent: std of the post_parent for the feature removed_by_someone


- removed_by_someone_std_children: std of the post_children for the feature removed_by_someone


- removed_by_someone_std_all_children: std of the post_all_children for the feature removed_by_someone


- removed_by_someone_max: max of the post for the feature removed_by_someone


- removed_by_someone_max_parent: max of the post_parent for the feature removed_by_someone


- removed_by_someone_max_children: max of the post_children for the feature removed_by_someone


- removed_by_someone_max_all_children: max of the post_all_children for the feature removed_by_someone


- removed_by_someone_min: min of the post for the feature removed_by_someone


- removed_by_someone_min_parent: min of the post_parent for the feature removed_by_someone


- removed_by_someone_min_children: min of the post_children for the feature removed_by_someone


- removed_by_someone_min_all_children: min of the post_all_children for the feature removed_by_someone


- removed_by_someone_first: first of the post for the feature removed_by_someone


- removed_by_someone_first_parent: first of the post_parent for the feature removed_by_someone


- removed_by_someone_first_children: first of the post_children for the feature removed_by_someone


- removed_by_someone_first_all_children: first of the post_all_children for the feature removed_by_someone


- removed_by_someone_last: last of the post for the feature removed_by_someone


- removed_by_someone_last_parent: last of the post_parent for the feature removed_by_someone


- removed_by_someone_last_children: last of the post_children for the feature removed_by_someone


- removed_by_someone_last_all_children: last of the post_all_children for the feature removed_by_someone


- quarantine_avg: avg of the post for the feature quarantine


- quarantine_avg_parent: avg of the post_parent for the feature quarantine


- quarantine_avg_children: avg of the post_children for the feature quarantine


- quarantine_avg_all_children: avg of the post_all_children for the feature quarantine


- quarantine_std: std of the post for the feature quarantine


- quarantine_std_parent: std of the post_parent for the feature quarantine


- quarantine_std_children: std of the post_children for the feature quarantine


- quarantine_std_all_children: std of the post_all_children for the feature quarantine


- quarantine_max: max of the post for the feature quarantine


- quarantine_max_parent: max of the post_parent for the feature quarantine


- quarantine_max_children: max of the post_children for the feature quarantine


- quarantine_max_all_children: max of the post_all_children for the feature quarantine


- quarantine_min: min of the post for the feature quarantine


- quarantine_min_parent: min of the post_parent for the feature quarantine


- quarantine_min_children: min of the post_children for the feature quarantine


- quarantine_min_all_children: min of the post_all_children for the feature quarantine


- quarantine_first: first of the post for the feature quarantine


- quarantine_first_parent: first of the post_parent for the feature quarantine


- quarantine_first_children: first of the post_children for the feature quarantine


- quarantine_first_all_children: first of the post_all_children for the feature quarantine


- quarantine_last: last of the post for the feature quarantine


- quarantine_last_parent: last of the post_parent for the feature quarantine


- quarantine_last_children: last of the post_children for the feature quarantine


- quarantine_last_all_children: last of the post_all_children for the feature quarantine


- created_utc_avg: avg of the post for the feature created_utc


- created_utc_avg_parent: avg of the post_parent for the feature created_utc


- created_utc_avg_children: avg of the post_children for the feature created_utc


- created_utc_avg_all_children: avg of the post_all_children for the feature created_utc


- created_utc_std: std of the post for the feature created_utc


- created_utc_std_parent: std of the post_parent for the feature created_utc


- created_utc_std_children: std of the post_children for the feature created_utc


- created_utc_std_all_children: std of the post_all_children for the feature created_utc


- created_utc_max: max of the post for the feature created_utc


- created_utc_max_parent: max of the post_parent for the feature created_utc


- created_utc_max_children: max of the post_children for the feature created_utc


- created_utc_max_all_children: max of the post_all_children for the feature created_utc


- created_utc_min: min of the post for the feature created_utc


- created_utc_min_parent: min of the post_parent for the feature created_utc


- created_utc_min_children: min of the post_children for the feature created_utc


- created_utc_min_all_children: min of the post_all_children for the feature created_utc


- created_utc_first: first of the post for the feature created_utc


- created_utc_first_parent: first of the post_parent for the feature created_utc


- created_utc_first_children: first of the post_children for the feature created_utc


- created_utc_first_all_children: first of the post_all_children for the feature created_utc


- created_utc_last: last of the post for the feature created_utc


- created_utc_last_parent: last of the post_parent for the feature created_utc


- created_utc_last_children: last of the post_children for the feature created_utc


- created_utc_last_all_children: last of the post_all_children for the feature created_utc


- locked_avg: avg of the post for the feature locked


- locked_avg_parent: avg of the post_parent for the feature locked


- locked_avg_children: avg of the post_children for the feature locked


- locked_avg_all_children: avg of the post_all_children for the feature locked


- locked_std: std of the post for the feature locked


- locked_std_parent: std of the post_parent for the feature locked


- locked_std_children: std of the post_children for the feature locked


- locked_std_all_children: std of the post_all_children for the feature locked


- locked_max: max of the post for the feature locked


- locked_max_parent: max of the post_parent for the feature locked


- locked_max_children: max of the post_children for the feature locked


- locked_max_all_children: max of the post_all_children for the feature locked


- locked_min: min of the post for the feature locked


- locked_min_parent: min of the post_parent for the feature locked


- locked_min_children: min of the post_children for the feature locked


- locked_min_all_children: min of the post_all_children for the feature locked


- locked_first: first of the post for the feature locked


- locked_first_parent: first of the post_parent for the feature locked


- locked_first_children: first of the post_children for the feature locked


- locked_first_all_children: first of the post_all_children for the feature locked


- locked_last: last of the post for the feature locked


- locked_last_parent: last of the post_parent for the feature locked


- locked_last_children: last of the post_children for the feature locked


- locked_last_all_children: last of the post_all_children for the feature locked


- is_submitter_avg: avg of the post for the feature is_submitter


- is_submitter_avg_parent: avg of the post_parent for the feature is_submitter


- is_submitter_avg_children: avg of the post_children for the feature is_submitter


- is_submitter_avg_all_children: avg of the post_all_children for the feature is_submitter


- is_submitter_std: std of the post for the feature is_submitter


- is_submitter_std_parent: std of the post_parent for the feature is_submitter


- is_submitter_std_children: std of the post_children for the feature is_submitter


- is_submitter_std_all_children: std of the post_all_children for the feature is_submitter


- is_submitter_max: max of the post for the feature is_submitter


- is_submitter_max_parent: max of the post_parent for the feature is_submitter


- is_submitter_max_children: max of the post_children for the feature is_submitter


- is_submitter_max_all_children: max of the post_all_children for the feature is_submitter


- is_submitter_min: min of the post for the feature is_submitter


- is_submitter_min_parent: min of the post_parent for the feature is_submitter


- is_submitter_min_children: min of the post_children for the feature is_submitter


- is_submitter_min_all_children: min of the post_all_children for the feature is_submitter


- is_submitter_first: first of the post for the feature is_submitter


- is_submitter_first_parent: first of the post_parent for the feature is_submitter


- is_submitter_first_children: first of the post_children for the feature is_submitter


- is_submitter_first_all_children: first of the post_all_children for the feature is_submitter


- is_submitter_last: last of the post for the feature is_submitter


- is_submitter_last_parent: last of the post_parent for the feature is_submitter


- is_submitter_last_children: last of the post_children for the feature is_submitter


- is_submitter_last_all_children: last of the post_all_children for the feature is_submitter


- is_meta_avg: avg of the post for the feature is_meta


- is_meta_avg_parent: avg of the post_parent for the feature is_meta


- is_meta_avg_children: avg of the post_children for the feature is_meta


- is_meta_avg_all_children: avg of the post_all_children for the feature is_meta


- is_meta_std: std of the post for the feature is_meta


- is_meta_std_parent: std of the post_parent for the feature is_meta


- is_meta_std_children: std of the post_children for the feature is_meta


- is_meta_std_all_children: std of the post_all_children for the feature is_meta


- is_meta_max: max of the post for the feature is_meta


- is_meta_max_parent: max of the post_parent for the feature is_meta


- is_meta_max_children: max of the post_children for the feature is_meta


- is_meta_max_all_children: max of the post_all_children for the feature is_meta


- is_meta_min: min of the post for the feature is_meta


- is_meta_min_parent: min of the post_parent for the feature is_meta


- is_meta_min_children: min of the post_children for the feature is_meta


- is_meta_min_all_children: min of the post_all_children for the feature is_meta


- is_meta_first: first of the post for the feature is_meta


- is_meta_first_parent: first of the post_parent for the feature is_meta


- is_meta_first_children: first of the post_children for the feature is_meta


- is_meta_first_all_children: first of the post_all_children for the feature is_meta


- is_meta_last: last of the post for the feature is_meta


- is_meta_last_parent: last of the post_parent for the feature is_meta


- is_meta_last_children: last of the post_children for the feature is_meta


- is_meta_last_all_children: last of the post_all_children for the feature is_meta


- media_only_avg: avg of the post for the feature media_only


- media_only_avg_parent: avg of the post_parent for the feature media_only


- media_only_avg_children: avg of the post_children for the feature media_only


- media_only_avg_all_children: avg of the post_all_children for the feature media_only


- media_only_std: std of the post for the feature media_only


- media_only_std_parent: std of the post_parent for the feature media_only


- media_only_std_children: std of the post_children for the feature media_only


- media_only_std_all_children: std of the post_all_children for the feature media_only


- media_only_max: max of the post for the feature media_only


- media_only_max_parent: max of the post_parent for the feature media_only


- media_only_max_children: max of the post_children for the feature media_only


- media_only_max_all_children: max of the post_all_children for the feature media_only


- media_only_min: min of the post for the feature media_only


- media_only_min_parent: min of the post_parent for the feature media_only


- media_only_min_children: min of the post_children for the feature media_only


- media_only_min_all_children: min of the post_all_children for the feature media_only


- media_only_first: first of the post for the feature media_only


- media_only_first_parent: first of the post_parent for the feature media_only


- media_only_first_children: first of the post_children for the feature media_only


- media_only_first_all_children: first of the post_all_children for the feature media_only


- media_only_last: last of the post for the feature media_only


- media_only_last_parent: last of the post_parent for the feature media_only


- media_only_last_children: last of the post_children for the feature media_only


- media_only_last_all_children: last of the post_all_children for the feature media_only


- whitelist_status_avg: avg of the post for the feature whitelist_status


- whitelist_status_avg_parent: avg of the post_parent for the feature whitelist_status


- whitelist_status_avg_children: avg of the post_children for the feature whitelist_status


- whitelist_status_avg_all_children: avg of the post_all_children for the feature whitelist_status


- whitelist_status_std: std of the post for the feature whitelist_status


- whitelist_status_std_parent: std of the post_parent for the feature whitelist_status


- whitelist_status_std_children: std of the post_children for the feature whitelist_status


- whitelist_status_std_all_children: std of the post_all_children for the feature whitelist_status


- whitelist_status_max: max of the post for the feature whitelist_status


- whitelist_status_max_parent: max of the post_parent for the feature whitelist_status


- whitelist_status_max_children: max of the post_children for the feature whitelist_status


- whitelist_status_max_all_children: max of the post_all_children for the feature whitelist_status


- whitelist_status_min: min of the post for the feature whitelist_status


- whitelist_status_min_parent: min of the post_parent for the feature whitelist_status


- whitelist_status_min_children: min of the post_children for the feature whitelist_status


- whitelist_status_min_all_children: min of the post_all_children for the feature whitelist_status


- whitelist_status_first: first of the post for the feature whitelist_status


- whitelist_status_first_parent: first of the post_parent for the feature whitelist_status


- whitelist_status_first_children: first of the post_children for the feature whitelist_status


- whitelist_status_first_all_children: first of the post_all_children for the feature whitelist_status


- whitelist_status_last: last of the post for the feature whitelist_status


- whitelist_status_last_parent: last of the post_parent for the feature whitelist_status


- whitelist_status_last_children: last of the post_children for the feature whitelist_status


- whitelist_status_last_all_children: last of the post_all_children for the feature whitelist_status


- can_gild_avg: avg of the post for the feature can_gild


- can_gild_avg_parent: avg of the post_parent for the feature can_gild


- can_gild_avg_children: avg of the post_children for the feature can_gild


- can_gild_avg_all_children: avg of the post_all_children for the feature can_gild


- can_gild_std: std of the post for the feature can_gild


- can_gild_std_parent: std of the post_parent for the feature can_gild


- can_gild_std_children: std of the post_children for the feature can_gild


- can_gild_std_all_children: std of the post_all_children for the feature can_gild


- can_gild_max: max of the post for the feature can_gild


- can_gild_max_parent: max of the post_parent for the feature can_gild


- can_gild_max_children: max of the post_children for the feature can_gild


- can_gild_max_all_children: max of the post_all_children for the feature can_gild


- can_gild_min: min of the post for the feature can_gild


- can_gild_min_parent: min of the post_parent for the feature can_gild


- can_gild_min_children: min of the post_children for the feature can_gild


- can_gild_min_all_children: min of the post_all_children for the feature can_gild


- can_gild_first: first of the post for the feature can_gild


- can_gild_first_parent: first of the post_parent for the feature can_gild


- can_gild_first_children: first of the post_children for the feature can_gild


- can_gild_first_all_children: first of the post_all_children for the feature can_gild


- can_gild_last: last of the post for the feature can_gild


- can_gild_last_parent: last of the post_parent for the feature can_gild


- can_gild_last_children: last of the post_children for the feature can_gild


- can_gild_last_all_children: last of the post_all_children for the feature can_gild


- author_premium_avg: avg of the post for the feature author_premium


- author_premium_avg_parent: avg of the post_parent for the feature author_premium


- author_premium_avg_children: avg of the post_children for the feature author_premium


- author_premium_avg_all_children: avg of the post_all_children for the feature author_premium


- author_premium_std: std of the post for the feature author_premium


- author_premium_std_parent: std of the post_parent for the feature author_premium


- author_premium_std_children: std of the post_children for the feature author_premium


- author_premium_std_all_children: std of the post_all_children for the feature author_premium


- author_premium_max: max of the post for the feature author_premium


- author_premium_max_parent: max of the post_parent for the feature author_premium


- author_premium_max_children: max of the post_children for the feature author_premium


- author_premium_max_all_children: max of the post_all_children for the feature author_premium


- author_premium_min: min of the post for the feature author_premium


- author_premium_min_parent: min of the post_parent for the feature author_premium


- author_premium_min_children: min of the post_children for the feature author_premium


- author_premium_min_all_children: min of the post_all_children for the feature author_premium


- author_premium_first: first of the post for the feature author_premium


- author_premium_first_parent: first of the post_parent for the feature author_premium


- author_premium_first_children: first of the post_children for the feature author_premium


- author_premium_first_all_children: first of the post_all_children for the feature author_premium


- author_premium_last: last of the post for the feature author_premium


- author_premium_last_parent: last of the post_parent for the feature author_premium


- author_premium_last_children: last of the post_children for the feature author_premium


- author_premium_last_all_children: last of the post_all_children for the feature author_premium


- comment_type_avg: avg of the post for the feature comment_type


- comment_type_avg_parent: avg of the post_parent for the feature comment_type


- comment_type_avg_children: avg of the post_children for the feature comment_type


- comment_type_avg_all_children: avg of the post_all_children for the feature comment_type


- comment_type_std: std of the post for the feature comment_type


- comment_type_std_parent: std of the post_parent for the feature comment_type


- comment_type_std_children: std of the post_children for the feature comment_type


- comment_type_std_all_children: std of the post_all_children for the feature comment_type


- comment_type_max: max of the post for the feature comment_type


- comment_type_max_parent: max of the post_parent for the feature comment_type


- comment_type_max_children: max of the post_children for the feature comment_type


- comment_type_max_all_children: max of the post_all_children for the feature comment_type


- comment_type_min: min of the post for the feature comment_type


- comment_type_min_parent: min of the post_parent for the feature comment_type


- comment_type_min_children: min of the post_children for the feature comment_type


- comment_type_min_all_children: min of the post_all_children for the feature comment_type


- comment_type_first: first of the post for the feature comment_type


- comment_type_first_parent: first of the post_parent for the feature comment_type


- comment_type_first_children: first of the post_children for the feature comment_type


- comment_type_first_all_children: first of the post_all_children for the feature comment_type


- comment_type_last: last of the post for the feature comment_type


- comment_type_last_parent: last of the post_parent for the feature comment_type


- comment_type_last_children: last of the post_children for the feature comment_type


- comment_type_last_all_children: last of the post_all_children for the feature comment_type


- hidden_avg: avg of the post for the feature hidden


- hidden_avg_parent: avg of the post_parent for the feature hidden


- hidden_avg_children: avg of the post_children for the feature hidden


- hidden_avg_all_children: avg of the post_all_children for the feature hidden


- hidden_std: std of the post for the feature hidden


- hidden_std_parent: std of the post_parent for the feature hidden


- hidden_std_children: std of the post_children for the feature hidden


- hidden_std_all_children: std of the post_all_children for the feature hidden


- hidden_max: max of the post for the feature hidden


- hidden_max_parent: max of the post_parent for the feature hidden


- hidden_max_children: max of the post_children for the feature hidden


- hidden_max_all_children: max of the post_all_children for the feature hidden


- hidden_min: min of the post for the feature hidden


- hidden_min_parent: min of the post_parent for the feature hidden


- hidden_min_children: min of the post_children for the feature hidden


- hidden_min_all_children: min of the post_all_children for the feature hidden


- hidden_first: first of the post for the feature hidden


- hidden_first_parent: first of the post_parent for the feature hidden


- hidden_first_children: first of the post_children for the feature hidden


- hidden_first_all_children: first of the post_all_children for the feature hidden


- hidden_last: last of the post for the feature hidden


- hidden_last_parent: last of the post_parent for the feature hidden


- hidden_last_children: last of the post_children for the feature hidden


- hidden_last_all_children: last of the post_all_children for the feature hidden


- banned_by_someone_avg: avg of the post for the feature banned_by_someone


- banned_by_someone_avg_parent: avg of the post_parent for the feature banned_by_someone


- banned_by_someone_avg_children: avg of the post_children for the feature banned_by_someone


- banned_by_someone_avg_all_children: avg of the post_all_children for the feature banned_by_someone


- banned_by_someone_std: std of the post for the feature banned_by_someone


- banned_by_someone_std_parent: std of the post_parent for the feature banned_by_someone


- banned_by_someone_std_children: std of the post_children for the feature banned_by_someone


- banned_by_someone_std_all_children: std of the post_all_children for the feature banned_by_someone


- banned_by_someone_max: max of the post for the feature banned_by_someone


- banned_by_someone_max_parent: max of the post_parent for the feature banned_by_someone


- banned_by_someone_max_children: max of the post_children for the feature banned_by_someone


- banned_by_someone_max_all_children: max of the post_all_children for the feature banned_by_someone


- banned_by_someone_min: min of the post for the feature banned_by_someone


- banned_by_someone_min_parent: min of the post_parent for the feature banned_by_someone


- banned_by_someone_min_children: min of the post_children for the feature banned_by_someone


- banned_by_someone_min_all_children: min of the post_all_children for the feature banned_by_someone


- banned_by_someone_first: first of the post for the feature banned_by_someone


- banned_by_someone_first_parent: first of the post_parent for the feature banned_by_someone


- banned_by_someone_first_children: first of the post_children for the feature banned_by_someone


- banned_by_someone_first_all_children: first of the post_all_children for the feature banned_by_someone


- banned_by_someone_last: last of the post for the feature banned_by_someone


- banned_by_someone_last_parent: last of the post_parent for the feature banned_by_someone


- banned_by_someone_last_children: last of the post_children for the feature banned_by_someone


- banned_by_someone_last_all_children: last of the post_all_children for the feature banned_by_someone


- link_flair_background_color_avg: avg of the post for the feature link_flair_background_color


- link_flair_background_color_avg_parent: avg of the post_parent for the feature link_flair_background_color


- link_flair_background_color_avg_children: avg of the post_children for the feature link_flair_background_color


- link_flair_background_color_avg_all_children: avg of the post_all_children for the feature link_flair_background_color


- link_flair_background_color_std: std of the post for the feature link_flair_background_color


- link_flair_background_color_std_parent: std of the post_parent for the feature link_flair_background_color


- link_flair_background_color_std_children: std of the post_children for the feature link_flair_background_color


- link_flair_background_color_std_all_children: std of the post_all_children for the feature link_flair_background_color


- link_flair_background_color_max: max of the post for the feature link_flair_background_color


- link_flair_background_color_max_parent: max of the post_parent for the feature link_flair_background_color


- link_flair_background_color_max_children: max of the post_children for the feature link_flair_background_color


- link_flair_background_color_max_all_children: max of the post_all_children for the feature link_flair_background_color


- link_flair_background_color_min: min of the post for the feature link_flair_background_color


- link_flair_background_color_min_parent: min of the post_parent for the feature link_flair_background_color


- link_flair_background_color_min_children: min of the post_children for the feature link_flair_background_color


- link_flair_background_color_min_all_children: min of the post_all_children for the feature link_flair_background_color


- link_flair_background_color_first: first of the post for the feature link_flair_background_color


- link_flair_background_color_first_parent: first of the post_parent for the feature link_flair_background_color


- link_flair_background_color_first_children: first of the post_children for the feature link_flair_background_color


- link_flair_background_color_first_all_children: first of the post_all_children for the feature link_flair_background_color


- link_flair_background_color_last: last of the post for the feature link_flair_background_color


- link_flair_background_color_last_parent: last of the post_parent for the feature link_flair_background_color


- link_flair_background_color_last_children: last of the post_children for the feature link_flair_background_color


- link_flair_background_color_last_all_children: last of the post_all_children for the feature link_flair_background_color


- subreddit_id_avg: avg of the post for the feature subreddit_id


- subreddit_id_avg_parent: avg of the post_parent for the feature subreddit_id


- subreddit_id_avg_children: avg of the post_children for the feature subreddit_id


- subreddit_id_avg_all_children: avg of the post_all_children for the feature subreddit_id


- subreddit_id_std: std of the post for the feature subreddit_id


- subreddit_id_std_parent: std of the post_parent for the feature subreddit_id


- subreddit_id_std_children: std of the post_children for the feature subreddit_id


- subreddit_id_std_all_children: std of the post_all_children for the feature subreddit_id


- subreddit_id_max: max of the post for the feature subreddit_id


- subreddit_id_max_parent: max of the post_parent for the feature subreddit_id


- subreddit_id_max_children: max of the post_children for the feature subreddit_id


- subreddit_id_max_all_children: max of the post_all_children for the feature subreddit_id


- subreddit_id_min: min of the post for the feature subreddit_id


- subreddit_id_min_parent: min of the post_parent for the feature subreddit_id


- subreddit_id_min_children: min of the post_children for the feature subreddit_id


- subreddit_id_min_all_children: min of the post_all_children for the feature subreddit_id


- subreddit_id_first: first of the post for the feature subreddit_id


- subreddit_id_first_parent: first of the post_parent for the feature subreddit_id


- subreddit_id_first_children: first of the post_children for the feature subreddit_id


- subreddit_id_first_all_children: first of the post_all_children for the feature subreddit_id


- subreddit_id_last: last of the post for the feature subreddit_id


- subreddit_id_last_parent: last of the post_parent for the feature subreddit_id


- subreddit_id_last_children: last of the post_children for the feature subreddit_id


- subreddit_id_last_all_children: last of the post_all_children for the feature subreddit_id


- upvote_ratio_avg: avg of the post for the feature upvote_ratio


- upvote_ratio_avg_parent: avg of the post_parent for the feature upvote_ratio


- upvote_ratio_avg_children: avg of the post_children for the feature upvote_ratio


- upvote_ratio_avg_all_children: avg of the post_all_children for the feature upvote_ratio


- upvote_ratio_std: std of the post for the feature upvote_ratio


- upvote_ratio_std_parent: std of the post_parent for the feature upvote_ratio


- upvote_ratio_std_children: std of the post_children for the feature upvote_ratio


- upvote_ratio_std_all_children: std of the post_all_children for the feature upvote_ratio


- upvote_ratio_max: max of the post for the feature upvote_ratio


- upvote_ratio_max_parent: max of the post_parent for the feature upvote_ratio


- upvote_ratio_max_children: max of the post_children for the feature upvote_ratio


- upvote_ratio_max_all_children: max of the post_all_children for the feature upvote_ratio


- upvote_ratio_min: min of the post for the feature upvote_ratio


- upvote_ratio_min_parent: min of the post_parent for the feature upvote_ratio


- upvote_ratio_min_children: min of the post_children for the feature upvote_ratio


- upvote_ratio_min_all_children: min of the post_all_children for the feature upvote_ratio


- upvote_ratio_first: first of the post for the feature upvote_ratio


- upvote_ratio_first_parent: first of the post_parent for the feature upvote_ratio


- upvote_ratio_first_children: first of the post_children for the feature upvote_ratio


- upvote_ratio_first_all_children: first of the post_all_children for the feature upvote_ratio


- upvote_ratio_last: last of the post for the feature upvote_ratio


- upvote_ratio_last_parent: last of the post_parent for the feature upvote_ratio


- upvote_ratio_last_children: last of the post_children for the feature upvote_ratio


- upvote_ratio_last_all_children: last of the post_all_children for the feature upvote_ratio


- num_of_guildings_avg: avg of the post for the feature num_of_guildings


- num_of_guildings_avg_parent: avg of the post_parent for the feature num_of_guildings


- num_of_guildings_avg_children: avg of the post_children for the feature num_of_guildings


- num_of_guildings_avg_all_children: avg of the post_all_children for the feature num_of_guildings


- num_of_guildings_std: std of the post for the feature num_of_guildings


- num_of_guildings_std_parent: std of the post_parent for the feature num_of_guildings


- num_of_guildings_std_children: std of the post_children for the feature num_of_guildings


- num_of_guildings_std_all_children: std of the post_all_children for the feature num_of_guildings


- num_of_guildings_max: max of the post for the feature num_of_guildings


- num_of_guildings_max_parent: max of the post_parent for the feature num_of_guildings


- num_of_guildings_max_children: max of the post_children for the feature num_of_guildings


- num_of_guildings_max_all_children: max of the post_all_children for the feature num_of_guildings


- num_of_guildings_min: min of the post for the feature num_of_guildings


- num_of_guildings_min_parent: min of the post_parent for the feature num_of_guildings


- num_of_guildings_min_children: min of the post_children for the feature num_of_guildings


- num_of_guildings_min_all_children: min of the post_all_children for the feature num_of_guildings


- num_of_guildings_first: first of the post for the feature num_of_guildings


- num_of_guildings_first_parent: first of the post_parent for the feature num_of_guildings


- num_of_guildings_first_children: first of the post_children for the feature num_of_guildings


- num_of_guildings_first_all_children: first of the post_all_children for the feature num_of_guildings


- num_of_guildings_last: last of the post for the feature num_of_guildings


- num_of_guildings_last_parent: last of the post_parent for the feature num_of_guildings


- num_of_guildings_last_children: last of the post_children for the feature num_of_guildings


- num_of_guildings_last_all_children: last of the post_all_children for the feature num_of_guildings


- can_mod_post_avg: avg of the post for the feature can_mod_post


- can_mod_post_avg_parent: avg of the post_parent for the feature can_mod_post


- can_mod_post_avg_children: avg of the post_children for the feature can_mod_post


- can_mod_post_avg_all_children: avg of the post_all_children for the feature can_mod_post


- can_mod_post_std: std of the post for the feature can_mod_post


- can_mod_post_std_parent: std of the post_parent for the feature can_mod_post


- can_mod_post_std_children: std of the post_children for the feature can_mod_post


- can_mod_post_std_all_children: std of the post_all_children for the feature can_mod_post


- can_mod_post_max: max of the post for the feature can_mod_post


- can_mod_post_max_parent: max of the post_parent for the feature can_mod_post


- can_mod_post_max_children: max of the post_children for the feature can_mod_post


- can_mod_post_max_all_children: max of the post_all_children for the feature can_mod_post


- can_mod_post_min: min of the post for the feature can_mod_post


- can_mod_post_min_parent: min of the post_parent for the feature can_mod_post


- can_mod_post_min_children: min of the post_children for the feature can_mod_post


- can_mod_post_min_all_children: min of the post_all_children for the feature can_mod_post


- can_mod_post_first: first of the post for the feature can_mod_post


- can_mod_post_first_parent: first of the post_parent for the feature can_mod_post


- can_mod_post_first_children: first of the post_children for the feature can_mod_post


- can_mod_post_first_all_children: first of the post_all_children for the feature can_mod_post


- can_mod_post_last: last of the post for the feature can_mod_post


- can_mod_post_last_parent: last of the post_parent for the feature can_mod_post


- can_mod_post_last_children: last of the post_children for the feature can_mod_post


- can_mod_post_last_all_children: last of the post_all_children for the feature can_mod_post


- score_hidden_avg: avg of the post for the feature score_hidden


- score_hidden_avg_parent: avg of the post_parent for the feature score_hidden


- score_hidden_avg_children: avg of the post_children for the feature score_hidden


- score_hidden_avg_all_children: avg of the post_all_children for the feature score_hidden


- score_hidden_std: std of the post for the feature score_hidden


- score_hidden_std_parent: std of the post_parent for the feature score_hidden


- score_hidden_std_children: std of the post_children for the feature score_hidden


- score_hidden_std_all_children: std of the post_all_children for the feature score_hidden


- score_hidden_max: max of the post for the feature score_hidden


- score_hidden_max_parent: max of the post_parent for the feature score_hidden


- score_hidden_max_children: max of the post_children for the feature score_hidden


- score_hidden_max_all_children: max of the post_all_children for the feature score_hidden


- score_hidden_min: min of the post for the feature score_hidden


- score_hidden_min_parent: min of the post_parent for the feature score_hidden


- score_hidden_min_children: min of the post_children for the feature score_hidden


- score_hidden_min_all_children: min of the post_all_children for the feature score_hidden


- score_hidden_first: first of the post for the feature score_hidden


- score_hidden_first_parent: first of the post_parent for the feature score_hidden


- score_hidden_first_children: first of the post_children for the feature score_hidden


- score_hidden_first_all_children: first of the post_all_children for the feature score_hidden


- score_hidden_last: last of the post for the feature score_hidden


- score_hidden_last_parent: last of the post_parent for the feature score_hidden


- score_hidden_last_children: last of the post_children for the feature score_hidden


- score_hidden_last_all_children: last of the post_all_children for the feature score_hidden


- treatment_tags_avg: avg of the post for the feature treatment_tags


- treatment_tags_avg_parent: avg of the post_parent for the feature treatment_tags


- treatment_tags_avg_children: avg of the post_children for the feature treatment_tags


- treatment_tags_avg_all_children: avg of the post_all_children for the feature treatment_tags


- treatment_tags_std: std of the post for the feature treatment_tags


- treatment_tags_std_parent: std of the post_parent for the feature treatment_tags


- treatment_tags_std_children: std of the post_children for the feature treatment_tags


- treatment_tags_std_all_children: std of the post_all_children for the feature treatment_tags


- treatment_tags_max: max of the post for the feature treatment_tags


- treatment_tags_max_parent: max of the post_parent for the feature treatment_tags


- treatment_tags_max_children: max of the post_children for the feature treatment_tags


- treatment_tags_max_all_children: max of the post_all_children for the feature treatment_tags


- treatment_tags_min: min of the post for the feature treatment_tags


- treatment_tags_min_parent: min of the post_parent for the feature treatment_tags


- treatment_tags_min_children: min of the post_children for the feature treatment_tags


- treatment_tags_min_all_children: min of the post_all_children for the feature treatment_tags


- treatment_tags_first: first of the post for the feature treatment_tags


- treatment_tags_first_parent: first of the post_parent for the feature treatment_tags


- treatment_tags_first_children: first of the post_children for the feature treatment_tags


- treatment_tags_first_all_children: first of the post_all_children for the feature treatment_tags


- treatment_tags_last: last of the post for the feature treatment_tags


- treatment_tags_last_parent: last of the post_parent for the feature treatment_tags


- treatment_tags_last_children: last of the post_children for the feature treatment_tags


- treatment_tags_last_all_children: last of the post_all_children for the feature treatment_tags


- allow_live_comments_avg: avg of the post for the feature allow_live_comments


- allow_live_comments_avg_parent: avg of the post_parent for the feature allow_live_comments


- allow_live_comments_avg_children: avg of the post_children for the feature allow_live_comments


- allow_live_comments_avg_all_children: avg of the post_all_children for the feature allow_live_comments


- allow_live_comments_std: std of the post for the feature allow_live_comments


- allow_live_comments_std_parent: std of the post_parent for the feature allow_live_comments


- allow_live_comments_std_children: std of the post_children for the feature allow_live_comments


- allow_live_comments_std_all_children: std of the post_all_children for the feature allow_live_comments


- allow_live_comments_max: max of the post for the feature allow_live_comments


- allow_live_comments_max_parent: max of the post_parent for the feature allow_live_comments


- allow_live_comments_max_children: max of the post_children for the feature allow_live_comments


- allow_live_comments_max_all_children: max of the post_all_children for the feature allow_live_comments


- allow_live_comments_min: min of the post for the feature allow_live_comments


- allow_live_comments_min_parent: min of the post_parent for the feature allow_live_comments


- allow_live_comments_min_children: min of the post_children for the feature allow_live_comments


- allow_live_comments_min_all_children: min of the post_all_children for the feature allow_live_comments


- allow_live_comments_first: first of the post for the feature allow_live_comments


- allow_live_comments_first_parent: first of the post_parent for the feature allow_live_comments


- allow_live_comments_first_children: first of the post_children for the feature allow_live_comments


- allow_live_comments_first_all_children: first of the post_all_children for the feature allow_live_comments


- allow_live_comments_last: last of the post for the feature allow_live_comments


- allow_live_comments_last_parent: last of the post_parent for the feature allow_live_comments


- allow_live_comments_last_children: last of the post_children for the feature allow_live_comments


- allow_live_comments_last_all_children: last of the post_all_children for the feature allow_live_comments


- num_of_gildings_avg: avg of the post for the feature num_of_gildings


- num_of_gildings_avg_parent: avg of the post_parent for the feature num_of_gildings


- num_of_gildings_avg_children: avg of the post_children for the feature num_of_gildings


- num_of_gildings_avg_all_children: avg of the post_all_children for the feature num_of_gildings


- num_of_gildings_std: std of the post for the feature num_of_gildings


- num_of_gildings_std_parent: std of the post_parent for the feature num_of_gildings


- num_of_gildings_std_children: std of the post_children for the feature num_of_gildings


- num_of_gildings_std_all_children: std of the post_all_children for the feature num_of_gildings


- num_of_gildings_max: max of the post for the feature num_of_gildings


- num_of_gildings_max_parent: max of the post_parent for the feature num_of_gildings


- num_of_gildings_max_children: max of the post_children for the feature num_of_gildings


- num_of_gildings_max_all_children: max of the post_all_children for the feature num_of_gildings


- num_of_gildings_min: min of the post for the feature num_of_gildings


- num_of_gildings_min_parent: min of the post_parent for the feature num_of_gildings


- num_of_gildings_min_children: min of the post_children for the feature num_of_gildings


- num_of_gildings_min_all_children: min of the post_all_children for the feature num_of_gildings


- num_of_gildings_first: first of the post for the feature num_of_gildings


- num_of_gildings_first_parent: first of the post_parent for the feature num_of_gildings


- num_of_gildings_first_children: first of the post_children for the feature num_of_gildings


- num_of_gildings_first_all_children: first of the post_all_children for the feature num_of_gildings


- num_of_gildings_last: last of the post for the feature num_of_gildings


- num_of_gildings_last_parent: last of the post_parent for the feature num_of_gildings


- num_of_gildings_last_children: last of the post_children for the feature num_of_gildings


- num_of_gildings_last_all_children: last of the post_all_children for the feature num_of_gildings


- link_flair_css_class_avg: avg of the post for the feature link_flair_css_class


- link_flair_css_class_avg_parent: avg of the post_parent for the feature link_flair_css_class


- link_flair_css_class_avg_children: avg of the post_children for the feature link_flair_css_class


- link_flair_css_class_avg_all_children: avg of the post_all_children for the feature link_flair_css_class


- link_flair_css_class_std: std of the post for the feature link_flair_css_class


- link_flair_css_class_std_parent: std of the post_parent for the feature link_flair_css_class


- link_flair_css_class_std_children: std of the post_children for the feature link_flair_css_class


- link_flair_css_class_std_all_children: std of the post_all_children for the feature link_flair_css_class


- link_flair_css_class_max: max of the post for the feature link_flair_css_class


- link_flair_css_class_max_parent: max of the post_parent for the feature link_flair_css_class


- link_flair_css_class_max_children: max of the post_children for the feature link_flair_css_class


- link_flair_css_class_max_all_children: max of the post_all_children for the feature link_flair_css_class


- link_flair_css_class_min: min of the post for the feature link_flair_css_class


- link_flair_css_class_min_parent: min of the post_parent for the feature link_flair_css_class


- link_flair_css_class_min_children: min of the post_children for the feature link_flair_css_class


- link_flair_css_class_min_all_children: min of the post_all_children for the feature link_flair_css_class


- link_flair_css_class_first: first of the post for the feature link_flair_css_class


- link_flair_css_class_first_parent: first of the post_parent for the feature link_flair_css_class


- link_flair_css_class_first_children: first of the post_children for the feature link_flair_css_class


- link_flair_css_class_first_all_children: first of the post_all_children for the feature link_flair_css_class


- link_flair_css_class_last: last of the post for the feature link_flair_css_class


- link_flair_css_class_last_parent: last of the post_parent for the feature link_flair_css_class


- link_flair_css_class_last_children: last of the post_children for the feature link_flair_css_class


- link_flair_css_class_last_all_children: last of the post_all_children for the feature link_flair_css_class


- gilded_avg: avg of the post for the feature gilded


- gilded_avg_parent: avg of the post_parent for the feature gilded


- gilded_avg_children: avg of the post_children for the feature gilded


- gilded_avg_all_children: avg of the post_all_children for the feature gilded


- gilded_std: std of the post for the feature gilded


- gilded_std_parent: std of the post_parent for the feature gilded


- gilded_std_children: std of the post_children for the feature gilded


- gilded_std_all_children: std of the post_all_children for the feature gilded


- gilded_max: max of the post for the feature gilded


- gilded_max_parent: max of the post_parent for the feature gilded


- gilded_max_children: max of the post_children for the feature gilded


- gilded_max_all_children: max of the post_all_children for the feature gilded


- gilded_min: min of the post for the feature gilded


- gilded_min_parent: min of the post_parent for the feature gilded


- gilded_min_children: min of the post_children for the feature gilded


- gilded_min_all_children: min of the post_all_children for the feature gilded


- gilded_first: first of the post for the feature gilded


- gilded_first_parent: first of the post_parent for the feature gilded


- gilded_first_children: first of the post_children for the feature gilded


- gilded_first_all_children: first of the post_all_children for the feature gilded


- gilded_last: last of the post for the feature gilded


- gilded_last_parent: last of the post_parent for the feature gilded


- gilded_last_children: last of the post_children for the feature gilded


- gilded_last_all_children: last of the post_all_children for the feature gilded


- is_original_content_avg: avg of the post for the feature is_original_content


- is_original_content_avg_parent: avg of the post_parent for the feature is_original_content


- is_original_content_avg_children: avg of the post_children for the feature is_original_content


- is_original_content_avg_all_children: avg of the post_all_children for the feature is_original_content


- is_original_content_std: std of the post for the feature is_original_content


- is_original_content_std_parent: std of the post_parent for the feature is_original_content


- is_original_content_std_children: std of the post_children for the feature is_original_content


- is_original_content_std_all_children: std of the post_all_children for the feature is_original_content


- is_original_content_max: max of the post for the feature is_original_content


- is_original_content_max_parent: max of the post_parent for the feature is_original_content


- is_original_content_max_children: max of the post_children for the feature is_original_content


- is_original_content_max_all_children: max of the post_all_children for the feature is_original_content


- is_original_content_min: min of the post for the feature is_original_content


- is_original_content_min_parent: min of the post_parent for the feature is_original_content


- is_original_content_min_children: min of the post_children for the feature is_original_content


- is_original_content_min_all_children: min of the post_all_children for the feature is_original_content


- is_original_content_first: first of the post for the feature is_original_content


- is_original_content_first_parent: first of the post_parent for the feature is_original_content


- is_original_content_first_children: first of the post_children for the feature is_original_content


- is_original_content_first_all_children: first of the post_all_children for the feature is_original_content


- is_original_content_last: last of the post for the feature is_original_content


- is_original_content_last_parent: last of the post_parent for the feature is_original_content


- is_original_content_last_children: last of the post_children for the feature is_original_content


- is_original_content_last_all_children: last of the post_all_children for the feature is_original_content


- hide_score_avg: avg of the post for the feature hide_score


- hide_score_avg_parent: avg of the post_parent for the feature hide_score


- hide_score_avg_children: avg of the post_children for the feature hide_score


- hide_score_avg_all_children: avg of the post_all_children for the feature hide_score


- hide_score_std: std of the post for the feature hide_score


- hide_score_std_parent: std of the post_parent for the feature hide_score


- hide_score_std_children: std of the post_children for the feature hide_score


- hide_score_std_all_children: std of the post_all_children for the feature hide_score


- hide_score_max: max of the post for the feature hide_score


- hide_score_max_parent: max of the post_parent for the feature hide_score


- hide_score_max_children: max of the post_children for the feature hide_score


- hide_score_max_all_children: max of the post_all_children for the feature hide_score


- hide_score_min: min of the post for the feature hide_score


- hide_score_min_parent: min of the post_parent for the feature hide_score


- hide_score_min_children: min of the post_children for the feature hide_score


- hide_score_min_all_children: min of the post_all_children for the feature hide_score


- hide_score_first: first of the post for the feature hide_score


- hide_score_first_parent: first of the post_parent for the feature hide_score


- hide_score_first_children: first of the post_children for the feature hide_score


- hide_score_first_all_children: first of the post_all_children for the feature hide_score


- hide_score_last: last of the post for the feature hide_score


- hide_score_last_parent: last of the post_parent for the feature hide_score


- hide_score_last_children: last of the post_children for the feature hide_score


- hide_score_last_all_children: last of the post_all_children for the feature hide_score


- have_unrepliable_reason_avg: avg of the post for the feature have_unrepliable_reason


- have_unrepliable_reason_avg_parent: avg of the post_parent for the feature have_unrepliable_reason


- have_unrepliable_reason_avg_children: avg of the post_children for the feature have_unrepliable_reason


- have_unrepliable_reason_avg_all_children: avg of the post_all_children for the feature have_unrepliable_reason


- have_unrepliable_reason_std: std of the post for the feature have_unrepliable_reason


- have_unrepliable_reason_std_parent: std of the post_parent for the feature have_unrepliable_reason


- have_unrepliable_reason_std_children: std of the post_children for the feature have_unrepliable_reason


- have_unrepliable_reason_std_all_children: std of the post_all_children for the feature have_unrepliable_reason


- have_unrepliable_reason_max: max of the post for the feature have_unrepliable_reason


- have_unrepliable_reason_max_parent: max of the post_parent for the feature have_unrepliable_reason


- have_unrepliable_reason_max_children: max of the post_children for the feature have_unrepliable_reason


- have_unrepliable_reason_max_all_children: max of the post_all_children for the feature have_unrepliable_reason


- have_unrepliable_reason_min: min of the post for the feature have_unrepliable_reason


- have_unrepliable_reason_min_parent: min of the post_parent for the feature have_unrepliable_reason


- have_unrepliable_reason_min_children: min of the post_children for the feature have_unrepliable_reason


- have_unrepliable_reason_min_all_children: min of the post_all_children for the feature have_unrepliable_reason


- have_unrepliable_reason_first: first of the post for the feature have_unrepliable_reason


- have_unrepliable_reason_first_parent: first of the post_parent for the feature have_unrepliable_reason


- have_unrepliable_reason_first_children: first of the post_children for the feature have_unrepliable_reason


- have_unrepliable_reason_first_all_children: first of the post_all_children for the feature have_unrepliable_reason


- have_unrepliable_reason_last: last of the post for the feature have_unrepliable_reason


- have_unrepliable_reason_last_parent: last of the post_parent for the feature have_unrepliable_reason


- have_unrepliable_reason_last_children: last of the post_children for the feature have_unrepliable_reason


- have_unrepliable_reason_last_all_children: last of the post_all_children for the feature have_unrepliable_reason


- is_crosspostable_avg: avg of the post for the feature is_crosspostable


- is_crosspostable_avg_parent: avg of the post_parent for the feature is_crosspostable


- is_crosspostable_avg_children: avg of the post_children for the feature is_crosspostable


- is_crosspostable_avg_all_children: avg of the post_all_children for the feature is_crosspostable


- is_crosspostable_std: std of the post for the feature is_crosspostable


- is_crosspostable_std_parent: std of the post_parent for the feature is_crosspostable


- is_crosspostable_std_children: std of the post_children for the feature is_crosspostable


- is_crosspostable_std_all_children: std of the post_all_children for the feature is_crosspostable


- is_crosspostable_max: max of the post for the feature is_crosspostable


- is_crosspostable_max_parent: max of the post_parent for the feature is_crosspostable


- is_crosspostable_max_children: max of the post_children for the feature is_crosspostable


- is_crosspostable_max_all_children: max of the post_all_children for the feature is_crosspostable


- is_crosspostable_min: min of the post for the feature is_crosspostable


- is_crosspostable_min_parent: min of the post_parent for the feature is_crosspostable


- is_crosspostable_min_children: min of the post_children for the feature is_crosspostable


- is_crosspostable_min_all_children: min of the post_all_children for the feature is_crosspostable


- is_crosspostable_first: first of the post for the feature is_crosspostable


- is_crosspostable_first_parent: first of the post_parent for the feature is_crosspostable


- is_crosspostable_first_children: first of the post_children for the feature is_crosspostable


- is_crosspostable_first_all_children: first of the post_all_children for the feature is_crosspostable


- is_crosspostable_last: last of the post for the feature is_crosspostable


- is_crosspostable_last_parent: last of the post_parent for the feature is_crosspostable


- is_crosspostable_last_children: last of the post_children for the feature is_crosspostable


- is_crosspostable_last_all_children: last of the post_all_children for the feature is_crosspostable

### sentiment


- sentiment_avg_avgfor_user: avg of the sentiment of the observation window for the user


- sentiment_std_avgfor_user: avg of the sentiment of the observation window for the user


- num_of_pos_avgfor_user: avg of the sentiment of the observation window for the user


- num_of_neg_avgfor_user: avg of the sentiment of the observation window for the user


- num_of_neu_avgfor_user: avg of the sentiment of the observation window for the user


- num_of_pos_neg_ratio_avgfor_user: avg of the sentiment of the observation window for the user


- most_sentiment_avgfor_user: avg of the sentiment of the observation window for the user


- times_of_most_sentiment_avgfor_user: avg of the sentiment of the observation window for the user


- times_of_sentiment_change_avgfor_user: avg of the sentiment of the observation window for the user


- times_of_sentiment_change_ratio_avgfor_user: avg of the sentiment of the observation window for the user


- times_of_sentiment_change_ratio_strong_avgfor_user: avg of the sentiment of the observation window for the user


- times_of_sentiment_keep_avgfor_user: avg of the sentiment of the observation window for the user


- times_of_sentiment_keep_ratio_avgfor_user: avg of the sentiment of the observation window for the user


- times_of_sentiment_keep_ratio_strong_avgfor_user: avg of the sentiment of the observation window for the user


- times_of_sentiment_keep_ratio_weak_avgfor_user: avg of the sentiment of the observation window for the user


- the_first_sentiment_avgfor_user: avg of the sentiment of the observation window for the user


- the_last_sentiment_avgfor_user: avg of the sentiment of the observation window for the user


- the_first_sentiment_ratio_avgfor_user: avg of the sentiment of the observation window for the user


- the_last_sentiment_ratio_avgfor_user: avg of the sentiment of the observation window for the user


- the_first_sentiment_ratio_strong_avgfor_user: avg of the sentiment of the observation window for the user


- the_last_sentiment_ratio_strong_avgfor_user: avg of the sentiment of the observation window for the user


- parent_sentiment_avg_avgfor_user: avg of the sentiment of the parent of the post for the user


- parent_sentiment_std_avgfor_user: avg of the sentiment of the parent of the post for the user


- parent_num_of_pos_avgfor_user: avg of the sentiment of the parent of the post for the user


- parent_num_of_neg_avgfor_user: avg of the sentiment of the parent of the post for the user


- parent_num_of_neu_avgfor_user: avg of the sentiment of the parent of the post for the user


- parent_num_of_pos_neg_ratio_avgfor_user: avg of the sentiment of the parent of the post for the user


- parent_most_sentiment_avgfor_user: avg of the sentiment of the parent of the post for the user


- parent_times_of_most_sentiment_avgfor_user: avg of the sentiment of the parent of the post for the user


- parent_times_of_sentiment_change_avgfor_user: avg of the sentiment of the parent of the post for the user


- parent_times_of_sentiment_change_ratio_avgfor_user: avg of the sentiment of the parent of the post for the user


- parent_times_of_sentiment_change_ratio_strong_avgfor_user: avg of the sentiment of the parent of the post for the user


- parent_times_of_sentiment_keep_avgfor_user: avg of the sentiment of the parent of the post for the user


- parent_times_of_sentiment_keep_ratio_avgfor_user: avg of the sentiment of the parent of the post for the user


- parent_times_of_sentiment_keep_ratio_strong_avgfor_user: avg of the sentiment of the parent of the post for the user


- parent_times_of_sentiment_keep_ratio_weak_avgfor_user: avg of the sentiment of the parent of the post for the user


- parent_the_first_sentiment_avgfor_user: avg of the sentiment of the parent of the post for the user


- parent_the_last_sentiment_avgfor_user: avg of the sentiment of the parent of the post for the user


- parent_the_first_sentiment_ratio_avgfor_user: avg of the sentiment of the parent of the post for the user


- parent_the_last_sentiment_ratio_avgfor_user: avg of the sentiment of the parent of the post for the user


- parent_the_first_sentiment_ratio_strong_avgfor_user: avg of the sentiment of the parent of the post for the user


- parent_the_last_sentiment_ratio_strong_avgfor_user: avg of the sentiment of the parent of the post for the user


- children_sentiment_avg_avgfor_user: avg of the sentiment of the children of the post for the user


- children_sentiment_std_avgfor_user: avg of the sentiment of the children of the post for the user


- children_num_of_pos_avgfor_user: avg of the sentiment of the children of the post for the user


- children_num_of_neg_avgfor_user: avg of the sentiment of the children of the post for the user


- children_num_of_neu_avgfor_user: avg of the sentiment of the children of the post for the user


- children_num_of_pos_neg_ratio_avgfor_user: avg of the sentiment of the children of the post for the user


- children_most_sentiment_avgfor_user: avg of the sentiment of the children of the post for the user


- children_times_of_most_sentiment_avgfor_user: avg of the sentiment of the children of the post for the user


- children_times_of_sentiment_change_avgfor_user: avg of the sentiment of the children of the post for the user


- children_times_of_sentiment_change_ratio_avgfor_user: avg of the sentiment of the children of the post for the user


- children_times_of_sentiment_change_ratio_strong_avgfor_user: avg of the sentiment of the children of the post for the user


- children_times_of_sentiment_keep_avgfor_user: avg of the sentiment of the children of the post for the user


- children_times_of_sentiment_keep_ratio_avgfor_user: avg of the sentiment of the children of the post for the user


- children_times_of_sentiment_keep_ratio_strong_avgfor_user: avg of the sentiment of the children of the post for the user


- children_times_of_sentiment_keep_ratio_weak_avgfor_user: avg of the sentiment of the children of the post for the user


- children_the_first_sentiment_avgfor_user: avg of the sentiment of the children of the post for the user


- children_the_last_sentiment_avgfor_user: avg of the sentiment of the children of the post for the user


- children_the_first_sentiment_ratio_avgfor_user: avg of the sentiment of the children of the post for the user


- children_the_last_sentiment_ratio_avgfor_user: avg of the sentiment of the children of the post for the user


- children_the_first_sentiment_ratio_strong_avgfor_user: avg of the sentiment of the children of the post for the user


- children_the_last_sentiment_ratio_strong_avgfor_user: avg of the sentiment of the children of the post for the user


- controversiality_avgfor_user: avg of the sentiment of the all children of the post for the user


- all_children_sentiment_avg_avgfor_user: avg of the sentiment of the all children of the post for the user


- all_children_sentiment_std_avgfor_user: avg of the sentiment of the all children of the post for the user


- all_children_num_of_pos_avgfor_user: avg of the sentiment of the all children of the post for the user


- all_children_num_of_neg_avgfor_user: avg of the sentiment of the all children of the post for the user


- all_children_num_of_neu_avgfor_user: avg of the sentiment of the all children of the post for the user


- all_children_num_of_pos_neg_ratio_avgfor_user: avg of the sentiment of the all children of the post for the user


- all_children_most_sentiment_avgfor_user: avg of the sentiment of the all children of the post for the user


- all_children_times_of_most_sentiment_avgfor_user: avg of the sentiment of the all children of the post for the user


- all_children_the_first_sentiment_avgfor_user: avg of the sentiment of the all children of the post for the user


- all_children_the_last_sentiment_avgfor_user: avg of the sentiment of the all children of the post for the user


- all_children_the_first_sentiment_ratio_avgfor_user: avg of the sentiment of the all children of the post for the user


- all_children_the_last_sentiment_ratio_avgfor_user: avg of the sentiment of the all children of the post for the user


- all_children_the_first_sentiment_ratio_strong_avgfor_user: avg of the sentiment of the all children of the post for the user


- all_children_the_last_sentiment_ratio_strong_avgfor_user: avg of the sentiment of the all children of the post for the user


- all_children_num_of_pos_tree_avgfor_user: avg of the sentiment of the all children of the post for the user


- all_children_num_of_neg_tree_avgfor_user: avg of the sentiment of the all children of the post for the user


- all_children_num_of_neu_tree_avgfor_user: avg of the sentiment of the all children of the post for the user


- all_children_num_of_pos_neg_ratio_tree_avgfor_user: avg of the sentiment of the all children of the post for the user


- all_children_most_sentiment_tree_avgfor_user: avg of the sentiment of the all children of the post for the user


- all_children_times_of_most_sentiment_tree_avgfor_user: avg of the sentiment of the all children of the post for the user


- all_children_the_first_sentiment_tree_avgfor_user: avg of the sentiment of the all children of the post for the user


- all_children_the_last_sentiment_tree_avgfor_user: avg of the sentiment of the all children of the post for the user


- all_children_the_first_sentiment_ratio_tree_avgfor_user: avg of the sentiment of the all children of the post for the user


- all_children_the_last_sentiment_ratio_tree_avgfor_user: avg of the sentiment of the all children of the post for the user


- all_children_num_of_controversiality_tree_avgfor_user: avg of the sentiment of the all children of the post for the user


- all_children_num_of_controversiality_ratio_tree_avgfor_user: avg of the sentiment of the all children of the post for the user


- all_children_the_most_attractive_tree_sentiment_avgfor_user: avg of the sentiment of the all children of the post for the user


- all_children_the_most_attractive_tree_controrversiality_avgfor_user: avg of the sentiment of the all children of the post for the user


- all_children_controversiality_avg_tree_avgfor_user: avg of the sentiment of the all children of the post for the user


- all_children_controversiality_std_tree_avgfor_user: avg of the sentiment of the all children of the post for the user


- all_children_controversiality_max_tree_avgfor_user: avg of the sentiment of the all children of the post for the user


- all_children_controversiality_min_tree_avgfor_user: avg of the sentiment of the all children of the post for the user


- all_children_controversiality_max_min_ratio_tree_avgfor_user: avg of the sentiment of the all children of the post for the user


- all_children_controversiality_max_tree_sentiment_avgfor_user: avg of the sentiment of the all children of the post for the user


- all_children_controversiality_min_tree_sentiment_avgfor_user: avg of the sentiment of the all children of the post for the user


- all_children_controversiality_max_tree_attraction_avgfor_user: avg of the sentiment of the all children of the post for the user


- all_children_controversiality_min_tree_attraction_avgfor_user: avg of the sentiment of the all children of the post for the user


- all_children_more_than_sentiment_avg_tree_avgfor_user: avg of the sentiment of the all children of the post for the user


- all_children_more_than_sentiment_avg_ratio_tree_avgfor_user: avg of the sentiment of the all children of the post for the user


- all_children_more_than_attraction_of_controversiality_max_tree_avgfor_user: avg of the sentiment of the all children of the post for the user


- all_children_more_than_attraction_of_controversiality_max_ratio_tree_avgfor_user: avg of the sentiment of the all children of the post for the user


- all_children_more_than_attraction_of_controversiality_min_tree_avgfor_user: avg of the sentiment of the all children of the post for the user


- all_children_more_than_attraction_of_controversiality_min_ratio_tree_avgfor_user: avg of the sentiment of the all children of the post for the user


- sentiment_avg_stdfor_user: std of the sentiment of the observation window for the user


- sentiment_std_stdfor_user: std of the sentiment of the observation window for the user


- num_of_pos_stdfor_user: std of the sentiment of the observation window for the user


- num_of_neg_stdfor_user: std of the sentiment of the observation window for the user


- num_of_neu_stdfor_user: std of the sentiment of the observation window for the user


- num_of_pos_neg_ratio_stdfor_user: std of the sentiment of the observation window for the user


- most_sentiment_stdfor_user: std of the sentiment of the observation window for the user


- times_of_most_sentiment_stdfor_user: std of the sentiment of the observation window for the user


- times_of_sentiment_change_stdfor_user: std of the sentiment of the observation window for the user


- times_of_sentiment_change_ratio_stdfor_user: std of the sentiment of the observation window for the user


- times_of_sentiment_change_ratio_strong_stdfor_user: std of the sentiment of the observation window for the user


- times_of_sentiment_keep_stdfor_user: std of the sentiment of the observation window for the user


- times_of_sentiment_keep_ratio_stdfor_user: std of the sentiment of the observation window for the user


- times_of_sentiment_keep_ratio_strong_stdfor_user: std of the sentiment of the observation window for the user


- times_of_sentiment_keep_ratio_weak_stdfor_user: std of the sentiment of the observation window for the user


- the_first_sentiment_stdfor_user: std of the sentiment of the observation window for the user


- the_last_sentiment_stdfor_user: std of the sentiment of the observation window for the user


- the_first_sentiment_ratio_stdfor_user: std of the sentiment of the observation window for the user


- the_last_sentiment_ratio_stdfor_user: std of the sentiment of the observation window for the user


- the_first_sentiment_ratio_strong_stdfor_user: std of the sentiment of the observation window for the user


- the_last_sentiment_ratio_strong_stdfor_user: std of the sentiment of the observation window for the user


- parent_sentiment_avg_stdfor_user: std of the sentiment of the parent of the post for the user


- parent_sentiment_std_stdfor_user: std of the sentiment of the parent of the post for the user


- parent_num_of_pos_stdfor_user: std of the sentiment of the parent of the post for the user


- parent_num_of_neg_stdfor_user: std of the sentiment of the parent of the post for the user


- parent_num_of_neu_stdfor_user: std of the sentiment of the parent of the post for the user


- parent_num_of_pos_neg_ratio_stdfor_user: std of the sentiment of the parent of the post for the user


- parent_most_sentiment_stdfor_user: std of the sentiment of the parent of the post for the user


- parent_times_of_most_sentiment_stdfor_user: std of the sentiment of the parent of the post for the user


- parent_times_of_sentiment_change_stdfor_user: std of the sentiment of the parent of the post for the user


- parent_times_of_sentiment_change_ratio_stdfor_user: std of the sentiment of the parent of the post for the user


- parent_times_of_sentiment_change_ratio_strong_stdfor_user: std of the sentiment of the parent of the post for the user


- parent_times_of_sentiment_keep_stdfor_user: std of the sentiment of the parent of the post for the user


- parent_times_of_sentiment_keep_ratio_stdfor_user: std of the sentiment of the parent of the post for the user


- parent_times_of_sentiment_keep_ratio_strong_stdfor_user: std of the sentiment of the parent of the post for the user


- parent_times_of_sentiment_keep_ratio_weak_stdfor_user: std of the sentiment of the parent of the post for the user


- parent_the_first_sentiment_stdfor_user: std of the sentiment of the parent of the post for the user


- parent_the_last_sentiment_stdfor_user: std of the sentiment of the parent of the post for the user


- parent_the_first_sentiment_ratio_stdfor_user: std of the sentiment of the parent of the post for the user


- parent_the_last_sentiment_ratio_stdfor_user: std of the sentiment of the parent of the post for the user


- parent_the_first_sentiment_ratio_strong_stdfor_user: std of the sentiment of the parent of the post for the user


- parent_the_last_sentiment_ratio_strong_stdfor_user: std of the sentiment of the parent of the post for the user


- children_sentiment_avg_stdfor_user: std of the sentiment of the children of the post for the user


- children_sentiment_std_stdfor_user: std of the sentiment of the children of the post for the user


- children_num_of_pos_stdfor_user: std of the sentiment of the children of the post for the user


- children_num_of_neg_stdfor_user: std of the sentiment of the children of the post for the user


- children_num_of_neu_stdfor_user: std of the sentiment of the children of the post for the user


- children_num_of_pos_neg_ratio_stdfor_user: std of the sentiment of the children of the post for the user


- children_most_sentiment_stdfor_user: std of the sentiment of the children of the post for the user


- children_times_of_most_sentiment_stdfor_user: std of the sentiment of the children of the post for the user


- children_times_of_sentiment_change_stdfor_user: std of the sentiment of the children of the post for the user


- children_times_of_sentiment_change_ratio_stdfor_user: std of the sentiment of the children of the post for the user


- children_times_of_sentiment_change_ratio_strong_stdfor_user: std of the sentiment of the children of the post for the user


- children_times_of_sentiment_keep_stdfor_user: std of the sentiment of the children of the post for the user


- children_times_of_sentiment_keep_ratio_stdfor_user: std of the sentiment of the children of the post for the user


- children_times_of_sentiment_keep_ratio_strong_stdfor_user: std of the sentiment of the children of the post for the user


- children_times_of_sentiment_keep_ratio_weak_stdfor_user: std of the sentiment of the children of the post for the user


- children_the_first_sentiment_stdfor_user: std of the sentiment of the children of the post for the user


- children_the_last_sentiment_stdfor_user: std of the sentiment of the children of the post for the user


- children_the_first_sentiment_ratio_stdfor_user: std of the sentiment of the children of the post for the user


- children_the_last_sentiment_ratio_stdfor_user: std of the sentiment of the children of the post for the user


- children_the_first_sentiment_ratio_strong_stdfor_user: std of the sentiment of the children of the post for the user


- children_the_last_sentiment_ratio_strong_stdfor_user: std of the sentiment of the children of the post for the user


- controversiality_stdfor_user: std of the sentiment of the all children of the post for the user


- all_children_sentiment_avg_stdfor_user: std of the sentiment of the all children of the post for the user


- all_children_sentiment_std_stdfor_user: std of the sentiment of the all children of the post for the user


- all_children_num_of_pos_stdfor_user: std of the sentiment of the all children of the post for the user


- all_children_num_of_neg_stdfor_user: std of the sentiment of the all children of the post for the user


- all_children_num_of_neu_stdfor_user: std of the sentiment of the all children of the post for the user


- all_children_num_of_pos_neg_ratio_stdfor_user: std of the sentiment of the all children of the post for the user


- all_children_most_sentiment_stdfor_user: std of the sentiment of the all children of the post for the user


- all_children_times_of_most_sentiment_stdfor_user: std of the sentiment of the all children of the post for the user


- all_children_the_first_sentiment_stdfor_user: std of the sentiment of the all children of the post for the user


- all_children_the_last_sentiment_stdfor_user: std of the sentiment of the all children of the post for the user


- all_children_the_first_sentiment_ratio_stdfor_user: std of the sentiment of the all children of the post for the user


- all_children_the_last_sentiment_ratio_stdfor_user: std of the sentiment of the all children of the post for the user


- all_children_the_first_sentiment_ratio_strong_stdfor_user: std of the sentiment of the all children of the post for the user


- all_children_the_last_sentiment_ratio_strong_stdfor_user: std of the sentiment of the all children of the post for the user


- all_children_num_of_pos_tree_stdfor_user: std of the sentiment of the all children of the post for the user


- all_children_num_of_neg_tree_stdfor_user: std of the sentiment of the all children of the post for the user


- all_children_num_of_neu_tree_stdfor_user: std of the sentiment of the all children of the post for the user


- all_children_num_of_pos_neg_ratio_tree_stdfor_user: std of the sentiment of the all children of the post for the user


- all_children_most_sentiment_tree_stdfor_user: std of the sentiment of the all children of the post for the user


- all_children_times_of_most_sentiment_tree_stdfor_user: std of the sentiment of the all children of the post for the user


- all_children_the_first_sentiment_tree_stdfor_user: std of the sentiment of the all children of the post for the user


- all_children_the_last_sentiment_tree_stdfor_user: std of the sentiment of the all children of the post for the user


- all_children_the_first_sentiment_ratio_tree_stdfor_user: std of the sentiment of the all children of the post for the user


- all_children_the_last_sentiment_ratio_tree_stdfor_user: std of the sentiment of the all children of the post for the user


- all_children_num_of_controversiality_tree_stdfor_user: std of the sentiment of the all children of the post for the user


- all_children_num_of_controversiality_ratio_tree_stdfor_user: std of the sentiment of the all children of the post for the user


- all_children_the_most_attractive_tree_sentiment_stdfor_user: std of the sentiment of the all children of the post for the user


- all_children_the_most_attractive_tree_controrversiality_stdfor_user: std of the sentiment of the all children of the post for the user


- all_children_controversiality_avg_tree_stdfor_user: std of the sentiment of the all children of the post for the user


- all_children_controversiality_std_tree_stdfor_user: std of the sentiment of the all children of the post for the user


- all_children_controversiality_max_tree_stdfor_user: std of the sentiment of the all children of the post for the user


- all_children_controversiality_min_tree_stdfor_user: std of the sentiment of the all children of the post for the user


- all_children_controversiality_max_min_ratio_tree_stdfor_user: std of the sentiment of the all children of the post for the user


- all_children_controversiality_max_tree_sentiment_stdfor_user: std of the sentiment of the all children of the post for the user


- all_children_controversiality_min_tree_sentiment_stdfor_user: std of the sentiment of the all children of the post for the user


- all_children_controversiality_max_tree_attraction_stdfor_user: std of the sentiment of the all children of the post for the user


- all_children_controversiality_min_tree_attraction_stdfor_user: std of the sentiment of the all children of the post for the user


- all_children_more_than_sentiment_avg_tree_stdfor_user: std of the sentiment of the all children of the post for the user


- all_children_more_than_sentiment_avg_ratio_tree_stdfor_user: std of the sentiment of the all children of the post for the user


- all_children_more_than_attraction_of_controversiality_max_tree_stdfor_user: std of the sentiment of the all children of the post for the user


- all_children_more_than_attraction_of_controversiality_max_ratio_tree_stdfor_user: std of the sentiment of the all children of the post for the user


- all_children_more_than_attraction_of_controversiality_min_tree_stdfor_user: std of the sentiment of the all children of the post for the user


- all_children_more_than_attraction_of_controversiality_min_ratio_tree_stdfor_user: std of the sentiment of the all children of the post for the user


- sentiment_avg_maxfor_user: max of the sentiment of the observation window for the user


- sentiment_std_maxfor_user: max of the sentiment of the observation window for the user


- num_of_pos_maxfor_user: max of the sentiment of the observation window for the user


- num_of_neg_maxfor_user: max of the sentiment of the observation window for the user


- num_of_neu_maxfor_user: max of the sentiment of the observation window for the user


- num_of_pos_neg_ratio_maxfor_user: max of the sentiment of the observation window for the user


- most_sentiment_maxfor_user: max of the sentiment of the observation window for the user


- times_of_most_sentiment_maxfor_user: max of the sentiment of the observation window for the user


- times_of_sentiment_change_maxfor_user: max of the sentiment of the observation window for the user


- times_of_sentiment_change_ratio_maxfor_user: max of the sentiment of the observation window for the user


- times_of_sentiment_change_ratio_strong_maxfor_user: max of the sentiment of the observation window for the user


- times_of_sentiment_keep_maxfor_user: max of the sentiment of the observation window for the user


- times_of_sentiment_keep_ratio_maxfor_user: max of the sentiment of the observation window for the user


- times_of_sentiment_keep_ratio_strong_maxfor_user: max of the sentiment of the observation window for the user


- times_of_sentiment_keep_ratio_weak_maxfor_user: max of the sentiment of the observation window for the user


- the_first_sentiment_maxfor_user: max of the sentiment of the observation window for the user


- the_last_sentiment_maxfor_user: max of the sentiment of the observation window for the user


- the_first_sentiment_ratio_maxfor_user: max of the sentiment of the observation window for the user


- the_last_sentiment_ratio_maxfor_user: max of the sentiment of the observation window for the user


- the_first_sentiment_ratio_strong_maxfor_user: max of the sentiment of the observation window for the user


- the_last_sentiment_ratio_strong_maxfor_user: max of the sentiment of the observation window for the user


- parent_sentiment_avg_maxfor_user: max of the sentiment of the parent of the post for the user


- parent_sentiment_std_maxfor_user: max of the sentiment of the parent of the post for the user


- parent_num_of_pos_maxfor_user: max of the sentiment of the parent of the post for the user


- parent_num_of_neg_maxfor_user: max of the sentiment of the parent of the post for the user


- parent_num_of_neu_maxfor_user: max of the sentiment of the parent of the post for the user


- parent_num_of_pos_neg_ratio_maxfor_user: max of the sentiment of the parent of the post for the user


- parent_most_sentiment_maxfor_user: max of the sentiment of the parent of the post for the user


- parent_times_of_most_sentiment_maxfor_user: max of the sentiment of the parent of the post for the user


- parent_times_of_sentiment_change_maxfor_user: max of the sentiment of the parent of the post for the user


- parent_times_of_sentiment_change_ratio_maxfor_user: max of the sentiment of the parent of the post for the user


- parent_times_of_sentiment_change_ratio_strong_maxfor_user: max of the sentiment of the parent of the post for the user


- parent_times_of_sentiment_keep_maxfor_user: max of the sentiment of the parent of the post for the user


- parent_times_of_sentiment_keep_ratio_maxfor_user: max of the sentiment of the parent of the post for the user


- parent_times_of_sentiment_keep_ratio_strong_maxfor_user: max of the sentiment of the parent of the post for the user


- parent_times_of_sentiment_keep_ratio_weak_maxfor_user: max of the sentiment of the parent of the post for the user


- parent_the_first_sentiment_maxfor_user: max of the sentiment of the parent of the post for the user


- parent_the_last_sentiment_maxfor_user: max of the sentiment of the parent of the post for the user


- parent_the_first_sentiment_ratio_maxfor_user: max of the sentiment of the parent of the post for the user


- parent_the_last_sentiment_ratio_maxfor_user: max of the sentiment of the parent of the post for the user


- parent_the_first_sentiment_ratio_strong_maxfor_user: max of the sentiment of the parent of the post for the user


- parent_the_last_sentiment_ratio_strong_maxfor_user: max of the sentiment of the parent of the post for the user


- children_sentiment_avg_maxfor_user: max of the sentiment of the children of the post for the user


- children_sentiment_std_maxfor_user: max of the sentiment of the children of the post for the user


- children_num_of_pos_maxfor_user: max of the sentiment of the children of the post for the user


- children_num_of_neg_maxfor_user: max of the sentiment of the children of the post for the user


- children_num_of_neu_maxfor_user: max of the sentiment of the children of the post for the user


- children_num_of_pos_neg_ratio_maxfor_user: max of the sentiment of the children of the post for the user


- children_most_sentiment_maxfor_user: max of the sentiment of the children of the post for the user


- children_times_of_most_sentiment_maxfor_user: max of the sentiment of the children of the post for the user


- children_times_of_sentiment_change_maxfor_user: max of the sentiment of the children of the post for the user


- children_times_of_sentiment_change_ratio_maxfor_user: max of the sentiment of the children of the post for the user


- children_times_of_sentiment_change_ratio_strong_maxfor_user: max of the sentiment of the children of the post for the user


- children_times_of_sentiment_keep_maxfor_user: max of the sentiment of the children of the post for the user


- children_times_of_sentiment_keep_ratio_maxfor_user: max of the sentiment of the children of the post for the user


- children_times_of_sentiment_keep_ratio_strong_maxfor_user: max of the sentiment of the children of the post for the user


- children_times_of_sentiment_keep_ratio_weak_maxfor_user: max of the sentiment of the children of the post for the user


- children_the_first_sentiment_maxfor_user: max of the sentiment of the children of the post for the user


- children_the_last_sentiment_maxfor_user: max of the sentiment of the children of the post for the user


- children_the_first_sentiment_ratio_maxfor_user: max of the sentiment of the children of the post for the user


- children_the_last_sentiment_ratio_maxfor_user: max of the sentiment of the children of the post for the user


- children_the_first_sentiment_ratio_strong_maxfor_user: max of the sentiment of the children of the post for the user


- children_the_last_sentiment_ratio_strong_maxfor_user: max of the sentiment of the children of the post for the user


- controversiality_maxfor_user: max of the sentiment of the all children of the post for the user


- all_children_sentiment_avg_maxfor_user: max of the sentiment of the all children of the post for the user


- all_children_sentiment_std_maxfor_user: max of the sentiment of the all children of the post for the user


- all_children_num_of_pos_maxfor_user: max of the sentiment of the all children of the post for the user


- all_children_num_of_neg_maxfor_user: max of the sentiment of the all children of the post for the user


- all_children_num_of_neu_maxfor_user: max of the sentiment of the all children of the post for the user


- all_children_num_of_pos_neg_ratio_maxfor_user: max of the sentiment of the all children of the post for the user


- all_children_most_sentiment_maxfor_user: max of the sentiment of the all children of the post for the user


- all_children_times_of_most_sentiment_maxfor_user: max of the sentiment of the all children of the post for the user


- all_children_the_first_sentiment_maxfor_user: max of the sentiment of the all children of the post for the user


- all_children_the_last_sentiment_maxfor_user: max of the sentiment of the all children of the post for the user


- all_children_the_first_sentiment_ratio_maxfor_user: max of the sentiment of the all children of the post for the user


- all_children_the_last_sentiment_ratio_maxfor_user: max of the sentiment of the all children of the post for the user


- all_children_the_first_sentiment_ratio_strong_maxfor_user: max of the sentiment of the all children of the post for the user


- all_children_the_last_sentiment_ratio_strong_maxfor_user: max of the sentiment of the all children of the post for the user


- all_children_num_of_pos_tree_maxfor_user: max of the sentiment of the all children of the post for the user


- all_children_num_of_neg_tree_maxfor_user: max of the sentiment of the all children of the post for the user


- all_children_num_of_neu_tree_maxfor_user: max of the sentiment of the all children of the post for the user


- all_children_num_of_pos_neg_ratio_tree_maxfor_user: max of the sentiment of the all children of the post for the user


- all_children_most_sentiment_tree_maxfor_user: max of the sentiment of the all children of the post for the user


- all_children_times_of_most_sentiment_tree_maxfor_user: max of the sentiment of the all children of the post for the user


- all_children_the_first_sentiment_tree_maxfor_user: max of the sentiment of the all children of the post for the user


- all_children_the_last_sentiment_tree_maxfor_user: max of the sentiment of the all children of the post for the user


- all_children_the_first_sentiment_ratio_tree_maxfor_user: max of the sentiment of the all children of the post for the user


- all_children_the_last_sentiment_ratio_tree_maxfor_user: max of the sentiment of the all children of the post for the user


- all_children_num_of_controversiality_tree_maxfor_user: max of the sentiment of the all children of the post for the user


- all_children_num_of_controversiality_ratio_tree_maxfor_user: max of the sentiment of the all children of the post for the user


- all_children_the_most_attractive_tree_sentiment_maxfor_user: max of the sentiment of the all children of the post for the user


- all_children_the_most_attractive_tree_controrversiality_maxfor_user: max of the sentiment of the all children of the post for the user


- all_children_controversiality_avg_tree_maxfor_user: max of the sentiment of the all children of the post for the user


- all_children_controversiality_std_tree_maxfor_user: max of the sentiment of the all children of the post for the user


- all_children_controversiality_max_tree_maxfor_user: max of the sentiment of the all children of the post for the user


- all_children_controversiality_min_tree_maxfor_user: max of the sentiment of the all children of the post for the user


- all_children_controversiality_max_min_ratio_tree_maxfor_user: max of the sentiment of the all children of the post for the user


- all_children_controversiality_max_tree_sentiment_maxfor_user: max of the sentiment of the all children of the post for the user


- all_children_controversiality_min_tree_sentiment_maxfor_user: max of the sentiment of the all children of the post for the user


- all_children_controversiality_max_tree_attraction_maxfor_user: max of the sentiment of the all children of the post for the user


- all_children_controversiality_min_tree_attraction_maxfor_user: max of the sentiment of the all children of the post for the user


- all_children_more_than_sentiment_avg_tree_maxfor_user: max of the sentiment of the all children of the post for the user


- all_children_more_than_sentiment_avg_ratio_tree_maxfor_user: max of the sentiment of the all children of the post for the user


- all_children_more_than_attraction_of_controversiality_max_tree_maxfor_user: max of the sentiment of the all children of the post for the user


- all_children_more_than_attraction_of_controversiality_max_ratio_tree_maxfor_user: max of the sentiment of the all children of the post for the user


- all_children_more_than_attraction_of_controversiality_min_tree_maxfor_user: max of the sentiment of the all children of the post for the user


- all_children_more_than_attraction_of_controversiality_min_ratio_tree_maxfor_user: max of the sentiment of the all children of the post for the user


- sentiment_avg_minfor_user: min of the sentiment of the observation window for the user


- sentiment_std_minfor_user: min of the sentiment of the observation window for the user


- num_of_pos_minfor_user: min of the sentiment of the observation window for the user


- num_of_neg_minfor_user: min of the sentiment of the observation window for the user


- num_of_neu_minfor_user: min of the sentiment of the observation window for the user


- num_of_pos_neg_ratio_minfor_user: min of the sentiment of the observation window for the user


- most_sentiment_minfor_user: min of the sentiment of the observation window for the user


- times_of_most_sentiment_minfor_user: min of the sentiment of the observation window for the user


- times_of_sentiment_change_minfor_user: min of the sentiment of the observation window for the user


- times_of_sentiment_change_ratio_minfor_user: min of the sentiment of the observation window for the user


- times_of_sentiment_change_ratio_strong_minfor_user: min of the sentiment of the observation window for the user


- times_of_sentiment_keep_minfor_user: min of the sentiment of the observation window for the user


- times_of_sentiment_keep_ratio_minfor_user: min of the sentiment of the observation window for the user


- times_of_sentiment_keep_ratio_strong_minfor_user: min of the sentiment of the observation window for the user


- times_of_sentiment_keep_ratio_weak_minfor_user: min of the sentiment of the observation window for the user


- the_first_sentiment_minfor_user: min of the sentiment of the observation window for the user


- the_last_sentiment_minfor_user: min of the sentiment of the observation window for the user


- the_first_sentiment_ratio_minfor_user: min of the sentiment of the observation window for the user


- the_last_sentiment_ratio_minfor_user: min of the sentiment of the observation window for the user


- the_first_sentiment_ratio_strong_minfor_user: min of the sentiment of the observation window for the user


- the_last_sentiment_ratio_strong_minfor_user: min of the sentiment of the observation window for the user


- parent_sentiment_avg_minfor_user: min of the sentiment of the parent of the post for the user


- parent_sentiment_std_minfor_user: min of the sentiment of the parent of the post for the user


- parent_num_of_pos_minfor_user: min of the sentiment of the parent of the post for the user


- parent_num_of_neg_minfor_user: min of the sentiment of the parent of the post for the user


- parent_num_of_neu_minfor_user: min of the sentiment of the parent of the post for the user


- parent_num_of_pos_neg_ratio_minfor_user: min of the sentiment of the parent of the post for the user


- parent_most_sentiment_minfor_user: min of the sentiment of the parent of the post for the user


- parent_times_of_most_sentiment_minfor_user: min of the sentiment of the parent of the post for the user


- parent_times_of_sentiment_change_minfor_user: min of the sentiment of the parent of the post for the user


- parent_times_of_sentiment_change_ratio_minfor_user: min of the sentiment of the parent of the post for the user


- parent_times_of_sentiment_change_ratio_strong_minfor_user: min of the sentiment of the parent of the post for the user


- parent_times_of_sentiment_keep_minfor_user: min of the sentiment of the parent of the post for the user


- parent_times_of_sentiment_keep_ratio_minfor_user: min of the sentiment of the parent of the post for the user


- parent_times_of_sentiment_keep_ratio_strong_minfor_user: min of the sentiment of the parent of the post for the user


- parent_times_of_sentiment_keep_ratio_weak_minfor_user: min of the sentiment of the parent of the post for the user


- parent_the_first_sentiment_minfor_user: min of the sentiment of the parent of the post for the user


- parent_the_last_sentiment_minfor_user: min of the sentiment of the parent of the post for the user


- parent_the_first_sentiment_ratio_minfor_user: min of the sentiment of the parent of the post for the user


- parent_the_last_sentiment_ratio_minfor_user: min of the sentiment of the parent of the post for the user


- parent_the_first_sentiment_ratio_strong_minfor_user: min of the sentiment of the parent of the post for the user


- parent_the_last_sentiment_ratio_strong_minfor_user: min of the sentiment of the parent of the post for the user


- children_sentiment_avg_minfor_user: min of the sentiment of the children of the post for the user


- children_sentiment_std_minfor_user: min of the sentiment of the children of the post for the user


- children_num_of_pos_minfor_user: min of the sentiment of the children of the post for the user


- children_num_of_neg_minfor_user: min of the sentiment of the children of the post for the user


- children_num_of_neu_minfor_user: min of the sentiment of the children of the post for the user


- children_num_of_pos_neg_ratio_minfor_user: min of the sentiment of the children of the post for the user


- children_most_sentiment_minfor_user: min of the sentiment of the children of the post for the user


- children_times_of_most_sentiment_minfor_user: min of the sentiment of the children of the post for the user


- children_times_of_sentiment_change_minfor_user: min of the sentiment of the children of the post for the user


- children_times_of_sentiment_change_ratio_minfor_user: min of the sentiment of the children of the post for the user


- children_times_of_sentiment_change_ratio_strong_minfor_user: min of the sentiment of the children of the post for the user


- children_times_of_sentiment_keep_minfor_user: min of the sentiment of the children of the post for the user


- children_times_of_sentiment_keep_ratio_minfor_user: min of the sentiment of the children of the post for the user


- children_times_of_sentiment_keep_ratio_strong_minfor_user: min of the sentiment of the children of the post for the user


- children_times_of_sentiment_keep_ratio_weak_minfor_user: min of the sentiment of the children of the post for the user


- children_the_first_sentiment_minfor_user: min of the sentiment of the children of the post for the user


- children_the_last_sentiment_minfor_user: min of the sentiment of the children of the post for the user


- children_the_first_sentiment_ratio_minfor_user: min of the sentiment of the children of the post for the user


- children_the_last_sentiment_ratio_minfor_user: min of the sentiment of the children of the post for the user


- children_the_first_sentiment_ratio_strong_minfor_user: min of the sentiment of the children of the post for the user


- children_the_last_sentiment_ratio_strong_minfor_user: min of the sentiment of the children of the post for the user


- controversiality_minfor_user: min of the sentiment of the all children of the post for the user


- all_children_sentiment_avg_minfor_user: min of the sentiment of the all children of the post for the user


- all_children_sentiment_std_minfor_user: min of the sentiment of the all children of the post for the user


- all_children_num_of_pos_minfor_user: min of the sentiment of the all children of the post for the user


- all_children_num_of_neg_minfor_user: min of the sentiment of the all children of the post for the user


- all_children_num_of_neu_minfor_user: min of the sentiment of the all children of the post for the user


- all_children_num_of_pos_neg_ratio_minfor_user: min of the sentiment of the all children of the post for the user


- all_children_most_sentiment_minfor_user: min of the sentiment of the all children of the post for the user


- all_children_times_of_most_sentiment_minfor_user: min of the sentiment of the all children of the post for the user


- all_children_the_first_sentiment_minfor_user: min of the sentiment of the all children of the post for the user


- all_children_the_last_sentiment_minfor_user: min of the sentiment of the all children of the post for the user


- all_children_the_first_sentiment_ratio_minfor_user: min of the sentiment of the all children of the post for the user


- all_children_the_last_sentiment_ratio_minfor_user: min of the sentiment of the all children of the post for the user


- all_children_the_first_sentiment_ratio_strong_minfor_user: min of the sentiment of the all children of the post for the user


- all_children_the_last_sentiment_ratio_strong_minfor_user: min of the sentiment of the all children of the post for the user


- all_children_num_of_pos_tree_minfor_user: min of the sentiment of the all children of the post for the user


- all_children_num_of_neg_tree_minfor_user: min of the sentiment of the all children of the post for the user


- all_children_num_of_neu_tree_minfor_user: min of the sentiment of the all children of the post for the user


- all_children_num_of_pos_neg_ratio_tree_minfor_user: min of the sentiment of the all children of the post for the user


- all_children_most_sentiment_tree_minfor_user: min of the sentiment of the all children of the post for the user


- all_children_times_of_most_sentiment_tree_minfor_user: min of the sentiment of the all children of the post for the user


- all_children_the_first_sentiment_tree_minfor_user: min of the sentiment of the all children of the post for the user


- all_children_the_last_sentiment_tree_minfor_user: min of the sentiment of the all children of the post for the user


- all_children_the_first_sentiment_ratio_tree_minfor_user: min of the sentiment of the all children of the post for the user


- all_children_the_last_sentiment_ratio_tree_minfor_user: min of the sentiment of the all children of the post for the user


- all_children_num_of_controversiality_tree_minfor_user: min of the sentiment of the all children of the post for the user


- all_children_num_of_controversiality_ratio_tree_minfor_user: min of the sentiment of the all children of the post for the user


- all_children_the_most_attractive_tree_sentiment_minfor_user: min of the sentiment of the all children of the post for the user


- all_children_the_most_attractive_tree_controrversiality_minfor_user: min of the sentiment of the all children of the post for the user


- all_children_controversiality_avg_tree_minfor_user: min of the sentiment of the all children of the post for the user


- all_children_controversiality_std_tree_minfor_user: min of the sentiment of the all children of the post for the user


- all_children_controversiality_max_tree_minfor_user: min of the sentiment of the all children of the post for the user


- all_children_controversiality_min_tree_minfor_user: min of the sentiment of the all children of the post for the user


- all_children_controversiality_max_min_ratio_tree_minfor_user: min of the sentiment of the all children of the post for the user


- all_children_controversiality_max_tree_sentiment_minfor_user: min of the sentiment of the all children of the post for the user


- all_children_controversiality_min_tree_sentiment_minfor_user: min of the sentiment of the all children of the post for the user


- all_children_controversiality_max_tree_attraction_minfor_user: min of the sentiment of the all children of the post for the user


- all_children_controversiality_min_tree_attraction_minfor_user: min of the sentiment of the all children of the post for the user


- all_children_more_than_sentiment_avg_tree_minfor_user: min of the sentiment of the all children of the post for the user


- all_children_more_than_sentiment_avg_ratio_tree_minfor_user: min of the sentiment of the all children of the post for the user


- all_children_more_than_attraction_of_controversiality_max_tree_minfor_user: min of the sentiment of the all children of the post for the user


- all_children_more_than_attraction_of_controversiality_max_ratio_tree_minfor_user: min of the sentiment of the all children of the post for the user


- all_children_more_than_attraction_of_controversiality_min_tree_minfor_user: min of the sentiment of the all children of the post for the user


- all_children_more_than_attraction_of_controversiality_min_ratio_tree_minfor_user: min of the sentiment of the all children of the post for the user


- sentiment_avg_firstfor_user: first of the sentiment of the observation window for the user


- sentiment_std_firstfor_user: first of the sentiment of the observation window for the user


- num_of_pos_firstfor_user: first of the sentiment of the observation window for the user


- num_of_neg_firstfor_user: first of the sentiment of the observation window for the user


- num_of_neu_firstfor_user: first of the sentiment of the observation window for the user


- num_of_pos_neg_ratio_firstfor_user: first of the sentiment of the observation window for the user


- most_sentiment_firstfor_user: first of the sentiment of the observation window for the user


- times_of_most_sentiment_firstfor_user: first of the sentiment of the observation window for the user


- times_of_sentiment_change_firstfor_user: first of the sentiment of the observation window for the user


- times_of_sentiment_change_ratio_firstfor_user: first of the sentiment of the observation window for the user


- times_of_sentiment_change_ratio_strong_firstfor_user: first of the sentiment of the observation window for the user


- times_of_sentiment_keep_firstfor_user: first of the sentiment of the observation window for the user


- times_of_sentiment_keep_ratio_firstfor_user: first of the sentiment of the observation window for the user


- times_of_sentiment_keep_ratio_strong_firstfor_user: first of the sentiment of the observation window for the user


- times_of_sentiment_keep_ratio_weak_firstfor_user: first of the sentiment of the observation window for the user


- the_first_sentiment_firstfor_user: first of the sentiment of the observation window for the user


- the_last_sentiment_firstfor_user: first of the sentiment of the observation window for the user


- the_first_sentiment_ratio_firstfor_user: first of the sentiment of the observation window for the user


- the_last_sentiment_ratio_firstfor_user: first of the sentiment of the observation window for the user


- the_first_sentiment_ratio_strong_firstfor_user: first of the sentiment of the observation window for the user


- the_last_sentiment_ratio_strong_firstfor_user: first of the sentiment of the observation window for the user


- parent_sentiment_avg_firstfor_user: first of the sentiment of the parent of the post for the user


- parent_sentiment_std_firstfor_user: first of the sentiment of the parent of the post for the user


- parent_num_of_pos_firstfor_user: first of the sentiment of the parent of the post for the user


- parent_num_of_neg_firstfor_user: first of the sentiment of the parent of the post for the user


- parent_num_of_neu_firstfor_user: first of the sentiment of the parent of the post for the user


- parent_num_of_pos_neg_ratio_firstfor_user: first of the sentiment of the parent of the post for the user


- parent_most_sentiment_firstfor_user: first of the sentiment of the parent of the post for the user


- parent_times_of_most_sentiment_firstfor_user: first of the sentiment of the parent of the post for the user


- parent_times_of_sentiment_change_firstfor_user: first of the sentiment of the parent of the post for the user


- parent_times_of_sentiment_change_ratio_firstfor_user: first of the sentiment of the parent of the post for the user


- parent_times_of_sentiment_change_ratio_strong_firstfor_user: first of the sentiment of the parent of the post for the user


- parent_times_of_sentiment_keep_firstfor_user: first of the sentiment of the parent of the post for the user


- parent_times_of_sentiment_keep_ratio_firstfor_user: first of the sentiment of the parent of the post for the user


- parent_times_of_sentiment_keep_ratio_strong_firstfor_user: first of the sentiment of the parent of the post for the user


- parent_times_of_sentiment_keep_ratio_weak_firstfor_user: first of the sentiment of the parent of the post for the user


- parent_the_first_sentiment_firstfor_user: first of the sentiment of the parent of the post for the user


- parent_the_last_sentiment_firstfor_user: first of the sentiment of the parent of the post for the user


- parent_the_first_sentiment_ratio_firstfor_user: first of the sentiment of the parent of the post for the user


- parent_the_last_sentiment_ratio_firstfor_user: first of the sentiment of the parent of the post for the user


- parent_the_first_sentiment_ratio_strong_firstfor_user: first of the sentiment of the parent of the post for the user


- parent_the_last_sentiment_ratio_strong_firstfor_user: first of the sentiment of the parent of the post for the user


- children_sentiment_avg_firstfor_user: first of the sentiment of the children of the post for the user


- children_sentiment_std_firstfor_user: first of the sentiment of the children of the post for the user


- children_num_of_pos_firstfor_user: first of the sentiment of the children of the post for the user


- children_num_of_neg_firstfor_user: first of the sentiment of the children of the post for the user


- children_num_of_neu_firstfor_user: first of the sentiment of the children of the post for the user


- children_num_of_pos_neg_ratio_firstfor_user: first of the sentiment of the children of the post for the user


- children_most_sentiment_firstfor_user: first of the sentiment of the children of the post for the user


- children_times_of_most_sentiment_firstfor_user: first of the sentiment of the children of the post for the user


- children_times_of_sentiment_change_firstfor_user: first of the sentiment of the children of the post for the user


- children_times_of_sentiment_change_ratio_firstfor_user: first of the sentiment of the children of the post for the user


- children_times_of_sentiment_change_ratio_strong_firstfor_user: first of the sentiment of the children of the post for the user


- children_times_of_sentiment_keep_firstfor_user: first of the sentiment of the children of the post for the user


- children_times_of_sentiment_keep_ratio_firstfor_user: first of the sentiment of the children of the post for the user


- children_times_of_sentiment_keep_ratio_strong_firstfor_user: first of the sentiment of the children of the post for the user


- children_times_of_sentiment_keep_ratio_weak_firstfor_user: first of the sentiment of the children of the post for the user


- children_the_first_sentiment_firstfor_user: first of the sentiment of the children of the post for the user


- children_the_last_sentiment_firstfor_user: first of the sentiment of the children of the post for the user


- children_the_first_sentiment_ratio_firstfor_user: first of the sentiment of the children of the post for the user


- children_the_last_sentiment_ratio_firstfor_user: first of the sentiment of the children of the post for the user


- children_the_first_sentiment_ratio_strong_firstfor_user: first of the sentiment of the children of the post for the user


- children_the_last_sentiment_ratio_strong_firstfor_user: first of the sentiment of the children of the post for the user


- controversiality_firstfor_user: first of the sentiment of the all children of the post for the user


- all_children_sentiment_avg_firstfor_user: first of the sentiment of the all children of the post for the user


- all_children_sentiment_std_firstfor_user: first of the sentiment of the all children of the post for the user


- all_children_num_of_pos_firstfor_user: first of the sentiment of the all children of the post for the user


- all_children_num_of_neg_firstfor_user: first of the sentiment of the all children of the post for the user


- all_children_num_of_neu_firstfor_user: first of the sentiment of the all children of the post for the user


- all_children_num_of_pos_neg_ratio_firstfor_user: first of the sentiment of the all children of the post for the user


- all_children_most_sentiment_firstfor_user: first of the sentiment of the all children of the post for the user


- all_children_times_of_most_sentiment_firstfor_user: first of the sentiment of the all children of the post for the user


- all_children_the_first_sentiment_firstfor_user: first of the sentiment of the all children of the post for the user


- all_children_the_last_sentiment_firstfor_user: first of the sentiment of the all children of the post for the user


- all_children_the_first_sentiment_ratio_firstfor_user: first of the sentiment of the all children of the post for the user


- all_children_the_last_sentiment_ratio_firstfor_user: first of the sentiment of the all children of the post for the user


- all_children_the_first_sentiment_ratio_strong_firstfor_user: first of the sentiment of the all children of the post for the user


- all_children_the_last_sentiment_ratio_strong_firstfor_user: first of the sentiment of the all children of the post for the user


- all_children_num_of_pos_tree_firstfor_user: first of the sentiment of the all children of the post for the user


- all_children_num_of_neg_tree_firstfor_user: first of the sentiment of the all children of the post for the user


- all_children_num_of_neu_tree_firstfor_user: first of the sentiment of the all children of the post for the user


- all_children_num_of_pos_neg_ratio_tree_firstfor_user: first of the sentiment of the all children of the post for the user


- all_children_most_sentiment_tree_firstfor_user: first of the sentiment of the all children of the post for the user


- all_children_times_of_most_sentiment_tree_firstfor_user: first of the sentiment of the all children of the post for the user


- all_children_the_first_sentiment_tree_firstfor_user: first of the sentiment of the all children of the post for the user


- all_children_the_last_sentiment_tree_firstfor_user: first of the sentiment of the all children of the post for the user


- all_children_the_first_sentiment_ratio_tree_firstfor_user: first of the sentiment of the all children of the post for the user


- all_children_the_last_sentiment_ratio_tree_firstfor_user: first of the sentiment of the all children of the post for the user


- all_children_num_of_controversiality_tree_firstfor_user: first of the sentiment of the all children of the post for the user


- all_children_num_of_controversiality_ratio_tree_firstfor_user: first of the sentiment of the all children of the post for the user


- all_children_the_most_attractive_tree_sentiment_firstfor_user: first of the sentiment of the all children of the post for the user


- all_children_the_most_attractive_tree_controrversiality_firstfor_user: first of the sentiment of the all children of the post for the user


- all_children_controversiality_avg_tree_firstfor_user: first of the sentiment of the all children of the post for the user


- all_children_controversiality_std_tree_firstfor_user: first of the sentiment of the all children of the post for the user


- all_children_controversiality_max_tree_firstfor_user: first of the sentiment of the all children of the post for the user


- all_children_controversiality_min_tree_firstfor_user: first of the sentiment of the all children of the post for the user


- all_children_controversiality_max_min_ratio_tree_firstfor_user: first of the sentiment of the all children of the post for the user


- all_children_controversiality_max_tree_sentiment_firstfor_user: first of the sentiment of the all children of the post for the user


- all_children_controversiality_min_tree_sentiment_firstfor_user: first of the sentiment of the all children of the post for the user


- all_children_controversiality_max_tree_attraction_firstfor_user: first of the sentiment of the all children of the post for the user


- all_children_controversiality_min_tree_attraction_firstfor_user: first of the sentiment of the all children of the post for the user


- all_children_more_than_sentiment_avg_tree_firstfor_user: first of the sentiment of the all children of the post for the user


- all_children_more_than_sentiment_avg_ratio_tree_firstfor_user: first of the sentiment of the all children of the post for the user


- all_children_more_than_attraction_of_controversiality_max_tree_firstfor_user: first of the sentiment of the all children of the post for the user


- all_children_more_than_attraction_of_controversiality_max_ratio_tree_firstfor_user: first of the sentiment of the all children of the post for the user


- all_children_more_than_attraction_of_controversiality_min_tree_firstfor_user: first of the sentiment of the all children of the post for the user


- all_children_more_than_attraction_of_controversiality_min_ratio_tree_firstfor_user: first of the sentiment of the all children of the post for the user


- sentiment_avg_lastfor_user: last of the sentiment of the observation window for the user


- sentiment_std_lastfor_user: last of the sentiment of the observation window for the user


- num_of_pos_lastfor_user: last of the sentiment of the observation window for the user


- num_of_neg_lastfor_user: last of the sentiment of the observation window for the user


- num_of_neu_lastfor_user: last of the sentiment of the observation window for the user


- num_of_pos_neg_ratio_lastfor_user: last of the sentiment of the observation window for the user


- most_sentiment_lastfor_user: last of the sentiment of the observation window for the user


- times_of_most_sentiment_lastfor_user: last of the sentiment of the observation window for the user


- times_of_sentiment_change_lastfor_user: last of the sentiment of the observation window for the user


- times_of_sentiment_change_ratio_lastfor_user: last of the sentiment of the observation window for the user


- times_of_sentiment_change_ratio_strong_lastfor_user: last of the sentiment of the observation window for the user


- times_of_sentiment_keep_lastfor_user: last of the sentiment of the observation window for the user


- times_of_sentiment_keep_ratio_lastfor_user: last of the sentiment of the observation window for the user


- times_of_sentiment_keep_ratio_strong_lastfor_user: last of the sentiment of the observation window for the user


- times_of_sentiment_keep_ratio_weak_lastfor_user: last of the sentiment of the observation window for the user


- the_first_sentiment_lastfor_user: last of the sentiment of the observation window for the user


- the_last_sentiment_lastfor_user: last of the sentiment of the observation window for the user


- the_first_sentiment_ratio_lastfor_user: last of the sentiment of the observation window for the user


- the_last_sentiment_ratio_lastfor_user: last of the sentiment of the observation window for the user


- the_first_sentiment_ratio_strong_lastfor_user: last of the sentiment of the observation window for the user


- the_last_sentiment_ratio_strong_lastfor_user: last of the sentiment of the observation window for the user


- parent_sentiment_avg_lastfor_user: last of the sentiment of the parent of the post for the user


- parent_sentiment_std_lastfor_user: last of the sentiment of the parent of the post for the user


- parent_num_of_pos_lastfor_user: last of the sentiment of the parent of the post for the user


- parent_num_of_neg_lastfor_user: last of the sentiment of the parent of the post for the user


- parent_num_of_neu_lastfor_user: last of the sentiment of the parent of the post for the user


- parent_num_of_pos_neg_ratio_lastfor_user: last of the sentiment of the parent of the post for the user


- parent_most_sentiment_lastfor_user: last of the sentiment of the parent of the post for the user


- parent_times_of_most_sentiment_lastfor_user: last of the sentiment of the parent of the post for the user


- parent_times_of_sentiment_change_lastfor_user: last of the sentiment of the parent of the post for the user


- parent_times_of_sentiment_change_ratio_lastfor_user: last of the sentiment of the parent of the post for the user


- parent_times_of_sentiment_change_ratio_strong_lastfor_user: last of the sentiment of the parent of the post for the user


- parent_times_of_sentiment_keep_lastfor_user: last of the sentiment of the parent of the post for the user


- parent_times_of_sentiment_keep_ratio_lastfor_user: last of the sentiment of the parent of the post for the user


- parent_times_of_sentiment_keep_ratio_strong_lastfor_user: last of the sentiment of the parent of the post for the user


- parent_times_of_sentiment_keep_ratio_weak_lastfor_user: last of the sentiment of the parent of the post for the user


- parent_the_first_sentiment_lastfor_user: last of the sentiment of the parent of the post for the user


- parent_the_last_sentiment_lastfor_user: last of the sentiment of the parent of the post for the user


- parent_the_first_sentiment_ratio_lastfor_user: last of the sentiment of the parent of the post for the user


- parent_the_last_sentiment_ratio_lastfor_user: last of the sentiment of the parent of the post for the user


- parent_the_first_sentiment_ratio_strong_lastfor_user: last of the sentiment of the parent of the post for the user


- parent_the_last_sentiment_ratio_strong_lastfor_user: last of the sentiment of the parent of the post for the user


- children_sentiment_avg_lastfor_user: last of the sentiment of the children of the post for the user


- children_sentiment_std_lastfor_user: last of the sentiment of the children of the post for the user


- children_num_of_pos_lastfor_user: last of the sentiment of the children of the post for the user


- children_num_of_neg_lastfor_user: last of the sentiment of the children of the post for the user


- children_num_of_neu_lastfor_user: last of the sentiment of the children of the post for the user


- children_num_of_pos_neg_ratio_lastfor_user: last of the sentiment of the children of the post for the user


- children_most_sentiment_lastfor_user: last of the sentiment of the children of the post for the user


- children_times_of_most_sentiment_lastfor_user: last of the sentiment of the children of the post for the user


- children_times_of_sentiment_change_lastfor_user: last of the sentiment of the children of the post for the user


- children_times_of_sentiment_change_ratio_lastfor_user: last of the sentiment of the children of the post for the user


- children_times_of_sentiment_change_ratio_strong_lastfor_user: last of the sentiment of the children of the post for the user


- children_times_of_sentiment_keep_lastfor_user: last of the sentiment of the children of the post for the user


- children_times_of_sentiment_keep_ratio_lastfor_user: last of the sentiment of the children of the post for the user


- children_times_of_sentiment_keep_ratio_strong_lastfor_user: last of the sentiment of the children of the post for the user


- children_times_of_sentiment_keep_ratio_weak_lastfor_user: last of the sentiment of the children of the post for the user


- children_the_first_sentiment_lastfor_user: last of the sentiment of the children of the post for the user


- children_the_last_sentiment_lastfor_user: last of the sentiment of the children of the post for the user


- children_the_first_sentiment_ratio_lastfor_user: last of the sentiment of the children of the post for the user


- children_the_last_sentiment_ratio_lastfor_user: last of the sentiment of the children of the post for the user


- children_the_first_sentiment_ratio_strong_lastfor_user: last of the sentiment of the children of the post for the user


- children_the_last_sentiment_ratio_strong_lastfor_user: last of the sentiment of the children of the post for the user


- controversiality_lastfor_user: last of the sentiment of the all children of the post for the user


- all_children_sentiment_avg_lastfor_user: last of the sentiment of the all children of the post for the user


- all_children_sentiment_std_lastfor_user: last of the sentiment of the all children of the post for the user


- all_children_num_of_pos_lastfor_user: last of the sentiment of the all children of the post for the user


- all_children_num_of_neg_lastfor_user: last of the sentiment of the all children of the post for the user


- all_children_num_of_neu_lastfor_user: last of the sentiment of the all children of the post for the user


- all_children_num_of_pos_neg_ratio_lastfor_user: last of the sentiment of the all children of the post for the user


- all_children_most_sentiment_lastfor_user: last of the sentiment of the all children of the post for the user


- all_children_times_of_most_sentiment_lastfor_user: last of the sentiment of the all children of the post for the user


- all_children_the_first_sentiment_lastfor_user: last of the sentiment of the all children of the post for the user


- all_children_the_last_sentiment_lastfor_user: last of the sentiment of the all children of the post for the user


- all_children_the_first_sentiment_ratio_lastfor_user: last of the sentiment of the all children of the post for the user


- all_children_the_last_sentiment_ratio_lastfor_user: last of the sentiment of the all children of the post for the user


- all_children_the_first_sentiment_ratio_strong_lastfor_user: last of the sentiment of the all children of the post for the user


- all_children_the_last_sentiment_ratio_strong_lastfor_user: last of the sentiment of the all children of the post for the user


- all_children_num_of_pos_tree_lastfor_user: last of the sentiment of the all children of the post for the user


- all_children_num_of_neg_tree_lastfor_user: last of the sentiment of the all children of the post for the user


- all_children_num_of_neu_tree_lastfor_user: last of the sentiment of the all children of the post for the user


- all_children_num_of_pos_neg_ratio_tree_lastfor_user: last of the sentiment of the all children of the post for the user


- all_children_most_sentiment_tree_lastfor_user: last of the sentiment of the all children of the post for the user


- all_children_times_of_most_sentiment_tree_lastfor_user: last of the sentiment of the all children of the post for the user


- all_children_the_first_sentiment_tree_lastfor_user: last of the sentiment of the all children of the post for the user


- all_children_the_last_sentiment_tree_lastfor_user: last of the sentiment of the all children of the post for the user


- all_children_the_first_sentiment_ratio_tree_lastfor_user: last of the sentiment of the all children of the post for the user


- all_children_the_last_sentiment_ratio_tree_lastfor_user: last of the sentiment of the all children of the post for the user


- all_children_num_of_controversiality_tree_lastfor_user: last of the sentiment of the all children of the post for the user


- all_children_num_of_controversiality_ratio_tree_lastfor_user: last of the sentiment of the all children of the post for the user


- all_children_the_most_attractive_tree_sentiment_lastfor_user: last of the sentiment of the all children of the post for the user


- all_children_the_most_attractive_tree_controrversiality_lastfor_user: last of the sentiment of the all children of the post for the user


- all_children_controversiality_avg_tree_lastfor_user: last of the sentiment of the all children of the post for the user


- all_children_controversiality_std_tree_lastfor_user: last of the sentiment of the all children of the post for the user


- all_children_controversiality_max_tree_lastfor_user: last of the sentiment of the all children of the post for the user


- all_children_controversiality_min_tree_lastfor_user: last of the sentiment of the all children of the post for the user


- all_children_controversiality_max_min_ratio_tree_lastfor_user: last of the sentiment of the all children of the post for the user


- all_children_controversiality_max_tree_sentiment_lastfor_user: last of the sentiment of the all children of the post for the user


- all_children_controversiality_min_tree_sentiment_lastfor_user: last of the sentiment of the all children of the post for the user


- all_children_controversiality_max_tree_attraction_lastfor_user: last of the sentiment of the all children of the post for the user


- all_children_controversiality_min_tree_attraction_lastfor_user: last of the sentiment of the all children of the post for the user


- all_children_more_than_sentiment_avg_tree_lastfor_user: last of the sentiment of the all children of the post for the user


- all_children_more_than_sentiment_avg_ratio_tree_lastfor_user: last of the sentiment of the all children of the post for the user


- all_children_more_than_attraction_of_controversiality_max_tree_lastfor_user: last of the sentiment of the all children of the post for the user


- all_children_more_than_attraction_of_controversiality_max_ratio_tree_lastfor_user: last of the sentiment of the all children of the post for the user


- all_children_more_than_attraction_of_controversiality_min_tree_lastfor_user: last of the sentiment of the all children of the post for the user


- all_children_more_than_attraction_of_controversiality_min_ratio_tree_lastfor_user: last of the sentiment of the all children of the post for the user
