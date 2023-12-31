# Leetcode 0417. Pacific Atlantic Water Flow

## Problem Description
Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

## Solution
```python
class Solution:
    def pacificAtlantic(self, matrix):
        if not matrix: return []
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        m, n = len(matrix), len(matrix[0])
        p_visited = [[False for _ in range(n)] for _ in range(m)]
        a_visited = [[False for _ in range(n)] for _ in range(m)]
        
        def dfs(visited, x, y):
            visited[x][y] = True
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if new_x < 0 or new_y < 0 or new_x >= m or new_y >= n or visited[new_x][new_y] or matrix[new_x][new_y] < matrix[x][y]:
                    continue
                dfs(visited, new_x, new_y)
        
        for i in range(m):
            dfs(p_visited, i, 0)
            dfs(a_visited, i, n-1)
        for j in range(n):
            dfs(p_visited, 0, j)
            dfs(a_visited, m-1, j)
        
        return [[i, j] for i in range(m) for j in range(n) if p_visited[i][j] and a_visited[i][j]]
```

Step-by-step Explanation: 
1. Initialize two 2D boolean arrays to keep track of the cells visited by the water from the Pacific and Atlantic oceans.
2. Define a DFS function to mark the cells that can be reached by the water.
3. Run the DFS for each cell on the borders of the matrix.
4. Finally, return the cells that can be reached by the water from both oceans.

Complexity Analysis: 
- Time complexity: O(m*n), where m is the number of rows and n is the number of columns in the matrix, because in the worst case we need to visit all cells.
- Space complexity: O(m*n), because we need to store the visited status for all cells.