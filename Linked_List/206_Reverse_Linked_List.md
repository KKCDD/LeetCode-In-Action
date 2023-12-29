# Leetcode 206. Reverse Linked List

## Problem Description
Problem Description:
Reverse a singly linked list.

Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

## Solution
Python Solution:
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def reverseList(head):
    # Initialize the previous and current nodes
    prev, curr = None, head

    # Iterate while the current node is not null
    while curr:
        # Store the next node
        next_node = curr.next
        # Reverse the link
        curr.next = prev
        # Move the previous and current nodes one step forward
        prev, curr = curr, next_node

    # The new head is the previous node
    return prev
```

Step-by-step explanation:
1. Initialize the previous node to null and the current node to the head of the list.
2. Iterate while the current node is not null.
3. For each iteration, store the next node, reverse the link from the current node to the previous node, and move the previous and current nodes one step forward.
4. After all nodes have been visited, the previous node will be the new head of the reversed list, so return it.

Complexity analysis:
- Time complexity: O(n), where n is the number of nodes in the list. This is because we are iterating over the list once.
- Space complexity: O(1), as we are only using a constant amount of space.