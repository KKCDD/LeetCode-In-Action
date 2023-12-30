# Leetcode 1209. Remove All Adjacent Duplicates in String II

## Problem Description
Given a string s, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them causing the left and the right side of the deleted substring to concatenate together. We repeatedly make k duplicate removals on s until we no longer can. Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

Example:
Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation: 
First, we delete "eee" and "ccc", getting "ddbbdaa"
Then we delete "bbb" and "ddd", getting "aa"

## Solution
Python Solution:
```python
def removeDuplicates(s, k):
    stack = [['#', 0]]
    for c in s:
        if stack[-1][0] == c:
            stack[-1][1] += 1
            if stack[-1][1] == k:
                stack.pop()
        else:
            stack.append([c, 1])
    return ''.join(c * k for c, k in stack)
```

Step-by-step explanation:
1. We initialize a stack with a dummy element.
2. We iterate over the string. If the current character is the same as the top character in the stack, we increment the count of the top element in the stack. If the count becomes k, we pop the top element from the stack.
3. If the current character is different from the top character in the stack, we push the current character and 1 onto the stack.
4. After iterating over the string, we convert the stack into a string and return it.

Complexity analysis:
- Time complexity: O(n), where n is the length of the string. This is because we are traversing the string once.
- Space complexity: O(n), where n is the length of the string. In the worst case, we will push all the characters onto the stack.