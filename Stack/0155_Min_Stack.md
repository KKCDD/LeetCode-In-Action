# Leetcode 0155. Min Stack

## Problem Description
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

- push(x) -- Push element x onto stack.
- pop() -- Removes the element on top of the stack.
- top() -- Get the top element.
- getMin() -- Retrieve the minimum element in the stack.

## Solution
Python Solution:
```python
class MinStack:

    def __init__(self):
        # Initialize data stack and min stack
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        # Push element into data stack
        self.stack.append(x)
        # If min stack is empty or x is smaller than the top element of min stack, push x into min stack
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self) -> None:
        # If the top element of data stack is the same as the top element of min stack, pop min stack
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        # Return the top element of data stack
        return self.stack[-1]

    def getMin(self) -> int:
        # Return the top element of min stack
        return self.min_stack[-1]
```

Step-by-step explanation:
1. We maintain two stacks: one for storing all the data (the data stack) and one for storing minimum values (the min stack).
2. When we push a new element onto the data stack, if the min stack is empty or the new element is smaller than or equal to the top element of the min stack, we also push it onto the min stack.
3. When we pop an element from the data stack, if it is the same as the top element of the min stack, we also pop it from the min stack.
4. The top element of the min stack is always the minimum element in the data stack.

Complexity analysis:
- Time complexity: O(1) for all operations. This is because we are using a stack for all operations, which has a time complexity of O(1).
- Space complexity: O(n), where n is the number of elements pushed onto the stack. This is because we are storing all elements in both the data stack and the min stack in the worst-case scenario.