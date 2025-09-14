# 19. Remove Nth Node From End of List

# * We need to remove the nth node from the END of the list
# *     - In other words, if n = 1, we remove the last
# *     - If n = 2, then we remove the second from the last
# *     - If the length of the list is 5, and n = 5, we remove the head
# * If we get the length of the list, then we know the bounds of the list
# * We need a pointer that points to the node BEFORE the nth node
# *     - After which, we can grab nth.next.next to get the rest of the list
# *     - n-1th.next = nth.next

from __future__ import annotations
from typing import Optional


class ListNode[int]:
    def __init__(self, val: int = 0, next: Optional[ListNode[int]] = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(
        self, head: Optional[ListNode[int]], n: int
    ) -> Optional[ListNode[int]]:
        if head is None:
            return head

        # * We may have to remove the head node
        dummy = ListNode(-1)
        dummy.next = head

        curr = head

        # * Calculate the length of the list
        length: int = 0
        count: int = 0

        while curr is not None:
            length += 1
            curr = curr.next

        curr = dummy

        # * Find the n-1th node (the one BEFORE the nth)
        while count < length - n and curr is not None:
            curr = curr.next
            count += 1

        curr.next = curr.next.next
        return dummy.next


# * Time: O(n) - The time taken scales with the size of the input

# * Space: O(1) - The memory usage remains constant regardless of input size
