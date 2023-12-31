# Leetcode 0105. Construct Binary Tree from Preorder and Inorder Traversal

## Problem Description
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

## Solution
```python
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        if inorder:
            index = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[index])
            root.left = self.buildTree(preorder, inorder[0:index])
            root.right = self.buildTree(preorder, inorder[index+1:])
            return root
```

Step-by-step Explanation: 
1. If inorder is empty, return None.
2. Pop the first element of preorder, which is the root of the current tree.
3. Find the index of the root in inorder.
4. Create a new tree node with the root value.
5. Recursively build the left subtree with the elements in preorder and the elements in inorder before the root.
6. Recursively build the right subtree with the elements in preorder and the elements in inorder after the root.
7. Return the root node of the tree.

Complexity Analysis: 
- Time complexity: O(n^2), where n is the number of nodes in the tree. This is because for each node we are finding its index in the inorder array.
- Space complexity: O(n), where n is the number of nodes in the tree. This is the space required to store the binary tree.