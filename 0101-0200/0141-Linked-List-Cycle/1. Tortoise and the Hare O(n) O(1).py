# 141. Linked List Cycle

# * We can use the tortoise and the hare algorithm here
# * There are two pointers:
# *     - slow -> moves 1 step per iteration
# *     - fast -> moves 2 steps per iteration
# * If there is no cycle, then we'll simply fall out of the loop and return false
# * Otherwise, we know there is a cycle, so since fast moves at double the rate of slow
# * Mathematically, the distance between slow and fast decreases by 1 each cycle
# *     - That is, after both pointers are in the cycle)
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

        slow: Optional[ListNode] = head  # * Jumps 1 per move
        fast: Optional[ListNode] = head  # * Jumps 2 per move

        # * If a cycle exists, fast gains on slow at a rate of 1 node per cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # * Thus, if a cycle does exist, we know they'll meet at some point
            if slow == fast:
                return True

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

# * Space: O(1) - The memory usage remains constant regardless of input size
