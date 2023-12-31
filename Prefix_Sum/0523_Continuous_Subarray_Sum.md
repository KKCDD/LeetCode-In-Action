# Leetcode 0523. Continuous Subarray Sum

## Problem Description
Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to a multiple of k, that is, sums up to n*k where n is also an integer.

## Solution
```python
class Solution:
    def checkSubarraySum(self, nums, k):
        if len(nums) < 2:
            return False

        # Map of running sum % k -> index
        mod_map = {0: -1}
        running_sum = 0

        for i, num in enumerate(nums):
            running_sum += num
            if k != 0:  # Avoid division by zero
                running_sum %= k
            if running_sum in mod_map:
                if i - mod_map[running_sum] > 1:
                    return True
            else:
                mod_map[running_sum] = i

        return False
```

Step-by-step Explanation: 
1. If the list has less than 2 numbers, return False.
2. Initialize a map `mod_map` to store the remainder of the running sum divided by `k` and its corresponding index. The initial value is `{0: -1}` to handle the case where the entire list is a valid subarray.
3. Initialize a variable `running_sum` to store the running sum of the numbers.
4. For each number in the list, add it to `running_sum`. If `k` is not zero, take the remainder of `running_sum` divided by `k`.
5. If the remainder is in `mod_map` and the distance between the current index and the index in `mod_map` is greater than 1, return True.
6. If the remainder is not in `mod_map`, add it to `mod_map` with the current index.
7. If no valid subarray is found, return False.

Complexity Analysis: 
- Time complexity: O(n), where n is the length of the list. We need to iterate through the list once.
- Space complexity: O(min(n, k)), where n is the length of the list and k is the target integer. In the worst case, all the running sum remainders are different and we need to store them all in the map.