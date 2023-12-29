# Leetcode 75. Sort Colors

## Problem Description
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue. We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

Example:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

## Solution
Python Solution:
```python
def sortColors(nums):
    # Initialize pointers for the next positions of 0 and 2
    p0 = p2 = 0
    # Initialize pointer for the current position
    p = 0

    # Iterate while the current position is less than the next position of 2
    while p <= p2:
        # If the current number is 0
        if nums[p] == 0:
            # Swap the numbers at the current position and the next position of 0
            nums[p], nums[p0] = nums[p0], nums[p]
            # Increment the next positions of 0 and the current position
            p0 += 1
            p += 1
        # If the current number is 2
        elif nums[p] == 2:
            # Swap the numbers at the current position and the next position of 2
            nums[p], nums[p2] = nums[p2], nums[p]
            # Decrement the next position of 2
            p2 -= 1
        # If the current number is 1
        else:
            # Increment the current position
            p += 1
```

Step-by-step explanation:
1. Initialize pointers for the next positions of 0 and 2 to 0, and the current position to 0.
2. Iterate while the current position is less than or equal to the next position of 2.
3. For each number, if it is 0, swap it with the number at the next position of 0 and increment the next position of 0 and the current position. If it is 2, swap it with the number at the next position of 2 and decrement the next position of 2. If it is 1, increment the current position. This effectively sorts the numbers in-place.

Complexity analysis:
- Time complexity: O(n), where n is the length of the array. This is because we are iterating over the array once.
- Space complexity: O(1), as we are not using any additional space.