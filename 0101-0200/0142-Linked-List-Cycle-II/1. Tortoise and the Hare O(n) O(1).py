# 142. Linked List Cycle II

# * We can use the tortoise and the hare algorithm here
# * But it is important to note that we need to know what node the cycle starts on
# * The usual fast/slow pointer approach works up until the pointers meet
# *     - If they don't then there is no cycle; in which case just return False
# * Otherwise, we know a cycle exists somewhere, so we need to find it
# ! Lets say there are `n` nodes in total, and `a` nodes do NOT exist in the cycle
# * This means there are (n - a) = b nodes that ARE part of the cycle
# * If we plug some numbers in like n = 7, a = 2, then b = 7 - 2
# *     - There are 2 nodes NOT part of the cycle
# *     - And there are 5 nodes that ARE part of the cycle
# * If we reset either slow OR fast (not both) back to head, we can make an observation
# *     - Lets say we set `fast` = `head` for clarity
# ! The distance from `head` to the cycle start is EQUAL to the distance from `slow` to the cycle start
# * For our example, the distance in both cases is TWO
# * Since the distances are equal, both pointers are guaranteed to meet if they move at the same rate
# *     - Thus, BOTH slow AND fast move at a rate of ONE node per iteration from this point onwards
from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # * Base Case: There is no cycle
        if head is None or head.next is None:
            return None

        slow: Optional[ListNode] = head  # * Moves one per iteration
        fast: Optional[ListNode] = head  # * Moves two per iteration

        # * Determine if a cycle exists in general
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # * There is a cycle; reset fast
            if slow == fast:
                break

        # * There is no cycle
        if fast is None or fast.next is None:
            return None

        # * If there are `n` nodes, and `a` are in the cycle
        # * Then there are (n - a) = b nodes NOT in the cycle
        # * Both `slow` and `fast` are equally as far from start (move both 1 per now)
        fast = head

        while slow != fast:
            slow = slow.next
            fast = fast.next

        # * The node that starts the cycle
        return fast


# * Time: O(n) - We have to process every element in the list in the worst case

# * Space: O(1) - The memory usage remains constant regardless of input size
