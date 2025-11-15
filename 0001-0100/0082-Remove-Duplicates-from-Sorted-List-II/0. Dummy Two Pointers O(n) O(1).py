# 82. Remove Duplicates from Sorted List II


from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None) -> None:
        self.val = val
        self.next = next


# * There are two cases:
# *     - curr has a duplicate
# *     - curr does not have a duplicate
# * In the case of the former, we need to iterate to the END of the duplicate sequence
# * In the case of the latter, it doesn't really matter since we'll already be at the end
# * Then, we check if prev.next is curr
# *     - If it is, then we know curr doesn't have any duplicates
# *       The reason being that curr would be further ahead if it
# * Else, then we have to remove all the duplicates from the list
# *     -
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # * Handle null head and single element list
        if head is None or head.next is None:
            return head

        # * We need a dummy incase the current head has a duplicate
        dummy = ListNode(-1)
        dummy.next = head

        curr = head  # * Travels through to the end of each duplicate node sequence
        prev = dummy  # * Non-duplicate nodes are attached to this node

        while curr:
            # * Move curr to the end of the duplicate sequence
            while curr.next and curr.val == curr.next.val:
                curr = curr.next

                # * Case 1: prev.next points to curr, which means no duplicate of curr was found
                if prev.next is curr:
                    prev = prev.next
                # * Case 2: curr has duplicates, so skip all the nodes with that value
                else:
                    prev.next = curr.next

        return dummy.next


# * Time: O(n) - We have to iterate over the entire linked list

# * Space: O(1) - The memory usage remains constant regardless of input size
