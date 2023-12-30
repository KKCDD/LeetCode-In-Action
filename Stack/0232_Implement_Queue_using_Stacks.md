# Leetcode 0232. Implement Queue using Stacks

## Problem Description
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

- push(x) -- Push element x to the back of queue.
- pop() -- Removes the element from in front of queue.
- peek() -- Get the front element.
- empty() -- Return whether the queue is empty.

## Solution
Python Solution:
```python
class MyQueue:

    def __init__(self):
        # Initialize your data structure here.
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        # Push element x to the back of queue.
        self.stack1.append(x)

    def pop(self) -> int:
        # Removes the element from in front of queue and returns that element.
        self.peek()
        return self.stack2.pop()

    def peek(self) -> int:
        # Get the front element.
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self) -> bool:
        # Returns whether the queue is empty.
        return not self.stack1 and not self.stack2
```

Step-by-step explanation:
1. We maintain two stacks: stack1 for storing all the data and stack2 for reversing the order of the elements when needed.
2. When we push an element, we simply push it onto stack1.
3. When we pop an element, we first call the peek operation to ensure stack2 has the reversed elements, then we pop and return the top element from stack2.
4. The peek operation is where we reverse the elements from stack1 to stack2. If stack2 is empty, we pop each element from stack1 and push it onto stack2, effectively reversing the order of the elements.
5. The empty operation checks if both stack1 and stack2 are empty.

Complexity analysis:
- Time complexity: O(1) for the push and empty operations, and O(n) for the pop and peek operations in the worst case scenario when we have to reverse the elements. However, the amortized time complexity for pop and peek is O(1) because each element is reversed only once.
- Space complexity: O(n), where n is the number of elements pushed onto the queue. This is because we store all the elements in the two stacks.