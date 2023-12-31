# Leetcode 0323. Connected Component in Undirected Graph

## Problem Description
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

Example 1:

Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]
Output: 2

Example 2:

Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
Output: 1

## Solution
```python
class Solution:
    def countComponents(self, n, edges):
        parent = list(range(n))
        
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(xy):
            x, y = map(find, xy)
            if x != y:
                parent[x] = y
                
        list(map(union, edges))
        return len(set(map(find, parent)))
```

Step-by-step Explanation: 
1. Initialize a list called parent where parent[i] is the parent of i. Initially, each node is its own parent.
2. Define a function find(x) to find the root of x. If x is not its own parent, recursively call find on its parent and update its parent to the root.
3. Define a function union(xy) to connect the two nodes in xy. Find their roots, and if they are different, make one the parent of the other.
4. Call union on each edge to connect the nodes.
5. Finally, find the root of each node and return the number of unique roots, which is the number of connected components.

Complexity Analysis: 
- Time complexity: O(n + e), where n is the number of nodes and e is the number of edges, because we perform a union operation for each edge and a find operation for each node.
- Space complexity: O(n), because we store a parent for each node.