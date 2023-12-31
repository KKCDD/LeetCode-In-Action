# Leetcode 0752. Open the Lock

## Problem Description
You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

## Solution
```python
class Solution:
    def openLock(self, deadends, target):
        visited = set(deadends)
        queue = [("0000", 0)]
        
        while queue:
            node, depth = queue.pop(0)
            if node == target: return depth
            if node in visited: continue
            visited.add(node)
            for i in range(4):
                digit = int(node[i])
                for move in [-1, 1]:
                    new_digit = (digit + move) % 10
                    new_node = node[:i] + str(new_digit) + node[i+1:]
                    queue.append((new_node, depth + 1))
        return -1
```

Step-by-step Explanation: 
1. Initialize a set visited to keep track of the nodes that have been visited.
2. Initialize a queue with the start node "0000" and its depth 0.
3. While the queue is not empty, pop a node and its depth from the queue.
4. If the node is the target, return the depth. If the node is in the visited set, skip it.
5. Add the node to the visited set.
6. For each digit in the node, calculate the new node after a move and add it to the queue with depth + 1.
7. If the target cannot be reached, return -1.

Complexity Analysis: 
- Time complexity: O(N^2 * A^N + D), where A is the number of digits in our alphabet, N is the number of digits in the lock, and D is the size of deadends. This is because in the worst case we need to visit every node and for each node, we spend a size of the node time to construct the next level nodes, and we spend D time going through the deadends.
- Space complexity: O(A^N + D), for the queue and the deadends.