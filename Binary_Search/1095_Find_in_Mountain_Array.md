# Leetcode 1095. Find in Mountain Array

## Problem Description
You are given an integer array `mountainArr` where:
- `mountainArr.length >= 3`
- There exists some index `i` (0-indexed) with `mountainArr[i] < mountainArr[i + 1]` and `mountainArr[i] > mountainArr[i - 1]`.
- There exists some index `j` (0-indexed) with `mountainArr[j] > mountainArr[j + 1]` and `mountainArr[j] > mountainArr[j - 1]`.
- `mountainArr[i]` and `mountainArr[j]` are the peak of the mountain, and `i < j`.
- `mountainArr` is strictly increasing in the range `[0, i]`, and strictly decreasing in the range `[i, mountainArr.length - 1]`.

You are also given these three APIs:
- `def get(self, index: int) -> int`
- `def length(self) -> int`
- `def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int`

You should return the index in the array such that `mountainArr.get(index) == target`. If such an index doesn't exist, return `-1`.

You may not directly access the `mountainArr` array.

## Solution
Python Solution:
```python
class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        left, right = 0, mountainArr.length() - 1
        while left < right:
            mid = (left + right) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                left = mid + 1
            else:
                right = mid
        peak = left
        left, right = 0, peak
        while left <= right:
            mid = (left + right) // 2
            if mountainArr.get(mid) < target:
                left = mid + 1
            elif mountainArr.get(mid) > target:
                right = mid - 1
            else:
                return mid
        left, right = peak, mountainArr.length() - 1
        while left <= right:
            mid = (left + right) // 2
            if mountainArr.get(mid) > target:
                left = mid + 1
            elif mountainArr.get(mid) < target:
                right = mid - 1
            else:
                return mid
        return -1
```

Step-by-step explanation:
1. We first find the peak of the mountain using binary search.
2. Then we perform a binary search in the increasing part of the mountain.
3. If the target is not found, we perform a binary search in the decreasing part of the mountain.
4. If the target is still not found, we return -1.

Complexity analysis:
- Time complexity: O(log n), where n is the length of the mountain. This is because we are using a binary search.
- Space complexity: O(1). This is because we are using a constant amount of space.