# Leetcode 0409. Longest Palindrome

## Problem Description
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

For example, given `s = "abccccdd"`, return `7` because one longest palindrome that can be built is `"dccaccd"`, which has length 7.

## Solution
Python Solution:
```python
def longestPalindrome(s):
    # Use a dictionary to count the frequency of each character
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1

    # Initialize the length of the longest palindrome and a flag for the middle character
    length = 0
    has_odd = False
    for count in counts.values():
        # Add the number of pairs of characters to the length
        length += count // 2 * 2
        # If there is an odd number of characters, set the flag for the middle character
        if count % 2 == 1:
            has_odd = True

    # If there is a middle character, add it to the length
    if has_odd:
        length += 1

    return length
```

Step-by-step explanation:
1. We use a dictionary to count the frequency of each character in the string.
2. We initialize the length of the longest palindrome and a flag for the middle character.
3. We iterate over the counts. For each count, we add the number of pairs of characters to the length. If there is an odd number of characters, we set the flag for the middle character.
4. If there is a middle character, we add it to the length.

Complexity analysis:
- Time complexity: O(n), where n is the length of the string. This is because we are traversing the string once.
- Space complexity: O(1). This is because we are using a constant amount of space to store the counts and the flag. The number of distinct characters is bounded, so the space complexity is constant.