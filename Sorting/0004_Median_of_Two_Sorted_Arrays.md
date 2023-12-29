# Leetcode 4. Median of Two Sorted Arrays

## Problem Description
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Example: Input: nums1 = [1,3], nums2 = [2] Output: 2.00000 Explanation: merged array = [1,2,3] and median is 2.

Input: nums1 = [1,2], nums2 = [3,4] Output: 2.50000 Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

## Solution 1
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

## Solution 2
We can use a binary search on the smaller array to find the partition positions for both arrays. This approach reduces the time complexity to O(log(min(m, n))), where m and n are the lengths of the two arrays. Here's how you can do it:

Python Solution:
```python
def findMedianSortedArrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    x, y = len(nums1), len(nums2)
    start = 0
    end = x

    while start <= end:
        partitionX = (start + end) // 2
        partitionY = (x + y + 1) // 2 - partitionX

        maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
        minRightX = float('inf') if partitionX == x else nums1[partitionX]

        maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
        minRightY = float('inf') if partitionY == y else nums2[partitionY]

        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            if (x + y) % 2 == 0:
                return max(maxLeftX, maxLeftY) / 2.0 + min(minRightX, minRightY) / 2.0
            else:
                return max(maxLeftX, maxLeftY)
        elif maxLeftX > minRightY:
            end = partitionX - 1
        else:
            start = partitionX + 1

    raise Exception("Input arrays are not sorted")
```

Step-by-step explanation:
1. Swap nums1 and nums2 if nums1 is larger. This ensures that we always perform the binary search on the smaller array.
2. Perform a binary search on nums1 to find the partition point. The goal is to partition nums1 and nums2 such that the maximum element on the left side is less than or equal to the minimum element on the right side.
3. Calculate the median based on the partitions. If the total length of the arrays is even, the median is the average of the maximum element on the left side and the minimum element on the right side. If the total length is odd, the median is the maximum element on the left side.

Complexity analysis:
