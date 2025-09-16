# 21. Merge Two Sorted Lists

# * We are given the heads of two sorted linked lists
# * The goal is to merge the two linked lists into one (while still being sorted)
# * The easiest thing to do is create a dummy node and attach the other nodes to it
# *     - This will be the only node we create
# *


from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # * Handles the case where both lists are empty
        if list1 is None and list2 is None:
            return None

        # * We need to attach the input nodes to this node
        dummy: ListNode = ListNode(-1)
        curr: ListNode = dummy

        # * Handle the merging
        left: Optional[ListNode] = list1
        right: Optional[ListNode] = list2

        while left and right:
            if left.val <= right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next

            curr = curr.next

        # * Handle the leftovers
        if left:
            curr.next = left

        if right:
            curr.next = right

        # * Return the head of the merged list
        return dummy.next


# * Time: O(n + m) - The time taken scales with the lengths of both input lists

# * Space: O(1) - The memory usage remains constant regardless of input size
# * We only ever create 1 node (the dummy node)
