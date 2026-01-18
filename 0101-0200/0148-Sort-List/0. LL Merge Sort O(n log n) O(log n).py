# 148. Sort List

# * Use merge sort, but on linked lists instead
# * Fast and slow pointers can be used to split the linked list up into two
# *     - Do this at every level of recursion (divide and conquer)
from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode] = None) -> Optional[ListNode]:
        # * Base Case
        if head is None or head.next is None:
            return head

        # * Split the list in half
        prev: Optional[ListNode] = None
        slow: Optional[ListNode] = head
        fast: Optional[ListNode] = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # * Detach the first half's tail from the second's head
        prev.next = None

        left = self.sortList(head)
        right = self.sortList(slow)

        return self.merge(left, right)

    def merge(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy: ListNode = ListNode(-1)
        curr: Optional[ListNode] = dummy

        left: Optional[ListNode] = l1
        right: Optional[ListNode] = l2

        # * Merge the lists
        while left and right:
            if left.val <= right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next

            curr = curr.next

        # * Collect any leftovers
        if left:
            curr.next = left
        if right:
            curr.next = right

        return dummy.next


# * Time: O(n log n) - It takes O(n / 2) per linked list split, and O(n) time to merge in the worst case
# * We do both of these at every level of recursion

# * Space: O(log n) - The maximum recursion depth scales with the number of times we can halve the linked list
# * Mathematically, that is logarithmic with respect to base 2 (8 -> 4 -> 2 -> 1). log2(8) = 3 splits
