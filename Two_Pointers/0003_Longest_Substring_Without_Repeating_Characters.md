# Leetcode 0003. Longest Substring Without Repeating Characters

## Problem Description
Given a string s, find the length of the longest substring without repeating characters.

## Solution
```python
class Solution:
    def lengthOfLongestSubstring(self, s):
        used_chars = {}
        start = max_length = 0

        for i, char in enumerate(s):
            if char in used_chars and start <= used_chars[char]:
                start = used_chars[char] + 1
            else:
                max_length = max(max_length, i - start + 1)

            used_chars[char] = i

        return max_length
```

Step-by-step Explanation: 
1. Initialize an empty dictionary `used_chars` to store the characters in the string and their indices.
2. Initialize two variables `start` and `max_length` to 0. `start` is the starting index of the current substring, and `max_length` is the length of the longest substring without repeating characters.
3. Iterate through the string. For each character, if it is in `used_chars` and its index is greater than or equal to `start`, update `start` to be the index of the character in `used_chars` plus 1. Otherwise, update `max_length` to be the maximum of `max_length` and the length of the current substring.
4. Update `used_chars` with the current character and its index.
5. After the loop, return `max_length`.

Complexity Analysis: 
- Time complexity: O(n), where n is the length of the string. We need to iterate through the string once.
- Space complexity: O(min(n, m)), where n is the length of the string and m is the size of the character set. In the worst case, all the characters in the string are different and we need to store them all in the dictionary.