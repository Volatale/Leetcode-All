# 142. Linked List Cycle II

# * Track the nodes we have already seen via a `visited` sett
# * If curr exists in `visited`, then a cycle exists
# *     - Thus we return `curr`
# * Otherwise, add `curr` to the set, and move onto the next node
# * If a cycle exists, eventually one of the nodes will already exist in the set
from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # * Base Case: There is no cycle
        if head is None:
            return None

        # * Track the nodes we have already visite
        visited: set[ListNode] = set()

        curr: Optional[ListNode] = head

        while curr:
            if curr in visited:
                return curr

            visited.add(curr)
            curr = curr.next

        return None


# * Time: O(n) - We have to process every element in the list in the worst case

# * Space: O(n) - The size of the set scales with the number of nodes in the input
