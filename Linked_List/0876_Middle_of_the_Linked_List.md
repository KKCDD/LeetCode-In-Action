# Leetcode 876. Middle of the Linked List

## Problem Description
Given a non-empty, singly linked list with head node head, return a middle node of linked list. If there are two middle nodes, return the second middle node.

Example:
Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
Explanation: The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).

## Solution
Python Solution:
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def middleNode(head):
    # Initialize two pointers, one moves one step at a time, the other moves two steps at a time
    slow = fast = head

    # Iterate while the fast pointer can still move forward
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # The slow pointer is at the middle node
    return slow
```

Step-by-step explanation:
1. Initialize two pointers, slow and fast, to the head of the list.
2. Iterate while the fast pointer can still move forward.
3. For each iteration, move the slow pointer one step forward and the fast pointer two steps forward.
4. When the fast pointer reaches the end of the list, the slow pointer will be at the middle node, so return it.

Complexity analysis:
- Time complexity: O(n), where n is the number of nodes in the list. This is because we are iterating over the list once.
- Space complexity: O(1), as we are only using two pointers.