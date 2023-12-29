# Leetcode 141. Linked List Cycle

## Problem Description
Given head, the head of a linked list, determine if the linked list has a cycle in it. There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter. Return true if there is a cycle in the linked list. Otherwise, return false.

Example:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

## Solution
Python Solution:
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def hasCycle(head):
    # Initialize two pointers, one moves one step at a time, the other moves two steps at a time
    slow = fast = head

    # Iterate while both pointers are not null and the fast pointer can still move forward
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        # If the two pointers meet, there is a cycle
        if slow == fast:
            return True

    # If the fast pointer reaches the end of the list, there is no cycle
    return False
```

Step-by-step explanation:
1. Initialize two pointers, slow and fast, to the head of the list.
2. Iterate while both pointers are not null and the fast pointer can still move forward.
3. For each iteration, move the slow pointer one step forward and the fast pointer two steps forward.
4. If the two pointers meet, there is a cycle in the list, so return true.
5. If the fast pointer reaches the end of the list, there is no cycle in the list, so return false.

Complexity analysis:
- Time complexity: O(n), where n is the number of nodes in the list. In the worst case, we need to traverse all the nodes in the list.
- Space complexity: O(1), as we are only using two pointers.