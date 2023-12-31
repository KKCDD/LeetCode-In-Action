# Leetcode 0005. Longest Palindromic Substring

## Problem Description
Given a string `s`, find the longest palindromic substring in `s`.

## Solution
Python Solution using Two Pointers (Expand Around Center):
```python
def longestPalindrome(s):
    def expandAroundCenter(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]

    longest = ""
    for i in range(len(s)):
        # Odd length palindrome
        palindrome_odd = expandAroundCenter(s, i, i)
        # Even length palindrome
        palindrome_even = expandAroundCenter(s, i, i+1)
        longest = max(longest, palindrome_odd, palindrome_even, key=len)
    return longest
```

Step-by-step explanation:
1. We define a helper function `expandAroundCenter` that expands around the center of a palindrome and returns the longest palindromic substring.
2. We initialize an empty string `longest` to store the longest palindromic substring.
3. We iterate over the string. For each character, we consider it as the center of a palindrome and expand around it.
4. We consider both odd length and even length palindromes.
5. We update `longest` if we find a longer palindromic substring.
6. We return the longest palindromic substring.

Complexity analysis:
- Time complexity: O(n^2), where n is the length of the string. This is because for each character, we are expanding around it which takes O(n) time.
- Space complexity: O(1). This is because we are using a constant amount of space.