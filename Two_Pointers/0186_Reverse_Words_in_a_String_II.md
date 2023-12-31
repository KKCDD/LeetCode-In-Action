# Leetcode 0186. Reverse Words in a String II

## Problem Description
Given an input string, reverse the string word by word. A word is defined as a sequence of non-space characters.

The input string does not contain leading or trailing spaces and the words are always separated by a single space.

For example, given `s = "the sky is blue"`, return `"blue is sky the"`.

## Solution 1
Python Solution:
```python
def reverseWords(s):
    # Split the string into words
    words = s.split(' ')
    # Reverse the list of words
    words.reverse()
    # Join the words back into a string with spaces in between
    return ' '.join(words)
```

Step-by-step explanation:
1. We split the string into words using the `split` method. This gives us a list of words.
2. We reverse the list of words using the `reverse` method.
3. We join the words back into a string with spaces in between using the `join` method.

Complexity analysis:
- Time complexity: O(n), where n is the length of the string. This is because we are traversing the string twice, once to split it into words and once to join the words back into a string.
- Space complexity: O(n). This is because we are storing the list of words.

## Solution 2
Python Solution using Two Pointers:
```python
def reverseWords(s):
    # Convert string to list to use two-pointer technique
    s = list(s)
    # Reverse the whole string
    s.reverse()
    # Initialize pointers
    i = j = 0
    for i in range(len(s)):
        # Find the end of the word
        if s[i] == ' ':
            # Reverse the word
            s[j:i] = reversed(s[j:i])
            # Move the pointer to the next word
            j = i + 1
    # Reverse the last word
    s[j:] = reversed(s[j:])
    # Convert list back to string
    return ''.join(s)
```

Step-by-step explanation:
1. We convert the string to a list to use the two-pointer technique.
2. We reverse the whole list.
3. We initialize two pointers, i and j, to the start of the list.
4. We iterate over the list. For each space character, we reverse the word before it and move the j pointer to the start of the next word.
5. After the loop, we reverse the last word.
6. We convert the list back to a string and return it.

Complexity analysis:
- Time complexity: O(n), where n is the length of the string. This is because we are traversing the string twice, once to reverse it and once to reverse the words.
- Space complexity: O(n). This is because we are storing the list.