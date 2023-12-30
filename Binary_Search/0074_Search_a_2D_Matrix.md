# Leetcode 0074. Search a 2D Matrix

## Problem Description
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
- Integers in each row are sorted from left to right.
- The first integer of each row is greater than the last integer of the previous row.

Example:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

## Solution
Python Solution:
```python
def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1

    while left <= right:
        mid = (left + right) // 2
        mid_value = matrix[mid // cols][mid % cols]

        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1

    return False
```

Step-by-step explanation:
1. We check if the matrix is empty. If it is, we return False.
2. We calculate the number of rows and columns in the matrix.
3. We initialize two pointers, left and right, to the start and end of the matrix.
4. We enter a loop that continues until left is greater than right.
5. We calculate the middle index and the value at the middle index. If the middle value is the target, we return True.
6. If the middle value is less than the target, we move the left pointer to the middle index plus 1. Otherwise, we move the right pointer to the middle index minus 1.
7. If we exit the loop without finding the target, we return False.

Complexity analysis:
- Time complexity: O(log(mn)), where m is the number of rows and n is the number of columns in the matrix. This is because we are using a binary search.
- Space complexity: O(1). This is because we are using a constant amount of space.