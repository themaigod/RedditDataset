from typing import Dict, Optional, List
from collections import defaultdict
import pandas as pd
import numpy as np


class Preframe:
    """
    This class is used to pre-process the data to feed into dataframe
    """
    def __init__(self, data_dict: Dict = None):
        """ Initialize the preframe with data

        Args:
            data_dict (Dict): {feature_name: list of feature_value}
            Notice: the feature_name should be string, and the feature_value should be int or float
        """
        self.data = defaultdict(list)
        if data_dict:
            self.update(data_dict)
        self.columns = list(self.data.keys())
        self.columns.sort()
        self.index = []
        if self.columns:
            self.index = list(range(len(self.data[self.columns[0]])))
        
    
    def update(self, data_dict: Dict):
        """ Update the preframe with new data

        Args:
            data_dict (Dict): {feature_name: list of feature_value}
        """
        for key, value in data_dict.items():
            self.data[key] = value
            
        # update the columns and index
        self.update_columns()
        self.update_index()
        
    def add(self, data_dict: Dict):
        """ Add new data to the preframe

        Args:
            data_dict (Dict): {feature_name: list of feature_value}
        """
        for key, value in data_dict.items():
            self.data[key].extend(value)
            
        # update the columns and index
        if not self.check_filled():
            self.fillna()
        self.update_columns()
        self.update_index()
        
    def combine(self, preframe: "Preframe"):
        """
        Combine another preframe with this preframe

        Args:
            preframe (Preframe): another preframe to combine with
        """
        for key, value in preframe.data.items():
            self.data[key].extend(value)
            
        # update the columns and index
        if not self.check_filled():
            self.fillna()
        self.update_columns()
        self.update_index()
        
    def to_dict(self) -> Dict:
        """ Convert the preframe to dictionary

        Returns:
            Dict: {feature_name: list of feature_value}
        """
        return self.data
    
    def __len__(self):
        return len(self.data)
    
    def add_with_list(self, data_list: list):
        """ Add the preframe with new data

        Args:
            data_list (list): [list of feature_value (for different feature_name)]
        """
        for index, value in enumerate(data_list):
            if index >= len(self.columns):
                break
            self.data[self.columns[index]].extend(value)
    
    def append(self, item):
        if isinstance(item, Preframe):
            self.combine(item)
        elif isinstance(item, dict):
            self.add(item)
        elif isinstance(item, list):
            self.add_with_list(item)
        elif isinstance(item, tuple):
            self.add_with_list(list(item))
        else:
            raise TypeError("Unsupported type: {}".format(type(item)))
        
    def __getitem__(self, key):
        if isinstance(key, int):
            return {k: v[key] for k, v in self.data.items()}
        elif isinstance(key, list) and len(key) > 0 and isinstance(key[0], int):
            return {k: [v[i] for i in key] for k, v in self.data.items()}
        elif isinstance(key, str):
            return self.data[key]
        elif isinstance(key, list) and len(key) > 0 and isinstance(key[0], str):
            return {k: self.data[k] for k in key}
        elif isinstance(key, slice):
            return {k: v[key] for k, v in self.data.items()}
        elif isinstance(key, tuple):
            return {k: [v[i] for i in key] for k, v in self.data.items()}
        elif isinstance(key, dict) and len(key) > 0 and isinstance(list(key.values())[0], list) and isinstance(list(key.values())[0][0], bool):
            return {k: [v[i] for i in range(len(v)) if key[k][i]] for k, v in self.data.items()}
        elif isinstance(key, dict) and len(key) > 0 and isinstance(list(key.values())[0], list) and isinstance(list(key.values())[0][0], int):
            return {k: [v[i] for i in key[k]] for k, v in self.data.items() if k in key}
        else:
            raise TypeError("Unsupported type: {}".format(type(key)))
        
    def __setitem__(self, key, value):
        if isinstance(key, str) and isinstance(value, list):
            self.data[key] = value
        elif isinstance(key, str) and (isinstance(value, int) or isinstance(value, float)):
            self.data[key] = [value] * len(self.index)
        elif isinstance(key, list) and len(key) > 0 and isinstance(key[0], str):
            if isinstance(value, list) and len(key) == len(value):
                for k, v in zip(key, value):
                    self.data[k] = v
            elif isinstance(value, list) and len(value) == len(self.index):
                for k in key:
                    if isinstance(value, list):
                        value = value.copy()
                    self.data[k] = value
        elif isinstance(key, dict) and len(key) > 0 and isinstance(list(key.values())[0], list) and isinstance(list(key.values())[0][0], int):
            index = 0
            for k, v in key.items():
                for i in v:
                    self.data[k][i] = value[index]
                    index += 1
        else:
            raise TypeError("Unsupported type: {}".format(type(key)))
        
    def to_dataframe(self) -> pd.DataFrame:
        """ Convert the preframe to dataframe

        Returns:
            pd.DataFrame: the dataframe of the preframe
            
            
        """
        return pd.DataFrame(self.data, index=self.index)
    
    
    def update_index(self):
        """ Update the index of the preframe

        Args:
            index (list): the new index
        """
        self.index = list(range(len(self.data[self.columns[0]])))
        
    def update_columns(self):
        """ Update the columns of the preframe

        Args:
            columns (list): the new columns
        """
        self.columns = list(self.data.keys())
        self.columns.sort()
        
    def fillna(self, value=None):
        """ Fill the missing value with the given value

        Args:
            value (int or float): the value to fill
        """
        if value is None:
            value = np.nan
        max_length = max([len(v) for v in self.data.values()])
        for k, v in self.data.items():
            if len(v) < max_length:
                self.data[k].extend([value] * (max_length - len(v)))
                
                
    def check_value(self, value=np.nan):
        """ Check if any value in the preframe is this value, then return the locations as an data_dict with bool item

        Args:
            value (int or float): the value to check, default is np.nan
        Returns:
            Dict: {feature_name: list of bool value}
        """
        # require consider the nan value
        if np.isnan(value):
            return {k: [np.isnan(vv) for vv in v] for k, v in self.data.items()}
        else:
            return {k: [vv == value for vv in v] for k, v in self.data.items()}

    def to_dataframe(self):
        """ Convert the preframe to dataframe

        Returns:
            pd.DataFrame: the dataframe of the preframe
        """
        return pd.DataFrame(self.data)
    
    def check_filled(self):
        """ Check if the preframe is filled with the same length

        Returns:
            bool: True if the preframe is filled with the same length
        """
        return len(set([len(v) for v in self.data.values()])) == 1
    
    @classmethod
    def from_dataframe(cls, dataframe: pd.DataFrame):
        """ Convert the dataframe to preframe

        Args:
            dataframe (pd.DataFrame): the dataframe to convert
        Returns:
            Preframe: the preframe of the dataframe
        """
        dict_data = dataframe.to_numpy().tolist()
        dict_data = {k: [v[i] for v in dict_data] for i, k in enumerate(dataframe.columns)}
        return cls(dict_data)
        
        
class SpeedPreframe:
    """
    It is similar to the preframe. But it is focus on the speed of appending data.
    This will reduce the supporting features and alignment checking.
    """
    def __init__(self, data_dict: Optional[Dict | Preframe] = None):
        """ Initialize the speedpreframe with data
        Args:
            data_dict (Dict | Preframe): {feature_name: list of feature_value}
            Notice: the feature_name should be string, and the feature_value should be int or float
        """
        self.data: List[List] = []
        if data_dict:
            if isinstance(data_dict, Preframe):
                data_dict = data_dict.to_dict()
            
            # assumes the data_dict is aligned
            self.columns = list(data_dict.keys())
            self.columns.sort()
            self.index = list(range(len(data_dict[self.columns[0]])))
            self.data = [[data_dict[k][i] for k in self.columns] for i in self.index]
        else:
            self.columns = []
            self.index = []
        
            
            
    def add(self, data_dict: Dict):
        """ Add new data to the preframe
        
        Args:
            data_dict (Dict): {feature_name: list of feature_value}
        """
        # assumes the data_dict is aligned with the columns if the columns is not empty
        if not self.columns:
            self.columns = list(data_dict.keys())
            self.columns.sort()
        self.index.extend(list(range(len(self.index), len(self.index) + len(data_dict[self.columns[0]]))))
        self.data.extend([[data_dict[k][i] for k in self.columns] for i in range(len(data_dict[self.columns[0]]))])
        
    def append(self, item) -> None:
        """ Append the item to the speedpreframe

        Args:
            item List: the item to append
        """
        self.data.append(item)
        self.index.append(len(self.index))
        
    def __getitem__(self, key):
        """ Get the item from the speedpreframe
        
        Args:
            key (int): the index
        Returns:
            List: the item
        """
        return self.data[key]
    
    def add_column(self, column_name: str):
        """ Add the column to the speedpreframe

        Args:
            column_name (str): the column name
        """
        # dangerous function, may cause alignment error
        self.columns.append(column_name)

    def append_from_dict(self, data_dict: Dict):
        """ Append the data from the data_dict
        
        Args:
            data_dict (Dict): {feature_name: feature_value}
        """
        # it will throw out the data if the data_dict is not aligned with the columns
        # be careful to use this function, should call add_column first if the column is not in the speedpreframe
        self.data.append([data_dict[k] for k in self.columns])
        self.index.append(len(self.index))
        
    def __setitem__(self, key, value):
        """ Set the item to the speedpreframe

        Args:
            key (int): the index
            value (List): the item
        """
        self.data[key] = value
        
    def setitem_from_dict(self, key, data_dict):
        """ Set the item from the data_dict

        Args:
            key (int): the index
            data_dict (Dict): {feature_name: feature_value}
        """
        self.data[key] = [data_dict[k] for k in self.columns]
        
    def update(self, index_tuple, value):
        """ Update the value in the speedpreframe

        Args:
            index_tuple (tuple): the index tuple (row, column_index)
            value (int or float): the value to update
        """
        self.data[index_tuple[0]][index_tuple[1]] = value
        
    def update_from_column(self, index, data_dict):
        """ Update the value in the speedpreframe with the column name
        
        Args:
            index (int): the index
            dict (Dict): {feature_name: feature_value}
        """
        # speed up index
        columns_index = {k: i for i, k in enumerate(self.columns)}
        update_list = [((index, columns_index[k]), value) for k, value in data_dict.items()]
        for index_tuple, value in update_list:
            self.update(index_tuple, value)
            
    def extend(self, data_list: List):
        """ Extend the speedpreframe with the data_list
        
        Args:
            data_list (List): the data_list to extend
        """
        self.data.extend(data_list)
        self.index.extend(list(range(len(self.index), len(self.index) + len(data_list))))
        
    def extend_from_dict_list(self, data_dict: List[Dict]):
        """ Extend the speedpreframe with a list of data_dict
        
        Args:
            data_dict (List[Dict]): the list of data_dict
        """
        # it will throw out the data if the data_dict is not aligned with the columns
        # be careful to use this function, should call add_column first if the column is not in the speedpreframe
        self.data.extend([[data_dict[k] for k in self.columns] for data_dict in data_dict])
        self.index.extend(list(range(len(self.index), len(self.index) + len(data_dict))))
        
    def combine(self, speedpreframe: "SpeedPreframe"):
        """ Combine the speedpreframe with another speedpreframe
        
        Args:
            speedpreframe (SpeedPreframe): the speedpreframe to combine
        """
        # would not check the alignment of the columns
        self.data.extend(speedpreframe.data)
        self.index.extend(speedpreframe.index)
        
    def to_dict(self) -> Dict:
        """ Convert the speedpreframe to dictionary

        Returns:
            Dict: {feature_name: list of feature_value}
        """
        return {k: [v[i] for i in range(len(v))] for k, v in zip(self.columns, np.transpose(self.data))}
    
    def to_list(self) -> List:
        """ Convert the speedpreframe to list

        Returns:
            List: the list of the speedpreframe
        """
        return self.data
    
    def to_preframe(self) -> Preframe:
        """ Convert the speedpreframe to preframe

        Returns:
            Preframe: the preframe of the speedpreframe
        """
        return Preframe(self.to_dict())
    
    def to_dataframe(self) -> pd.DataFrame:
        """ Convert the speedpreframe to dataframe

        Returns:
            pd.DataFrame: the dataframe of the speedpreframe
        """
        # here we try a faster way to convert the speedpreframe to dataframe
        # we assume the data is aligned, so we can use the np.array to convert the data and then transpose it
        data = np.array(self.data)
        return pd.DataFrame(data, columns=self.columns)
    
    @classmethod
    def from_dataframe(cls, dataframe: pd.DataFrame):
        """ Convert the dataframe to speedpreframe

        Args:
            dataframe (pd.DataFrame): the dataframe to convert
        Returns:
            SpeedPreframe: the speedpreframe of the dataframe
        """
        dict_data = dataframe.to_numpy().tolist()
        speedpreframe = cls()
        speedpreframe.columns = dataframe.columns.tolist()
        speedpreframe.extend(dict_data)
        
        return speedpreframe
            
            
if __name__ == "__main__":
    # Test all the functions
    # test the preframe
    preframe = Preframe()
    preframe = Preframe({"a": [1, 2, 3], "b": [4, 5, 6]})
    preframe = Preframe.from_dataframe(pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]}))
    
    # test the update and to_dict
    preframe.update({"c": [7, 8, 9]})
    preframe.update({"a": [10, 11, 12]})
    assert preframe.to_dict() == {"a": [10, 11, 12], "b": [4, 5, 6], "c": [7, 8, 9]}
    
    # test the add
    preframe.add({"a": [13], "b": [14], "c": [15]})
    assert preframe.to_dict() == {"a": [10, 11, 12, 13], "b": [4, 5, 6, 14], "c": [7, 8, 9, 15]}
    preframe.add({"a": [16]})
    assert preframe.to_dict() == {"a": [10, 11, 12, 13, 16], "b": [4, 5, 6, 14, np.nan], "c": [7, 8, 9, 15, np.nan]}
    
    # test the combine
    preframe2 = Preframe({"a": [17, 18], "b": [19, 20], "c": [21, 22]})
    preframe.combine(preframe2)
    assert preframe.to_dict() == {"a": [10, 11, 12, 13, 16, 17, 18], "b": [4, 5, 6, 14, np.nan, 19, 20], "c": [7, 8, 9, 15, np.nan, 21, 22]}
    
    # test add with list
    preframe = Preframe({"a": [1, 2, 3], "b": [4, 5, 6]})
    preframe.add_with_list([[7], [8]])
    assert preframe.to_dict() == {"a": [1, 2, 3, 7], "b": [4, 5, 6, 8]}
    
    # test append
    preframe = Preframe({"a": [1, 2, 3], "b": [4, 5, 6]})
    preframe.append({"a": [7], "b": [8]})
    assert preframe.to_dict() == {"a": [1, 2, 3, 7], "b": [4, 5, 6, 8]}
    preframe.append([[9], [10]])
    assert preframe.to_dict() == {"a": [1, 2, 3, 7, 9], "b": [4, 5, 6, 8, 10]}
    preframe.append(([11], [12]))
    assert preframe.to_dict() == {"a": [1, 2, 3, 7, 9, 11], "b": [4, 5, 6, 8, 10, 12]}
    preframe.append(Preframe({"a": [13], "b": [14]}))
    assert preframe.to_dict() == {"a": [1, 2, 3, 7, 9, 11, 13], "b": [4, 5, 6, 8, 10, 12, 14]}
    
    # test __getitem__
    preframe = Preframe({"a": [1, 2, 3], "b": [4, 5, 6]})
    assert preframe["a"] == [1, 2, 3]
    assert preframe[0] == {"a": 1, "b": 4}
    assert preframe[[0, 1]] == {"a": [1, 2], "b": [4, 5]}
    assert preframe[["a", "b"]] == {"a": [1, 2, 3], "b": [4, 5, 6]}
    assert preframe[0:2] == {"a": [1, 2], "b": [4, 5]}
    assert preframe[(0, 1)] == {"a": [1, 2], "b": [4, 5]}
    assert preframe[{"a": [True, False, True], "b": [False, True, False]}] == {"a": [1, 3], "b": [5]}
    assert preframe[{"a": [0]}] == {"a": [1]}
    
    # test __setitem__
    preframe["c"] = [7, 8, 9]
    assert preframe.to_dict() == {"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]}
    preframe["d"] = 10
    assert preframe.to_dict() == {"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9], "d": [10, 10, 10]}
    preframe[["a", "b"]] = [[10, 11, 12], [13, 14, 15]]
    assert preframe.to_dict() == {"a": [10, 11, 12], "b": [13, 14, 15], "c": [7, 8, 9], "d": [10, 10, 10]}
    preframe[["a", "b"]] = [16, 17, 18]
    assert preframe.to_dict() == {"a": [16, 17, 18], "b": [16, 17, 18], "c": [7, 8, 9], "d": [10, 10, 10]}
    preframe[{"a": [0, 2]}] = [19, 20, 21]
    assert preframe.to_dict() == {"a": [19, 17, 20], "b": [16, 17, 18], "c": [7, 8, 9], "d": [10, 10, 10]}
    
    # test to_dataframe
    preframe = Preframe({"a": [1, 2, 3], "b": [4, 5, 6]})
    assert preframe.to_dataframe().to_dict() == {"a": {0: 1, 1: 2, 2: 3}, "b": {0: 4, 1: 5, 2: 6}}
    
    # test fillna
    preframe = Preframe({"a": [1, 2, 3], "b": [4, 5]})
    preframe.fillna()
    assert preframe.to_dict() == {"a": [1, 2, 3], "b": [4, 5, np.nan]}
    preframe = Preframe({"a": [1, 2, 3], "b": [4, 5]})
    preframe.fillna(0)
    assert preframe.to_dict() == {"a": [1, 2, 3], "b": [4, 5, 0]}
    
    # test check_value
    preframe = Preframe({"a": [1, 2, 3], "b": [4, 5, np.nan]})
    assert preframe.check_value() == {"a": [False, False, False], "b": [False, False, True]}
    assert preframe.check_value(4) == {"a": [False, False, False], "b": [True, False, False]}
    
    print("Preframe test passed!")
    
    # test the speedpreframe
    speedpreframe = SpeedPreframe()
    speedpreframe = SpeedPreframe({"a": [1, 2, 3], "b": [4, 5, 6]})
    speedpreframe = SpeedPreframe(Preframe({"a": [1, 2, 3], "b": [4, 5, 6]}))
    speedpreframe = SpeedPreframe.from_dataframe(pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]}))
    
    # test the add
    speedpreframe.add({"a": [7, 8, 9], "b": [10, 11, 12]})
    assert speedpreframe.to_dict() == {"a": [1, 2, 3, 7, 8, 9], "b": [4, 5, 6, 10, 11, 12]}
    
    # test the append
    speedpreframe = SpeedPreframe({"a": [1, 2, 3], "b": [4, 5, 6]})
    speedpreframe.append([7, 8])
    assert speedpreframe.data == [[1, 4], [2, 5], [3, 6], [7, 8]]
    
    # test the __getitem__
    assert speedpreframe[0] == [1, 4]
    
    # test the add_column
    speedpreframe.add_column("c")
    assert speedpreframe.columns == ["a", "b", "c"]
    
    # test the append_from_dict
    speedpreframe = SpeedPreframe({"a": [1, 2, 3], "b": [4, 5, 6]})
    speedpreframe.append_from_dict({"a": 9, "b": 10, "c": 11})
    assert speedpreframe.data == [[1, 4], [2, 5], [3, 6], [9, 10]]
    
    # test the setitem
    speedpreframe[0] = [7, 8]
    assert speedpreframe.data == [[7, 8], [2, 5], [3, 6], [9, 10]]
    
    # test the setitem_from_dict
    speedpreframe.setitem_from_dict(0, {"a": 11, "b": 12})
    assert speedpreframe.data == [[11, 12], [2, 5], [3, 6], [9, 10]]
    
    # test the update
    speedpreframe.update((0, 0), 13)
    assert speedpreframe.data == [[13, 12], [2, 5], [3, 6], [9, 10]]
    
    # test the update_from_column
    speedpreframe.update_from_column(0, {"a": 14, "b": 15})
    assert speedpreframe.data == [[14, 15], [2, 5], [3, 6], [9, 10]]
    
    # test the extend
    speedpreframe.extend([[16, 17], [18, 19]])
    assert speedpreframe.data == [[14, 15], [2, 5], [3, 6], [9, 10], [16, 17], [18, 19]]
    
    # test the extend_from_dict_list
    speedpreframe.extend_from_dict_list([{"a": 20, "b": 21}, {"a": 22, "b": 23}])
    assert speedpreframe.data == [[14, 15], [2, 5], [3, 6], [9, 10], [16, 17], [18, 19], [20, 21], [22, 23]]
    
    # test the combine
    speedpreframe = SpeedPreframe({"a": [1, 2, 3], "b": [4, 5, 6]})
    speedpreframe2 = SpeedPreframe({"a": [7, 8], "b": [9, 10]})
    speedpreframe.combine(speedpreframe2)
    assert speedpreframe.data == [[1, 4], [2, 5], [3, 6], [7, 9], [8, 10]]
    
    # test the to_dict
    speedpreframe = SpeedPreframe({"a": [1, 2, 3], "b": [4, 5, 6]})
    assert speedpreframe.to_dict() == {"a": [1, 2, 3], "b": [4, 5, 6]}

    # test the to_list
    speedpreframe = SpeedPreframe({"a": [1, 2, 3], "b": [4, 5, 6]})
    assert speedpreframe.to_list() == [[1, 4], [2, 5], [3, 6]]
    
    # test the to_preframe
    speedpreframe = SpeedPreframe({"a": [1, 2, 3], "b": [4, 5, 6]})
    assert speedpreframe.to_preframe().to_dict() == {"a": [1, 2, 3], "b": [4, 5, 6]}
    
    # test the to_dataframe
    speedpreframe = SpeedPreframe({"a": [1, 2, 3], "b": [4, 5, 6]})
    assert speedpreframe.to_dataframe().to_dict() == {"a": {0: 1, 1: 2, 2: 3}, "b": {0: 4, 1: 5, 2: 6}}
    
    print("SpeedPreframe test passed!")
    