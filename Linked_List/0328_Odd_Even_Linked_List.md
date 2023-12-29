# Leetcode 328. Odd Even Linked List

## Problem Description
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes. You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL

## Solution
Python Solution:
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def oddEvenList(head):
    # If the list is empty or has only one node, return it
    if not head or not head.next:
        return head

    # Initialize the heads of the odd and even lists
    odd = head
    even = head.next
    even_head = even

    # Iterate while there are still nodes in the list
    while even and even.next:
        # Link the odd nodes together
        odd.next = even.next
        odd = odd.next
        # Link the even nodes together
        even.next = odd.next
        even = even.next

    # Link the odd list to the even list
    odd.next = even_head

    return head
```

Step-by-step explanation:
1. If the list is empty or has only one node, return it.
2. Initialize the heads of the odd and even lists to the first and second nodes of the list, respectively.
3. Iterate while there are still nodes in the list.
4. For each iteration, link the odd nodes together and link the even nodes together.
5. After all nodes have been visited, link the odd list to the even list.
6. Return the head of the odd list, which is the new head of the list.

Complexity analysis:
- Time complexity: O(n), where n is the number of nodes in the list. This is because we are iterating over the list once.
- Space complexity: O(1), as we are only using a constant amount of space.