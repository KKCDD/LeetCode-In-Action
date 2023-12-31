# Leetcode 0987. Vertical Order Traversal of a Binary Tree

## Problem Description
Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column). If two nodes are in the same row and column, the order should be from left to right.

## Solution
```python
from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def verticalTraversal(self, root):
        node_list = []

        def DFS(node, row, column):
            if node is not None:
                heappush(node_list, (column, row, node.val))
                DFS(node.left, row + 1, column - 1)
                DFS(node.right, row + 1, column + 1)

        DFS(root, 0, 0)

        res = defaultdict(list)
        while node_list:
            column, row, value = heappop(node_list)
            res[column].append(value)

        return [res[i] for i in sorted(res)]
```

Step-by-step Explanation: 
1. Define a list `node_list` to store the nodes. Each node is represented by a tuple (column, row, value).
2. Define a recursive function `DFS(node, row, column)` to traverse the tree. For each node, add a tuple (column, row, value) to `node_list`, and recursively call `DFS` for the left child with `row + 1` and `column - 1`, and for the right child with `row + 1` and `column + 1`.
3. Call `DFS(root, 0, 0)` to start the traversal from the root.
4. Sort `node_list`, and group the values by column. For each column, sort the values by row, and if two nodes are in the same row, sort them by value.
5. Return the values grouped by column, in ascending order of column.

Complexity Analysis: 
- Time complexity: O(N log N), where N is the number of nodes in the tree. We need to sort all the nodes.
- Space complexity: O(N), where N is the number of nodes in the tree. We need to store all the nodes in `node_list`.