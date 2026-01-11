# 141. Linked List Cycle

# * Track which nodes we have already visited
# * After we visit a new node, add it to the visited set
# * If we ever revisit the same node (i.e. it exists in the visited set); we know a cycle exists
# * Otherwise, if no cycle exists, we fall out of the loop and thus no cycle exists
from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # * An empty linked list has no cycle
        if head is None:
            return False

        # * Tracks the nodes we have already seen
        visited: set[ListNode] = set()
        curr: Optional[ListNode] = head

        while curr:
            if curr in visited:
                return True

            visited.add(curr)
            curr = curr.next

        return False


head: Optional[ListNode] = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next  # * Links to 2

sol: Solution = Solution()
print(sol.hasCycle(head))  # * True
print(sol.hasCycle(None))  # * False

# * Time: O(n) - We need to process every node in the input (and possibly one extra in the case of a cycle)

# * Space: O(n) - In the worst case(s), the `visited` set's size scales proportionally with the input size
