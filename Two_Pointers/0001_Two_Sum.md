# Leetcode 0001. Two Sum

## Problem Description
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

## Solution
Python Solution using Two Pointers:
```python
def twoSum(nums, target):
    nums = [(num, i) for i, num in enumerate(nums)]
    nums.sort()
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left][0] + nums[right][0]
        if current_sum == target:
            return [nums[left][1], nums[right][1]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
```

Step-by-step explanation:
1. We create a list of tuples where each tuple contains a number from the array and its index.
2. We sort the list of tuples.
3. We initialize two pointers, left and right, to the start and end of the sorted list.
4. We enter a loop that continues until left is less than right.
5. We calculate the sum of the numbers at the left and right pointers. If the sum is equal to the target, we return the indices of the numbers.
6. If the sum is less than the target, we move the left pointer to the right. Otherwise, we move the right pointer to the left.

Complexity analysis:
- Time complexity: O(n log n), where n is the number of elements in the array. This is because we are sorting the array.
- Space complexity: O(n). This is because we are creating a new list of tuples.

Note: This solution assumes that the input array is not sorted. If the array is sorted, we can skip the sorting step and the time complexity will be O(n).