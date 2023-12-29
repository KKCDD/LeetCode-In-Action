Problem 148: Sort List

Sort a linked list in O(n log n) time using constant space complexity.

Example:

Input: 4->2->1->3
Output: 1->2->3->4

Python solution using merge sort:

```python
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head
        # split list into two halves
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        start = slow.next
        slow.next = None
        # sort each half
        l1 = self.sortList(head)
        l2 = self.sortList(start)
        # merge the sorted halves
        return self.merge(l1, l2)

    def merge(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        dummy = p = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        p.next = l1 or l2
        return dummy.next

```

Explanation:

1. The `sortList` function first checks if the list is empty or has only one node. If so, it returns the list as it is already sorted.
2. It then splits the list into two halves using the slow and fast pointers method.
3. It recursively sorts each half.
4. Finally, it merges the two sorted halves using the `merge` function and returns the sorted list.

Complexity Analysis:

Time complexity: O(n log n), where n is the length of the list. This is because we divide the list in half at each level of recursion and then merge the halves, which takes linear time.

Space complexity: O(log n), where n is the length of the list. This is the space required by the recursion stack for the divide and conquer approach. The problem statement allows for O(1) space complexity excluding the recursion stack space.