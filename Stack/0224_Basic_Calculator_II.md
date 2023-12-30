# Leetcode 0224. Basic Calculator II

## Problem Description
Implement a basic calculator to evaluate a simple expression string. The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces.

Example:
Input: s = "1 + 1"
Output: 2

## Solution
Python Solution:
```python
def calculate(s):
    stack = []
    operand = 0
    res = 0    # For the on-going result
    sign = 1   # 1 means positive, -1 means negative  

    for ch in s:
        if ch.isdigit():
            # Forming operand, since it could be more than one digit
            operand = (operand * 10) + int(ch)
        elif ch == '+':
            # Evaluate the expression to the left
            res += sign * operand
            # Save the recently encountered '+' sign
            sign = 1
            # Reset operand
            operand = 0
        elif ch == '-':
            res += sign * operand
            sign = -1
            operand = 0
        elif ch == '(':
            # Push the result and sign on to the stack, for later
            stack.append(res)
            stack.append(sign)
            # Reset operand and result, as if new evaluation begins for the new sub-expression
            sign = 1
            res = 0
        elif ch == ')':
            # Evaluate the expression to the left
            res += sign * operand
            # ')' marks end of expression within a set of parenthesis
            # Its result is multiplied with sign on top of stack
            # as stack.pop() is the sign before the parenthesis
            res *= stack.pop()  # stack pop 1, the sign before the parenthesis
            res += stack.pop()  # stack pop 2, the result calculated before the parenthesis
            # Reset the operand
            operand = 0

    return res + sign * operand
```

Step-by-step explanation:
1. We initialize a stack, a variable to store the current operand, a variable to store the ongoing result, and a variable to store the current sign.
2. We iterate over the string. If the current character is a digit, we update the operand. If it's a '+' or '-', we update the result and the sign. If it's a '(', we push the current result and sign onto the stack and reset them. If it's a ')', we update the result and then add the result before the '(' and multiply by the sign before the '('.
3. After iterating over the string, we add the last result to the ongoing result and return it.

Complexity analysis:
- Time complexity: O(n), where n is the length of the string. This is because we are traversing the string once.
- Space complexity: O(n), where n is the length of the string. In the worst case, we will push all the characters onto the stack.