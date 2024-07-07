from typing import List, Dict, Set, Tuple, Optional

class KeyValueManager:
    """
    A class to manage key-value pairs. It can be used to store the key-value pairs in a dictionary, and also store the keys that have no value yet.
    It can also be used to hash the keys for those that are not hashable.
    """
    
    def __init__(self, key_value_store: Optional[dict | Tuple[List, List]] = None, unvalued_keys: set = None, use_hash: bool = True):
        """
        Parameters
        ----------
        key_value_store : dict|Tuple[List, List], optional
            A dictionary or a tuple of two lists, by default None
            If it is a dictionary, it stores the key-value pairs.
            If it is a tuple of two lists, it stores the keys in the first list and the values in the second list.
        unvalued_keys : set, optional
            A set of keys that have no value yet, by default None
        use_hash : bool, optional
            Whether to hash the keys, by default True
        """
        self.key_value_store = key_value_store
        if self.key_value_store is None:
            self.key_value_store = {}
        if isinstance(self.key_value_store, tuple) and not use_hash:
            self.key_value_store = dict(zip(*self.key_value_store))
        
        self.unvalued_keys = set()
        if unvalued_keys is not None:
            self.unvalued_keys = unvalued_keys
            
        self.use_hash = use_hash
        if self.use_hash:
            self.hash_table = {}
            self.hash_list = []
            self.hash_current = 0
            if isinstance(self.key_value_store, dict):
                self.key_value_store = self.hash_key_dict(self.key_value_store)
            else:
                key_list = self.hash_key_list(self.key_value_store[0])
                self.key_value_store = dict(zip(key_list, self.key_value_store[1]))
            self.unvalued_keys = self.hash_key_set(self.unvalued_keys)
                

    def get(self, key):
        """
        Get the value of a key.
        """
        if self.use_hash:
            key = self.hash_key(key)
        return self.key_value_store.get(key)

    def set(self, key, value):
        """
        Set the value of a key. If the key is in the unvalued_keys, remove it from the unvalued_keys.
        """
        if self.use_hash:
            key = self.hash_key(key)
        self.key_value_store[key] = value
        if key in self.unvalued_keys:
            self.unvalued_keys.remove(key)
        
    def combine(self, other:'KeyValueManager'):
        """
        Combine the key-value pairs and unvalued keys of two KeyValueManager objects.
        Notice that if the keys are the same, the values of the first KeyValueManager object will be replaced by the values of the second KeyValueManager object.
        """
        if self.use_hash and other.use_hash:
            unhashed_keys, values = other.recover_key_dict(other.key_value_store, hashable=False)
            hashed_keys = self.hash_key_list(unhashed_keys)
            hash_dict = dict(zip(hashed_keys, values))
            self.key_value_store.update(hash_dict)
            self.unvalued_keys.update(self.hash_key_set(other.recover_key_set(other.unvalued_keys)))
        elif self.use_hash and not other.use_hash:
            self.key_value_store.update(self.hash_key_dict(other.key_value_store))
            self.unvalued_keys.update(self.hash_key_set(other.unvalued_keys))
        elif not self.use_hash and other.use_hash:
            unhashed_keys, values = other.recover_key_dict(other.key_value_store, hashable=False)
            self.key_value_store.update(dict(zip(unhashed_keys, values)))
            self.unvalued_keys.update(other.recover_key_set(other.unvalued_keys))
        else:
            self.key_value_store.update(other.key_value_store)
            self.unvalued_keys.update(other.unvalued_keys)
        
    def key_count(self):
        """
        Get the number of keys.
        """
        return len(self.key_value_store) + len(self.unvalued_keys)
    
    def value_count(self):
        """
        Get the number of keys that have values.
        """
        return len(self.key_value_store)
    
    def unvalued_key_count(self):
        """
        Get the number of keys that have no values.
        """
        return len(self.unvalued_keys)
    
    def keys(self):
        """
        Get all the keys.
        """
        if self.use_hash:
            return self.recover_key_list(list(self.key_value_store.keys())) + self.recover_key_list(list(self.unvalued_keys))
        return list(self.key_value_store.keys()) + list(self.unvalued_keys)
        
    def seperate_unvalued_keys(self, size):
        """
        Seperate the unvalued keys into several KeyValueManager objects, each of which has at most size unvalued keys.
        It is used to generate batches of unvalued keys.
        
        Parameters
        ----------
        size : int
            The maximum number of unvalued keys in each KeyValueManager object.
        """
        if len(self.unvalued_keys) < size:
            return [self]
        else:
            unvalued_keys = list(self.unvalued_keys)
            if self.use_hash:
                unvalued_keys = self.recover_key_list(unvalued_keys)
            key_value_managers = []
            for i in range(len(unvalued_keys) // size):
                key_value_managers.append(KeyValueManager(unvalued_keys=unvalued_keys[i*size:(i+1)*size], use_hash=self.use_hash))
            if len(unvalued_keys) % size != 0:
                key_value_managers.append(KeyValueManager(unvalued_keys=unvalued_keys[(i+1)*size:], use_hash=self.use_hash))
            return key_value_managers
        
    
    def seperate_valued_keys(self, size):
        """
        Seperate the valued keys into several KeyValueManager objects, each of which has at most size valued keys.
        It is used to generate batches of valued keys.
        
        Parameters
        ----------
        size : int
            The maximum number of valued keys in each KeyValueManager object.
        """
        if len(self.key_value_store) < size:
            return [self]
        else:
            keys = list(self.key_value_store.keys())
            if self.use_hash:
                keys = self.recover_key_list(keys)
            key_value_managers = []
            for i in range(len(keys) // size):
                key_value_managers.append(KeyValueManager(key_value_store=dict(zip(keys[i*size:(i+1)*size], [self.get(key) for key in keys[i*size:(i+1)*size]])), use_hash=self.use_hash))
            if len(keys) % size != 0:
                key_value_managers.append(KeyValueManager(key_value_store=dict(zip(keys[(i+1)*size:], [self.get(key) for key in keys[(i+1)*size:]])), use_hash=self.use_hash))
            return key_value_managers
        
    
    def hash_key(self, key):
        """
        Hash a key. If the key is already hashed, return the hash value directly.
        We use the __hash__ method of the key if it exists, otherwise we use the hash function of the string representation of the key.
        The return hash value is a string of an integer.
        
        Parameters
        ----------
        key : hashable or unhashable but can be converted to string
            The key to be hashed.
        """
        # capture __hash__ method of the key if it exists
        hash_method = getattr(key, '__hash__', None)
        if hash_method is None:
            hashed_key = hash(str(key))
        else:
            hashed_key = hash(key)
        if hashed_key in self.hash_table:
            return self.hash_table[hashed_key]
        
        hash_value = str(self.hash_current)
        self.hash_current += 1
       
        self.hash_table[hashed_key] = hash_value
        self.hash_list.append(key)
        return hash_value
    
    def recover_key(self, hash_value):
        """
        Recover a key from its hash value.
        
        Parameters
        ----------
        hash_value : str
            The hash value of a key.
        """
        return self.hash_list[int(hash_value)]
    
    def hash_key_list(self, key_list):
        """
        Hash a list of keys.
        
        Parameters
        ----------
        key_list : list
            A list of keys to be hashed.
        """
        return [self.hash_key(key) for key in key_list]
    
    def hash_key_dict(self, key_value_dict):
        """
        Hash a dictionary of keys.
        
        Parameters
        ----------
        key_value_dict : dict
            A dictionary of keys to be hashed.
        """
        return {self.hash_key(key): value for key, value in key_value_dict.items()}
    
    def recover_key_dict(self, hash_dict, hashable=False):
        """
        Recover a dictionary of keys from its hash dictionary.
        
        Parameters
        ----------
        hash_dict : dict
            A dictionary of hash keys.
        hashable : bool, optional
            Whether the keys are hashable, by default False
            
        Returns
        -------
        if hashable:
            dict
                A dictionary of recovered keys.
        else:
            key_list, value_list
                A list of recovered keys and a list of values.
        """
        if hashable:
            return {self.recover_key(key): value for key, value in hash_dict.items()}
        else:
            key_list = []
            value_list = []
            for key, value in hash_dict.items():
                key_list.append(self.recover_key(hash_value=key))
                value_list.append(value)
            return key_list, value_list
                
    
    def recover_key_list(self, hash_list):
        """
        Recover a list of keys from its hash list.
        
        Parameters
        ----------
        hash_list : list
            A list of hash keys.
        """
        return [self.recover_key(key) for key in hash_list]
        
    def recover_key_set(self, hash_set):
        """
        Recover a set of keys from its hash set.
        
        Parameters
        ----------
        hash_set : set
            A set of hash keys.
        """
        return {self.recover_key(key) for key in hash_set}
        
    def hash_key_set(self, key_set):
        """
        Hash a set of keys.
        
        Parameters
        ----------
        key_set : set
            A set of keys to be hashed.
        """
        return {self.hash_key(key) for key in key_set}
    
    def unvalued_keys_list(self):
        """
        Get the unvalued keys as a list.
        """
        temp_unvalued_keys = list(self.unvalued_keys)
        if self.use_hash:
            temp_unvalued_keys = self.recover_key_list(temp_unvalued_keys)
        else:
            temp_unvalued_keys = self.temp_unvalued_keys
        self.temp_unvalued_keys = temp_unvalued_keys
        return temp_unvalued_keys
    
    def set_all(self, key_value_dict):
        """
        Set all the key-value pairs.
        
        Parameters
        ----------
        key_value_dict : dict
            A dictionary of key-value pairs.
        """
        if self.use_hash:
            self.key_value_store.update(self.hash_key_dict(key_value_dict))
        else:
            self.key_value_store.update(key_value_dict)
        self.unvalued_keys = set()
        
    def set_all_by_list(self, value_list, key_list=None, ):
        """
        Set all the key-value pairs.
        
        Parameters
        ----------
        value_list : list
            A list of values.
        key_list : list, optional
            A list of keys, by default None
            If it is None, you should call the unvalued_keys_list method first to get the unvalued keys.
        """
        if key_list is None:
            key_list = getattr(self, 'temp_unvalued_keys', None)
            if key_list is None:
                raise ValueError('key_list is not provided and unvalued_keys is not sorted')
        if self.use_hash:
            self.key_value_store.update(dict(zip(self.hash_key_list(key_list), value_list)))
        else:
            self.key_value_store.update(dict(zip(key_list, value_list)))
        self.unvalued_keys = set()
        
    def to_valued_list(self):
        """
        Get the key-value pairs as a list.
        """
        if self.use_hash:
            unhashed_keys, values = self.recover_key_dict(self.key_value_store, hashable=False)
        else:
            unhashed_keys, values = [], []
            for key, value in self.key_value_store.items():
                unhashed_keys.append(key)
                values.append(value)
        return unhashed_keys, values
    
    def valued_keys_list(self):
        """
        Get the valued keys as a list.
        """
        if self.use_hash:
            unhashed_keys, values = self.recover_key_dict(self.key_value_store, hashable=False)
        else:
            unhashed_keys = list(self.key_value_store.keys())
            values = [self.key_value_store[key] for key in unhashed_keys]
        self.temp_valued_keys = unhashed_keys
        self.temp_valued_values = values
        return unhashed_keys
    
    def value_list(self):
        """
        Get the values as a list.
        """
        if self.use_hash:
            unhashed_keys, values = self.recover_key_dict(self.key_value_store, hashable=False)
        else:
            unhashed_keys = list(self.key_value_store.keys())
            values = [self.key_value_store[key] for key in unhashed_keys]
        self.temp_valued_keys = unhashed_keys
        self.temp_valued_values = values
        return values
    
    def regenerate_key_value_store_dict(self, keys: List = None, values: List = None, use_hash: bool = False):
        """
        Regenerate the key-value store dict aligned with the valued keys list and the values list.
        If the keys or values are not provided, use the temp_valued_keys and temp_valued_values. So you should call the valued_keys_list or value_list method first.
        
        Parameters
        ----------
        keys : List, optional
            A list of keys, by default None
        values : List, optional
            A list of values, by default None
        use_hash : bool, optional
            Whether to hash the keys, by default False. If the keys are not hashable, you should set it to True.
        """
        if keys is None:
            keys = getattr(self, 'temp_valued_keys', None)
            if keys is None:
                raise ValueError('keys is not provided and valued_keys_list is not sorted')
        if values is None:
            values = getattr(self, 'temp_valued_values', None)
            if values is None:
                raise ValueError('values is not provided and value_list is not sorted')
        if use_hash:
            key_value_store = dict(zip(self.hash_key_list(keys), values))
        else:
            key_value_store = dict(zip(keys, values))
        return key_value_store
    
    def copy(self):
        """
        Copy the KeyValueManager object.
        """
        key_value_manager = self.__new__(self.__class__)
        setattr(key_value_manager, 'key_value_store', self.key_value_store.copy())
        setattr(key_value_manager, 'unvalued_keys', self.unvalued_keys.copy())
        setattr(key_value_manager, 'use_hash', self.use_hash)
        if self.use_hash:
            setattr(key_value_manager, 'hash_table', self.hash_table.copy())
            setattr(key_value_manager, 'hash_list', self.hash_list.copy())
            setattr(key_value_manager, 'hash_current', self.hash_current)
        if hasattr(self, 'temp_unvalued_keys'):
            setattr(key_value_manager, 'temp_unvalued_keys', self.temp_unvalued_keys.copy())
        if hasattr(self, 'temp_valued_keys'):
            setattr(key_value_manager, 'temp_valued_keys', self.temp_valued_keys.copy())
        if hasattr(self, 'temp_valued_values'):
            setattr(key_value_manager, 'temp_valued_values', self.temp_valued_values.copy())
            
        return key_value_manager
    
    @classmethod
    def reconstruct_from_hashed(cls, 
                                key_value_store: dict = None,
                                unvalued_keys: set = None, 
                                hash_table: dict = None,
                                hash_list: list = None,
                                hash_current: int = None, 
                                pervious_key_value_manager: 'KeyValueManager' = None):
        """
        Reconstruct a KeyValueManager object from its hashed version.
        You should provide (the hash_table and hash_list) or pervious_key_value_manager, but not both.
        This method reconstructs through a temp KeyValueManager object in an not-allowed way, because hash_table may contain non-exist keys. So it will be deprecated in the future if further features relly on it.
        
        Parameters
        ----------
        key_value_store : dict
            A dictionary of key-value pairs, by default None
        unvalued_keys : set
            A set of keys that have no values, by default None
        hash_table : dict
            A dictionary mapping the hash values to the keys, by default None
        hash_list : list
            A list of keys, by default None
        hash_current : int
            The current hash value, by default None
        pervious_key_value_manager : KeyValueManager
            The previous KeyValueManager object, by default None
        """
        if (hash_table is None and hash_list is None) and pervious_key_value_manager is None:
            raise ValueError('You should provide (the hash_table and hash_list) or pervious_key_value_manager')
        if (hash_table is not None and hash_list is not None) and pervious_key_value_manager is not None:
            raise ValueError('You should provide (the hash_table and hash_list) or pervious_key_value_manager, but not both')
        
        if pervious_key_value_manager:
            temp_key_value_object = pervious_key_value_manager.copy()
            if key_value_store is not None:
                temp_key_value_object.key_value_store = key_value_store
            if unvalued_keys is not None:
                temp_key_value_object.unvalued_keys = unvalued_keys
        
        else:
            temp_key_value_object = cls.__new__(cls)
            if key_value_store:
                setattr(temp_key_value_object, 'key_value_store', key_value_store)
            if unvalued_keys:
                setattr(temp_key_value_object, 'unvalued_keys', unvalued_keys)
            setattr(temp_key_value_object, 'use_hash', True)
            setattr(temp_key_value_object, 'hash_table', hash_table)
            setattr(temp_key_value_object, 'hash_list', hash_list)
            if hash_current is None:
                hash_current = len(hash_table)
            setattr(temp_key_value_object, 'hash_current', hash_current)
            
        reconstructed_key_value_store = temp_key_value_object.recover_key_dict(temp_key_value_object.key_value_store)
        reconstructed_unvalued_keys = temp_key_value_object.recover_key_set(temp_key_value_object.unvalued_keys)
        return cls(key_value_store=reconstructed_key_value_store, unvalued_keys=reconstructed_unvalued_keys, use_hash=True)
    
    def to_dict(self):
        """
        Get the key-value pairs as a dictionary.
        """
        if self.use_hash:
            return self.recover_key_dict(self.key_value_store)
        return self.key_value_store
    
    def __contains__(self, key):
        """
        Check whether a key is in the key-value pairs.
        """
        if self.use_hash:
            key = self.hash_key(key)
        return key in self.key_value_store
    

if __name__ == '__main__':
    # test the KeyValueManager class
    key_value_manager = KeyValueManager()
    key_value_manager = KeyValueManager(key_value_store={'a': 1, 'b': 2, 'c': 3}, unvalued_keys={'d', 'e', 'f'})
    print(key_value_manager.key_value_store)
    key_value_manager = KeyValueManager(key_value_store=({'a', 'b', 'c'}, [1, 2, 3]), unvalued_keys={'d', 'e', 'f'}, use_hash=False)
    print(key_value_manager.key_value_store)
    
    # test get and set
    print(key_value_manager.get('a'))
    key_value_manager.set('a', 4)
    print(key_value_manager.get('a'))
    
    # test combine
    key_value_manager2 = KeyValueManager(key_value_store={'a': 5, 'g': 6}, unvalued_keys={'h', 'i', 'j'})
    key_value_manager.combine(key_value_manager2)
    assert key_value_manager.get('a') == 5
    
    # test key_count, value_count, unvalued_key_count, keys
    assert key_value_manager.key_count() == 10
    assert key_value_manager.value_count() == 4
    assert key_value_manager.unvalued_key_count() == 6
    assert len(key_value_manager.keys()) == 10
    
    # test seperate_unvalued_keys
    key_value_manager_list = key_value_manager.seperate_unvalued_keys(2)
    assert len(key_value_manager_list) == 3
    assert key_value_manager_list[0].key_count() == 2
    
    # test seperate_valued_keys
    key_value_manager_list = key_value_manager.seperate_valued_keys(2)
    assert len(key_value_manager_list) == 2
    assert key_value_manager_list[0].key_count() == 2
    
    # test hash_key
    key_value_manager = KeyValueManager(key_value_store={'a': 1, 'b': 2, 'c': 3}, unvalued_keys={'d', 'e', 'f'}, use_hash=True)
    assert key_value_manager.hash_key('a') == '0'
    
    # test recover_key
    assert key_value_manager.recover_key('0') == 'a'
    
    # test hash_key_list
    assert key_value_manager.hash_key_list(['a', 'b', 'c']) == ['0', '1', '2']
    
    # test hash_key_dict
    assert key_value_manager.hash_key_dict({'a': 1, 'b': 2, 'c': 3}) == {'0': 1, '1': 2, '2': 3}
    
    # test recover_key_dict
    assert key_value_manager.recover_key_dict({'0': 1, '1': 2, '2': 3}) == (['a', 'b', 'c'], [1, 2, 3])
    
    # test recover_key_list
    assert key_value_manager.recover_key_list(['0', '1', '2']) == ['a', 'b', 'c']
    
    # test recover_key_set
    assert key_value_manager.recover_key_set({'0', '1', '2'}) == {'a', 'b', 'c'}
    
    # test hash_key_set
    assert key_value_manager.hash_key_set({'a', 'b', 'c'}) == {'0', '1', '2'}
    
    # test unvalued_keys_list
    assert key_value_manager.unvalued_keys_list().sort() == ['d', 'e', 'f'].sort()
    
    # test set_all
    key_value_manager.set_all({'d': 4, 'e': 5, 'f': 6})
    assert key_value_manager.value_count() == 6 and key_value_manager.unvalued_key_count() == 0
    
    # test set_all_by_list
    key_value_manager = KeyValueManager(key_value_store={'a': 1, 'b': 2, 'c': 3}, unvalued_keys={'d', 'e', 'f'}, use_hash=True)
    key_value_manager.unvalued_keys_list()
    key_value_manager.set_all_by_list([4, 5, 6])
    assert key_value_manager.value_count() == 6 and key_value_manager.unvalued_key_count() == 0
    
    # test to_valued_list
    key_value_manager = KeyValueManager(key_value_store={'a': 1, 'b': 2, 'c': 3}, unvalued_keys={'d', 'e', 'f'}, use_hash=True)
    assert key_value_manager.to_valued_list() == (['a', 'b', 'c'], [1, 2, 3])
    
    # test valued_keys_list
    assert key_value_manager.valued_keys_list() == ['a', 'b', 'c']
    
    # test value_list
    assert key_value_manager.value_list() == [1, 2, 3]
    
    # test regenerate_key_value_store_dict
    assert key_value_manager.regenerate_key_value_store_dict(values=[4, 5, 6]) == {'a': 4, 'b': 5, 'c': 6}
    
    # test copy
    key_value_manager2 = key_value_manager.copy()
    
    # test reconstruct_from_hashed
    key_value_manager = KeyValueManager(key_value_store={'a': 1, 'b': 7}, use_hash=True)
    key_value_manager3 = KeyValueManager.reconstruct_from_hashed(pervious_key_value_manager=key_value_manager2, key_value_store=key_value_manager.key_value_store)
    assert key_value_manager3.key_value_store == {'0': 1, '1': 7}
    
    print('All tests passed!')