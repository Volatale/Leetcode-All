# 19. Remove Nth Node From End of List

# * We need to remove the nth node from the END of the list
# *     - In other words, if n = 1, we remove the last
# *     - If n = 2, then we remove the second from the last
# *     - If the length of the list is 5, and n = 5, we remove the head
# ! Instead of getting the length of the list, we can apply fast and slow pointers
# * The `fast`` pointer should be "n" nodes ahead of `slow``
# * Then, by the time that "fast" is unable to move, slow will be at the perfect node
# * In which case, we can simply perform the removal
# ! Why does this work? Because "fast" is being used as the boundary
# *     - If `fast` is not None, then we know accessing `slow.next.next` won't cause an error
# * `fast` is used SOLELY to avoid needing to get the length of the linked list

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

        # * Fast and slow pointers to avoid getting the list length
        slow = dummy
        fast = dummy

        # * Move `fast` n nodes ahead of slow
        for _ in range(n):
            if fast is None:
                return None

            fast = fast.next

        # * Move both pointers ahead
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next

        # * Slow now points to the n-1th node, and fast points to the n+1th node
        slow.next = slow.next.next

        return dummy.next


# * Time: O(n) - The time taken scales with the size of the input

# * Space: O(1) - The memory usage remains constant regardless of input size
