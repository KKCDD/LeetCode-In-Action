# Leetcode 160. Intersection of Two Linked Lists

## Problem Description
Problem Description:
Write a program to find the node at which the intersection of two singly linked lists begins. If the two linked lists have no intersection at all, return null.

Example:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.

## Solution
Python Solution:
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def getIntersectionNode(headA, headB):
    # Initialize two pointers to the heads of the lists
    pA, pB = headA, headB

    # Iterate while the two pointers do not meet
    while pA != pB:
        # Move each pointer to the next node in its list, or to the head of the other list if it reaches the end
        pA = pA.next if pA else headB
        pB = pB.next if pB else headA

    # Return the intersection node, or null if there is no intersection
    return pA
```

Step-by-step explanation:
1. Initialize two pointers, pA and pB, to the heads of the lists.
2. Iterate while the two pointers do not meet.
3. For each iteration, move each pointer to the next node in its list, or to the head of the other list if it reaches the end. This ensures that each pointer traverses both lists, so they will meet at the intersection node if there is one.
4. Return the intersection node, or null if there is no intersection.

Complexity analysis:
- Time complexity: O(n + m), where n and m are the lengths of the lists. This is because each pointer traverses both lists.
- Space complexity: O(1), as we are only using two pointers.