# Leetcode 0020. Valid Parentheses

## Problem Description
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.

Example:
Input: s = "{[]}"
Output: true

## Solution
Python Solution:
```python
def isValid(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)

    return not stack
```

Step-by-step explanation:
1. We initialize a stack and a dictionary to map each closing bracket to its corresponding opening bracket.
2. We iterate over the string. If the current character is a closing bracket, we check if the top of the stack is the corresponding opening bracket. If it's not, the string is not valid.
3. If the current character is an opening bracket, we push it onto the stack.
4. After iterating over the string, if the stack is empty, the string is valid. Otherwise, it's not valid.

Complexity analysis:
- Time complexity: O(n), where n is the length of the string. This is because we are traversing the string once.
- Space complexity: O(n), where n is the length of the string. In the worst case, we will push all the characters onto the stack.