# Leetcode 0073. Set Matrix Zeroes

## Problem Description
Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

## Solution
Python Solution:
```python
def setZeroes(matrix):
    rows, cols = len(matrix), len(matrix[0])
    row_zero = col_zero = False

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                if i == 0:
                    row_zero = True
                if j == 0:
                    col_zero = True
                matrix[i][0] = matrix[0][j] = 0

    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    if row_zero:
        for j in range(cols):
            matrix[0][j] = 0

    if col_zero:
        for i in range(rows):
            matrix[i][0] = 0
```

Step-by-step explanation:
1. We first check if the first row or the first column has any zeros, and we store this information.
2. Then we use the first row and the first column to mark the rows and columns that should be set to zero.
3. We then iterate over the rest of the matrix and set a cell to zero if its row or column is marked to be zeroed.
4. Finally, we zero out the first row and the first column if they were originally supposed to be zeroed.

Complexity analysis:
- Time complexity: O(m*n), where m is the number of rows and n is the number of columns in the matrix. This is because we are traversing the entire matrix twice.
- Space complexity: O(1), as we are not using any extra space that scales with the size of the input.