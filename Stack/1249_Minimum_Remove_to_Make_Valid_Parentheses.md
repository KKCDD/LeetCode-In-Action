# Leetcode 1249. Minimum Remove to Make Valid Parentheses

## Problem Description
Given a string s of '(' , ')' and lowercase English characters. Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Example:
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"

## Solution
Python Solution:
```python
def minRemoveToMakeValid(s):
    s = list(s)
    stack = []
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                s[i] = ''
    while stack:
        s[stack.pop()] = ''
    return ''.join(s)
```

Step-by-step explanation:
1. We convert the string to a list for easy modification.
2. We initialize a stack to store the indices of the open parentheses.
3. We iterate over the string. If the current character is an open parenthesis, we push its index onto the stack. If it's a close parenthesis and the stack is not empty, we pop the top index from the stack. If it's a close parenthesis and the stack is empty, we remove it from the string.
4. After iterating over the string, if there are still indices in the stack, we remove the corresponding open parentheses from the string.
5. We convert the list back to a string and return it.

Complexity analysis:
- Time complexity: O(n), where n is the length of the string. This is because we are traversing the string once.
- Space complexity: O(n), where n is the length of the string. In the worst case, we will push all the characters onto the stack.