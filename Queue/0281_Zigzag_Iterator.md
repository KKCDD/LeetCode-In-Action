# Leetcode 281. Zigzag Iterator

## Problem Description
Given two 1d vectors, implement an iterator to return their elements alternately.

Example:
Input: v1 = [1,2] and v2 = [3,4,5,6]
Output: [1,3,2,4,5,6]

## Solution
Python Solution:
```python
class ZigzagIterator:
    def __init__(self, v1, v2):
        self.data = [(len(v), iter(v)) for v in (v1, v2) if v]

    def next(self):
        len, iter = self.data.pop(0)
        if len > 1:
            self.data.append((len-1, iter))
        return next(iter)

    def hasNext(self):
        return bool(self.data)
```

Step-by-step explanation:
1. In the constructor, we create a list of tuples, where each tuple contains the length of a vector and an iterator for that vector. We only include vectors that are not empty.
2. In the `next` method, we pop the first tuple from the list, decrement the length, and if there are still elements left in that vector, we append the tuple back to the end of the list. We then return the next element from the iterator.
3. In the `hasNext` method, we simply check if the list is not empty.

Complexity analysis:
- Time complexity: O(1) for both `next` and `hasNext` methods.
- Space complexity: O(n), where n is the total number of elements in the two vectors.