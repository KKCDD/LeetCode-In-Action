# Leetcode 0200. Number of Islands



## Problem Description
Given a 2D grid map of `'1'`s (land) and `'0'`s (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Input:

```
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

```

Output: `1`

## DFS
A simple way to approach this problem is by using DFS (Depth First Search). Whenever a land cell (`'1'`) is found, traverse all its connected land cells to mark them as visited, thereby ensuring that each distinct group of connected land cells is counted as one island.

Here's how the solution works:

1. Iterate over each cell in the grid.
2. If the current cell is a land (`'1'`), increase the island count and start a DFS traversal from that cell to mark all its connected land cells.
3. During the DFS traversal, ensure to mark the visited land cells to avoid repeated traversal.

Here's a possible Python code:

```python
def numIslands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    islands = 0

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
            return
        grid[r][c] = '0'  # Mark the cell as visited
        # Explore 4 directions: up, down, left, right
        dfs(r-1, c)
        dfs(r+1, c)
        dfs(r, c-1)
        dfs(r, c+1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':  # Found an island
                islands += 1
                dfs(r, c)

    return islands

```

- For each land cell encountered, we start the DFS process. The DFS function (`dfs`) is defined to explore all connected land cells and mark them as visited.
- We only count the number of starting points of DFS as islands since all connected cells are treated as one island.

## BFS

BFS (Breadth First Search) can also be applied to solve the "Number of Islands" problem. Using BFS, we would use a queue to traverse all the adjacent land cells of a given cell, instead of using recursion like in DFS.

Here's how the solution with BFS would work:

1. Iterate over each cell in the grid.
2. If the current cell is land (`'1'`), increase the island count and start a BFS traversal from that cell to mark all its connected land cells.
3. Use a queue to help in BFS traversal. Enqueue the starting land cell and then continue to enqueue its adjacent land cells, marking them as visited in the process.

Here's a Python code using BFS:

```python
from collections import deque

def numIslands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    islands = 0

    # Define possible directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':  # Found an island
                islands += 1
                queue = deque([(r, c)])
                grid[r][c] = '0'  # Mark the cell as visited

                # BFS traversal
                while queue:
                    row, col = queue.popleft()
                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                            queue.append((nr, nc))
                            grid[nr][nc] = '0'  # Mark the cell as visited

    return islands

```

- Similar to the DFS approach, we start the BFS traversal for each unvisited land cell encountered. However, in BFS, instead of using recursion, we use a queue to help traverse all connected cells.
- The queue starts with the current land cell, and then we continue to enqueue all unvisited adjacent land cells, marking them as visited in the process.
- The BFS traversal continues until the queue is empty, which means all the connected land cells have been visited.
- We count the number of BFS traversals as the number of islands.