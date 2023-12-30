# Leetcode 0150. Evaluate Reverse Polish Notation

## Problem Description
Evaluate the value of an arithmetic expression in Reverse Polish Notation. Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Example:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

## Solution
Python Solution:
```python
def evalRPN(tokens):
    stack = []
    operators = {
        "+": lambda y, x: x + y,
        "-": lambda y, x: x - y,
        "*": lambda y, x: x * y,
        "/": lambda y, x: int(x / y)  # need int for python division
    }

    for token in tokens:
        if token in operators:
            stack.append(operators[token](stack.pop(), stack.pop()))
        else:
            stack.append(int(token))

    return stack[0]
```

Step-by-step explanation:
1. We initialize a stack and a dictionary to map each operator to its corresponding operation.
2. We iterate over the tokens. If the current token is an operator, we pop the top two elements from the stack, perform the operation, and push the result back onto the stack.
3. If the current token is a number, we push it onto the stack.
4. After iterating over all the tokens, the final result is on the top of the stack.

Complexity analysis:
- Time complexity: O(n), where n is the number of tokens. This is because we are traversing the tokens once.
- Space complexity: O(n), where n is the number of tokens. In the worst case, we will push all the tokens onto the stack.