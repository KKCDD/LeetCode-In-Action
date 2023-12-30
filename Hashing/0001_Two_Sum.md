# Leetcode 0001. Two Sum

## Problem Description
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

## Solution
Python Solution:
```python
def twoSum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []
```

Step-by-step explanation:
1. We create a dictionary to store the numbers in the array and their indices.
2. For each number, we calculate the complement (target - number).
3. If the complement is in the dictionary, we return the indices of the number and its complement.
4. If the complement is not in the dictionary, we add the number and its index to the dictionary.
5. If we don't find any two numbers that add up to the target, we return an empty list.

Complexity analysis:
- Time complexity: O(n), where n is the number of elements in the array. This is because we are traversing the array once.
- Space complexity: O(n), as we are storing all elements in the dictionary.
