# Leetcode 362. Design Hit Counter

## Problem Description
Design a hit counter which counts the number of hits received in the past 5 minutes. Each function accepts a timestamp parameter (in seconds granularity) and you may assume that calls are being made to the system in chronological order (ie, the timestamp is monotonically increasing). You may assume that the earliest timestamp starts at 1.

## Solution
Python Solution:
```python
from collections import deque

class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hits = deque()

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        """
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        """
        while self.hits and timestamp - self.hits[0] >= 300:
            self.hits.popleft()
        return len(self.hits)
```

Step-by-step explanation:
1. We use a Python deque to store the timestamps of the hits. The deque is a suitable data structure because it allows efficient addition and removal of elements from both ends.
2. When a hit occurs, we simply append the timestamp to the deque.
3. To get the number of hits in the past 5 minutes, we remove all timestamps that are more than 5 minutes older than the current timestamp from the front of the deque, then return the size of the deque.

Complexity analysis:
- Time complexity: O(1) for the `hit` method, and O(n) for the `getHits` method in the worst case, where n is the number of hits in the past 5 minutes.
- Space complexity: O(n), where n is the total number of hits.