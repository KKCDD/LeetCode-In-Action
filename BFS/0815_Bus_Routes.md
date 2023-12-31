# Leetcode 0815. Bus Routes

## Problem Description
We have a list of bus routes. Each routes[i] is a bus route that the i-th bus repeats forever. For example if routes[0] = [1, 5, 7], this means that the first bus (0-th indexed) travels in the sequence 1->5->7->1->5->7->1->... forever.

We start at bus stop S (initially not on a bus), and we want to go to bus stop T. Travelling by buses only, what is the least number of buses we must take to reach our destination? Return -1 if it is not possible.

## Solution
```python
from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes, S, T):
        if S == T: return 0
        stop_to_route = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_route[stop].add(i)
        queue = deque([(S, 0)])
        visited = set([S])
        while queue:
            stop, bus_count = queue.popleft()
            if stop == T: return bus_count
            for i in stop_to_route[stop]:
                for next_stop in routes[i]:
                    if next_stop not in visited:
                        visited.add(next_stop)
                        queue.append((next_stop, bus_count + 1))
        return -1
```

Step-by-step Explanation: 
1. If the start stop S is the same as the target stop T, return 0 because no bus needs to be taken.
2. Create a mapping from each stop to the bus routes that pass through it.
3. Initialize a queue with the start stop and the number of buses taken so far (0 at the start).
4. While the queue is not empty, pop a stop and the number of buses taken to reach it.
5. If the stop is the target stop T, return the number of buses taken.
6. For each bus route that passes through the stop, add all the stops on the route to the queue with the number of buses taken + 1, if they haven't been visited before.
7. If the target stop cannot be reached, return -1.

Complexity Analysis: 
- Time complexity: O(N^2), where N is the total number of stops, because in the worst case we need to visit every stop and for each stop, we spend a time proportional to the number of stops to construct the next level stops.
- Space complexity: O(N), for the queue and the visited set.