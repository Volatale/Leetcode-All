# 160. Intersection of Two Linked Lists

from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, x: int = 0, next: Optional[ListNode] = None) -> None:
        self.x = x
        self.next = next


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        currA: Optional[ListNode] = headA
        currB: Optional[ListNode] = headB

        # * Track the nodes we have already visited
        visited: set[ListNode] = set()

        # * Iterate through headA to record the nodes
        while currA:
            visited.add(currA)
            currA = currA.next

        # * Now iterate through headB - if currB in visited, we have an intersection
        while currB:
            if currB in visited:
                return currB

            currB = currB.next

        # * There is no intersection
        return None


# * Time: O(n + m) - In the worst case there is no intersection, so we iterate over both lists entirely

# * Space: O(n) - The `visited` set's size scales with the size of `headA`
