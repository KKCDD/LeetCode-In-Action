# Leetcode 0167. Two Sum II - Input array is sorted

## Problem Description
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

For example, given array `numbers = [2, 7, 11, 15]`, and `target = 9`, the output should be `[1, 2]` because `numbers[0] + numbers[1] = 2 + 7 = 9`.

## Solution
Python Solution using Two Pointers:
```python
def twoSum(numbers, target):
    # Initialize two pointers at the beginning and end of the array
    left, right = 0, len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            # Indices are not zero-based in the problem statement
            return [left + 1, right + 1]
        elif current_sum < target:
            # If current sum is less than target, move left pointer to the right
            left += 1
        else:
            # If current sum is greater than target, move right pointer to the left
            right -= 1
```

Step-by-step explanation:
1. We initialize two pointers, left and right, to the start and end of the array respectively.
2. We enter a loop that continues until left is less than right.
3. We calculate the current sum as the sum of the numbers at the left and right pointers.
4. If the current sum is equal to the target, we return the indices of the numbers. We add 1 to the indices because the problem statement specifies that the indices are not zero-based.
5. If the current sum is less than the target, we move the left pointer to the right. If the current sum is greater than the target, we move the right pointer to the left.

Complexity analysis:
- Time complexity: O(n), where n is the number of elements in the array. This is because we are traversing the array once.
- Space complexity: O(1). This is because we are using a constant amount of space.