# Leetcode 0380. Insert Delete GetRandom O(1)

## Problem Description
Design a data structure that supports all following operations in average O(1) time.

- insert(val): Inserts an item val to the set if not already present.
- remove(val): Removes an item val from the set if present.
- getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.

## Solution
Python Solution:
```python
import random

class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        last_element, idx = self.list[-1], self.dict[val]
        self.list[idx], self.dict[last_element] = last_element, idx
        self.list.pop()
        del self.dict[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.list)
```

Step-by-step explanation:
1. We use a dictionary to store the values and their indices, and a list to store the values in the order they are inserted.
2. When inserting a value, we add it to the end of the list and store its index in the dictionary.
3. When removing a value, we replace it with the last value in the list, update the index of the last value in the dictionary, and remove the last value from the list and the value from the dictionary.
4. To get a random value, we simply return a random element from the list.

Complexity analysis:
- Time complexity: O(1) for all operations. This is because we are using a dictionary for lookups and a list for insertions and deletions at the end.
- Space complexity: O(n), where n is the number of values inserted. This is because we are storing each value in both a dictionary and a list.