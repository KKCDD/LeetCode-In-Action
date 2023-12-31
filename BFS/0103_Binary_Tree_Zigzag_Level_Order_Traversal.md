# Leetcode 0103. Binary Tree Zigzag Level Order Traversal

## Problem Description
Problem Description:
Given a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

For example, given binary tree `[3,9,20,null,null,15,7]`, return `[[3],[20,9],[15,7]]`.

## Solution
Python Solution:
```python
from collections import deque

def zigzagLevelOrder(root):
    if not root:
        return []
    result, queue = [], deque([(root, 0)])
    while queue:
        node, level = queue.popleft()
        if len(result) == level:
            result.append([])
        if level % 2 == 0:
            result[level].append(node.val)
        else:
            result[level].insert(0, node.val)
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))
    return result
```

Step-by-step explanation:
1. If the root is null, return an empty list.
2. Initialize the result list and a queue with the root node and its level.
3. While the queue is not empty, pop a node and its level from the queue.
4. If the level is equal to the length of the result, append a new list to the result.
5. If the level is even, append the node's value to the end of the list at its level in the result. If the level is odd, insert the node's value at the beginning of the list.
6. If the node has a left child, append the left child and its level to the queue.
7. If the node has a right child, append the right child and its level to the queue.
8. Return the result.

Complexity analysis:
- Time complexity: O(n), where n is the number of nodes in the tree. This is because we are visiting each node once.
- Space complexity: O(n), because in the worst case, the queue will contain all nodes in one level of the binary tree. For a balanced binary tree, this will be the last level, which contains approximately n/2 nodes.
