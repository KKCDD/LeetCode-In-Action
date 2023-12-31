# Leetcode 0951. Flip Equivalent Binary Trees

## Problem Description
For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees. A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations. Write a function that determines whether two binary trees are flip equivalent. The trees are given by root nodes root1 and root2.

## Solution
```python
class Solution:
    def flipEquiv(self, root1, root2):
        if root1 is root2:
            return True
        if not root1 or not root2 or root1.val != root2.val:
            return False

        return (self.flipEquiv(root1.left, root2.left) and
                self.flipEquiv(root1.right, root2.right) or
                self.flipEquiv(root1.left, root2.right) and
                self.flipEquiv(root1.right, root2.left))
```

Step-by-step Explanation: 
1. If both trees are empty, they are flip equivalent.
2. If one of them is empty, or the roots have different values, they are not flip equivalent.
3. Otherwise, the two trees are flip equivalent if and only if one of the following conditions is true:
   - The left subtrees and the right subtrees are flip equivalent.
   - The left subtree of the first tree is flip equivalent to the right subtree of the second tree, and the right subtree of the first tree is flip equivalent to the left subtree of the second tree.

Complexity Analysis: 
- Time complexity: O(min(n1, n2)), where n1 and n2 are the sizes of the two trees. We process each node at most once.
- Space complexity: O(min(h1, h2)), where h1 and h2 are the heights of the two trees. The space is used for the recursion stack. In the worst case, the tree is completely unbalanced, e.g., each node has only left child node, the recursion call would occur N times (the height of the tree), therefore the storage to keep the call stack would be O(N). But in the best case (the tree is completely balanced), the height of the tree would be log(N). Hence, the space complexity in this case would be O(log(N)).