# Leetcode 0053. Maximum Subarray

## Problem Description
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: The contiguous subarray with the largest sum is [4, -1, 2, 1], and its sum is 6.

## Solution
```python
class Solution:
    def maxSubArray(self, nums):
        if not nums:
            return 0

        cur_sum = max_sum = nums[0]

        for num in nums[1:]:
            cur_sum = max(num, cur_sum + num)
            max_sum = max(max_sum, cur_sum)

        return max_sum
```

Step-by-step Explanation: 
1. If the list is empty, return 0.
2. Initialize `cur_sum` and `max_sum` with the first number in the list.
3. For each number in the list starting from the second number:
   - Update `cur_sum` with the maximum of the current number and the sum of the current number and the previous `cur_sum`.
   - Update `max_sum` with the maximum of `max_sum` and `cur_sum`.
4. Return `max_sum`, which is the maximum sum of a contiguous subarray.

Complexity Analysis: 
- Time complexity: O(n), where n is the length of the list. We need to iterate through the list once.
- Space complexity: O(1), because we only use a constant amount of space to store the variables `cur_sum` and `max_sum`.