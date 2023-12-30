# Leetcode 0350. Intersection of Two Arrays II

## Problem Description
Given two arrays, write a function to compute their intersection. Each element in the result should appear as many times as it shows in both arrays. The result can be in any order.

Example:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

## Solution
Python Solution:
```python
def intersect(nums1, nums2):
    counts = {}
    res = []

    for num in nums1:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    for num in nums2:
        if num in counts and counts[num] > 0:
            res.append(num)
            counts[num] -= 1

    return res
```

Step-by-step explanation:
1. We create a dictionary to count the occurrences of each number in the first array.
2. We then iterate over the second array, and for each number, if it is in the dictionary and its count is greater than 0, we add it to the result and decrement its count in the dictionary.

Complexity analysis:
- Time complexity: O(n + m), where n and m are the lengths of the two arrays. This is because we are traversing each array once.
- Space complexity: O(n), where n is the length of the first array. This is because we are storing the counts of the numbers in the first array in a dictionary.