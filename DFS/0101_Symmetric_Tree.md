# Leetcode 0101. Symmetric Tree

## Problem Description
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

## Solution
```python
class Solution:
    def isSymmetric(self, root):
        def isMirror(t1, t2):
            if t1 is None and t2 is None: return True
            if t1 is None or t2 is None: return False
            return (t1.val == t2.val) and isMirror(t1.right, t2.left) and isMirror(t1.left, t2.right)

        return isMirror(root, root)
```

Step-by-step Explanation: 
1. Define a helper function `isMirror` that takes two trees and checks if they are mirror of each other.
2. If both trees are empty, they are mirror of each other.
3. If only one of the trees is empty, they are not mirror of each other.
4. Two trees are mirror of each other if: the two root nodes have the same value, and the right subtree of each tree is a mirror of the left subtree of the other tree.
5. Call the `isMirror` function with the root of the given tree as both arguments.

Complexity Analysis: 
- Time complexity: O(n), where n is the number of nodes in the tree, because we are visiting each node once.
- Space complexity: O(n), in the worst case, we might have to hold all nodes in the call stack if the tree is skewed.