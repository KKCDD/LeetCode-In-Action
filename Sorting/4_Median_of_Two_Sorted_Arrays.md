# Leetcode 4. Median of Two Sorted Arrays

## Problem Description
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Example: Input: nums1 = [1,3], nums2 = [2] Output: 2.00000 Explanation: merged array = [1,2,3] and median is 2.

Input: nums1 = [1,2], nums2 = [3,4] Output: 2.50000 Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

## Solution
```python
def findMedianSortedArrays(nums1, nums2):
    # Combine the two lists and sort them
    nums = sorted(nums1 + nums2)

    # Calculate the length of the combined list
    length = len(nums)

    # If the length is even, the median is the average of the two middle numbers
    if length % 2 == 0:
        return (nums[length // 2] + nums[length // 2 - 1]) / 2

    # If the length is odd, the median is the middle number
    else:
        return nums[length // 2]
```

Step-by-step explanation:
1. Combine the two input lists and sort the combined list. This ensures that the numbers are in ascending order.
2. Calculate the length of the combined list.
3. If the length is even, the median is the average of the two middle numbers. This is because a list with an even number of elements has two middle numbers.
4. If the length is odd, the median is the middle number. This is because a list with an odd number of elements has one middle number.
5. Return the median.

Complexity analysis:
- Time complexity: O((n+m) log (n+m)) where n and m are the lengths of the two input lists. This is because we are sorting the combined list, which has n+m elements.
- Space complexity: O(n+m) because we are storing the combined list.