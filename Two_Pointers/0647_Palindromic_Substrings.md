# Leetcode 0647. Palindromic Substrings

## Problem Description
Given a string, your task is to count how many palindromic substrings in this string. The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

For example, given `s = "abc"`, return `3` because the palindromic substrings are `"a"`, `"b"`, `"c"`.

## Solution
Python Solution:
```python
def countSubstrings(s):
    # Initialize the count of palindromic substrings
    count = 0
    # Iterate over the string
    for center in range(2*len(s) - 1):
        left = center // 2
        right = left + center % 2
        # Expand around the center and count the palindromic substrings
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
    return count
```

Step-by-step explanation:
1. We initialize the count of palindromic substrings.
2. We iterate over the string. For each character, we consider it as the center of a possible palindromic substring.
3. We expand around the center and count the palindromic substrings. We continue expanding as long as the characters on both sides are the same.

Complexity analysis:
- Time complexity: O(n^2), where n is the length of the string. This is because in the worst case, we could end up visiting each substring once and there are O(n^2) such substrings.
- Space complexity: O(1). This is because we are using a constant amount of space to store the count and the two pointers.
