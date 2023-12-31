# Leetcode 0104. Maximum Depth of Binary Tree

## Problem Description
Given the root of a binary tree, return its maximum depth. A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

## Solution
```python
class Solution:
    def maxDepth(self, root):
        if root is None: 
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) + 1
```

Step-by-step Explanation: 
1. If the tree is empty (root is None), its height is 0.
2. Otherwise, compute the height of each subtree, which is the maximum depth of the left subtree and the right subtree.
3. The height of the tree is the maximum height of the subtrees plus 1 (for the root node).

Complexity Analysis: 
- Time complexity: O(n), where n is the number of nodes in the tree, because we are visiting each node once.
- Space complexity: O(height of the tree), because in the worst case, that's the maximum number of recursive calls that will be placed on the stack.