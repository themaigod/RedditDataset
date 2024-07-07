from data_process.graph_generator import GraphGenerator
from typing import Tuple        
import numpy as np
from collections import defaultdict


feature_function = {}

feature_function_low_level = defaultdict(dict)
feature_function_low_level_unleaked = defaultdict(dict)


# a decorator to register a feature function
def feature_function_register(name):
    def decorator(f):
        feature_function[name] = f
        return f
    return decorator

# a decorator to register a low level feature function
def feature_function_low_level_register(level, name, unleaked=True):
    def decorator(f):
        feature_function_low_level[level][name] = f
        if unleaked:
            feature_function_low_level_unleaked[level][name] = f
        return f
    return decorator




# user level features
@feature_function_register('user_id')
def get_user_id(user_id, graph_generator: GraphGenerator, **kwargs):
    return user_id


@feature_function_register('user_created_utc')
def get_user_created_utc(user_id, graph_generator: GraphGenerator, **kwargs):
    idx = 0
    while True:
        activity: Tuple = graph_generator.data['redditor'][user_id].activity[idx]
        activity_object = graph_generator.data[activity[2]][activity[1]]
        try:
            user_created_utc = activity_object.author_created_utc
            if user_created_utc is not None:
                break
        except:
            pass
        idx += 1
        if idx >= len(graph_generator.data['redditor'][user_id].activity):
            user_created_utc = None
            break
    if user_created_utc is None:
        return np.nan
    
    return user_created_utc

@feature_function_register('user_premium')
def get_user_premium(user_id, graph_generator: GraphGenerator, **kwargs):
    idx = 0
    while True:
        activity: Tuple = graph_generator.data['redditor'][user_id].activity[idx]
        activity_object = graph_generator.data[activity[2]][activity[1]]
        try:
            user_premium = activity_object.author_premium
            if user_premium is not None:
                break
        except:
            pass
        idx += 1
        if idx >= len(graph_generator.data['redditor'][user_id].activity):
            user_premium = None
            break
    if user_premium is None:
        return np.nan
    
    return user_premium


# instance level features
@feature_function_register('time_end_time_stamp')
def get_time_end_time_stamp(observation_time_window, graph_generator: GraphGenerator, **kwargs):
    return observation_time_window[1]


# comment level features, which cannot directly contribute to the user level features
# so we use the low level decorator
@feature_function_low_level_register('comment', 'num_of_all_awardings', unleaked=False)
def get_num_of_all_awardings_comment(comment_id, graph_generator: GraphGenerator, **kwargs):
    try:
        return len(graph_generator.data['comment'][comment_id].all_awardings)
    except:
        return np.nan
    
    
@feature_function_low_level_register('comment', 'comment_id')
def get_comment_id_comment(comment_id, graph_generator: GraphGenerator, **kwargs):
    return comment_id


@feature_function_low_level_register('comment', 'observation_time_window_end')
def get_observation_time_window_end_comment(comment_id, graph_generator: GraphGenerator, observation_time_window, **kwargs):
    return observation_time_window[1]
    
@feature_function_low_level_register('comment', 'archived')
def get_archived_comment(comment_id, graph_generator: GraphGenerator, **kwargs):
    try:
        archived = graph_generator.data['comment'][comment_id].archived
        if archived is None:
            return np.nan
        else:
            return int(archived)
    except:
        return np.nan
    

@feature_function_low_level_register('comment', 'stickied')
def get_stickied_comment(comment_id, graph_generator: GraphGenerator, **kwargs):
    try:
        stickied = graph_generator.data['comment'][comment_id].stickied
        if stickied is None:
            return np.nan
        else:
            return int(stickied)
    except:
        return np.nan
    

@feature_function_low_level_register('comment', 'collapsed')
def get_collapsed_comment(comment_id, graph_generator: GraphGenerator, **kwargs):
    try:
        collapsed = graph_generator.data['comment'][comment_id].collapsed
        if collapsed is None:
            return np.nan
        else:
            return int(collapsed)
    except:
        return np.nan
    

@feature_function_low_level_register('comment', 'controversiality', unleaked=False)
def get_controversiality_comment(comment_id, graph_generator: GraphGenerator, **kwargs):
    try:
        controversiality = graph_generator.data['comment'][comment_id].controversiality
        if controversiality is None:
            return np.nan
        else:
            return int(controversiality)
    except:
        return np.nan
    
    
@feature_function_low_level_register('comment', 'gilded', unleaked=False)
def get_gilded_comment(comment_id, graph_generator: GraphGenerator, **kwargs):
    try:
        gilded = graph_generator.data['comment'][comment_id].gilded
        if gilded is None:
            return np.nan
        else:
            return int(gilded)
    except:
        return np.nan
    
    
@feature_function_low_level_register('comment', 'edited')
def get_edited_comment(comment_id, graph_generator: GraphGenerator, **kwargs):
    try:
        edited = graph_generator.data['comment'][comment_id].edited
        if edited is None:
            return np.nan
        else:
            return int(edited)
    except:
        return np.nan
    
    
@feature_function_low_level_register('comment', 'num_of_gildings', unleaked=False)
def get_num_of_gildings_comment(comment_id, graph_generator: GraphGenerator, **kwargs):
    try:
        return len(graph_generator.data['comment'][comment_id].gildings)
    except:
        return np.nan
    
    
@feature_function_low_level_register('comment', 'locked')
def get_locked_comment(comment_id, graph_generator: GraphGenerator, **kwargs):
    try:
        locked = graph_generator.data['comment'][comment_id].locked
        if locked is None:
            return np.nan
        else:
            return int(locked)
    except:
        return np.nan
    

@feature_function_low_level_register('comment', 'no_follow')
def get_no_follow_comment(comment_id, graph_generator: GraphGenerator, **kwargs):
    try:
        no_follow = graph_generator.data['comment'][comment_id].no_follow
        if no_follow is None:
            return np.nan
        else:
            return int(no_follow)
    except:
        return np.nan
    
    
@feature_function_low_level_register('comment', 'body_length')
def get_body_length_comment(comment_id, graph_generator: GraphGenerator, **kwargs):
    try:
        return len(graph_generator.data['comment'][comment_id].body)
    except:
        return np.nan
    
    
@feature_function_low_level_register('comment', 'body_word_count')
def get_body_word_count_comment(comment_id, graph_generator: GraphGenerator, **kwargs):
    try:
        return len(graph_generator.data['comment'][comment_id].body.split())
    except:
        return np.nan
    

@feature_function_low_level_register('comment', 'can_gild')
def get_can_gild_comment(comment_id, graph_generator: GraphGenerator, **kwargs):
    try:
        can_gild = graph_generator.data['comment'][comment_id].can_gild
        if can_gild is None:
            return np.nan
        else:
            return int(can_gild)
    except:
        return np.nan
    
    
@feature_function_low_level_register('comment', 'created_utc')
def get_created_utc_comment(comment_id, graph_generator: GraphGenerator, **kwargs):
    try:
        return int(graph_generator.data['comment'][comment_id].created_utc)
    except:
        return np.nan
    
    
@feature_function_low_level_register('comment', 'num_of_gildings', unleaked=False)
def get_num_of_gildings_comment(comment_id, graph_generator: GraphGenerator, **kwargs):
    try:
        return len(graph_generator.data['comment'][comment_id].gildings)
    except:
        return np.nan
    

@feature_function_low_level_register('comment', 'score', unleaked=False)
def get_score_comment(comment_id, graph_generator: GraphGenerator, **kwargs):
    try:
        return int(graph_generator.data['comment'][comment_id].score)
    except:
        return np.nan
    

@feature_function_low_level_register('comment', 'score_hidden')
def get_score_hidden_comment(comment_id, graph_generator: GraphGenerator, **kwargs):
    try:
        score_hidden = graph_generator.data['comment'][comment_id].score_hidden
        if score_hidden is None:
            return np.nan
        else:
            return int(score_hidden)
    except:
        return np.nan
    
    
@feature_function_low_level_register('comment', 'send_replies')
def get_send_replies_comment(comment_id, graph_generator: GraphGenerator, **kwargs):
    try:
        send_replies = graph_generator.data['comment'][comment_id].send_replies
        if send_replies is None:
            return np.nan
        else:
            return int(send_replies)
    except:
        return np.nan
    
    
@feature_function_low_level_register('comment', 'is_submitter')
def get_is_submitter_comment(comment_id, graph_generator: GraphGenerator, **kwargs):
    try:
        is_submitter = graph_generator.data['comment'][comment_id].is_submitter
        if is_submitter is None:
            return np.nan
        else:
            return int(is_submitter)
    except:
        return np.nan
    
    
@feature_function_low_level_register('comment', 'have_unrepliable_reason')
def get_have_unrepliable_reason_comment(comment_id, graph_generator: GraphGenerator, **kwargs):
    try:
        have_unrepliable_reason = graph_generator.data['comment'][comment_id].unrepliable_reason
        if have_unrepliable_reason is None:
            return 0
        else:
            return 1
    except:
        return np.nan
    
    
@feature_function_low_level_register('comment', 'post_level')
def get_post_level_comment(comment_id, graph_generator: GraphGenerator, **kwargs):
    try:
        return len(graph_generator.data['comment'][comment_id].generate_parent_chain())
    except:
        return np.nan
    
    
comment_type_dict = {}
    
@feature_function_low_level_register('comment', 'comment_type')
def get_comment_type_comment(comment_id, graph_generator: GraphGenerator, **kwargs):
    try:
        comment_type = graph_generator.data['comment'][comment_id].comment_type
        if comment_type is None:
            return np.nan
        comment_type_id = comment_type_dict.get(comment_type, None)
        if comment_type_id is None:
            comment_type_id = len(comment_type_dict)
            comment_type_dict[graph_generator.data['comment'][comment_id].comment_type] = comment_type_id
        return comment_type_id
    except:
        return np.nan
    

@feature_function_low_level_register('comment', 'num_of_comments')
def get_num_of_comments_comment(comment_id, graph_generator: GraphGenerator, observation_time_window, **kwargs):
    try:
        comment = graph_generator.data['comment'][comment_id]
        comment_replies = comment.comments_id
        num = 0
        for comment_reply in comment_replies:
            comment_reply_object = graph_generator.data['comment'][comment_reply]
            if comment_reply_object.created_utc < observation_time_window[1]:
                num += 1
        return num
    except:
        return np.nan
    
    
@feature_function_low_level_register('comment', 'num_of_all_comments')
def get_num_of_all_comments_comment(comment_id, graph_generator: GraphGenerator, **kwargs):
    try:
        return len(graph_generator.data['comment'][comment_id].comments_total_id)
    except:
        return np.nan
                

# subreddit level features
@feature_function_low_level_register('subreddit', 'subscribers', unleaked=False)
def get_subscribers_subreddit(subreddit_id, graph_generator: GraphGenerator, **kwargs):
    try:
        idx = 0
        while True:
            submission_id: Tuple = graph_generator.data['subreddit'][subreddit_id].submissions_id[idx]
            submission = graph_generator.data['submission'][submission_id]
            subscribers = submission.subreddit_subscribers
            if subscribers is not None:
                break
            idx += 1
            if idx >= len(graph_generator.data['subreddit'][subreddit_id].submissions_id):
                subscribers = None
                break
            
        idx = 0
        while True:
            comment_id: Tuple = graph_generator.data['subreddit'][subreddit_id].comments_id[idx]
            comment = graph_generator.data['comment'][comment_id]
            subscribers = comment.subreddit_subscribers
            if subscribers is not None:
                break
            idx += 1
            if idx >= len(graph_generator.data['subreddit'][subreddit_id].comments_id):
                subscribers = None
                break
            
        if subscribers is None:
            return np.nan
        else:
            return subscribers
            
    except:
        return np.nan
    
    
    
subreddit_type_dict = {}
    
@feature_function_low_level_register('subreddit', 'subreddit_type')
def get_subreddit_type_subreddit(subreddit_id, graph_generator: GraphGenerator, **kwargs):
    try:
        idx = 0
        while True:
            submission_id: Tuple = graph_generator.data['subreddit'][subreddit_id].submissions_id[idx]
            submission = graph_generator.data['submission'][submission_id]
            subreddit_type = submission.subreddit_type
            if subreddit_type is not None:
                break
            idx += 1
            if idx >= len(graph_generator.data['subreddit'][subreddit_id].submissions_id):
                subreddit_type = None
                break
            
        idx = 0
        while True:
            comment_id: Tuple = graph_generator.data['subreddit'][subreddit_id].comments_id[idx]
            comment = graph_generator.data['comment'][comment_id]
            subreddit_type = comment.subreddit_type
            if subreddit_type is not None:
                break
            idx += 1
            if idx >= len(graph_generator.data['subreddit'][subreddit_id].comments_id):
                subreddit_type = None
                break
            
        if subreddit_type is None:
            return np.nan
        else:
            subreddit_type_id = subreddit_type_dict.get(subreddit_type, None)
            if subreddit_type_id is None:
                subreddit_type_id = len(subreddit_type_dict)
                subreddit_type_dict[subreddit_type] = subreddit_type_id
            return subreddit_type_id
            
    except:
        return np.nan
    
    
# submission level features
@feature_function_low_level_register('submission', 'num_of_all_awardings', unleaked=False)
def get_num_of_all_awardings_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        return len(graph_generator.data['submission'][submission_id].all_awardings)
    except:
        return np.nan
    
    
@feature_function_low_level_register('submission', 'submission_id')
def get_submission_id_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    return submission_id


@feature_function_low_level_register('submission', 'observation_time_window_end')
def get_observation_time_window_end_submission(submission_id, graph_generator: GraphGenerator, observation_time_window, **kwargs):
    return observation_time_window[1]
    
    
@feature_function_low_level_register('submission', "allow_live_comments")
def get_allow_live_comments_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        allow_live_comments = graph_generator.data['submission'][submission_id].allow_live_comments
        if allow_live_comments is None:
            return np.nan
        else:
            return int(allow_live_comments)
    except:
        return np.nan
    
    
@feature_function_low_level_register('submission', "archived")
def get_archived_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        archived = graph_generator.data['submission'][submission_id].archived
        if archived is None:
            return np.nan
        else:
            return int(archived)
    except:
        return np.nan
    
@feature_function_low_level_register('submission', "num_of_awarders", unleaked=False)
def get_num_of_awarders_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        return len(graph_generator.data['submission'][submission_id].awarders)
    except:
        return np.nan
    

@feature_function_low_level_register('submission', "banned_by_someone")
def get_banned_by_someone_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        banned_by = graph_generator.data['submission'][submission_id].banned_by
        if banned_by is None:
            return 0
        else:
            return 1
    except:
        return np.nan
    
    
@feature_function_low_level_register('submission', "can_gild")
def get_can_gild_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        can_gild = graph_generator.data['submission'][submission_id].can_gild
        if can_gild is None:
            return np.nan
        else:
            return int(can_gild)
    except:
        return np.nan
    
    
@feature_function_low_level_register('submission', "can_mod_post")
def get_can_mod_post_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        can_mod_post = graph_generator.data['submission'][submission_id].can_mod_post
        if can_mod_post is None:
            return np.nan
        else:
            return int(can_mod_post)
    except:
        return np.nan
    
    
submission_category_dict = {}
    
@feature_function_low_level_register('submission', "category")
def get_category_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        category = graph_generator.data['submission'][submission_id].category
        if category is None:
            return np.nan
        category_id = submission_category_dict.get(category, None)
        if category_id is None:
            category_id = len(submission_category_dict)
            submission_category_dict[category] = category_id
        return category_id
    except:
        return np.nan


@feature_function_low_level_register('submission', "num_of_comments")
def get_num_of_comments_submission(submission_id, graph_generator: GraphGenerator, observation_time_window, **kwargs):
    try:
        submission = graph_generator.data['submission'][submission_id]
        submission_comments = submission.comments_id
        num = 0
        for submission_comment in submission_comments:
            submission_comment_object = graph_generator.data['comment'][submission_comment]
            if submission_comment_object.created_utc < observation_time_window[1]:
                num += 1
        return num
    except:
        return np.nan
    
    
@feature_function_low_level_register('submission', "num_of_all_comments")
def get_num_of_all_comments_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        return len(graph_generator.data['submission'][submission_id].comments_total_id)
    except:
        return np.nan
    
    
@feature_function_low_level_register('submission', "contest_mode")
def get_contest_mode_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        contest_mode = graph_generator.data['submission'][submission_id].contest_mode
        if contest_mode is None:
            return np.nan
        else:
            return int(contest_mode)
    except:
        return np.nan
    
    
@feature_function_low_level_register('submission', "created_utc")
def get_created_utc_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        return int(graph_generator.data['submission'][submission_id].created_utc)
    except:
        return np.nan
    
    
@feature_function_low_level_register('submission', "content_categories")
def get_content_categories_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        content_categories = graph_generator.data['submission'][submission_id].content_categories
        if content_categories is None:
            return np.nan
        else:
            return len(content_categories)
    except:
        return np.nan


submission_discussion_type_dict = {}
@feature_function_low_level_register('submission', "discussion_type")
def get_discussion_type_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        discussion_type = graph_generator.data['submission'][submission_id].discussion_type
        if discussion_type is None:
            return np.nan
        discussion_type_id = submission_discussion_type_dict.get(discussion_type, None)
        if discussion_type_id is None:
            discussion_type_id = len(submission_discussion_type_dict)
            submission_discussion_type_dict[discussion_type] = discussion_type_id
        return discussion_type_id
    except:
        return np.nan


@feature_function_low_level_register('submission', "distinguished")
def get_distinguished_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        distinguished = graph_generator.data['submission'][submission_id].distinguished
        if distinguished is None:
            return np.nan
        else:
            return int(distinguished)
    except:
        return np.nan
    
    
@feature_function_low_level_register('submission', "domain")
def get_domain_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        domain = graph_generator.data['submission'][submission_id].domain
        if domain is None:
            return np.nan
        else:
            return len(domain)
    except:
        return np.nan
    
    
@feature_function_low_level_register('submission', "edited")
def get_edited_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        edited = graph_generator.data['submission'][submission_id].edited
        if edited is None:
            return np.nan
        else:
            return int(edited)
    except:
        return np.nan
    

@feature_function_low_level_register('submission', "num_of_gildings", unleaked=False)
def get_num_of_gildings_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        return len(graph_generator.data['submission'][submission_id].gildings)
    except:
        return np.nan
    
    
@feature_function_low_level_register('submission', "gilded", unleaked=False)
def get_gilded_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        gilded = graph_generator.data['submission'][submission_id].gilded
        if gilded is None:
            return np.nan
        else:
            return int(gilded)
    except:
        return np.nan
    
    
@feature_function_low_level_register('submission', "hidden")
def get_hidden_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        hidden = graph_generator.data['submission'][submission_id].hidden
        if hidden is None:
            return np.nan
        else:
            return int(hidden)
    except:
        return np.nan
    
    
@feature_function_low_level_register('submission', "hide_score")
def get_hide_score_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        hide_score = graph_generator.data['submission'][submission_id].hide_score
        if hide_score is None:
            return np.nan
        else:
            return int(hide_score)
    except:
        return np.nan
    
    
@feature_function_low_level_register('submission', "is_crosspostable")
def get_is_crosspostable_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        is_crosspostable = graph_generator.data['submission'][submission_id].is_crosspostable
        if is_crosspostable is None:
            return np.nan
        else:
            return int(is_crosspostable)
    except:
        return np.nan
    
    
@feature_function_low_level_register('submission', "is_meta")
def get_is_meta_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        is_meta = graph_generator.data['submission'][submission_id].is_meta
        if is_meta is None:
            return np.nan
        else:
            return int(is_meta)
    except:
        return np.nan
    
    
@feature_function_low_level_register('submission', "is_original_content")
def get_is_original_content_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        is_original_content = graph_generator.data['submission'][submission_id].is_original_content
        if is_original_content is None:
            return np.nan
        else:
            return int(is_original_content)
    except:
        return np.nan
    
    
@feature_function_low_level_register('submission', "is_created_from_ads_ui")
def get_is_created_from_ads_ui_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        is_created_from_ads_ui = graph_generator.data['submission'][submission_id].is_created_from_ads_ui
        if is_created_from_ads_ui is None:
            return np.nan
        else:
            return int(is_created_from_ads_ui)
    except:
        return np.nan
    
    
@feature_function_low_level_register('submission', "is_reddit_media_domain")
def get_is_reddit_media_domain_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        is_reddit_media_domain = graph_generator.data['submission'][submission_id].is_reddit_media_domain
        if is_reddit_media_domain is None:
            return np.nan
        else:
            return int(is_reddit_media_domain)
    except:
        return np.nan
    
    
@feature_function_low_level_register('submission', "is_robot_indexable")
def get_is_robot_indexable_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        is_robot_indexable = graph_generator.data['submission'][submission_id].is_robot_indexable
        if is_robot_indexable is None:
            return np.nan
        else:
            return int(is_robot_indexable)
    except:
        return np.nan
    
    
@feature_function_low_level_register('submission', "is_self")
def get_is_self_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        is_self = graph_generator.data['submission'][submission_id].is_self
        if is_self is None:
            return np.nan
        else:
            return int(is_self)
    except:
        return np.nan
    
    
@feature_function_low_level_register('submission', "is_video")
def get_is_video_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        is_video = graph_generator.data['submission'][submission_id].is_video
        if is_video is None:
            return np.nan
        else:
            return int(is_video)
    except:
        return np.nan
    
    
submission_link_flair_type_dict = {}
@feature_function_low_level_register('submission', "link_flair_background_color")
def get_link_flair_background_color_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        link_flair_background_color = graph_generator.data['submission'][submission_id].link_flair_background_color
        if link_flair_background_color is None:
            return np.nan
        link_flair_background_color_id = submission_link_flair_type_dict.get(link_flair_background_color, None)
        if link_flair_background_color_id is None:
            link_flair_background_color_id = len(submission_link_flair_type_dict)
            submission_link_flair_type_dict[link_flair_background_color] = link_flair_background_color_id
        return link_flair_background_color_id
    except:
        return np.nan
    
    
submission_link_flair_css_class_dict = {}
@feature_function_low_level_register('submission', "link_flair_css_class")
def get_link_flair_css_class_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        link_flair_css_class = graph_generator.data['submission'][submission_id].link_flair_css_class
        if link_flair_css_class is None:
            return np.nan
        link_flair_css_class_id = submission_link_flair_css_class_dict.get(link_flair_css_class, None)
        if link_flair_css_class_id is None:
            link_flair_css_class_id = len(submission_link_flair_css_class_dict)
            submission_link_flair_css_class_dict[link_flair_css_class] = link_flair_css_class_id
        return link_flair_css_class_id
    except:
        return np.nan
    
    
submission_link_flair_richtext_dict = {}
@feature_function_low_level_register('submission', "link_flair_richtext")
def get_link_flair_richtext_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        link_flair_richtext = graph_generator.data['submission'][submission_id].link_flair_richtext
        if link_flair_richtext is None:
            return np.nan
        link_flair_richtext_id = submission_link_flair_richtext_dict.get(link_flair_richtext, None)
        if link_flair_richtext_id is None:
            link_flair_richtext_id = len(submission_link_flair_richtext_dict)
            submission_link_flair_richtext_dict[link_flair_richtext] = link_flair_richtext_id
        return link_flair_richtext_id
    except:
        return np.nan
    
    
submission_link_flair_template_id_dict = {}
@feature_function_low_level_register('submission', "link_flair_template_id")
def get_link_flair_template_id_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        link_flair_template_id = graph_generator.data['submission'][submission_id].link_flair_template_id
        if link_flair_template_id is None:
            return np.nan
        link_flair_template_id_id = submission_link_flair_template_id_dict.get(link_flair_template_id, None)
        if link_flair_template_id_id is None:
            link_flair_template_id_id = len(submission_link_flair_template_id_dict)
            submission_link_flair_template_id_dict[link_flair_template_id] = link_flair_template_id_id
        return link_flair_template_id_id
    except:
        return np.nan
    

submission_link_flair_text_color_dict = {}
@feature_function_low_level_register('submission', "link_flair_text_color")
def get_link_flair_text_color_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        link_flair_text_color = graph_generator.data['submission'][submission_id].link_flair_text_color
        if link_flair_text_color is None:
            return np.nan
        link_flair_text_color_id = submission_link_flair_text_color_dict.get(link_flair_text_color, None)
        if link_flair_text_color_id is None:
            link_flair_text_color_id = len(submission_link_flair_text_color_dict)
            submission_link_flair_text_color_dict[link_flair_text_color] = link_flair_text_color_id
        return link_flair_text_color_id
    except:
        return np.nan
    
    
submission_link_flair_text_dict = {}
@feature_function_low_level_register('submission', "link_flair_text")
def get_link_flair_text_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        link_flair_text = graph_generator.data['submission'][submission_id].link_flair_text
        if link_flair_text is None:
            return np.nan
        link_flair_text_id = submission_link_flair_text_dict.get(link_flair_text, None)
        if link_flair_text_id is None:
            link_flair_text_id = len(submission_link_flair_text_dict)
            submission_link_flair_text_dict[link_flair_text] = link_flair_text_id
        return link_flair_text_id
    except:
        return np.nan
    
    
submission_link_flair_type_dict = {}
@feature_function_low_level_register('submission', "link_flair_type")
def get_link_flair_type_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        link_flair_type = graph_generator.data['submission'][submission_id].link_flair_type
        if link_flair_type is None:
            return np.nan
        link_flair_type_id = submission_link_flair_type_dict.get(link_flair_type, None)
        if link_flair_type_id is None:
            link_flair_type_id = len(submission_link_flair_type_dict)
            submission_link_flair_type_dict[link_flair_type] = link_flair_type_id
        return link_flair_type_id
    except:
        return np.nan
    
    
@feature_function_low_level_register('submission', "locked")
def get_locked_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        locked = graph_generator.data['submission'][submission_id].locked
        if locked is None:
            return np.nan
        else:
            return int(locked)
    except:
        return np.nan
    
    
@feature_function_low_level_register('submission', "media_only")
def get_media_only_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        media_only = graph_generator.data['submission'][submission_id].media_only
        if media_only is None:
            return np.nan
        else:
            return int(media_only)
    except:
        return np.nan
    
    
@feature_function_low_level_register('submission', "no_follow")
def get_no_follow_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        no_follow = graph_generator.data['submission'][submission_id].no_follow
        if no_follow is None:
            return np.nan
        else:
            return int(no_follow)
    except:
        return np.nan
    
    
@feature_function_low_level_register('submission', "num_crossposts", unleaked=False)
def get_num_crossposts_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        return int(graph_generator.data['submission'][submission_id].num_crossposts)
    except:
        return np.nan
    

@feature_function_low_level_register('submission', "over_18")
def get_over_18_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        over_18 = graph_generator.data['submission'][submission_id].over_18
        if over_18 is None:
            return np.nan
        else:
            return int(over_18)
    except:
        return np.nan
    
    
@feature_function_low_level_register('submission', "pwls")
def get_parent_whitelist_status_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        pwls = graph_generator.data['submission'][submission_id].pwls
        if pwls is None:
            return np.nan
        else:
            return int(pwls)
    except:
        return np.nan
    
    
@feature_function_low_level_register('submission', "pinned")
def get_pinned_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        pinned = graph_generator.data['submission'][submission_id].pinned
        if pinned is None:
            return np.nan
        else:
            return int(pinned)
    except:
        return np.nan
    
    
@feature_function_low_level_register('submission', "quarantine")
def get_quarantine_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        quarantine = graph_generator.data['submission'][submission_id].quarantine
        if quarantine is None:
            return np.nan
        else:
            return int(quarantine)
    except:
        return np.nan
    
    
@feature_function_low_level_register('submission', "removal_by_someone")
def get_removal_by_someone_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        removal_by = graph_generator.data['submission'][submission_id].removal_by
        if removal_by is None:
            return 0
        else:
            return 1
    except:
        return np.nan
    
    
@feature_function_low_level_register('submission', "score", unleaked=False)
def get_score_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        return int(graph_generator.data['submission'][submission_id].score)
    except:
        return np.nan
    
    
@feature_function_low_level_register('submission', "length_of_selftext")
def get_selftext_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        selftext = graph_generator.data['submission'][submission_id].selftext
        if selftext is None:
            return np.nan
        else:
            return len(selftext)
    except:
        return np.nan
    
    
@feature_function_low_level_register('submission', "length_of_title")
def get_title_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        title = graph_generator.data['submission'][submission_id].title
        if title is None:
            return np.nan
        else:
            return len(title)
    except:
        return np.nan
    
    
@feature_function_low_level_register('submission', "send_replies")
def get_send_replies_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        send_replies = graph_generator.data['submission'][submission_id].send_replies
        if send_replies is None:
            return np.nan
        else:
            return int(send_replies)
    except:
        return np.nan
    
    
@feature_function_low_level_register('submission', "spoiler")
def get_spoiler_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        spoiler = graph_generator.data['submission'][submission_id].spoiler
        if spoiler is None:
            return np.nan
        else:
            return int(spoiler)
    except:
        return np.nan
    
    
@feature_function_low_level_register('submission', "stickied")
def get_stickied_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        stickied = graph_generator.data['submission'][submission_id].stickied
        if stickied is None:
            return np.nan
        else:
            return int(stickied)
    except:
        return np.nan
    
    
@feature_function_low_level_register('submission', "thumbnail")
def get_thumbnail_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        thumbnail = graph_generator.data['submission'][submission_id].thumbnail
        if thumbnail is None:
            return np.nan
        else:
            return len(thumbnail)
    except:
        return np.nan
    
    
@feature_function_low_level_register('submission', "top_awarded_type", unleaked=False)
def get_top_awarded_type_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        top_awarded_type = graph_generator.data['submission'][submission_id].top_awarded_type
        if top_awarded_type is None:
            return np.nan
        else:
            return len(top_awarded_type)
    except:
        return np.nan
    
    
@feature_function_low_level_register('submission', "total_awards_received", unleaked=False)
def get_total_awards_received_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        return int(graph_generator.data['submission'][submission_id].total_awards_received)
    except:
        return np.nan
    
    
@feature_function_low_level_register('submission', "upvote_ratio", unleaked=False)
def get_upvote_ratio_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        return float(graph_generator.data['submission'][submission_id].upvote_ratio)
    except:
        return np.nan
    
    
@feature_function_low_level_register('submission', "whitelist_status")
def get_whitelist_status_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        whitelist_status = graph_generator.data['submission'][submission_id].whitelist_status
        if whitelist_status is None:
            return np.nan
        else:
            return len(whitelist_status)
    except:
        return np.nan
    
    
@feature_function_low_level_register('submission', "wls")
def get_wls_submission(submission_id, graph_generator: GraphGenerator, **kwargs):
    try:
        wls = graph_generator.data['submission'][submission_id].wls
        if wls is None:
            return np.nan
        else:
            return int(wls)
    except:
        return np.nan
