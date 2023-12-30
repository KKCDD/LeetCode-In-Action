# Leetcode 0162. Find Peak Element

## Problem Description
A peak element is an element that is strictly greater than its neighbors. Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks. You may imagine that nums[-1] = nums[n] = -∞. You must write an algorithm that runs in O(log n) time.

Example:
Input: nums = [1,2,3,1]
Output: 2

## Solution
Python Solution:
```python
def findPeakElement(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left
```

Step-by-step explanation:
1. We initialize two pointers, left and right, to the start and end of the array.
2. We enter a loop that continues until left is equal to right.
3. We calculate the middle index. If the middle element is less than the next element, we move the left pointer to the middle index plus 1. Otherwise, we move the right pointer to the middle index.
4. When left is equal to right, we have found a peak element, and we return its index.

Complexity analysis:
- Time complexity: O(log n), where n is the number of elements in the array. This is because we are using a binary search.
- Space complexity: O(1). This is because we are using a constant amount of space.