# Leetcode 0133. Clone Graph

## Problem Description
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a value (`int`) and a list (`List[Node]`) of its neighbors.

Example:

```
Input:
{"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}

The graph looks like this:

    1---2
    |   |
    4---3

Output:
{"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}

```

There are multiple ways to solve this problem, such as using BFS or DFS.

## DFS

To deep copy the graph, you can start at the given node and traverse its neighbors using DFS, creating new nodes for each node you visit and copying over the neighbors' relationships.

Python solution using DFS:

```python
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def __init__(self):
        # Dictionary to save the visited node and its corresponding clone
        # as key and value respectively. This helps to avoid cycles.
        self.visited = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        # If the node was already visited before.
        # Return the clone from the visited dictionary.
        if node in self.visited:
            return self.visited[node]

        # Create a clone for the given node.
        # Note that we don't have cloned neighbors as of now, hence [].
        clone_node = Node(node.val, [])

        # The key is the original node and value being the clone node.
        self.visited[node] = clone_node

        # Iterate through the neighbors to generate their clones
        # and prepare a list of cloned neighbors to be added to the cloned node.
        for neighbor in node.neighbors:
            clone_node.neighbors.append(self.cloneGraph(neighbor))

        return clone_node

```

This code recursively clones nodes. Whenever a node is cloned, it's stored in the `visited` dictionary to avoid recloning and to handle cycles in the graph.

The DFS traversal ensures that every node and its relationships are copied over to the new graph.


## BFS
Using BFS (Breadth First Search) is another common approach for this problem. The idea is to start at the given node and traverse its neighbors layer by layer using a queue, creating new nodes for each node you visit and copying over the neighbor relationships.

```python
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        # Dictionary to store the visited nodes. The key is the original node
        # and the value is its clone.
        visited = {}

        # Start BFS traversal by adding the first node to the queue.
        queue = [node]
        visited[node] = Node(node.val, [])  # Clone the first node.

        while queue:
            # Pop a node from the front of the queue and visit its neighbors.
            n = queue.pop(0)

            for neighbor in n.neighbors:
                if neighbor not in visited:
                    # Clone and store in the visited dictionary.
                    visited[neighbor] = Node(neighbor.val, [])
                    # Add the neighbor to the queue to visit its neighbors later.
                    queue.append(neighbor)

                # Attach the clone of the neighbor to the current node.
                visited[n].neighbors.append(visited[neighbor])

        # Return the clone of the initial node.
        return visited[node]

```

In this approach:

1. We use a `queue` to facilitate BFS traversal.
2. We use a `visited` dictionary to keep track of nodes that have already been cloned. This helps in handling cycles in the graph and also avoids recloning nodes.
3. For each node popped from the queue, we visit its neighbors, clone them if they haven't been cloned already, and then attach the cloned neighbors to the currently cloned node.

Using BFS ensures that all nodes and their relationships are copied over to the new graph in a layer-by-layer manner.