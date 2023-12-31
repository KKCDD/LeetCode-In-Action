# Leetcode 0130. Surrounded Regions

## Problem Description
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'. A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example, given the following board:
```
X X X X
X O O X
X X O X
X O X X
```
After running your function, the board should be:
```
X X X X
X X X X
X X X X
X O X X
```

## Solution 1
Python Solution:
```python
def solve(board):
    if not board:
        return
    rows, cols = len(board), len(board[0])
    borders = [(i, j) for i in range(rows) for j in range(cols) if i in [0, rows-1] or j in [0, cols-1]]
    while borders:
        i, j = borders.pop()
        if 0 <= i < rows and 0 <= j < cols and board[i][j] == 'O':
            board[i][j] = 'D'
            borders += (i, j-1), (i, j+1), (i-1, j), (i+1, j)
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == 'D':
                board[i][j] = 'O'
```

Step-by-step explanation:
1. If the board is empty, return.
2. Initialize a list of border cells.
3. While there are still cells in the list, pop a cell.
4. If the cell is within the board and contains an 'O', change it to 'D' and add its neighboring cells to the list.
5. Iterate over the board, change all 'O's to 'X's and all 'D's back to 'O's.

Complexity analysis:
- Time complexity: O(n), where n is the number of cells in the board. This is because we are visiting each cell once.
- Space complexity: O(n), because in the worst case, the queue will contain all cells in the board.


## Solution 2
Python code:
```python
def solve(board):
    if not board:
        return

    rows, cols = len(board), len(board[0])

    # Helper function to perform DFS
    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != 'O':
            return

        # Mark the current cell
        board[r][c] = 'D'

        # DFS in all 4 directions
        dfs(r-1, c)
        dfs(r+1, c)
        dfs(r, c-1)
        dfs(r, c+1)

    # Mark 'O's on the boundary and all connected cells
    for i in range(rows):
        dfs(i, 0)
        dfs(i, cols-1)

    for i in range(cols):
        dfs(0, i)
        dfs(rows-1, i)

    # Flip all unmarked 'O's to 'X' and revert marked cells to 'O'
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'O':
                board[r][c] = 'X'
            elif board[r][c] == 'D':
                board[r][c] = 'O'
```

Step-by-step explanation:
1. If the board is empty, return.
2. Define a helper function `dfs` to perform DFS from a given cell.
3. In the `dfs` function, if the current cell is out of bounds or is not an 'O', return. Otherwise, mark the current cell as 'D' and perform DFS on its 4 neighboring cells.
4. Perform DFS from all 'O's on the boundary of the board.
5. Iterate over the board, flip all unmarked 'O's to 'X' and revert all marked 'D's back to 'O'.

Complexity analysis:
- Time complexity: O(n), where n is the number of cells in the board. This is because we are visiting each cell once.
- Space complexity: O(n), because in the worst case, the depth of the recursive call stack can go up to n.
