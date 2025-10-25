# 61. Rotate List

from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


# * The easiest thing to do here is to create a circular link from the tail to the head
# * Additionally, iterating through the entire list lets us get the length of the list
# * Then, move head to where the tail of the rotated list
# * Once the head is there, we can set head.next = None (since this is the new tail)
# ! We need to make sure we have a reference to the rest of the list before doing so, however
# *     - new_head = head.next
# * It is possible that k > len(head), so we want to mod k by the length to avoid unnecessary rotations
# *     - For example, 3 % 4 is congruent to 7 % 4 and 7 % 4 is congruent to 11 % 4
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None or k <= 0:
            return head

        length: int = 1
        curr = head

        # * Iterate to the end of the entire list (get length, and create circular link)
        while curr.next:
            length += 1
            curr = curr.next

        curr.next = head  # * Create a circular link back to the head
        k = k % length  # * Removes unneeded iterations

        # * Move head to the tail of the new list
        for _ in range(length - k - 1):
            if head:
                head = head.next

        new_head = head.next  # * "new_head" is the head of the rotated linked list
        head.next = None  # * "head" now points to the tail of the new linked list
        return new_head


# * Time: O(n) - It takes O(n) to iterate through the entire list to create the circular link
# * Then, in the worst case there are n more iterations (for the rotation)

# * Space: O(1) - The memory usage remains constant regardless of the input size
