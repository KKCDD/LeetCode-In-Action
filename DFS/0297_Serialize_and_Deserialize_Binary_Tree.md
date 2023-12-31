# Leetcode 0297. Serialize and Deserialize Binary Tree

## Problem Description
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"

## Solution
Python Solution:
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def dfs(node):
            if node:
                vals.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
            else:
                vals.append('#')
        vals = []
        dfs(root)
        return ' '.join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def dfs():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
        vals = iter(data.split())
        return dfs()
```

Step-by-step explanation:
1. For serialization, we perform a depth-first traversal of the tree. We record each node's value and use '#' to denote a null pointer. We join all the values and null pointers into a string with spaces as separators.
2. For deserialization, we split the string by spaces to get an iterator of values. We then build the tree by reading from the iterator: if the current value is not '#', we create a node with the current value and recursively construct the left and right subtrees; otherwise, we return a null pointer.

Complexity analysis:
- Time complexity: O(n) for both serialization and deserialization, where n is the number of nodes in the tree, because we visit each node exactly once.
- Space complexity: O(n) for both serialization and deserialization, because in the worst case (when the tree is skewed), the depth of the recursive call stack can be n.