import json
import os
from typing import Dict, List, Tuple, Callable, Iterable, Set

import numpy as np
import scipy.sparse as sp
from tqdm import tqdm
from . import objects
from .data_processor import DataProcessor, DataProcessorReddit, access_attribute
from collections import defaultdict
import matplotlib.pyplot as plt
import networkx as nx
import copy

"""
construct graph
"""


# Notice that the reddit object link to other reddit objects attributes are (all start with "_"):
#     "submission": ["_submission", "_author", "_subreddit", "_comment_tree"],
#     "comment": ["_submission", "_author", "_subreddit", "_comment_tree", "_parent"],
#     "redditor": [],
#     "subreddit": [],
#     "comment_tree": ["_head", "_submission"],
#     "reddit_object": [],
# if you want to access attribute value of an object, object.attribute is fine
# if the value is not a reddit object, you can also find it by object._data[str(attribute)]
# but if you want to access attribute that may not exist, you should use access_attribute(object, ["attribute1", "attribute2", ...])


class ConstructGraph:
    def __init__(self):
        self.init()

    def init(self, data: Dict[str, Dict[int, objects.RedditObjectBase]] = None,
             time_tuple: Tuple[int, int] = None,
             graph_type: str = None,
             **kwargs):
        """
        :param data: A dictionary of lists of objects
        :param time_tuple: A tuple of two integers, indicating the time range of the data (in UTC)
        :param graph_type: A string, indicating the type of the graph
        :param kwargs: Other arguments
        """
        self.data = data
        self.time_tuple = time_tuple
        self.graph_type = graph_type
        self.kwargs = kwargs

    def construct_graph(self, *args, **kwargs) -> sp.csr_matrix:
        """
        construct graph
        """
        raise NotImplementedError

    def __call__(self, data, time_tuple, graph_type, *args, **kwargs):
        self.init(data, time_tuple, graph_type, **kwargs)
        return self.construct_graph(*args, **kwargs)


class ConstructGraphReddit(ConstructGraph):
    def init(self, data: Dict[str, Dict[int, objects.RedditObjectBase]] = None,
             time_tuple: Tuple[int, int] = None,
             graph_type: str = None,
             **kwargs):
        """
        :param data: A dictionary of dicts of objects
        :param time_tuple: A tuple of two integers, indicating the time range of the data (in UTC)
        :param graph_type: A string, indicating the type of the graph
        :param kwargs: Other arguments
        """
        super().init(data, time_tuple, graph_type, **kwargs)
        self.used_comments_attempt = kwargs.get("used_comments", None)
        self.used_submissions_attempt = kwargs.get("used_submissions", None)
        self.used_redditors_attempt = kwargs.get("used_redditors", None)
        self.considered_comments_attempt = kwargs.get("considered_comments", None)
        self.considered_submissions_attempt = kwargs.get("considered_submissions", None)
        self.considered_redditors_attempt = kwargs.get("considered_redditors", None)
        self.graphs = {}
        self.graphs_edge_type = {}
        self.graphs_edge_content = {}

    def construct_graph(self, *args, **kwargs) -> sp.csr_matrix:
        """
        construct graph
        """

        self.used_range()
        if self.graph_type == "user":
            return self.construct_user_graph(*args, **kwargs)
        elif self.graph_type == "comment":
            return self.construct_comment_graph(*args, **kwargs)
        else:
            raise NotImplementedError

    def construct_user_graph(self, *args, **kwargs) -> sp.csr_matrix:
        """
        construct user graph
        """
        return self.construct_user_graph_from_used(*args, **kwargs)

    def used_range(self):

        self.used_comments = set()
        self.used_submissions = set()
        self.used_redditors = set()

        self.considered_comments = set()
        self.considered_submissions = set()
        self.considered_redditors = set()

        for comment in list(self.data["comment"].values()):
            comment: objects.Comment

            if self.used_comments_attempt and comment.id not in self.used_comments_attempt:
                continue

            if not comment._author:
                continue

            if self.used_redditors_attempt and comment._author.id not in self.used_redditors_attempt:
                continue

            if self.time_tuple[0] <= comment.created_utc <= self.time_tuple[1]:
                if comment.id in self.used_comments:
                    continue
                if comment._parent is not None:
                    parent_chain = comment.generate_parent_chain()
                    parent_count = 0
                    for parent_id, parent_type in parent_chain:
                        if parent_type == "comment":

                            if self.used_comments_attempt and parent_id not in self.used_comments_attempt:
                                continue

                            if not self.data["comment"][parent_id]._author:
                                continue

                            if self.used_redditors_attempt and self.data["comment"][
                                parent_id]._author.id not in self.used_redditors_attempt:
                                continue

                            self.used_comments.add(parent_id)

                            if self.time_tuple[0] <= self.data["comment"][parent_id].created_utc <= self.time_tuple[1]:
                                if self.used_redditors_attempt:
                                    if access_attribute(self.data["comment"][parent_id],
                                                        ["_author", "id"]) not in self.used_redditors_attempt and \
                                            access_attribute(comment,
                                                             ["_author", "id"]) not in self.used_redditors_attempt:
                                        continue
                                self.considered_comments.add(parent_id)

                        elif parent_type == "submission":

                            if self.used_submissions_attempt and parent_id not in self.used_submissions_attempt:
                                continue

                            if not self.data["submission"][parent_id]._author:
                                continue

                            if self.used_redditors_attempt and self.data["submission"][
                                parent_id]._author.id not in self.used_redditors_attempt:
                                continue

                            self.used_submissions.add(parent_id)

                            if self.time_tuple[0] <= self.data["submission"][parent_id].created_utc <= self.time_tuple[
                                1]:
                                if self.used_redditors_attempt:
                                    if access_attribute(self.data["submission"][parent_id],
                                                        ["_author", "id"]) not in self.used_redditors_attempt and \
                                            access_attribute(comment,
                                                             ["_author", "id"]) not in self.used_redditors_attempt:
                                        continue
                                self.considered_submissions.add(parent_id)

                        else:
                            raise KeyError
                        parent_count += 1

                    if parent_count > 0:
                        self.used_comments.add(comment.id)
                        self.considered_comments.add(comment.id)

        for comment_id in self.used_comments:
            comment = self.data["comment"][comment_id]
            self.used_redditors.add(comment._author.id)
        for submission_id in self.used_submissions:
            submission = self.data["submission"][submission_id]
            self.used_redditors.add(submission._author.id)

        for comment_id in self.considered_comments:
            comment = self.data["comment"][comment_id]
            self.considered_redditors.add(comment._author.id)
        for submission_id in self.considered_submissions:
            submission = self.data["submission"][submission_id]
            self.considered_redditors.add(submission._author.id)

        self.comments_time_window = self.considered_comments
        self.submissions_time_window = self.considered_submissions
        self.redditors_time_window = self.considered_redditors

        if self.considered_comments_attempt:
            self.considered_comments = self.considered_comments_attempt & self.considered_comments
        if self.considered_submissions_attempt:
            self.considered_submissions = self.considered_submissions_attempt & self.considered_submissions
        if self.considered_redditors_attempt:
            self.considered_redditors = self.considered_redditors_attempt & self.considered_redditors

    def construct_user_graph_from_used(self, *args, **kwargs) -> sp.csr_matrix:
        """
        construct user graph from used comments, submissions and redditors
        """
        # construct user graph
        user_graph = sp.dok_matrix((len(self.used_redditors), len(self.used_redditors)), dtype=np.float32)
        edge_content: Dict[Tuple[int, int], List] = defaultdict(list)
        edge_type: Dict[Tuple[int, int], List] = defaultdict(list)
        used_redditors = {i: j for j, i in enumerate(self.used_redditors)}
        for comment_id in self.comments_time_window:
            comment = self.data["comment"][comment_id]
            comment: objects.Comment

            parent_chain = comment.generate_parent_chain()

            for parent_id, parent_type in parent_chain:
                if parent_type == "comment":
                    if parent_id in self.used_comments:
                        parent_author_id = access_attribute(self.data["comment"][parent_id], ["_author", "id"])
                        if not parent_author_id:
                            continue

                        user_graph[used_redditors[comment._author.id], used_redditors[
                            parent_author_id]] = 1
                        user_graph[used_redditors[parent_author_id], used_redditors[
                            comment._author.id]] = 1
                        edge_content[(used_redditors[comment._author.id], used_redditors[parent_author_id])].append(
                            comment_id)
                        edge_content[(used_redditors[parent_author_id], used_redditors[comment._author.id])].append(
                            parent_id)

                        edge_type[(used_redditors[comment._author.id], used_redditors[parent_author_id])].append(
                            "reply")

                        edge_type[(used_redditors[parent_author_id], used_redditors[comment._author.id])].append(
                            "replied")

                elif parent_type == "submission":
                    if parent_id in self.used_submissions:
                        parent_author_id = access_attribute(self.data["submission"][parent_id], ["_author", "id"])
                        if not parent_author_id:
                            continue
                        user_graph[used_redditors[comment._author.id], used_redditors[
                            parent_author_id]] = 1
                        user_graph[used_redditors[parent_author_id], used_redditors[
                            comment._author.id]] = 1
                        edge_content[
                            (used_redditors[comment._author.id], used_redditors[parent_author_id])].append(
                            comment_id)
                        edge_content[
                            (used_redditors[parent_author_id], used_redditors[comment._author.id])].append(
                            parent_id)

                        edge_type[(used_redditors[comment._author.id], used_redditors[parent_author_id])].append(
                            "reply")

                        edge_type[(used_redditors[parent_author_id], used_redditors[comment._author.id])].append(
                            "replied")

        self.graphs_edge_content["user"] = edge_content
        self.graphs_edge_type["user"] = edge_type
        self.graphs["user"] = user_graph.tocsr()
        self.used_redditors_index = used_redditors

        return self.graphs["user"]

    def construct_comment_graph(self, *args, **kwargs) -> sp.csr_matrix:
        """
        construct comment graph
        """
        return self.construct_comment_graph_from_used(*args, **kwargs)

    def construct_comment_graph_from_used(self, *args, **kwargs) -> sp.csr_matrix:
        """
        construct comment graph from used comments
        """
        # construct comment graph
        comment_graph = sp.dok_matrix((len(self.used_comments) + len(self.used_submissions)
                                       , len(self.used_comments) + len(self.used_submissions)), dtype=int)
        edge_content: Dict[Tuple[int, int], List] = defaultdict(list)
        edge_type: Dict[Tuple[int, int], List] = defaultdict(list)
        used_comments = {i: j for j, i in enumerate(self.used_comments)}
        used_submissions = {i: j + len(self.used_comments) for j, i in enumerate(self.used_submissions)}
        for comment_id in self.comments_time_window:
            comment = self.data["comment"][comment_id]
            comment: objects.Comment

            parent_chain = comment.generate_parent_chain()

            for parent_id, parent_type in parent_chain:
                if parent_type == "comment":
                    if parent_id in self.used_comments:
                        comment_graph[used_comments[comment.id], used_comments[parent_id]] = 1
                        comment_graph[used_comments[parent_id], used_comments[comment.id]] = 1
                        edge_content[(used_comments[comment.id], used_comments[parent_id])].append(comment_id)
                        edge_content[(used_comments[parent_id], used_comments[comment.id])].append(parent_id)

                        edge_type[(used_comments[comment.id], used_comments[parent_id])].append("reply")

                        edge_type[(used_comments[parent_id], used_comments[comment.id])].append("replied")

                elif parent_type == "submission":
                    if parent_id in self.used_submissions:
                        comment_graph[used_comments[comment.id], used_submissions[parent_id]] = 1
                        comment_graph[used_submissions[parent_id], used_comments[comment.id]] = 1
                        edge_content[(used_comments[comment.id], used_submissions[parent_id])].append(comment_id)
                        edge_content[(used_submissions[parent_id], used_comments[comment.id])].append(parent_id)

                        edge_type[(used_comments[comment.id], used_submissions[parent_id])].append("reply")

                        edge_type[(used_submissions[parent_id], used_comments[comment.id])].append("replied")

        self.graphs_edge_content["comment"] = edge_content
        self.graphs_edge_type["comment"] = edge_type
        self.graphs["comment"] = comment_graph.tocsr()
        self.used_comments_index = used_comments
        self.used_submissions_index = used_submissions

        return self.graphs["comment"]


class GraphGenerator:
    def __init__(self, data: Dict[str, Dict[int, objects.RedditObjectBase]] or DataProcessor,
                 time_range: Tuple[int, int] = None,
                 time_window=24 * 60 * 60,
                 default_graph_constructor: ConstructGraph or Callable = None,
                 load_page_bool: bool = False,
                 **kwargs):
        """
        :param data: A dictionary of lists of objects, or a DataProcessorReddit object
        :param time_range: A tuple of two integers, indicating the time range of the data (in UTC)
        :param time_window: An integer, indicating the time window of the graph (in seconds)
        :param kwargs: Other arguments
        """
        self.data = data if isinstance(data, Dict) else data.objects
        self.time_range = time_range
        self.time_window = time_window

        self.time_range = self.process_time_range(self.time_range)
        self.time_tuples = self.get_time_tuples()

        self.default_graph_constructor = default_graph_constructor
        if kwargs.get("graph_type", None) is None:
            self.graph_type = "user"
        else:
            self.graph_type = kwargs["graph_type"]

        self.graphs = {}
        self.graphs_info = defaultdict(dict)

        self.post_embeddings = defaultdict(dict)

        self.post2page = {}
        self.page2post = defaultdict(list)
        self.page_path = {}
        self.page_size = kwargs.get("page_size", 1000)
        self.page_temp = defaultdict(dict)

        self.user_embeddings = defaultdict(dict)
        self.user2page = {}
        self.page2user = defaultdict(list)
        self.user_page_path = {}
        self.user_page_size = kwargs.get("user_page_size", 1000)
        self.user_page_temp = defaultdict(dict)

        self.page_dir = kwargs.get("page_dir", "./page")
        self.user_page_dir = kwargs.get("user_page_dir", "./user_page")

        if not os.path.exists(self.page_dir):
            os.makedirs(self.page_dir)
        if not os.path.exists(self.user_page_dir):
            os.makedirs(self.user_page_dir)

        if len(os.listdir(self.page_dir)) > 0 and load_page_bool:
            self.load_page()

        if len(os.listdir(self.user_page_dir)) > 0 and load_page_bool:
            self.load_user_page()

    def load_page(self):
        file_list = os.listdir(self.page_dir)
        start_index = 0
        while True:
            if "{}.json".format(str(start_index)) in file_list:
                self.page_path[start_index] = os.path.join(self.page_dir, "{}.json".format(str(start_index)))
                load_object = json.load(open(self.page_path[start_index], "r"))
                # for j in load_object.values():
                #     assert len(j) == 768
                load_object = {i: np.array(j) for i, j in load_object.items()}
                page2post_temp = list(load_object.keys())
                # page2post_temp style is List[str], while str is str(Tuple[int, str])
                # it need to be converted to List[Tuple[int, str]]
                # self.page2post[start_index] = [tuple(int(j) for j in i[1:-1].split(", ")) for i in page2post_temp]
                for i in page2post_temp:
                    i = i[1:-1].split(", ")
                    self.page2post[start_index].append((int(i[0]), i[1][1:-1]))
                self.post2page.update({i: start_index for i in self.page2post[start_index]})
                start_index += 1
            else:
                try:
                    self.page_temp[start_index - 1] = load_object
                except:
                    pass
                break

    def load_user_page(self):
        file_list = os.listdir(self.user_page_dir)
        start_index = 0
        while True:
            if "{}.json".format(str(start_index)) in file_list:
                self.user_page_path[start_index] = os.path.join(self.user_page_dir, "{}.json".format(str(start_index)))
                load_object = json.load(open(self.user_page_path[start_index], "r"))
                load_object = {i: np.array(j) for i, j in load_object.items()}
                page2user_temp = list(load_object.keys())
                # page2user_temp style is List[str], while str is str(Tuple[int, Tuple[int, int]])
                # it need to be converted to List[Tuple[int, Tuple[int, int]]]
                # self.page2user[start_index] = [tuple(int(j) for j in i[1:-1].split(", ")) for i in page2user_temp]
                for i in page2user_temp:
                    i = i[1:-1].split(", ")
                    self.page2user[start_index].append((int(i[0]), (int(i[1][1:]), int(i[2][:-1]))))
                self.user2page.update({i: start_index for i in self.page2user[start_index]})
                start_index += 1
            else:
                self.user_page_temp[start_index - 1] = load_object
                break

    def clean_embeddings(self, input_idx=None, type_clear="user", time_tuple=None, input_type="comment"):
        if type_clear == "user":
            if input_idx is None:
                self.user_embeddings = defaultdict(dict)
            else:
                user_embeddings = defaultdict(dict)
                if isinstance(input_idx, int):
                    if not time_tuple:
                        user_embeddings.update({i: self.user_embeddings[i] for i in self.user_embeddings if
                                                i != input_idx})
                    else:
                        user_embeddings.update({i: self.user_embeddings[i] for i in self.user_embeddings if
                                                i != input_idx or (i == input_idx and self.user_embeddings[i][
                                                    1] != time_tuple)})
                elif isinstance(input_idx, Iterable):
                    if not time_tuple:
                        user_embeddings.update({i: self.user_embeddings[i] for i in self.user_embeddings if
                                                i not in input_idx})
                    else:
                        user_embeddings.update({i: self.user_embeddings[i] for i in self.user_embeddings if
                                                i not in input_idx or
                                                (i in input_idx and self.user_embeddings[i][1] != time_tuple)})
                else:
                    raise NotImplementedError
                self.user_embeddings = user_embeddings

        elif type_clear == "post":
            if input_idx is None:
                self.post_embeddings = defaultdict(dict)
            else:
                post_embeddings = defaultdict(dict)
                if isinstance(input_idx, int):
                    post_embeddings.update({i: self.post_embeddings[input_type][i] for i in self.post_embeddings if
                                            i != input_idx})
                elif isinstance(input_idx, Iterable):
                    post_embeddings.update({i: self.post_embeddings[input_type][i] for i in self.post_embeddings if
                                            i not in input_idx})
                else:
                    raise NotImplementedError
                self.post_embeddings = post_embeddings

        else:
            raise NotImplementedError

    def process_time_range(self, time_range: Tuple[int, int] or None) -> Tuple[int, int]:
        """
        process time range
        if time_range is not None, return time_range
        else, return the time range of the data
        """
        if time_range is not None:
            return time_range
        else:
            return self.get_time_range()

    def get_time_range(self, range_type=None, used_existing=False) -> Tuple[int, int]:
        if used_existing and self.time_range is not None:
            return self.time_range
        raise NotImplementedError

    def get_time_tuples(self, time_range: Tuple[int, int] or None = None, time_window: int = None) -> List[
        Tuple[int, int]]:
        """
        get time tuples
        """
        if time_range is None:
            time_range = self.time_range
        if time_window is None:
            time_window = self.time_window
        return [(i, i + time_window) for i in range(time_range[0], time_range[1], time_window)]

    def construct_graph(self, construct_func: Callable = None, register_func=True, **kwargs) -> List[sp.csr_matrix]:
        """
        construct graph
        """
        graphs = []

        for time_tuple in tqdm(self.time_tuples, desc="Constructing graph"):
            if construct_func is None:
                construct_func = self.default_graph_constructor()
            if register_func:
                self.graphs_info[time_tuple] = construct_func
            graphs.append(construct_func(time_tuple=time_tuple, **kwargs))

        return graphs

    def get_post_embeddings(self, embedding_func: Callable, post_list: List[str], **kwargs):
        """
        get post embeddings
        """
        raise NotImplementedError

    def get_embeddings(self, embedding_func: Callable, gather_func: Callable,
                       time_tuple: int,
                       user_list: List[int],
                       **kwargs):
        """
        get user embeddings
        """
        raise NotImplementedError


class GraphGeneratorReddit(GraphGenerator):
    def __init__(self, data: Dict[str, Dict[int, objects.RedditObjectBase]] or DataProcessorReddit,
                 time_range: Tuple[int, int] = None,
                 time_window=24 * 60 * 60,
                 default_graph_constructor=None,
                 if_selected_redditors=True,
                 **kwargs):
        """
        :param data: A dictionary of lists of objects, or a DataProcessorReddit object
        :param time_range: A tuple of two integers, indicating the time range of the data (in UTC)
        :param time_window: An integer, indicating the time window of the graph (in seconds)
        :param default_graph_constructor: A generator to generate the callable to construct the graph
        :param kwargs: Other arguments
        """
        super(GraphGeneratorReddit, self).__init__(data, time_range, time_window, default_graph_constructor,
                                                   **kwargs)
        self.used_comments = kwargs.get("used_comments", None)
        self.used_submissions = kwargs.get("used_submissions", None)
        self.used_redditors = kwargs.get("used_redditors", None)
        self.considered_redditors = kwargs.get("considered_redditors", None)

        if self.default_graph_constructor is None:
            self.default_graph_constructor = ConstructGraphReddit

        if if_selected_redditors:
            # select_type: str = "Interactions"
            # if_reversed = True
            # size: int = 4000,
            # distribution: bool = True
            select_type = kwargs.get("select_type", "Interactions")
            if_reversed = kwargs.get("if_reversed", True)
            size = kwargs.get("size", 1000)
            used_size = kwargs.get("used_size", 2000)
            distribution = kwargs.get("distribution", True)

            self.considered_redditors = self.select_users(select_type, if_reversed, size, distribution)
            self.used_redditors = self.select_users(select_type, if_reversed, used_size, distribution,
                                                    init_redditors=self.considered_redditors)

    def get_time_range(self, range_type=None, used_existing=False) -> Tuple[int, int]:
        if used_existing and self.time_range is not None:
            return self.time_range

        if range_type == "comment":
            comment_range = min([obj.created_utc for obj in self.data["comment"].values()]), max(
                [obj.created_utc for obj in self.data["comment"].values()])
            return comment_range

        elif range_type == "submission":
            submission_range = min([obj.created_utc for obj in self.data["submission"].values()]), max(
                [obj.created_utc for obj in self.data["submission"].values()])
            return submission_range

        elif range_type is None:
            comment_range = min([obj.created_utc for obj in self.data["comment"].values()]), max(
                [obj.created_utc for obj in self.data["comment"].values()])
            submission_range = min([obj.created_utc for obj in self.data["submission"].values()]), max(
                [obj.created_utc for obj in self.data["submission"].values()])
            return min(comment_range[0], submission_range[0]), max(comment_range[1], submission_range[1])
        else:
            raise ValueError("range_type must be comment, submission or None")

    def select_users(self, select_type: str = "Interactions", if_reversed: bool = True, size: int = 4000,
                     distribution: bool = True, **kwargs) -> Set[int]:
        """
        select users
        """
        if select_type == "Times":
            return self.select_users_by_times(reversed=if_reversed, size=size, distribution=distribution, **kwargs)
        elif select_type == "Time Range":
            return self.select_users_by_time_range(reversed=if_reversed, size=size, distribution=distribution, **kwargs)
        elif select_type == "Interactions":
            return self.select_users_by_interactions(reversed=if_reversed, size=size, distribution=distribution,
                                                     **kwargs)
        else:
            raise ValueError("select_type must be comment, submission or redditor")

    def select_users_by_times(self, reversed: bool = True, size=4000, distribution: bool = True, **kwargs) -> Set[int]:
        """
        select users by the number of comments and submissions
        """
        redditor_dict = {}
        for redditor_id, redditor in self.data["redditor"].items():
            if access_attribute(redditor, ["created_utc"]) is not None:
                if redditor.created_utc > self.time_range[0]:
                    continue
            redditor_dict[redditor_id] = len(redditor.activity)
        sorted_redditor_list = sorted(list(redditor_dict.items()), key=lambda x: x[1], reverse=reversed)
        if size is not None:
            sorted_redditor_list = sorted_redditor_list[:size]

        if distribution:
            values = [item[1] for item in sorted_redditor_list]
            plt.hist(values, bins='auto', edgecolor='black')
            plt.title('Distribution of Numbers')
            plt.xlabel('Number')
            plt.ylabel('Frequency')
            plt.savefig('vis/histogram.png')

        return set([item[0] for item in sorted_redditor_list])

    def select_users_by_time_range(self, reversed: bool = True, size=4000, distribution: bool = True,
                                   **kwargs) -> Set[int]:
        """
        select users by the time range of their activities
        """
        redditor_dict = {}
        for redditor_id, redditor in self.data["redditor"].items():
            if access_attribute(redditor, ["created_utc"]) is not None:
                if redditor.created_utc > self.time_range[0]:
                    continue
            redditor_dict[redditor_id] = redditor.time_range[1] - redditor.time_range[0]
        sorted_redditor_list = sorted(redditor_dict.items(), key=lambda x: x[1], reverse=reversed)
        if size is not None:
            sorted_redditor_list = sorted_redditor_list[:size]

        if distribution:
            values = [item[1] for item in sorted_redditor_list]
            plt.hist(values, bins='auto', edgecolor='black')
            plt.title('Distribution of Time Range')
            plt.xlabel('Time Range')
            plt.ylabel('Frequency')
            plt.savefig('vis/histogram.png')

        return set([item[0] for item in sorted_redditor_list])

    def select_users_by_interactions(self, reversed: bool = True, size=4000, distribution: bool = True,
                                     **kwargs) -> Set[int]:
        """
        First choose the user(s) with the most activities (comments and submissions) as Set A.
        Then choose the user(s) with the most interactions with Set A, add them to Set A.
        Repeat the process until the size of Set A reaches the required size.
        """
        initial_size = kwargs.get("initial_size", 100)
        each_add_size = kwargs.get("each_add_size", 100)
        redditor_dict = {}
        if kwargs.get("init_redditors", None) is None:
            for redditor_id, redditor in self.data["redditor"].items():
                if access_attribute(redditor, ["created_utc"]) is not None:
                    if redditor.created_utc > self.time_range[0]:
                        continue
                redditor_dict[redditor_id] = len(redditor.activity)
            sorted_redditor_list = sorted(redditor_dict.items(), key=lambda x: x[1], reverse=reversed)
            sorted_redditor_list = sorted_redditor_list[:initial_size]
            selected_redditor_set = set([item[0] for item in sorted_redditor_list])
        else:
            selected_redditor_set = set(kwargs.get("init_redditors"))
        while len(selected_redditor_set) < size:
            redditor_dict = {}
            for redditor_id, redditor in self.data["redditor"].items():
                if access_attribute(redditor, ["created_utc"]) is not None:
                    if redditor.created_utc > self.time_range[0]:
                        continue
                if redditor_id in selected_redditor_set:
                    continue
                redditor_dict[redditor_id] = self.find_interactions(redditor_id, selected_redditor_set)
            sorted_redditor_list = sorted(redditor_dict.items(), key=lambda x: x[1], reverse=reversed)
            if size - len(selected_redditor_set) < each_add_size:
                sorted_redditor_list = sorted_redditor_list[:size - len(selected_redditor_set)]
            else:
                sorted_redditor_list = sorted_redditor_list[:each_add_size]
            selected_redditor_set |= set([item[0] for item in sorted_redditor_list])

        if distribution:
            interaction_count_dict = {}
            for redditor in tqdm(selected_redditor_set, desc="Calculating Interactions"):
                interaction_count_dict[redditor] = self.find_interactions(redditor, selected_redditor_set)
            values = list(interaction_count_dict.values())

            plt.hist(values, bins='auto', edgecolor='black')
            plt.title('Distribution of Interactions')
            plt.xlabel('Interactions')
            plt.ylabel('Frequency')
            plt.yscale('log')
            plt.xscale('log')
            plt.savefig('vis/histogram_{}.png'.format(size))
            plt.clf()

            if False:
                graph = sp.lil_matrix((len(selected_redditor_set), len(selected_redditor_set)))
                selected_redditor = list(selected_redditor_set)
                for index1, redditor in tqdm(enumerate(selected_redditor), desc="Constructing Inner Graph",
                                             total=len(selected_redditor)):
                    for index2, redditor2 in enumerate(selected_redditor):
                        if redditor == redditor2:
                            continue
                        graph[index1, index2] = self.find_interactions(redditor, set([redditor2]))

                graph = graph.tocsr()
                nx_graph = nx.from_scipy_sparse_matrix(graph)
                pos = nx.kamada_kawai_layout(nx_graph)
                nx.draw_networkx(nx_graph, pos=pos, alpha=0.5, node_color='blue')
                plt.savefig('inner_graph.svg', format='svg')
                plt.clf()
                graph_without_weight = copy.deepcopy(graph)
                graph_without_weight.data = np.ones(graph_without_weight.data.shape)
                nx_graph_without_weight = nx.from_scipy_sparse_matrix(graph_without_weight)
                pos = nx.kamada_kawai_layout(nx_graph_without_weight)
                nx.draw_networkx(nx_graph_without_weight, pos=pos, alpha=0.5, node_color='blue')
                plt.savefig('inner_graph_without_weight.svg', format='svg')

        return selected_redditor_set

    def find_interactions(self, redditor_id: int, selected_redditor_set: Set[int]) -> int:
        """
        find the number of interactions between a redditor and a set of redditors
        """
        redditor = self.data["redditor"][redditor_id]
        redditor: objects.Redditor
        interaction_count = 0

        for (created_utc, activity_id, activity_type) in redditor.activity:
            if activity_type == "comment":
                activity = self.data["comment"][activity_id]
                activity: objects.Comment
                if len(activity._comment_tree.comments_total_id) > 0:
                    for comment_id in activity._comment_tree.comments_total_id:
                        comment = self.data["comment"][comment_id]
                        comment: objects.Comment
                        try:
                            if comment._author.id in selected_redditor_set:
                                interaction_count += 1
                        except:
                            pass

                parent_ids = activity.generate_parent_chain()
                for parent_id, parent_type in parent_ids:
                    parent = self.data[parent_type][parent_id]
                    parent: objects.Comment
                    try:
                        if parent._author.id in selected_redditor_set:
                            interaction_count += 1
                    except:
                        pass

            elif activity_type == "submission":
                activity = self.data["submission"][activity_id]
                activity: objects.Submission
                if len(activity._comment_tree.comments_total_id) > 0:
                    for comment_id in activity._comment_tree.comments_total_id:
                        comment = self.data["comment"][comment_id]
                        comment: objects.Comment
                        try:
                            if comment._author.id in selected_redditor_set:
                                interaction_count += 1
                        except:
                            pass

        return interaction_count

    def construct_graph(self, construct_func: ConstructGraphReddit or Callable = None, register_func=True, **kwargs) -> \
            List[sp.csr_matrix]:
        """
        construct graph
        """
        if_default = True if construct_func is None else False
        graphs = []
        for time_tuple in tqdm(self.time_tuples, desc="Constructing graph"):
            args = {"data": self.data,
                    "graph_type": self.graph_type, "time_tuple": time_tuple,
                    "used_comments": self.used_comments, "used_submissions": self.used_submissions,
                    "used_redditors": self.used_redditors,
                    "considered_redditors": self.considered_redditors}
            args.update(kwargs)
            if kwargs.get("graph_type", None) is not None:
                args["graph_type"] = kwargs["graph_type"]
                self.graph_type = kwargs["graph_type"]
            if if_default:
                construct_func = self.default_graph_constructor()

            if register_func:
                self.graphs_info[time_tuple][args['graph_type']] = construct_func
            graphs.append(construct_func(**args))

        self.graphs[self.graph_type] = graphs
        return graphs

    def get_post_embeddings(self, embedding_func: Callable, post_list: List[str], **kwargs):
        """
        get post embeddings
        """
        # self.post_embeddings = defaultdict(dict)
        if self.post_embeddings is None:
            self.post_embeddings = defaultdict(dict)

        post_embeddings = []
        for post_id, post_type in post_list:
            if post_id in self.post_embeddings[post_type]:
                post_embeddings.append(self.post_embeddings[post_type][post_id])
                continue

            if (post_id, post_type) in self.post2page:
                page_id = self.post2page[(post_id, post_type)]
                if page_id in self.page_temp:
                    post_embeddings.append(self.page_temp[page_id][str((post_id, post_type))])
                    continue

                page_path = self.page_path[page_id]
                load_object = json.load(open(page_path, "r"))
                # for j in load_object.values():
                #     assert isinstance(j, list)
                self.page_temp[page_id] = {i: np.array(j) for i, j in load_object.items()}
                post_embeddings.append(self.page_temp[page_id][str((post_id, post_type))])
                continue

            post = self.data[post_type][post_id]
            text = post.title + " " + post.selftext if post_type == "submission" else post.body
            post_embedding = embedding_func(text)
            self.post_embeddings[post_type][post_id] = post_embedding
            post_embeddings.append(post_embedding)

            if len(self.page2post) == 0:
                page_id = 0
            else:
                page_id = max(self.page2post.keys())
            if len(self.page2post[page_id]) >= self.page_size:
                self.page_path[page_id] = os.path.join(self.page_dir, str(page_id) + ".json")
                save_object = {i: j.tolist() for i, j in self.page_temp[page_id].items()}
                json.dump(save_object, open(self.page_path[page_id], "w"))
                # self.page_temp[page_id] = {}
                del self.page_temp[page_id]
                page_id += 1

            self.post2page[(post_id, post_type)] = page_id
            self.page2post[page_id].append((post_id, post_type))
            self.page_temp[page_id][str((post_id, post_type))] = post_embedding

        return post_embeddings

    def get_embeddings(self, embedding_func: Callable, gather_func: Callable, time_tuple: Tuple[int, int],
                       user_list: List[int], **kwargs):
        """
        get user embeddings
        """

        use_batch = kwargs.get("use_batch", True)

        embedding_size = kwargs.get("embedding_size", 768)

        embedding_lookup = kwargs.get("embedding_lookup", None)

        if embedding_lookup is not None:
            time_size = embedding_lookup * (time_tuple[1] - time_tuple[0])
            lookup_start = time_tuple[1] - time_size

        batch_text = []

        embeddings: Dict[int, List[np.ndarray]] = defaultdict(list)
        for user in user_list:

            if user in self.user_embeddings and time_tuple in self.user_embeddings[user]:
                continue

            if (user, time_tuple) in self.user2page:
                continue

            redditor = self.data["redditor"][user]
            redditor_activity = redditor.activity
            for activity_time, activity_id, activity_type in redditor_activity:
                if activity_time > time_tuple[1]:
                    continue

                if embedding_lookup and activity_time <= lookup_start:
                    continue

                try:
                    if self.post_embeddings[activity_type][activity_id] is not None:
                        embeddings[user].append(self.post_embeddings[activity_type][activity_id])
                        continue
                except:
                    pass

                activity_obj = self.data[activity_type][activity_id]
                text = activity_obj.body if activity_type == "comment" \
                    else "title: " + activity_obj.title + " body: " + activity_obj.selftext
                if use_batch:
                    post_id = activity_id
                    post_type = activity_type
                    if (post_id, post_type) in self.post2page:
                        page_id = self.post2page[(post_id, post_type)]
                        if page_id in self.page_temp:
                            embeddings[user].append(self.page_temp[page_id][str((post_id, post_type))])
                            continue

                        page_path = self.page_path[page_id]
                        load_object = json.load(open(page_path, "r"))
                        self.page_temp[page_id] = {i: np.array(j) for i, j in load_object.items()}
                        embeddings[user].append(self.page_temp[page_id][str((post_id, post_type))])
                        continue
                    batch_text.append((user, activity_id, activity_type, text))
                    if len(batch_text) == 10:
                        batch_text_input = [text for _, _, _, text in batch_text]

                        batch_embeddings = embedding_func(batch_text_input, embedding_size)
                        for (user, activity_id, activity_type, text), embedding in zip(batch_text, batch_embeddings):
                            self.post_embeddings[activity_type][activity_id] = embedding
                            embeddings[user].append(embedding)

                            post_id = activity_id
                            post_type = activity_type
                            if len(self.page2post) == 0:
                                page_id = 0
                            else:
                                page_id = max(self.page2post.keys())

                            if len(self.page2post[page_id]) >= self.page_size:
                                self.page_path[page_id] = os.path.join(self.page_dir, str(page_id) + ".json")
                                save_object = {i: j.tolist() for i, j in self.page_temp[page_id].items()}
                                json.dump(save_object, open(self.page_path[page_id], "w"))
                                # self.page_temp[page_id] = {}
                                del self.page_temp[page_id]
                                page_id += 1

                            self.post2page[(post_id, post_type)] = page_id
                            self.page2post[page_id].append((post_id, post_type))
                            self.page_temp[page_id][str((post_id, post_type))] = embedding

                        batch_text = []
                    continue
                embedding = embedding_func(text, embedding_size)
                self.post_embeddings[activity_type][activity_id] = embedding
                embeddings[user].append(embedding)

        if use_batch and len(batch_text) > 0:
            batch_text_input = [text for _, _, _, text in batch_text]
            batch_embeddings = embedding_func(batch_text_input, embedding_size)
            if len(batch_text_input) == 1:
                batch_embeddings = [batch_embeddings]
            for (user, activity_id, activity_type, text), embedding in zip(batch_text, batch_embeddings):
                self.post_embeddings[activity_type][activity_id] = embedding
                embeddings[user].append(embedding)

                post_id = activity_id
                post_type = activity_type
                if len(self.page2post) == 0:
                    page_id = 0
                else:
                    page_id = max(self.page2post.keys())
                if len(self.page2post[page_id]) >= self.page_size:
                    self.page_path[page_id] = os.path.join(self.page_dir, str(page_id) + ".json")
                    save_object = {i: j.tolist() for i, j in self.page_temp[page_id].items()}
                    json.dump(save_object, open(self.page_path[page_id], "w"))
                    del self.page_temp[page_id]
                    page_id += 1

                self.post2page[(post_id, post_type)] = page_id
                self.page2post[page_id].append((post_id, post_type))
                self.page_temp[page_id][str((post_id, post_type))] = embedding

        user_embeddings = []
        for user in user_list:
            if user in self.user_embeddings and time_tuple in self.user_embeddings[user]:
                user_embeddings.append(self.user_embeddings[user][time_tuple])
                continue

            if (user, time_tuple) in self.user2page:
                page_id = self.user2page[(user, time_tuple)]
                if page_id in self.user_page_temp:
                    user_embeddings.append(self.user_page_temp[page_id][str((user, time_tuple))])
                    continue

                page_path = self.user_page_path[page_id]
                load_object = json.load(open(page_path, "r"))

                self.user_page_temp[page_id] = {i: np.array(j) for i, j in load_object.items()}
                user_embeddings.append(self.user_page_temp[page_id][str((user, time_tuple))])
                continue

            user_embedding = gather_func(embeddings[user])
            self.user_embeddings[user][time_tuple] = user_embedding
            user_embeddings.append(user_embedding)

            if len(self.page2user) == 0:
                page_id = 0
            else:
                page_id = max(self.page2user.keys())

            if len(self.page2user[page_id]) >= self.page_size:
                self.user_page_path[page_id] = os.path.join(self.user_page_dir, str(page_id) + ".json")
                save_object = {i: j.tolist() for i, j in self.user_page_temp[page_id].items()}
                json.dump(save_object, open(self.user_page_path[page_id], "w"))
                del self.user_page_temp[page_id]
                page_id += 1

            self.user2page[(user, time_tuple)] = page_id
            self.page2user[page_id].append((user, time_tuple))
            self.user_page_temp[page_id][str((user, time_tuple))] = user_embedding

        return user_embeddings
