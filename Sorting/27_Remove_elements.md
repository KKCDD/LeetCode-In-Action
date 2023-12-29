# Leetcode 27. Remove elements

## Problem Description
Given an array nums and a value val, remove all instances of that value in-place and return the new length. Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory. The order of elements can be changed.

Example:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2]
Explanation: Your function should return length = 2, with the first two elements of nums being 2. It doesn't matter what you leave beyond the returned length.

## Solution
Python Solution:
```python
def removeElement(nums, val):
    # Initialize the index of the first occurrence of the value
    index = 0

    # Iterate over the array
    for num in nums:
        # If the current number is not the value
        if num != val:
            # Replace the number at the index with the current number
            nums[index] = num
            # Increment the index
            index += 1

    # Return the new length of the array
    return index
```

Step-by-step explanation:
1. Initialize the index of the first occurrence of the value to 0.
2. Iterate over the array.
3. For each number, if it is not the value, replace the number at the index with the current number and increment the index. This effectively removes all instances of the value from the array.
4. Return the new length of the array, which is the value of the index.

Complexity analysis:
- Time complexity: O(n), where n is the length of the array. This is because we are iterating over the array once.
- Space complexity: O(1), as we are not using any additional space.