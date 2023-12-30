# Leetcode 0348. Design Tic-Tac-Toe

## Problem Description
Design a Tic-tac-toe game that is played between two players on a n x n grid.

You may assume the following rules:
- A move is guaranteed to be valid and is placed on an empty block.
- Once a winning condition is reached, no more moves are allowed.
- A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.

## Solution
Python Solution:
```python
class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = 0
        self.anti_diagonal = 0

    def move(self, row: int, col: int, player: int) -> int:
        toAdd = 1 if player == 1 else -1

        self.rows[row] += toAdd
        self.cols[col] += toAdd
        if row == col:
            self.diagonal += toAdd
        if col == self.n - row - 1:
            self.anti_diagonal += toAdd

        if abs(self.rows[row]) == self.n or abs(self.cols[col]) == self.n or abs(self.diagonal) == self.n or abs(self.anti_diagonal) == self.n:
            return player

        return 0
```

Step-by-step explanation:
1. We initialize the game with n rows and n columns, and two diagonals.
2. Each player is represented by a unique integer (1 for Player 1 and -1 for Player 2), and each move by a player increments or decrements the count in the corresponding row, column, and possibly one or both diagonals.
3. After each move, we check if the absolute value of the count in the current row, column, or any diagonal is equal to n, which means the current player has won.

Complexity analysis:
- Time complexity: O(1) for both the constructor and the move operation. This is because we are simply updating and checking a fixed number of variables.
- Space complexity: O(n), where n is the size of the board. This is because we are storing the counts for each row and column.