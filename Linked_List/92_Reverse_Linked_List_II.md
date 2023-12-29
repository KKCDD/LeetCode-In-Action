# Leetcode 92. Reverse Linked List II

## Problem Description
Reverse a linked list from position m to n. Do it in one-pass. Note: 1 ≤ m ≤ n ≤ length of list.

Example:
Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL

## Solution
Python Solution:
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def reverseBetween(head, m, n):
    # Create a dummy node to mark the head of this list
    dummy = ListNode(0)
    dummy.next = head

    # Make a pointer pre as a marker for the node before reversing
    pre = dummy
    for _ in range(m - 1):
        pre = pre.next

    # A pointer to the beginning of a sub-list that will be reversed
    start = pre.next

    # A pointer to a node that will be reversed
    then = start.next

    # Reverse the sub-list
    for _ in range(n - m):
        start.next = then.next
        then.next = pre.next
        pre.next = then
        then = start.next

    return dummy.next
```

Step-by-step explanation:
1. Create a dummy node to mark the head of the list.
2. Make a pointer pre as a marker for the node before reversing.
3. A pointer start is a pointer to the beginning of the sub-list that will be reversed.
4. A pointer then is a pointer to a node that will be reversed.
5. Reverse the sub-list.
6. Return the new head.

Complexity analysis:
- Time complexity: O(n), where n is the length of the list. This is because we are iterating over the list once.
- Space complexity: O(1), as we are not using any additional space.