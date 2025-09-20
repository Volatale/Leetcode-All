# 25. Reverse Nodes in k-Group

# * The goal is to reverse linked list nodes in groups of `k`
# *     - If there is ever a situation where there aren't `k` nodes in a group, execution should exit
# * Reversing a linked list from start to finish is relatively simple
# * We need a reference to the previous node and a reference to the rest of the list (post reversal)
# * Since we need to perform multiple reversals, it makes sense to modularize the behaviour into its own function (reusability)
# ! One problem we have is that we aren't necessarily trying to reverse the entire list in one go
# * Thus, we need some sort of `limit` or boundary when it comes to knowing when to STOP the reversal
# * As we travel through the list, we need to track the tail of the previous group (which is originally a dummy node)
# * And we also need to track the limit or boundary node so we don't reverse anything that isn't part of the current group
# ! Before each reversal, the `curr` pointer will move ahead `k` nodes
# *     - If this is ever impossible, it implies there we don't have enough nodes left to create a "k-group"
# *     - Thus, we early return at this point
# * Otherwise, we pass in the "starting point" (head) of where the reversal will begin, and a limit node
# * We keep reversing until the function hits a point where curr is equal to limit (which could also be None)

from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # * Handle the case where the input is empty
        if head is None:
            return head

        # * We need something to attach the first group to
        dummy = ListNode(-1)
        dummy.next = head

        # * `prev` represents the head of the PREVIOUS group
        prev = dummy
        curr = head

        while curr:
            # * Mark the START of the group to be reversed
            group_start = prev.next

            # * Move `curr` ahead by `k` nodes (to the END of the group)
            for _ in range(k):
                # * Handle the case where there aren't `k` nodes (so we can't reverse)
                if curr is None:
                    return dummy.next

                curr = curr.next

            prev.next = self._reverse(group_start, curr)
            group_start.next = curr
            prev = group_start

        return dummy.next

    def _reverse(
        self, head: Optional[ListNode], limit: Optional[ListNode]
    ) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr is not limit:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev


# * Time: O(n) - The time taken scales both with the size of the input and with `k`
# * However, `k` is bounded by `n`, so this is not multiplicative

# * Space: O(1) - The memory usage remains constant regardless of input size
