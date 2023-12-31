# Leetcode 0543. Diameter of Binary Tree

## Problem Description
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

## Solution
```python
class Solution:
    def diameterOfBinaryTree(self, root):
        self.ans = 1
        def depth(node):
            if not node: return 0
            L = depth(node.left)
            R = depth(node.right)
            self.ans = max(self.ans, L+R+1)
            return max(L, R) + 1

        depth(root)
        return self.ans - 1
```

Step-by-step Explanation: 
1. Initialize the diameter `ans` as 1.
2. Define a recursive function `depth(node)` that calculates the depth of a node.
3. If the node is null, its depth is 0.
4. Otherwise, calculate the depth of the left child and the right child.
5. Update the diameter `ans` with the maximum of its current value and the sum of the depths of the left and right children plus 1.
6. Return the depth of the node, which is the maximum depth of its children plus 1.
7. Call `depth(root)` to calculate the depth of the root and update the diameter.
8. Return `ans - 1` because the diameter is the number of edges, which is one less than the number of nodes.

Complexity Analysis: 
- Time complexity: O(n), where n is the number of nodes in the tree, because we are visiting each node once.
- Space complexity: O(h), where h is the height of the tree. This space is used for the recursion stack. In the worst case, the tree is completely unbalanced, e.g., each node has only left child node, the recursion call would occur N times (the height of the tree), therefore the storage to keep the call stack would be O(N). But in the best case (the tree is completely balanced), the height of the tree would be log(N). Hence, the space complexity in this case would be O(log(N)).