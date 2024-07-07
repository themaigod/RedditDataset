
# user-level traditional features, train instance level features, combinations of submisisons / comments level features, sentiment features, graph features, subreddit features
user_feature = {
    # user-level traditional features
    "user_id": "user id in reddit",
    "user_created_utc": "the created time of the user",
    "user_premium": "the user is premium or not",
}

instance_feature = {
    # train instance level features
    # "time_start_time_stamp": "the start time stamp of the time window",
    "time_end_time_stamp": "the end time stamp of the time window",
}

# combinations of submisisons / comments level features
# features of seperate days in the time window (train_size)
seperate_day_features = {
    "post_number_{i}_day": "the post number of the user in the {i} day, i = 1, 2, ..., train_size, started from the prediction period",
    "time_gap_{i}_day": "the time gap between the first post and the last post in the {i} day, i = 1, 2, ..., train_size, started from the prediction period",
    "max_time_gap_{i}_day": "the max time gap between two posts in the {i} day, i = 1, 2, ..., train_size, started from the prediction period",
    "min_time_gap_{i}_day": "the min time gap between two posts in the {i} day, i = 1, 2, ..., train_size, started from the prediction period",
    "mean_time_gap_{i}_day": "the mean time gap between two posts in the {i} day, i = 1, 2, ..., train_size, started from the prediction period. it will ignore the max time gap period.",
}
# features of the whole time window (train_size)
whole_time_window_features = {
    "post_number": "the post number of the user in the whole time window",
    "time_gap": "the time gap between the first post and the last post in the whole time window",
    "max_time_gap": "the max time gap between two posts in the whole time window",
    "min_time_gap": "the min time gap between two posts in the whole time window",
    "mean_time_gap": "the mean time gap between two posts in the whole time window. it will ignore the max time gap period.",
}
# features of single comment
comment_features = {
    "num_of_all_awardings": "the number of all awardings of the comment. it will be 0 if the comment has no awardings. it may show the popularity of the comment, but may leaking the information of the future related to the label.",
    "achieved": "achieved or not of the comment, post will be achieved if it has been 180 days since the post was created",
    # "num_of_awarders": "the nums of awarders of the comment. it will be 0 if the comment has no awarders. it may show the popularity of the comment, but may leaking the information of the future related to the label.",
    # "hide_score": "hide score of the comment",
    # "is_crosspostable": "is a sharing post from another subreddit or not",
    # "is_meta": "is a meta post or not, it may be a post about the subreddit itself",
    # "is_created_from_ads_ui": "is created from ads ui or not",
    # "is_original_content": "is original content or not",
    # "is_robot_indexable": "is the post can be indexed by robots or not",
    # "is_video": "is a video post or not",
    # "media_only": "if the post only contains media or not",
    # "if_video": "if the post contains video or not",
    # "over_18": "if the post is visible only to users over 18 or not",
    # "spoiler": "if the post is a spoiler or not, it may be a spoiler of a movie or a game",
    "stickied": "if the post is stickied or not, it may be a post that the moderator wants to highlight",
    # "upvote_ratio": "the upvote ratio of the post, it may be a good feature, but may leaking the information of the future related to the label.",
    "collapsed": "collapsed or not for the comment, it is judged by the reddit algorithm which may be related to the label",
    "controversiality": "the controversiality of the comment, it may be a good feature, but may leaking the information of the future related to the label.",
    "gilded": "the gilded of the comment, it means the author will get a month of Reddit Premium and 100 Coins, it may be a good feature, but may leaking the information of the future related to the label.",
    "edited":"edited or not for the comment.",
    "num_of_guildings": "the number of guildings of the comment, it may be a good feature, but may leaking the information of the future related to the label.",
    "locked": "locked or not for the comment, it means the comment is locked by the moderator and no one can comment on it.",
    "no_follow": "no follow or not for the comment, it means tell the search engines to not follow the link.",
    "body_length": "the length of the body of the comment",
    "can_gild": "can gild or not for the comment, it means the comment can be gilded or not.",
    "created_utc": "the created time of the comment",
    "num_of_gildings": "the number of gildings of the comment, it may be a good feature, but may leaking the information of the future related to the label.",
    "score": "the score of the comment, it may be a good feature, but may leaking the information of the future related to the label.",
    "score_hidden": "score hidden or not for the comment, it means the score of the comment is hidden or not.",
    "send_replies": "send replies or not for the comment, it means the author will receive a notification when someone comments on the comment.",
    "is_submitter": "the author is the submitter of the post or not",
    "have_unrepliable_reason": "have unrepliable reason or not for the comment.",
    "post_level": "the level of the whole post tree, it means the post is the i level leaves of the whole post tree. i.e. 0 means the post is the root of the whole post tree.",
    "comment_type": "the type of the comment, mostly it is None",
    "num_of_comments": "the number of comments of the comment in the observation period",
    "subreddit_subscribers": "the number of subscribers of the subreddit of the comment",
    "subreddit_type": "the type of the subreddit of the comment, mostly it is None",
    "subreddit_id": "the id of the subreddit of the comment",

    # author features
    "author_created_utc": "the created time of the author",
    "author_premium": "the author is premium or not",
}
# features of single submission
submission_features = {
    "num_of_all_awardings": "the number of all awardings of the submission. it will be 0 if the submission has no awardings. it may show the popularity of the submission, but may leaking the information of the future related to the label.",
    "allow_live_comments": "allow live comments or not for the submission, it means the submission can be commented on while it is live.",
    "archived": "archived or not for the submission, it will be archived if it has been 180 days since the submission was created.",
    "num_of_awarders": "the nums of awarders of the submission. it will be 0 if the submission has no awarders. it may show the popularity of the submission, but may leaking the information of the future related to the label.",
    "banned_by_someone": "banned by someone or not for the submission",
    "can_gild": "can gild or not for the submission, it means the submission can be gilded or not.",
    "can_mod_post": "Whether the logged-in user can modify the post",
    "category": "the category of the submission, mostly it is None",
    "num_of_comments": "the number of comments of the submission in the observation period",
    "contest_mode": "if the moderators choose to enable contest mode for the subreddit, it means the comment scores will be hidden and comments will be sorted randomly.",
    "created_utc": "the created time of the submission",
    "content_categories": "the content categories of the submission, mostly it is None",
    "discussion_type": "the discussion type of the submission, mostly it is None",
    "distinguished": "the distinguished of the submission, mostly it is None",
    "domain": "the domain of the submission",
    "edited": "edited or not for the submission.",
    "num_of_guildings": "the number of guildings of the submission, it may be a good feature, but may leaking the information of the future related to the label.",
    "gilded": "the gilded of the submission, it means the author will get a month of Reddit Premium and 100 Coins, it may be a good feature, but may leaking the information of the future related to the label.",
    "hidden": "hidden or not for the submission, it means the submission is hidden or not.",
    "hide_score": "hide score or not for the submission, it means the score of the submission is hidden or not.",
    "is_crosspostable": "is a sharing post from another subreddit or not",
    "is_meta": "is a meta post or not, it may be a post about the subreddit itself",
    "is_created_from_ads_ui": "is created from ads ui or not",
    "is_original_content": "is original content or not",
    "is_reddit_media_domain": "is reddit media domain or not",
    "is_robot_indexable": "is the post can be indexed by robots or not",
    "is_self": "is self or not for the submission, it means the submission is a self post or not.",
    "is_video": "is a video post or not",
    "link_flair_background_color": "the link flair background color of the submission, mostly it is None",
    "link_flair_css_class": "the link flair css class of the submission, mostly it is None",
    "link_flair_richtext": "the link flair richtext of the submission, mostly it is None",
    "link_flair_template_id": "the link flair template id of the submission, mostly it is None",
    "link_flair_text": "the link flair text of the submission, mostly it is None",
    "link_flair_text_color": "the link flair text color of the submission, mostly it is None",
    "link_flair_type": "the link flair type of the submission, mostly it is None",
    "locked": "locked or not for the submission, it means the submission is locked by the moderator and no one can comment on it.",
    "media_only": "if the submission only contains media or not",
    "no_follow": "no follow or not for the submission, it means tell the search engines to not follow the link.",
    "num_crossposts": "the number of crossposts of the submission. it may be a good feature, but may leaking the information of the future related to the label.",
    "over_18": "if the submission is visible only to users over 18 or not",
    "parent_whitelist_status": "the parent whitelist status of the submission, mostly it is None",
    "pinned": "pinned or not for the submission, it means the submission is pinned or not.",
    "pwls": "the pwls of the submission",
    "quarantine": "quarantine or not for the submission, it means the submission is quarantined or not.",
    "removed_by_someone": "removed by someone or not for the submission",
    "score": "the score of the submission, it may be a good feature, but may leaking the information of the future related to the label.",
    "length_of_selftext": "the length of the selftext of the submission",
    "length_of_title": "the length of the title of the submission",
    "send_replies": "send replies or not for the submission, it means the author will receive a notification when someone comments on the submission.",
    "spoiler": "if the submission is a spoiler or not, it may be a spoiler of a movie or a game",
    "stickied": "if the submission is stickied or not, it may be a post that the moderator wants to highlight",
    "subreddit_subscribers": "the number of subscribers of the subreddit of the submission",
    "suggested_sort": "the suggested sort of the submission, mostly it is None",
    "subreddit_id": "the id of the subreddit of the submission",
    "subreddit_type": "the type of the subreddit of the submission, mostly it is None",
    "thumbnail": "the thumbnail of the submission, mostly it is default",
    "top_awarded_type": "the top awarded type of the submission, mostly it is None",
    "total_awards_received": "the total awards received of the submission, it may be a good feature, but may leaking the information of the future related to the label.",
    "treatment_tags": "the treatment tags of the submission, mostly it is None",
    "upvote_ratio": "the upvote ratio of the submission, it may be a good feature, but may leaking the information of the future related to the label.",
    "whitelist_status": "the whitelist status of the submission, mostly it is None",
    "wls": "the wls of the submission, mostly it is 6",
    "num_of_all_comments": "the number of all comments of the submission in the observation period, including the comments of the comments",
    
    # author features
    "author_created_utc": "the created time of the author",
    "author_premium": "the author is premium or not",
}

label = {
    "label": "the label of the user, it means the user will be engaged or not in the prediction period",
}

# sentiment features
# single post sentiment features
sentiment_features_of_single_post = {
    "sentiment": "the sentiment of the post",
}
# sentiment features of the whole time window (train_size)
sentiment_features_of_whole_time_window = {
    "sentiment_avg": "the average sentiment of the whole time window",
    "sentiment_std": "the standard deviation of the sentiment of the whole time window",
    "num_of_pos": "the number of positive posts of the whole time window",
    "num_of_neg": "the number of negative posts of the whole time window",
    "num_of_neu": "the number of neutral posts of the whole time window",
    "num_of_pos_neg_ratio": "the number of positive posts divided by the number of negative posts of the whole time window",
    "most_sentiment": "the most sentiment of the whole time window",
    "times_of_most_sentiment": "the times of the most sentiment of the whole time window",
    "times_of_sentiment_change": "the times of the sentiment change of the whole time window",
    "times_of_sentiment_change_ratio": "the times of the sentiment change divided by the number of posts of the whole time window",
    "times_of_sentiment_change_ratio_strong": "the times of the sentiment change divided by the number of posts of the whole time window, but the sentiment change is only counted when the sentiment is changed from positive to negative or negative to positive",
    "times_of_sentiment_keep": "the times of the sentiment keep of the whole time window",
    "times_of_sentiment_keep_ratio": "the times of the sentiment keep divided by the number of posts of the whole time window",
    "times_of_sentiment_keep_ratio_strong": "the times of the sentiment keep divided by the number of posts of the whole time window, but the sentiment keep is only counted when the sentiment is positive or negative",
    "times_of_sentiment_keep_ratio_weak": "the times of the sentiment keep divided by the number of posts of the whole time window, but the sentiment keep is counted even when the sentiment is neutral",
    "the_first_sentiment": "the first sentiment of the whole time window",
    "the_last_sentiment": "the last sentiment of the whole time window",
    "the_first_sentiment_ratio": "the first sentiment divided by the number of posts of the whole time window",
    "the_last_sentiment_ratio": "the last sentiment divided by the number of posts of the whole time window",
    "the_first_sentiment_ratio_strong": "the first sentiment divided by the number of posts of the whole time window, but the first sentiment is only counted when the sentiment is positive or negative",
    "the_last_sentiment_ratio_strong": "the last sentiment divided by the number of posts of the whole time window, but the last sentiment is only counted when the sentiment is positive or negative",
}
# sentiment features of seperate days in the time window (train_size)
sentiment_features_of_seperate_days = {
    key + "_{i}_day": value + " in the {i} day, i = 1, 2, ..., train_size, started from the prediction period" for key, value in sentiment_features_of_whole_time_window.items()
}
# sentiment features of single post in a post tree
sentiment_features_of_single_post_in_a_post_tree_about_parent = {
    "parent_sentiment_avg": "the average sentiment of the parent of the post",
    "parent_sentiment_std": "the standard deviation of the sentiment of the parent of the post",
    "parent_num_of_pos": "the number of positive posts of the parent of the post",
    "parent_num_of_neg": "the number of negative posts of the parent of the post",
    "parent_num_of_neu": "the number of neutral posts of the parent of the post",
    "parent_num_of_pos_neg_ratio": "the number of positive posts divided by the number of negative posts of the parent of the post",
    "parent_most_sentiment": "the most sentiment of the parent of the post",
    "parent_times_of_most_sentiment": "the times of the most sentiment of the parent of the post",
    "parent_times_of_sentiment_change": "the times of the sentiment change of the parent of the post",
    "parent_times_of_sentiment_change_ratio": "the times of the sentiment change divided by the number of posts of the parent of the post",
    "parent_times_of_sentiment_change_ratio_strong": "the times of the sentiment change divided by the number of posts of the parent of the post, but the sentiment change is only counted when the sentiment is changed from positive to negative or negative to positive",
    "parent_times_of_sentiment_keep": "the times of the sentiment keep of the parent of the post",
    "parent_times_of_sentiment_keep_ratio": "the times of the sentiment keep divided by the number of posts of the parent of the post",
    "parent_times_of_sentiment_keep_ratio_strong": "the times of the sentiment keep divided by the number of posts of the parent of the post, but the sentiment keep is only counted when the sentiment is positive or negative",
    "parent_times_of_sentiment_keep_ratio_weak": "the times of the sentiment keep divided by the number of posts of the parent of the post, but the sentiment keep is counted even when the sentiment is neutral",
    "parent_the_first_sentiment": "the first sentiment of the parent of the post",
    "parent_the_last_sentiment": "the last sentiment of the parent of the post",
    "parent_the_first_sentiment_ratio": "the first sentiment divided by the number of posts of the parent of the post",
    "parent_the_last_sentiment_ratio": "the last sentiment divided by the number of posts of the parent of the post",
    "parent_the_first_sentiment_ratio_strong": "the first sentiment divided by the number of posts of the parent of the post, but the first sentiment is only counted when the sentiment is positive or negative",
    "parent_the_last_sentiment_ratio_strong": "the last sentiment divided by the number of posts of the parent of the post, but the last sentiment is only counted when the sentiment is positive or negative",
}
sentiment_features_of_single_post_in_a_post_tree_about_children = {
    "children_sentiment_avg": "the average sentiment of the children of the post",
    "children_sentiment_std": "the standard deviation of the sentiment of the children of the post",
    "children_num_of_pos": "the number of positive posts of the children of the post",
    "children_num_of_neg": "the number of negative posts of the children of the post",
    "children_num_of_neu": "the number of neutral posts of the children of the post",
    "children_num_of_pos_neg_ratio": "the number of positive posts divided by the number of negative posts of the children of the post",
    "children_most_sentiment": "the most sentiment of the children of the post",
    "children_times_of_most_sentiment": "the times of the most sentiment of the children of the post",
    "children_times_of_sentiment_change": "the times of the sentiment change of the children of the post",
    "children_times_of_sentiment_change_ratio": "the times of the sentiment change divided by the number of posts of the children of the post",
    "children_times_of_sentiment_change_ratio_strong": "the times of the sentiment change divided by the number of posts of the children of the post, but the sentiment change is only counted when the sentiment is changed from positive to negative or negative to positive",
    "children_times_of_sentiment_keep": "the times of the sentiment keep of the children of the post",
    "children_times_of_sentiment_keep_ratio": "the times of the sentiment keep divided by the number of posts of the children of the post",
    "children_times_of_sentiment_keep_ratio_strong": "the times of the sentiment keep divided by the number of posts of the children of the post, but the sentiment keep is only counted when the sentiment is positive or negative",
    "children_times_of_sentiment_keep_ratio_weak": "the times of the sentiment keep divided by the number of posts of the children of the post, but the sentiment keep is counted even when the sentiment is neutral",
    "children_the_first_sentiment": "the first sentiment of the children of the post",
    "children_the_last_sentiment": "the last sentiment of the children of the post",
    "children_the_first_sentiment_ratio": "the first sentiment divided by the number of posts of the children of the post",
    "children_the_last_sentiment_ratio": "the last sentiment divided by the number of posts of the children of the post",
    "children_the_first_sentiment_ratio_strong": "the first sentiment divided by the number of posts of the children of the post, but the first sentiment is only counted when the sentiment is positive or negative",
    "children_the_last_sentiment_ratio_strong": "the last sentiment divided by the number of posts of the children of the post, but the last sentiment is only counted when the sentiment is positive or negative",
}
sentiment_features_of_single_post_in_a_post_tree_about_all_children = {
    "controversiality": "the controversiality of the post, it means the ratio of childrens (including the current post) which are controversial to the root of the post tree",
    "all_children_sentiment_avg": "the average sentiment of the all children of the post, including the children of the children",
    "all_children_sentiment_std": "the standard deviation of the sentiment of the all children of the post, including the children of the children",
    "all_children_num_of_pos": "the number of positive posts of the all children of the post, including the children of the children",
    "all_children_num_of_neg": "the number of negative posts of the all children of the post, including the children of the children",
    "all_children_num_of_neu": "the number of neutral posts of the all children of the post, including the children of the children",
    "all_children_num_of_pos_neg_ratio": "the number of positive posts divided by the number of negative posts of the all children of the post, including the children of the children",
    "all_children_most_sentiment": "the most sentiment of the all children of the post, including the children of the children",
    "all_children_times_of_most_sentiment": "the times of the most sentiment of the all children of the post, including the children of the children",
    "all_children_the_first_sentiment": "the first sentiment of the all children of the post, including the children of the children",
    "all_children_the_last_sentiment": "the last sentiment of the all children of the post, including the children of the children",
    "all_children_the_first_sentiment_ratio": "the first sentiment divided by the number of posts of the all children of the post, including the children of the children",
    "all_children_the_last_sentiment_ratio": "the last sentiment divided by the number of posts of the all children of the post, including the children of the children",
    "all_children_the_first_sentiment_ratio_strong": "the first sentiment divided by the number of posts of the all children of the post, including the children of the children, but the first sentiment is only counted when the sentiment is positive or negative",
    "all_children_the_last_sentiment_ratio_strong": "the last sentiment divided by the number of posts of the all children of the post, including the children of the children, but the last sentiment is only counted when the sentiment is positive or negative",
    "all_children_num_of_pos_tree": "the number of positive posts of the all children of the post, including the children of the children, but the positive posts are only counted when the sentiment is positive or negative",
    "all_children_num_of_neg_tree": "the number of negative posts of the all children of the post, including the children of the children, but the negative posts are only counted when the sentiment is positive or negative",
    "all_children_num_of_neu_tree": "the number of neutral posts of the all children of the post, including the children of the children, but the neutral posts are only counted when the sentiment is positive or negative",
    "all_children_num_of_pos_neg_ratio_tree": "the number of positive posts divided by the number of negative posts of the all children of the post, including the children of the children, but the positive posts and negative posts are only counted when the sentiment is positive or negative",
    "all_children_most_sentiment_tree": "the most sentiment of the all children of the post, including the children of the children, but the most sentiment is only counted when the sentiment is positive or negative",
    "all_children_times_of_most_sentiment_tree": "the times of the most sentiment of the all children of the post, including the children of the children, but the most sentiment is only counted when the sentiment is positive or negative",
    "all_children_the_first_sentiment_tree": "the first sentiment of the all children of the post, including the children of the children, but the first sentiment is only counted when the sentiment is positive or negative",
    "all_children_the_last_sentiment_tree": "the last sentiment of the all children of the post, including the children of the children, but the last sentiment is only counted when the sentiment is positive or negative",
    "all_children_the_first_sentiment_ratio_tree": "the first sentiment divided by the number of posts of the all children of the post, including the children of the children, but the first sentiment is only counted when the sentiment is positive or negative",
    "all_children_the_last_sentiment_ratio_tree": "the last sentiment divided by the number of posts of the all children of the post, including the children of the children, but the last sentiment is only counted when the sentiment is positive or negative",
    "all_children_num_of_controversiality_tree": "the number of post trees which are controversiality. it means the controversal sentiment of the root of the post tree is more than 0.5 in the all children of the post, including the children of the children",
    "all_children_num_of_controversiality_ratio_tree": "the number of post trees which are controversiality divided by the number of post trees in the all children of the post, including the children of the children",
    "all_children_the_most_attractive_tree_sentiment": "the most attractive sentiment of the all children of the post, including the children of the children, but the most attractive sentiment is only counted when the sentiment is positive or negative",
    "all_children_the_most_attractive_tree_controrversiality": "the most attractive controversiality of the all children of the post, including the children of the children, but the most attractive controversiality is only counted when the sentiment is positive or negative",
    "all_children_controversiality_avg_tree": "the average controversiality of the all children of the post, including the children of the children, but the controversiality is only counted when the sentiment is positive or negative",
    "all_children_controversiality_std_tree": "the standard deviation of the controversiality of the all children of the post, including the children of the children, but the controversiality is only counted when the sentiment is positive or negative",
    "all_children_controversiality_max_tree": "the max controversiality of the all children of the post, including the children of the children, but the controversiality is only counted when the sentiment is positive or negative",
    "all_children_controversiality_min_tree": "the min controversiality of the all children of the post, including the children of the children, but the controversiality is only counted when the sentiment is positive or negative",
    "all_children_controversiality_max_min_ratio_tree": "the max controversiality divided by the min controversiality of the all children of the post, including the children of the children, but the controversiality is only counted when the sentiment is positive or negative",
    "all_children_controversiality_max_tree_sentiment": "the max controversiality sentiment of the all children of the post, including the children of the children, but the controversiality sentiment is only counted when the sentiment is positive or negative",
    "all_children_controversiality_min_tree_sentiment": "the min controversiality sentiment of the all children of the post, including the children of the children, but the controversiality sentiment is only counted when the sentiment is positive or negative",
    "all_children_controversiality_max_tree_attraction": "the max controversiality attraction of the all children of the post, including the children of the children, but the controversiality attraction is only counted when the sentiment is positive or negative",
    "all_children_controversiality_min_tree_attraction": "the min controversiality attraction of the all children of the post, including the children of the children, but the controversiality attraction is only counted when the sentiment is positive or negative",
    "all_children_more_than_sentiment_avg_tree": "the number of posts which are more than the average sentiment of the all children of the post, including the children of the children, but the sentiment is only counted when the sentiment is positive or negative",
    "all_children_more_than_sentiment_avg_ratio_tree": "the number of posts which are more than the average sentiment divided by the number of posts of the all children of the post, including the children of the children, but the sentiment is only counted when the sentiment is positive or negative",
    "all_children_more_than_attraction_of_controversiality_max_tree": "the number of posts which are more than the controversiality max attraction of the all children of the post, including the children of the children, but the controversiality attraction is only counted when the sentiment is positive or negative",
    "all_children_more_than_attraction_of_controversiality_max_ratio_tree": "the number of posts which are more than the controversiality max attraction divided by the number of posts of the all children of the post, including the children of the children, but the controversiality attraction is only counted when the sentiment is positive or negative",
    "all_children_more_than_attraction_of_controversiality_min_tree": "the number of posts which are more than the controversiality min attraction of the all children of the post, including the children of the children, but the controversiality attraction is only counted when the sentiment is positive or negative",
    "all_children_more_than_attraction_of_controversiality_min_ratio_tree": "the number of posts which are more than the controversiality min attraction divided by the number of posts of the all children of the post, including the children of the children, but the controversiality attraction is only counted when the sentiment is positive or negative",
}

# combine comment features to user features, using average, std, max, min, first, last for itself, parent, children, all_children.
user_feature_comment = {}
for key, value in comment_features.items():
    for method in ["avg", "std", "max", "min", "first", "last"]:
        for type_ in ["", "_parent", "_children", "_all_children"]:
            user_feature_comment[key + "_" + method + type_] = value + " " + method + " of the comment" + type_
            
# combine submission features to user features, using average, std, max, min, first, last for itself, children, all_children.
user_feature_submission = {}
for key, value in submission_features.items():
    for method in ["avg", "std", "max", "min", "first", "last"]:
        for type_ in ["", "_children", "_all_children"]:
            user_feature_submission[key + "_" + method + type_] = value + " " + method + " of the submission" + type_
            
# combine comment and submission features to user features, using average, std, max, min, first, last for itself, parent, children, all_children.
user_feature_post = {}
key_set = set(comment_features.keys()) | set(submission_features.keys())
for key in key_set:
    for method in ["avg", "std", "max", "min", "first", "last"]:
        for type_ in ["", "_parent", "_children", "_all_children"]:
            user_feature_post[key + "_" + method + type_] = method + " of the post" + type_ + " for the feature " + key
            
# sentiment features from post level to user level
user_feature_sentiment = {}
for method in ["avg", "std", "max", "min", "first", "last"]:
    for key, value in sentiment_features_of_whole_time_window.items():
        user_feature_sentiment[key + "_" + method + "for_user"] = method + " of the sentiment of the observation window for the user"
    for key, value in sentiment_features_of_single_post_in_a_post_tree_about_parent.items():
        user_feature_sentiment[key + "_" + method + "for_user"] = method + " of the sentiment of the parent of the post for the user"
    for key, value in sentiment_features_of_single_post_in_a_post_tree_about_children.items():
        user_feature_sentiment[key + "_" + method + "for_user"] = method + " of the sentiment of the children of the post for the user"
    for key, value in sentiment_features_of_single_post_in_a_post_tree_about_all_children.items():
        user_feature_sentiment[key + "_" + method + "for_user"] = method + " of the sentiment of the all children of the post for the user"

def generate_feature_tree():
    feature_tree = {
        "user": user_feature,
        "instance": instance_feature,
        "comment": comment_features,
        "submission": submission_features,
        "label": label,
        "sentiment": {
            "post": sentiment_features_of_single_post,
            "whole_time_window": sentiment_features_of_whole_time_window,
            "seperate_days": sentiment_features_of_seperate_days,
            "single_post_in_a_post_tree": {
                "parent": sentiment_features_of_single_post_in_a_post_tree_about_parent,
                "children": sentiment_features_of_single_post_in_a_post_tree_about_children,
                "all_children": sentiment_features_of_single_post_in_a_post_tree_about_all_children,
            },
            
        },
        "user_feature_from_post": {
            "comment": user_feature_comment,
            "submission": user_feature_submission,
            "post": user_feature_post,
            "sentiment": user_feature_sentiment,
        },
    }
    return feature_tree


def generate_markdown_file(path=None):
    if path is None:
        path = "features.md"
        
    feature_tree = generate_feature_tree()
    

    def decode_feature_tree_recursively(feature_tree, depth=0):
        output_str = ""
        for key, value in feature_tree.items():
            if isinstance(value, dict):
                # output_str += "\n" * depth + f"## {key}\n"
                # title level is judged by the depth
                output_str += "\n" * depth + f"{'#' * (depth + 2)} {key}\n"
                output_str += decode_feature_tree_recursively(value, depth + 1)
            else:
                output_str += "\n" * depth + f"- {key}: {value}\n"
        return output_str
                
    md_content = decode_feature_tree_recursively(feature_tree)
    
    with open(path, "w") as f:
        f.write(md_content)
        
        
if __name__ == "__main__":
    generate_markdown_file()
    
            


    


    
    
    

