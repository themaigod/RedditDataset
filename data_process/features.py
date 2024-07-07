import numpy as np
from tqdm import tqdm
from data_process.dataset import embedding_fn_bert


def max_influence_submissions(user_embeddings, graph_generator):
    new_user_embeddings = {}
    default_submission = list(graph_generator.data['submission'].values())[0]
    default_submission_score = 0

    for i in tqdm(user_embeddings, desc="Max influence submissions"):
        user = graph_generator.data['redditor'][i]

        max_influence_score = 0
        max_influence_submission = None
        for (created_utc, object_id, object_type) in user.activity:
            if object_type == 'submission':
                submission = graph_generator.data['submission'][object_id]
                influence_score = submission.score * submission.upvote_ratio
                if influence_score > max_influence_score:
                    max_influence_score = influence_score
                    max_influence_submission = submission
            elif object_type == 'comment':
                comment = graph_generator.data['comment'][object_id]
                submission = graph_generator.data['submission'][comment._submission.id]
                influence_score = submission.score * submission.upvote_ratio
                if influence_score > max_influence_score:
                    max_influence_score = influence_score
                    max_influence_submission = submission

        if max_influence_submission is not None:
            max_influence_embedding = graph_generator.get_post_embeddings(embedding_fn_bert,
                                                                          [(
                                                                              max_influence_submission.id,
                                                                              "submission")])

            if max_influence_score > default_submission_score:
                default_submission_score = max_influence_score
                default_submission = max_influence_submission

        else:
            max_influence_embedding = graph_generator.get_post_embeddings(embedding_fn_bert,
                                                                          [(default_submission.id, "submission")])

        max_influence_embedding = max_influence_embedding[0]
        new_user_embeddings[i] = np.concatenate((user_embeddings[i], max_influence_embedding))

    return new_user_embeddings


def max_influence_submissions_discrete(user_embeddings, graph_generator):
    new_user_embeddings = {}
    default_submission = list(graph_generator.data['submission'].values())[0]
    default_submission_score = 0

    for i in tqdm(user_embeddings, desc="Max influence submissions"):
        user = graph_generator.data['redditor'][i]

        max_influence_score = 0
        max_influence_submission = None
        for (created_utc, object_id, object_type) in user.activity:
            if object_type == 'submission':
                submission = graph_generator.data['submission'][object_id]
                influence_score = submission.score * submission.upvote_ratio
                if influence_score > max_influence_score:
                    max_influence_score = influence_score
                    max_influence_submission = submission
            elif object_type == 'comment':
                comment = graph_generator.data['comment'][object_id]
                submission = graph_generator.data['submission'][comment._submission.id]
                influence_score = submission.score * submission.upvote_ratio
                if influence_score > max_influence_score:
                    max_influence_score = influence_score
                    max_influence_submission = submission

        if max_influence_submission is not None:
            max_influence_embedding = graph_generator.get_post_embeddings(embedding_fn_bert,
                                                                          [(
                                                                              max_influence_submission.id,
                                                                              "submission")])

            if max_influence_score > default_submission_score:
                default_submission_score = max_influence_score
                default_submission = max_influence_submission

        else:
            max_influence_embedding = graph_generator.get_post_embeddings(embedding_fn_bert,
                                                                          [(default_submission.id, "submission")])

        max_influence_embedding = max_influence_embedding[0]
        new_user_embeddings[i] = [np.concatenate((user_embeddings[i][0], max_influence_embedding))]

    return new_user_embeddings
