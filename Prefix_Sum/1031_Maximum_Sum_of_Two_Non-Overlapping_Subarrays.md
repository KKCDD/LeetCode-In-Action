# Leetcode 1031. Maximum Sum of Two Non-Overlapping Subarrays

## Problem Description
Given an array A of non-negative integers, return the maximum sum of elements in two non-overlapping (contiguous) subarrays, which have lengths L and M. (For clarification, the L-length subarray could occur before or after the M-length subarray.)

## Solution
```python
class Solution:
    def maxSumTwoNoOverlap(self, A, L, M):
        for i in range(1, len(A)):
            A[i] += A[i - 1]
        res, Lmax, Mmax = A[L + M - 1], A[L - 1], A[M - 1]
        for i in range(L + M, len(A)):
            Lmax = max(Lmax, A[i - M] - A[i - L - M])
            Mmax = max(Mmax, A[i - L] - A[i - L - M])
            res = max(res, Lmax + A[i] - A[i - M], Mmax + A[i] - A[i - L])
        return res
```

Step-by-step Explanation: 
1. Convert A into a prefix sum array.
2. Initialize the result `res` to be the sum of the first L + M numbers.
3. Initialize `Lmax` and `Mmax` to be the sum of the first L and M numbers respectively.
4. Slide the window towards the right by one step each time. Update `Lmax` and `Mmax` to be the maximum sum of the L-length and M-length subarray respectively.
5. Update the result by comparing it with the sum of the current L-length subarray and the maximum M-length subarray, and the sum of the current M-length subarray and the maximum L-length subarray.

Complexity Analysis: 
- Time complexity: O(n), where n is the length of the array. We need to iterate through the array once.
- Space complexity: O(1), because we only use a constant amount of space to store the variables `res`, `Lmax`, and `Mmax`.