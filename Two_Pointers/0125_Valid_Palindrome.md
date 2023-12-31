# Leetcode 0125. Valid Palindrome

## Problem Description
Given a string `s`, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example, `"A man, a plan, a canal: Panama"` is a palindrome. `"race a car"` is not a palindrome.

## Solution 1
Python Solution:
```python
def isPalindrome(s):
    s = ''.join(ch for ch in s if ch.isalnum()).lower()
    return s == s[::-1]
```

Step-by-step explanation:
1. We remove all non-alphanumeric characters from the string and convert it to lowercase.
2. We check if the string is the same when reversed. If it is, the string is a palindrome.

Complexity analysis:
- Time complexity: O(n), where n is the length of the string. This is because we are traversing the string once.
- Space complexity: O(n). This is because we are storing the cleaned string.

## Solution 2
Python Solution using Two Pointers:
```python
def isPalindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left, right = left + 1, right - 1
    return True
```

Step-by-step explanation:
1. We initialize two pointers, left and right, to the start and end of the string respectively.
2. We move the left pointer to the right until we find an alphanumeric character or until it meets the right pointer.
3. We move the right pointer to the left until we find an alphanumeric character or until it meets the left pointer.
4. We compare the characters at the left and right pointers. If they are not the same, the string is not a palindrome.
5. We move the left pointer to the right and the right pointer to the left and repeat the process until the pointers meet.
6. If all pairs of characters are the same, the string is a palindrome.

Complexity analysis:
- Time complexity: O(n), where n is the length of the string. This is because we are traversing the string once.
- Space complexity: O(1). This is because we are not using any extra space that scales with the size of the input string.