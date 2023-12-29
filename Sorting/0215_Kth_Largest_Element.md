# Leetcode 215. Kth Largest Element

## Problem Description
Problem Description:
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example:
Input: [3,2,1,5,6,4] and k = 2
Output: 5

## Solution
Python Solution:
```python
def findKthLargest(nums, k):
    # Sort the array in descending order
    nums.sort(reverse=True)

    # Return the kth largest element
    return nums[k - 1]
```

Step-by-step explanation:
1. Sort the array in descending order. This ensures that the largest element is at the beginning of the array and the smallest element is at the end.
2. Return the kth largest element, which is at index k - 1 because array indices start at 0.

Complexity analysis:
- Time complexity: O(n log n), where n is the number of elements in the array. This is because we are sorting the array, which takes O(n log n) time in the worst case.
- Space complexity: O(1), as we are not using any additional space. Note that the space used by the sort method is not counted towards the space complexity.