from sentiment_preparation import get_sentiment_batch
from key_manager import KeyValueManager
import json
import os
from data_process.graph_generator import GraphGenerator
from typing import List, Set


class Sentiment:
    def __init__(self, keys=None, texts=None, batch_size=100, save_path=None):
        self.text_manager = KeyValueManager((keys, texts), use_hash=True)
        self.sentiment_manager = KeyValueManager(unvalued_keys=set(keys), use_hash=True)
        self.batch_size = batch_size
        self.save_path = save_path
        if save_path is None:
            self.save_path = "sentiment_result.json"
        self.load()
        self.pre_sentiment()
        self.save()
        
    def load(self):
        if os.path.exists(self.save_path):
            with open(self.save_path, "r") as f:
                sentiment_dict = json.load(f)
            temp_manager = KeyValueManager(sentiment_dict, use_hash=True)
            self.sentiment_manager.combine(temp_manager)
        
        self.full = True
        if len(self.sentiment_manager.unvalued_keys) != 0:
            self.full = False
            
    def pre_sentiment(self):
        if self.full:
            return
        
        text_list = []
        for key in self.sentiment_manager.unvalued_keys_list():
            text_list.append(self.text_manager.get(key))
            
        sentiment_list = get_sentiment_batch(text_list)
        self.sentiment_manager.set_all_by_list(sentiment_list)
        
    def save(self):
        with open(self.save_path, "w") as f:
            json.dump(self.sentiment_manager.to_dict(), f)
            
        self.full = True
        
    def __getitem__(self, key):
        return self.sentiment_manager.get(key)
    
    def __setitem__(self, key, value):
        self.sentiment_manager.set(key, value)
        
    def __contains__(self, key):
        return key in self.sentiment_manager
    
    def __len__(self):
        return self.sentiment_manager.value_count()
    
    def getitem_list(self, key_list):
        return [self[key] for key in key_list]

    def getitem_list_unaligned(self, key_list, text_list=None):
        sentiment_list = []

        required_text_index = []
        for index, key in enumerate(key_list):
            if key not in self.sentiment_manager:
                if text_list is None:
                    sentiment_list.append(None)
                else:
                    required_text_index.append(index)
                    sentiment_list.append(None)
            else:
                sentiment_list.append(self[key])
        if text_list is not None:
            if len(required_text_index) != 0:
                required_text_list = [text_list[index] for index in required_text_index]
                required_sentiment_list = get_sentiment_batch(required_text_list)
                for index, item in enumerate(required_sentiment_list):
                    sentiment_list[required_text_index[index]] = item
                    
        return sentiment_list
    

def generate_key_text_from_graph_generator(graph_generator: GraphGenerator):
    key_list = []
    text_list = []
    graphs_info = [graph_generator.graphs_info[time_tuple][graph_generator.graph_type] for time_tuple in graph_generator.time_tuples]
    used_submissions: List[Set] = [graphs_info[index].used_submissions for index in range(len(graphs_info))]
    used_comments: List[Set] = [graphs_info[index].used_comments for index in range(len(graphs_info))]
    
    # combine all used submissions in the used_submissions list into one set
    used_submission_set = set()
    for submission_set in used_submissions:
        used_submission_set = used_submission_set.union(submission_set)
        
    # combine all used comments in the used_comments list into one set
    used_comment_set = set()
    for comment_set in used_comments:
        used_comment_set = used_comment_set.union(comment_set)
        
    # add all submission keys into the key_list
    for submission_key in used_submission_set:
        key_list.append((submission_key, "submission"))
        submission = graph_generator.data['submission'][submission_key]
        submission_text = submission['title'] + " " + submission['selftext']
        text_list.append(submission_text)
        
    # add all comment keys into the key_list
    for comment_key in used_comment_set:
        key_list.append((comment_key, "comment"))
        comment = graph_generator.data['comment'][comment_key]
        comment_text = comment['body']
        text_list.append(comment_text)
        
    return key_list, text_list