# Leetcode 0236. Lowest Common Ancestor of a Binary Tree

## Problem Description
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree. According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

## Solution
```python
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left:
            return right
        elif not right:
            return left
        else:
            return root
```

Step-by-step Explanation: 
1. If the root is None or the root is either p or q, return the root.
2. Recursively call the function for the left and right subtrees.
3. If both left and right are not None, then one node is in the left subtree and the other is in the right, so root is the LCA.
4. If left is None and right is not None, return right because that means the LCA is in the right subtree.
5. If right is None and left is not None, return left because that means the LCA is in the left subtree.
6. If both are None, return None.

Complexity Analysis: 
- Time complexity: O(n), where n is the number of nodes in the tree, because we are visiting each node once.
- Space complexity: O(h), where h is the height of the tree. This space is used for the recursion stack. In the worst case, the tree is completely unbalanced, e.g., each node has only left child node, the recursion call would occur N times (the height of the tree), therefore the storage to keep the call stack would be O(N). But in the best case (the tree is completely balanced), the height of the tree would be log(N). Hence, the space complexity in this case would be O(log(N)).