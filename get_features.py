import get_basic_features
from preframe import SpeedPreframe
from data_process.graph_generator import GraphGenerator
from typing import Tuple
import pandas as pd



user_speed_preframe_total = SpeedPreframe()

def get_user_features(user_ids, graph_generator: GraphGenerator, observation_time_window: Tuple[int, int]):
    """
    :param user_ids: list of user ids
    :param graph_generator: GraphGenerator object
    :return: user features
    """
    user_speed_preframe = SpeedPreframe()
    user_feature_names = list(get_basic_features.feature_function.keys())
    for feature_name in user_feature_names:
        if feature_name not in user_speed_preframe.columns:
            user_speed_preframe.add_column(feature_name)
        if feature_name not in user_speed_preframe_total.columns:
            user_speed_preframe_total.add_column(feature_name)
            
        
    for user_id in user_ids:
        user_feature = []
        for feature_name in user_feature_names:
            feature_value = get_basic_features.feature_function[feature_name](user_id=user_id, graph_generator=graph_generator, observation_time_window=observation_time_window)
            user_feature.append(feature_value)
        user_speed_preframe.append(user_feature)
        
    user_speed_preframe_total.combine(user_speed_preframe)
    return user_speed_preframe.to_dataframe()


comment_speed_preframe_total = SpeedPreframe()


def get_comment_features(comment_ids, graph_generator: GraphGenerator, observation_time_window: Tuple[int, int], unleaked=True):
    """
    :param comment_ids: list of comment ids
    :param graph_generator: GraphGenerator object
    :return: comment features
    """
    comment_speed_preframe = SpeedPreframe()
    if unleaked:
        comment_feature_names = list(get_basic_features.feature_function_low_level_unleaked['comment'].keys())
    else:
        comment_feature_names = list(get_basic_features.feature_function_low_level['comment'].keys())
    for feature_name in comment_feature_names:
        if feature_name not in comment_speed_preframe.columns:
            comment_speed_preframe.add_column(feature_name)
    for comment_id in comment_ids:
        comment_feature = []
        for feature_name in comment_feature_names:
            feature_value = get_basic_features.feature_function_low_level['comment'][feature_name](comment_id=comment_id, graph_generator=graph_generator, observation_time_window=observation_time_window)
            comment_feature.append(feature_value)
        comment_speed_preframe.append(comment_feature)
        
    comment_speed_preframe_total.combine(comment_speed_preframe)
    return comment_speed_preframe.to_dataframe()


submission_speed_preframe_total = SpeedPreframe()


def get_submission_features(submission_ids, graph_generator: GraphGenerator, observation_time_window: Tuple[int, int], unleaked=True):
    """
    :param submission_ids: list of submission ids
    :param graph_generator: GraphGenerator object
    :return: submission features
    """
    submission_speed_preframe = SpeedPreframe()
    if unleaked:
        submission_feature_names = list(get_basic_features.feature_function_low_level_unleaked['submission'].keys())
    else:
        submission_feature_names = list(get_basic_features.feature_function_low_level['submission'].keys())
    for feature_name in submission_feature_names:
        if feature_name not in submission_speed_preframe.columns:
            submission_speed_preframe.add_column(feature_name)
        
        
    for submission_id in submission_ids:
        submission_feature = []
        for feature_name in submission_feature_names:
            feature_value = get_basic_features.feature_function_low_level['submission'][feature_name](submission_id=submission_id, graph_generator=graph_generator, observation_time_window=observation_time_window)
            submission_feature.append(feature_value)
        submission_speed_preframe.append(submission_feature)
        
    submission_speed_preframe_total.combine(submission_speed_preframe)
    
    return submission_speed_preframe.to_dataframe()


subreddit_speed_preframe_total = SpeedPreframe()


def get_subreddit_features(subreddit_ids, graph_generator: GraphGenerator, observation_time_window: Tuple[int, int], unleaked=True):
    """
    :param subreddit_ids: list of subreddit ids
    :param graph_generator: GraphGenerator object
    :return: subreddit features
    """
    subreddit_speed_preframe = SpeedPreframe()
    if unleaked:
        subreddit_feature_names = list(get_basic_features.feature_function_low_level_unleaked['subreddit'].keys())
    else:
        subreddit_feature_names = list(get_basic_features.feature_function_low_level['subreddit'].keys())
    for feature_name in subreddit_feature_names:
        if feature_name not in subreddit_speed_preframe.columns:
            subreddit_speed_preframe.add_column(feature_name)
        
        
    for subreddit_id in subreddit_ids:
        subreddit_feature = []
        for feature_name in subreddit_feature_names:
            feature_value = get_basic_features.feature_function_low_level['subreddit'][feature_name](subreddit_id=subreddit_id, graph_generator=graph_generator, observation_time_window=observation_time_window)
            subreddit_feature.append(feature_value)
        subreddit_speed_preframe.append(subreddit_feature)
    
    subreddit_speed_preframe_total.combine(subreddit_speed_preframe)
        
    return subreddit_speed_preframe.to_dataframe()


def generate_user_feature_dataset(continuous_time_tuples, graph_generator, train_size=7, label_size=1):
    dataframes_user = []

    for i in range(len(continuous_time_tuples) - train_size - label_size + 1):
        used_user_ids = set()
        for j in range(train_size):
            graph_info = graph_generator.graphs_info[continuous_time_tuples[i + j]][graph_generator.graph_type]
            used_user_ids |= graph_info.used_redditors
        used_user_ids = list(used_user_ids)
        observation_time_window = (continuous_time_tuples[i][0], continuous_time_tuples[i + train_size - 1][1])
        
        dataframes_user.append(get_user_features(user_ids=used_user_ids, observation_time_window=observation_time_window, graph_generator=graph_generator))
        
    return_data = pd.concat(dataframes_user, ignore_index=True)
    return return_data


def generate_comment_feature_dataset(continuous_time_tuples, graph_generator, train_size=7, label_size=1, unleaked=True):
    dataframes_comment = []

    for i in range(len(continuous_time_tuples) - train_size - label_size + 1):
        used_comment_ids = set()
        for j in range(train_size):
            graph_info = graph_generator.graphs_info[continuous_time_tuples[i + j]][graph_generator.graph_type]
            used_comment_ids |= graph_info.used_comments
        used_comment_ids = list(used_comment_ids)
        observation_time_window = (continuous_time_tuples[i][0], continuous_time_tuples[i + train_size - 1][1])
        
        dataframes_comment.append(get_comment_features(comment_ids=used_comment_ids, observation_time_window=observation_time_window, graph_generator=graph_generator, unleaked=unleaked))
        
    return_data = pd.concat(dataframes_comment, ignore_index=True)
    return return_data


def generate_submission_feature_dataset(continuous_time_tuples, graph_generator, train_size=7, label_size=1, unleaked=True):
    dataframes_submission = []

    for i in range(len(continuous_time_tuples) - train_size - label_size + 1):
        used_submission_ids = set()
        for j in range(train_size):
            graph_info = graph_generator.graphs_info[continuous_time_tuples[i + j]][graph_generator.graph_type]
            used_submission_ids |= graph_info.used_submissions
        used_submission_ids = list(used_submission_ids)
        observation_time_window = (continuous_time_tuples[i][0], continuous_time_tuples[i + train_size - 1][1])
        
        dataframes_submission.append(get_submission_features(submission_ids=used_submission_ids, observation_time_window=observation_time_window, graph_generator=graph_generator, unleaked=unleaked))
        
    return_data = pd.concat(dataframes_submission, ignore_index=True)
    return return_data


def fill_nan_in_dataframe(dataframe, value=0):
    """
    :param dataframe: dataframe
    :return: dataframe with nan filled
    """
    dataframe = dataframe.fillna(value)
    return dataframe

def fill_nan_in_dataframe_for_column(dataframe, column, value=0):
    """
    :param dataframe: dataframe
    :return: dataframe with nan filled
    """
    dataframe[column] = dataframe[column].fillna(value)
    return dataframe
