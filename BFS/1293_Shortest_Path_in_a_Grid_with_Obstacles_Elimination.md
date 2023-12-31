# Leetcode 1293. Shortest Path in a Grid with Obstacles Elimination

## Problem Description
LeetCode 1293: Shortest Path in a Grid with Obstacles Elimination

Given a m * n grid, where each cell is either 0 (empty) or 1 (obstacle). In one step, you can move up, down, left or right from and to an empty cell.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m-1, n-1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.

## Solution
```python
from collections import deque

class Solution:
    def shortestPath(self, grid, k):
        # Get the dimensions of the grid
        m, n = len(grid), len(grid[0])
        
        # If the grid has only one cell, return 0 because no step is needed.
        if m == n == 1: return 0
        
        # If the number of obstacles k is larger than or equal to m + n - 2, 
        # return m + n - 2 because we can eliminate all obstacles and walk straight to the end.
        if k >= m + n - 2: return m + n - 2
        
        # Initialize a queue with the start cell, the number of obstacles that can be eliminated, 
        # and the number of steps taken so far (0 at the start).
        queue = deque([(0, 0, k, 0)])
        
        # Initialize a visited dictionary to keep track of the maximum number of obstacles 
        # that can be eliminated when reaching each cell.
        visited = {(0, 0): k}
        
        # While the queue is not empty, pop a cell, the number of obstacles that can be eliminated, 
        # and the number of steps taken to reach it.
        while queue:
            x, y, k, steps = queue.popleft()
            
            # For each neighboring cell
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                
                # If it's within the grid
                if 0 <= nx < m and 0 <= ny < n:
                    # Calculate the new number of obstacles that can be eliminated after moving to it
                    new_k = k - grid[nx][ny]
                    
                    # If the new number of obstacles that can be eliminated is negative, skip this cell
                    if new_k < 0: continue
                    
                    # If the cell is the end cell, return the number of steps + 1
                    if (nx, ny) == (m - 1, n - 1): return steps + 1
                    
                    # If the cell has not been visited before or the new number of obstacles that can be eliminated 
                    # is larger than the current number, update the visited dictionary and add the cell to the queue
                    if (nx, ny) not in visited or new_k > visited[(nx, ny)]:
                        visited[(nx, ny)] = new_k
                        queue.append((nx, ny, new_k, steps + 1))
        
        # If the end cell cannot be reached, return -1
        return -1
```
This solution uses a breadth-first search (BFS) algorithm to find the shortest path from the start cell to the end cell, while keeping track of the maximum number of obstacles that can be eliminated when reaching each cell. The BFS algorithm ensures that the shortest path is found first. The visited dictionary is used to avoid visiting the same cell multiple times with the same or a smaller number of obstacles that can be eliminated, which reduces the time complexity.

Step-by-step Explanation: 
1. If the grid has only one cell, return 0 because no step is needed.
2. If the number of obstacles k is larger than or equal to m + n - 2, return m + n - 2 because we can eliminate all obstacles and walk straight to the end.
3. Initialize a queue with the start cell, the number of obstacles that can be eliminated, and the number of steps taken so far (0 at the start).
4. Initialize a visited dictionary to keep track of the maximum number of obstacles that can be eliminated when reaching each cell.
5. While the queue is not empty, pop a cell, the number of obstacles that can be eliminated, and the number of steps taken to reach it.
6. For each neighboring cell, if it's within the grid and the number of obstacles that can be eliminated is non-negative after moving to it, add it to the queue with the new number of obstacles that can be eliminated and the number of steps + 1, and update the visited dictionary.
7. If the end cell cannot be reached, return -1.

Complexity Analysis: 
- Time complexity: O(m*n*k), where m and n are the number of rows and columns in the grid, and k is the number of obstacles that can be eliminated, because in the worst case we need to visit every cell with every possible number of obstacles that can be eliminated.
- Space complexity: O(m*n*k), for the queue and the visited dictionary.

