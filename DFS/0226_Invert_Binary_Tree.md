# Leetcode 0226. Invert Binary Tree

## Problem Description
Invert a binary tree.

## Solution
```python
class Solution:
    def invertTree(self, root):
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root
```

Step-by-step Explanation: 
1. If the root is None (i.e., the tree is empty), the inverted tree is also empty.
2. Otherwise, invert the left and right subtrees recursively.
3. Then swap the left and right subtrees of the root.
4. Return the root of the inverted tree.

Complexity Analysis: 
- Time complexity: O(n), where n is the number of nodes in the tree, because we are visiting each node once.
- Space complexity: O(h), where h is the height of the tree. This space is used for the recursion stack. In the worst case, the tree is completely unbalanced, e.g., each node has only left child node, the recursion call would occur N times (the height of the tree), therefore the storage to keep the call stack would be O(N). But in the best case (the tree is completely balanced), the height of the tree would be log(N). Hence, the space complexity in this case would be O(log(N)).