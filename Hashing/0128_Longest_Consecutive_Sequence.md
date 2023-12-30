# Leetcode 0128. Longest Consecutive Sequence

## Problem Description
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

Example:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

## Solution
Python Solution:
```python
def longestConsecutive(nums):
    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak
```

Step-by-step explanation:
1. We convert the array into a set for efficient lookups.
2. We iterate over each number in the set. If the number is the start of a sequence (i.e., num - 1 is not in the set), we try to extend the sequence as far as possible.
3. For each sequence, we keep track of the longest sequence we've seen so far.

Complexity analysis:
- Time complexity: O(n), where n is the number of elements in the array. This is because we are traversing the array once to create the set, and then traversing the set once to find the longest sequence.
- Space complexity: O(n), as we are storing all elements in the set.