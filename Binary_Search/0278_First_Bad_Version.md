# Leetcode 0278. First Bad Version

## Problem Description
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad. Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad. You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

## Solution
Python Solution:
```python
def firstBadVersion(n):
    left, right = 1, n
    while left < right:
        mid = (left + right) // 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1
    return left
```

Step-by-step explanation:
1. We initialize two pointers, left and right, to the start and end of the version range.
2. We enter a loop that continues until left is equal to right.
3. We calculate the middle version. If the middle version is bad, we move the right pointer to the middle version. Otherwise, we move the left pointer to the middle version plus 1.
4. When left is equal to right, we have found the first bad version, and we return its number.

Complexity analysis:
- Time complexity: O(log n), where n is the number of versions. This is because we are using a binary search.
- Space complexity: O(1). This is because we are using a constant amount of space.

Note: The function `isBadVersion` is a placeholder and is assumed to be provided in the problem context.