# Leetcode 0016. 3Sum Closest

## Problem Description
Given an array `nums` of `n` integers and an integer `target`, find three integers in `nums` such that the sum is closest to `target`. Return the sum of the three integers.

For example, given array `nums = [-1, 2, 1, -4]`, and `target = 1`, the sum that is closest to the target is `2` (`-1 + 2 + 1 = 2`).

## Solution
Python Solution using Two Pointers:
```python
def threeSumClosest(nums, target):
    nums.sort()
    closest_sum = float('inf')
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if abs(target - current_sum) < abs(target - closest_sum):
                closest_sum = current_sum
            if current_sum < target:
                left += 1
            else:
                right -= 1
    return closest_sum
```

Step-by-step explanation:
1. We sort the array.
2. We initialize `closest_sum` to infinity.
3. We iterate over the array. For each number, we use it as the first number of the triplet and find two numbers in the remaining array that make the sum closest to the target.
4. We use two pointers, left and right, to find the two numbers. If the current sum is less than the target, we move the left pointer to the right. If the current sum is greater than or equal to the target, we move the right pointer to the left.
5. We update `closest_sum` if the absolute difference between the target and the current sum is less than the absolute difference between the target and `closest_sum`.
6. We return `closest_sum`.

Complexity analysis:
- Time complexity: O(n^2), where n is the number of elements in the array. This is because we are using two nested loops.
- Space complexity: O(n) or O(log n), depending on the implementation of the sorting algorithm. This is because we are storing the sorted array.