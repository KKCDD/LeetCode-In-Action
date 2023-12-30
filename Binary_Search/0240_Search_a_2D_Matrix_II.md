# Leetcode 0240. Search a 2D Matrix II

## Problem Description
Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:
- Integers in each row are sorted in ascending from left to right.
- Integers in each column are sorted in ascending from top to bottom.

Example:
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true

## Solution
Python Solution:
```python
def searchMatrix(matrix, target):
    if not matrix:
        return False

    row, col = 0, len(matrix[0]) - 1

    while row < len(matrix) and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            row += 1
        else:
            col -= 1

    return False
```

Step-by-step explanation:
1. We check if the matrix is empty. If it is, we return False.
2. We initialize two pointers, row and col, to the top-right corner of the matrix.
3. We enter a loop that continues until row is equal to the number of rows or col is less than 0.
4. If the current element is the target, we return True.
5. If the current element is less than the target, we move down to the next row. Otherwise, we move left to the previous column.
6. If we exit the loop without finding the target, we return False.

Complexity analysis:
- Time complexity: O(m + n), where m is the number of rows and n is the number of columns in the matrix. This is because in the worst case, we might have to traverse the matrix from the top-right corner to the bottom-left corner.
- Space complexity: O(1). This is because we are using a constant amount of space.