# Leetcode 54. Spiral Matrix

## Problem Description
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

## Solution
Python Solution:
```python
def spiralOrder(matrix):
    if not matrix:
        return []

    result = []
    top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Traverse from left to right.
        for j in range(left, right + 1):
            result.append(matrix[top][j])
        top += 1

        # Traverse downwards.
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            # Traverse from right to left.
            for j in range(right, left - 1, -1):
                result.append(matrix[bottom][j])
            bottom -= 1

        if left <= right:
            # Traverse upwards.
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result
```

Step-by-step explanation:
1. Initialize four pointers: top, bottom, left, and right. These pointers define the current layer that needs to be traversed.
2. Traverse the current layer in a spiral order: from left to right, top to bottom, right to left, and bottom to top.
3. After each traversal, update the corresponding pointer to move to the next layer.
4. Repeat the process until all layers have been traversed.

Complexity analysis:
- Time complexity: O(m * n), where m is the number of rows and n is the number of columns. This is because we are visiting each element once.
- Space complexity: O(m * n), as we are storing all elements in the result array.

Using a queue won't necessarily make the solution better for this problem. The spiral traversal of a matrix is a systematic process that doesn't require the use of a queue. A queue is typically used when the order of processing is important, such as in a breadth-first search (BFS) where we process nodes in the order they are discovered.

In the case of spiral matrix traversal, we know exactly the order in which to process the elements: left to right, top to bottom, right to left, and bottom to top. This order is determined by the current boundaries of the matrix (top, bottom, left, right), which we update as we traverse each layer.

Using a queue would add unnecessary complexity to the solution and increase the space complexity. The current solution has a space complexity of O(m * n) because we store the result. If we used a queue to store the elements before adding them to the result, the space complexity would still be O(m * n), but with an additional overhead of managing the queue.

Therefore, the current solution is more efficient and straightforward for this problem.