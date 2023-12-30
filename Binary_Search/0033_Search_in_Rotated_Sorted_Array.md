# Leetcode 0033. Search in Rotated Sorted Array

## Problem Description
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand. You are given a target value to search. If found in the array return its index, otherwise return -1. You may assume no duplicate exists in the array. Your algorithm's runtime complexity must be in the order of O(log n).

Example:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

## Solution
Python Solution:
```python
def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] >= nums[left]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
```

Step-by-step explanation:
1. We initialize two pointers, left and right, to the start and end of the array.
2. We enter a loop that continues until left is greater than right.
3. We calculate the middle index. If the middle element is the target, we return the middle index.
4. If the middle element is greater than or equal to the left element, the left half is sorted. If the target is in the left half, we move the right pointer to the middle index minus 1. Otherwise, we move the left pointer to the middle index plus 1.
5. If the middle element is less than the left element, the right half is sorted. If the target is in the right half, we move the left pointer to the middle index plus 1. Otherwise, we move the right pointer to the middle index minus 1.
6. If we exit the loop without finding the target, we return -1.

Complexity analysis:
- Time complexity: O(log n), where n is the number of elements in the array. This is because we are using a binary search.
- Space complexity: O(1). This is because we are using a constant amount of space.