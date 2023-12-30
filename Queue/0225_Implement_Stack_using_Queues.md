# Leetcode 225. Implement Stack using Queues

## Problem Description
Implement the following operations of a stack using queues.

- push(x) -- Push element x onto stack.
- pop() -- Removes the element on top of the stack.
- top() -- Get the top element.
- empty() -- Return whether the stack is empty.

## Solution
Python Solution:
```python
from collections import deque

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.queue
```

Step-by-step explanation:
1. We use a single Python deque to simulate a stack. Python's deque is implemented as a doubly-linked list which provides O(1) time complexity for append and popleft operations.
2. When we push an element onto the "stack", we first add it to the end of the queue, then we move all elements that were in the queue before the pushed element to the end of the queue.
3. To pop an element, we simply popleft from the queue.
4. The top element is always at the front of the queue.
5. To check if the stack is empty, we check if the queue is empty.

Complexity analysis:
- Time complexity: O(1) for pop, top, and empty operations, and O(n) for push operation, where n is the number of elements in the stack.
- Space complexity: O(n), where n is the number of elements in the stack.