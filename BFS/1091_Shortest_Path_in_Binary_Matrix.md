# Leetcode 1091. Shortest Path in Binary Matrix

## Problem Description
In an N by N square grid, each cell is either empty (0) or blocked (1). A clear path from top-left to bottom-right has length k if and only if it is composed of cells C_1, C_2, ..., C_k such that:

- Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
- C_1 is at (0, 0) (ie. has value grid[0][0])
- C_k is at (N-1, N-1) (ie. has value grid[N-1][N-1])
- If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).

Return the length of the shortest such clear path from top-left to bottom-right. If such a path does not exist, return -1.

## Solution
```python
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]: return -1
        queue = deque([(0, 0, 1)])
        grid[0][0] = 1
        for i, j, d in queue:
            if i == n-1 and j == n-1: return d
            for x, y in ((i-1,j-1), (i-1,j), (i-1,j+1), (i,j-1), (i,j+1), (i+1,j-1), (i+1,j), (i+1,j+1)):
                if 0 <= x < n and 0 <= y < n and not grid[x][y]:
                    queue.append((x, y, d+1))
                    grid[x][y] = 1
        return -1
```

Step-by-step Explanation: 
1. If the start cell or the end cell is blocked, return -1 because no path exists.
2. Initialize a queue with the start cell and its distance from the start (1 at the start).
3. While the queue is not empty, pop a cell and its distance from the start.
4. If the cell is the end cell, return the distance.
5. For each of the 8 neighboring cells, if it's within the grid and not blocked, add it to the queue with the distance + 1, and mark it as visited.
6. If the end cell cannot be reached, return -1.

Complexity Analysis: 
- Time complexity: O(N^2), where N is the number of cells in the grid, because in the worst case we need to visit every cell.
- Space complexity: O(N), for the queue and the visited cells.