# Leetcode 0314. Binary Tree Vertical Order Traversal

## Problem Description
LeetCode 314: Binary Tree Vertical Order Traversal

Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

For example, given the following binary tree:

    3
   /\
  9  20
     /\
    15 7

The output should be:

[
  [9],
  [3,15],
  [20],
  [7]
]

## Solution
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict, deque

class Solution:
    def verticalOrder(self, root):
        if not root:
            return []
        
        columnTable = defaultdict(list)
        min_column = max_column = 0
        queue = deque([(root, 0)])
        
        while queue:
            node, column = queue.popleft()
            
            if node is not None:
                columnTable[column].append(node.val)
                min_column = min(min_column, column)
                max_column = max(max_column, column)

                queue.append((node.left, column - 1))
                queue.append((node.right, column + 1))
        
        return [columnTable[x] for x in range(min_column, max_column + 1)]
```

Step-by-step Explanation:
1. We use a breadth-first search (BFS) to traverse the tree, keeping track of the column index for each node.
2. We use a dictionary to store the nodes for each column. The keys in the dictionary are the column indices, and the values are lists of nodes in each column.
3. We also keep track of the minimum and maximum column indices encountered during the traversal.
4. After the traversal, we return the nodes column by column, from the minimum column index to the maximum column index.

Complexity Analysis:
- Time complexity: O(n), where n is the number of nodes in the tree, because we visit each node exactly once.
- Space complexity: O(n), because we need to store the nodes in the columnTable dictionary and the queue.