# Leetcode 0146. LRU Cache

## Problem Description
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

- get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
- put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

## Solution
Python Solution:
```python
from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
```

Step-by-step explanation:
1. We use an ordered dictionary to implement the LRU cache. The keys of the dictionary are the keys of the cache, and the values are the values of the cache.
2. When we get a key, if the key is in the cache, we move it to the end of the dictionary to mark it as recently used, and return its value. If the key is not in the cache, we return -1.
3. When we put a key-value pair, if the key is already in the cache, we move it to the end. We then set the value of the key in the dictionary. If this causes the size of the cache to exceed its capacity, we remove the least recently used item, which is the first item in the dictionary.

Complexity analysis:
- Time complexity: O(1) for both get and put operations.
- Space complexity: O(capacity), as we store up to 'capacity' number of keys.