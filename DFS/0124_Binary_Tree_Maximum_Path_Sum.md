# Leetcode 0124. Binary Tree Maximum Path Sum

## Problem Description
Given a non-empty binary tree, find the maximum path sum. For this problem, a path is defined as any node sequence from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

## Solution
```python
class Solution:
    def maxPathSum(self, root):
        self.max_sum = float('-inf')
        self.max_gain(root)
        return self.max_sum

    def max_gain(self, node):
        if not node:
            return 0

        # compute the maximum path sum that each child of node can contribute to the path
        left_gain = max(self.max_gain(node.left), 0)
        right_gain = max(self.max_gain(node.right), 0)

        # the price to start a new path where `node` is the highest node
        price_newpath = node.val + left_gain + right_gain

        # update max_sum if it's better to start a new path
        self.max_sum = max(self.max_sum, price_newpath)

        # for recursion, return the max gain the node and one of its subtrees could contribute to the max path
        return node.val + max(left_gain, right_gain)
```

Step-by-step Explanation: 
1. Initialize `max_sum` as the smallest possible integer.
2. Call the recursive helper function `max_gain(node)` with the root node.
3. If the node is null, the maximum gain is 0.
4. Call `max_gain` for the node's left child and right child to compute the maximum path sum that each child can contribute to the path. If the child's maximum gain is negative, we should ignore the child and set its contribution to 0.
5. Check the price of a new path which starts at the left child, moves up to the node and then down to the right child.
6. Update `max_sum` with the maximum of `max_sum` and the price of the new path.
7. For the recursion return the maximum gain the node could add to the maximum path: it's either the node's value + the gain of the left child, or the node's value + the gain of the right child, depending on which child contributes more to the path.

Complexity Analysis: 
- Time complexity: O(N), where N is number of nodes, since we visit each node not more than 2 times.
- Space complexity: O(log(N)), in the worst case when the tree is completely unbalanced, e.g. each node has only left child node, we would keep all NN nodes in the recursion call stack. However, in the best case (the tree is completely balanced), the height of the tree would be log(N). Hence, the space complexity in this case would be O(log(N)).