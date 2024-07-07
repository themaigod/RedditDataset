from get_features import get_comment_features, get_submission_features, get_user_features
from data_process.graph_generator import GraphGenerator
from typing import Tuple
import pandas as pd
from preframe import SpeedPreframe
import get_basic_features
import numpy as np
from tqdm import tqdm


def get_user_features_from_submission(user_features: pd.DataFrame, submission_features: pd.DataFrame, graph_generator: GraphGenerator, observation_time_window: Tuple[int, int], use_sentiment=True, **kwargs):
    """
    :param user_features: user features
    :param submission_features: submission features
    :param graph_generator: GraphGenerator object
    :return: user features from submission features
    """
    user_speed_preframe = SpeedPreframe()
    methods = ['mean', 'std', 'max', 'min', "first", "last", "num"]
    submission_feature_names = list(submission_features.columns)
    if use_sentiment:
        sentiment_manager = kwargs['sentiment_manager']
        submission_feature_names.append('sentiment')
    user_feature_names_from_submission = []
    for method in methods:
        if method == 'num':
            user_feature_names_from_submission.append('num_submissions')
            continue
        for feature_name in submission_feature_names:
            user_feature_names_from_submission.append(feature_name + "_" + method)
               
    for feature_name in user_feature_names_from_submission:
        if feature_name not in user_speed_preframe.columns:
            user_speed_preframe.add_column(feature_name)
            
    for user_id, time_end_time_stamp in tqdm(user_features[['user_id', 'time_end_time_stamp']].values):
        user_object = graph_generator.data['redditor'][user_id]
        activities = user_object.activity
        user_features_from_submission_list = []
        for activity_time, activity_id, activity_type in activities:
            if activity_type == 'submission' and activity_time <= time_end_time_stamp:
                # submission_features['submission_id'] == activity_id and submission_features['observation_time_window_end'] == time_end_time_stamp
                # located the only one row and get its values
                submission_feature = submission_features.loc[(submission_features['submission_id'] == activity_id) & (submission_features['observation_time_window_end'] == time_end_time_stamp)].values
                # to make shape of submission_feature is (n,)
                submission_feature = submission_feature.reshape(-1)
                if len(submission_feature) == 0:
                    continue
                if use_sentiment:
                    submission_feature = np.append(submission_feature, sentiment_manager.get((activity_id, activity_type)))
                user_features_from_submission_list.append(submission_feature)
        if len(user_features_from_submission_list) == 0:
            user_features_from_submission_list.append([0] * len(submission_feature_names))
        
        # because user_features_from_submission_list is a list of numpy array, so we need to convert it to numpy array by concatenate
        user_features_from_submission_list = np.stack(user_features_from_submission_list)
        user_features_from_submission = []
        for method in methods:
            if method == 'mean':
                user_feature = np.mean(user_features_from_submission_list, axis=0)
            elif method == 'std':
                user_feature = np.std(user_features_from_submission_list, axis=0)
            elif method == 'max':
                user_feature = np.max(user_features_from_submission_list, axis=0)
            elif method == 'min':
                user_feature = np.min(user_features_from_submission_list, axis=0)
            elif method == 'first':
                user_feature = user_features_from_submission_list[0]
            elif method == 'last':
                user_feature = user_features_from_submission_list[-1]
            elif method == 'num':
                user_feature = np.array([len(user_features_from_submission_list)])
                
            if method == 'num':
                user_features_from_submission.extend(user_feature.tolist())
                continue
            user_features_from_submission.extend(user_feature.tolist())
        user_speed_preframe.append(user_features_from_submission)
        
    return user_speed_preframe.to_dataframe()
        
        

def get_user_features_from_comment(user_features: pd.DataFrame, comment_features: pd.DataFrame, graph_generator: GraphGenerator, observation_time_window: Tuple[int, int], use_sentiment=True, **kwargs):
    """
    :param user_features: user features
    :param comment_features: comment features
    :param graph_generator: GraphGenerator object
    :return: user features from comment features
    """
    user_speed_preframe = SpeedPreframe()
    methods = ['mean', 'std', 'max', 'min', "first", "last", "num"]
    comment_feature_names = list(comment_features.columns)
    if use_sentiment:
        sentiment_manager = kwargs['sentiment_manager']
        comment_feature_names.append('sentiment')
    user_feature_names_from_comment = []
    for method in methods:
        if method == 'num':
            user_feature_names_from_comment.append('num_comments')
            continue
        for feature_name in comment_feature_names:
            user_feature_names_from_comment.append(feature_name + "_" + method)

    for feature_name in user_feature_names_from_comment:
        if feature_name not in user_speed_preframe.columns:
            user_speed_preframe.add_column(feature_name)
            
    for user_id, time_end_time_stamp in tqdm(user_features[['user_id', 'time_end_time_stamp']].values):
        user_object = graph_generator.data['redditor'][user_id]
        activities = user_object.activity
        user_features_from_comment_list = []
        for activity_time, activity_id, activity_type in activities:
            if activity_type == 'comment' and activity_time <= time_end_time_stamp:
                # comment_features['comment_id'] == activity_id and comment_features['observation_time_window_end'] == time_end_time_stamp
                # located the only one row and get its values
                comment_feature = comment_features.loc[(comment_features['comment_id'] == activity_id) & (comment_features['observation_time_window_end'] == time_end_time_stamp)].values
                # to make shape of comment_feature is (n,)
                comment_feature = comment_feature.reshape(-1)
                if len(comment_feature) == 0:
                    continue
                if use_sentiment:
                    comment_feature = np.append(comment_feature, sentiment_manager.get((activity_id, activity_type)))
                user_features_from_comment_list.append(comment_feature)
        if len(user_features_from_comment_list) == 0:
            user_features_from_comment_list.append([0] * len(comment_feature_names))
        # because user_features_from_comment_list is a list of numpy array, so we need to convert it to numpy array by stack
        user_features_from_comment_list = np.stack(user_features_from_comment_list)
        user_features_from_comment = []
        for method in methods:
            if method == 'mean':
                user_feature = np.mean(user_features_from_comment_list, axis=0)
            elif method == 'std':
                user_feature = np.std(user_features_from_comment_list, axis=0)
            elif method == 'max':
                user_feature = np.max(user_features_from_comment_list, axis=0)
            elif method == 'min':
                user_feature = np.min(user_features_from_comment_list, axis=0)
            elif method == 'first':
                user_feature = user_features_from_comment_list[0]
            elif method == 'last':
                user_feature = user_features_from_comment_list[-1]
            elif method == 'num':
                user_feature = np.array([len(user_features_from_comment_list)])
            
            if method == 'num':
                user_features_from_comment.extend(user_feature.tolist())
                continue
            user_features_from_comment.extend(user_feature.tolist())
        user_speed_preframe.append(user_features_from_comment)
    
    print(set([len(i) for i in user_speed_preframe.data]))
    for i in user_speed_preframe.data:
        for j in i:
            if not isinstance(j, int) and not isinstance(j, float):
                print(type(j), j)
    return user_speed_preframe.to_dataframe()
        
            
        
                