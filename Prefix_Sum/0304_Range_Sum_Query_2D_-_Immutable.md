# Leetcode 0304. Range Sum Query 2D - Immutable

## Problem Description
Given a 2D matrix matrix, handle multiple queries of the following type: Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

## Solution
```python
class NumMatrix:

    def __init__(self, matrix):
        if not matrix:
            return
        self.dp = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                self.dp[r + 1][c + 1] = self.dp[r + 1][c] + self.dp[r][c + 1] - self.dp[r][c] + matrix[r][c]

    def sumRegion(self, row1, col1, row2, col2):
        return self.dp[row2 + 1][col2 + 1] - self.dp[row1][col2 + 1] - self.dp[row2 + 1][col1] + self.dp[row1][col1]
```

Step-by-step Explanation: 
1. In the `__init__` method, create a 2D list `dp` with the same dimensions as `matrix`, but with an extra row and column of zeros at the top and left. Then, for each cell in `matrix`, calculate the sum of the values in the rectangle from the top-left corner of `matrix` to this cell, and store it in the corresponding cell in `dp`.
2. In the `sumRegion` method, calculate the sum of the values in the rectangle from `(row1, col1)` to `(row2, col2)` by subtracting the sum of the values in the rectangles from the top-left corner to `(row1 - 1, col2)`, `(row2, col1 - 1)`, and `(row1 - 1, col1 - 1)` from the sum of the values in the rectangle from the top-left corner to `(row2, col2)`.

Complexity Analysis: 
- Time complexity: O(1) per query, O(mn) precomputation time. Here, m and n are the number of rows and columns in the matrix.
- Space complexity: O(mn), where m and n are the number of rows and columns in the matrix. We need to store the cumulative sums in a 2D list.