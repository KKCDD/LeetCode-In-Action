# Leetcode 1429. First Unique Number

## Problem Description
Implement the FirstUnique class:

- FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
- int showFirstUnique() returns the value of the first unique number of the queue, and returns -1 if there is no such number.
- void add(int value) insert value to the queue.

## Solution
Python Solution:
```python
from collections import OrderedDict

class FirstUnique:

    def __init__(self, nums):
        self.d = OrderedDict()
        for num in nums:
            self.add(num)

    def showFirstUnique(self):
        if len(self.d) == 0:
            return -1
        # The first unique number is the first key in the ordered dictionary
        return next(iter(self.d))

    def add(self, value):
        # If the value is already in the dictionary, remove it
        if value in self.d:
            self.d.pop(value)
        else:
            self.d[value] = None
```

Step-by-step explanation:
1. We use an ordered dictionary to keep track of the numbers and their order of insertion. The keys of the dictionary are the numbers, and the values are not used.
2. When we add a number, if it's already in the dictionary, we remove it, because it's no longer unique. If it's not in the dictionary, we add it.
3. To show the first unique number, we simply return the first key in the dictionary. If the dictionary is empty, we return -1.

Complexity analysis:
- Time complexity: O(1) for both `showFirstUnique` and `add` methods.
- Space complexity: O(n), where n is the number of unique numbers.