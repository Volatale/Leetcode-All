# 83. Remove Duplicates from Sorted List

from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


# * The goal is to remove all of the duplicate nodes
# * Therefore, if curr.val == curr.next.val, curr.next should be removed from the list
# * For example:
# *     1 -> 1 -> 1 -> 2 -> 2 -> 3
# *     H
# *     C
# * curr.val == curr.next.val (both are 1)
# * So by setting curr.next = curr.next.next, the middle 1 is dropped
# *     1 -> 1 -> 2 -> 2 -> 3
# *     H
# *     C
# ! Don't move curr until curr.val != curr.next.val
# * Essetially, for each unique value `v`, remove all of the sequential duplicate nodes
# * Then move onto the next value in the linked list
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        curr = head

        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next  # * Next node is removed from list
            else:
                curr = curr.next  # * Next node is not a duplicate, so just move to it

        return head


# * Time: O(n) - We iterate over the entire linked list, so the time taken scales with the input size

# * Space: O(1) - The memory usage remains constant regardless of input size
