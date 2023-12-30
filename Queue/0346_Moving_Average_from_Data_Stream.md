# Leetcode 346. Moving Average from Data Stream

## Problem Description
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

## Solution
Python Solution:
```python
from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.queue = deque()
        self.window_sum = 0

    def next(self, val: int) -> float:
        """
        Calculate the moving average.
        """
        if len(self.queue) == self.size:
            self.window_sum -= self.queue.popleft()
        self.queue.append(val)
        self.window_sum += val
        return self.window_sum / len(self.queue)
```

Step-by-step explanation:
1. We use a Python deque to simulate the sliding window. We also keep track of the sum of the elements in the window.
2. When we add a new element, if the window is already full (i.e., its size equals the specified size), we remove the leftmost element from the window and subtract it from the sum.
3. We then add the new element to the window and add it to the sum.
4. The moving average is then the sum divided by the current size of the window.

Complexity analysis:
- Time complexity: O(1) for both adding a new element and calculating the moving average.
- Space complexity: O(n), where n is the size of the window.