# Leetcode 0283. Move Zeroes

## Problem Description
Given an array `nums`, write a function to move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

For example, given `nums = [0,1,0,3,12]`, after running your function, `nums` should be `[1,3,12,0,0]`.

## Solution
Python Solution:
```python
def moveZeroes(nums):
    # Initialize a pointer for the position of the next non-zero element
    pos = 0
    for i in range(len(nums)):
        # If the current element is not zero
        if nums[i] != 0:
            # Swap the current element with the element at the pos pointer
            nums[i], nums[pos] = nums[pos], nums[i]
            # Move the pos pointer to the right
            pos += 1
```

Step-by-step explanation:
1. We initialize a pointer `pos` for the position of the next non-zero element.
2. We iterate over the array. For each non-zero element, we swap it with the element at the `pos` pointer and move the `pos` pointer to the right.

Complexity analysis:
- Time complexity: O(n), where n is the number of elements in the array. This is because we are traversing the array once.
- Space complexity: O(1). This is because we are using a constant amount of space.