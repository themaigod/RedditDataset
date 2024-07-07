# Build Reddit Graph Dataset

## Introduction

Based on the [Reddit Process Repository](https://github.com/themaigod/RedditProcess), this repository provides a script
to build the graph of reddit, and then build a dataset, labeled with the community of each node. We construct a series
of features for each node, and we provide an example of using xgboost to classify the community of each node.

## Requirements

```
xgboost
networkx
numpy
scipy
tqdm
matplotlib
notebook
```


## Run the code

Put code files from [Reddit Process Repository](https://github.com/themaigod/RedditProcess) to data process code

Then, you can check `process.ipynb` to see how to build the graph and dataset.

## More details

### data_process.graph_generator

This is key module to construct the graph of reddit. After initializing the module, you can call `construct_graph` to
build the graph. Actually, it allows you to build the graph in different ways if you feed different `graph_type`
parameter in initialization.

In the example, we build the graph with `graph_type='user_parent'`, which means we build the graph with user as nodes
and parent relation of comments as edges.

### data_process.train_test_split

This provides a flexible way to split the dataset into train, (val optional) and test set. You can specify the ratio of 
the split.

### feature_description

Our feature generation contains so many features that we provide a way to generate the description of each feature.

### feature_combinations, get_basic_features, get_features, get_sentiment, key_manager, preframe, sentiment_preparation

These modules are used to generate features for each node. We provide a series of features.

### sentiment_preparation, get_sentiment

This call the sentiment analysis API to get the sentiment of each comment.

### get_basic_features

We provide a series of basic features for each node. Due to the basic data processing that makes the value of these
features have different types, we further process these features to make them become numerical features.

### get_features

Generate the features provided by `get_basic_features`.

### feature_combinations

For user nodes as example, the post features should be transformed to the user level. This module provides a way to 
combine a series of post features to user features.

### key_manager

A more powerful way to manage the key-value pairs and only keys, especially easy to check missing keys. Useful when
you have a lot of features.

### preframe

A much quicker way to store the features in a pandas-DataFrame-like way. It has a better performance than pandas for
large data. In addition, due to the update of pandas, it is not easy to use pandas to append data to a DataFrame. This
module provides a way to append data to a DataFrame. Also, you can easily transform it to pandas DataFrame, or
transform pandas DataFrame to preframe.

This is released, since we find that a large time cost is spent on pandas operations. To speed up the process, finally
we have this. If you want complex operations, you can transform it to pandas DataFrame. In preframe, you can check
`if __name__ == '__main__':` to see examples that test the features of preframe.



