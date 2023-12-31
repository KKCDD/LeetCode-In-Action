# Leetcode 0490. The Maze

## Problem Description
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.

## Solution
```python
class Solution:
    def hasPath(self, maze, start, destination):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False]*len(maze[0]) for _ in maze]
        
        def dfs(x, y):
            if [x, y] == destination:
                return True
            if visited[x][y]:
                return False
            visited[x][y] = True
            for dx, dy in directions:
                nx, ny = x, y
                while 0 <= nx+dx < len(maze) and 0 <= ny+dy < len(maze[0]) and maze[nx+dx][ny+dy] == 0:
                    nx += dx
                    ny += dy
                if dfs(nx, ny):
                    return True
            return False
        
        return dfs(*start)
```

Step-by-step Explanation: 
1. Initialize a 2D boolean array to keep track of the cells visited by the ball.
2. Define a DFS function to explore the maze. The ball keeps rolling in the current direction until it hits a wall.
3. If the ball reaches the destination, return True. If the cell has been visited before, return False.
4. For each direction, keep moving the ball until it hits a wall, then recursively call the DFS function.
5. If the DFS function returns True for any direction, return True. Otherwise, return False.
6. Call the DFS function for the start cell.

Complexity Analysis: 
- Time complexity: O(m*n), where m is the number of rows and n is the number of columns in the maze, because in the worst case we need to visit all cells.
- Space complexity: O(m*n), because we need to store the visited status for all cells.