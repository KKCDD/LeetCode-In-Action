# Leetcode 0034. Find First and Last Position of Element in Sorted Array

## Problem Description
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value. If target is not found in the array, return [-1, -1]. You must write an algorithm with O(log n) runtime complexity.

Example:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

## Solution
Python Solution:
```python
def searchRange(nums, target):
    def findFirst(nums, target):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target: left = mid + 1
            else: right = mid
        return left if nums[left] == target else -1

    def findLast(nums, target):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2 + 1
            if nums[mid] > target: right = mid - 1
            else: left = mid
        return left if nums[left] == target else -1

    return [findFirst(nums, target), findLast(nums, target)]
```

Step-by-step explanation:
1. We define two functions, findFirst and findLast, to find the first and last occurrence of the target in the array.
2. In findFirst, we perform a binary search. If the middle element is less than the target, we move the left pointer to the middle index plus 1. Otherwise, we move the right pointer to the middle index. If we find the target, we return the left pointer. Otherwise, we return -1.
3. In findLast, we perform a binary search. If the middle element is greater than the target, we move the right pointer to the middle index minus 1. Otherwise, we move the left pointer to the middle index. If we find the target, we return the left pointer. Otherwise, we return -1.
4. We call findFirst and findLast and return their results as a list.

Complexity analysis:
- Time complexity: O(log n), where n is the number of elements in the array. This is because we are using a binary search.
- Space complexity: O(1). This is because we are using a constant amount of space.