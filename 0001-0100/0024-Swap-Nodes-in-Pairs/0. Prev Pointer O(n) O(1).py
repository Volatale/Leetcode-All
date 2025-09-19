# 24. Swap Nodes in Pairs

# * We are given a linked list, and the goal is to swap every two adjacent linked list nodes in pairs
# * Since we need to swap the first two, we should use a dummy node
# *     - Otherwise we can't perform the swap
# * Ultimately, a swap is only possible if there exists two nodes ahead of the current
# * For example, if we have (1 -> 2 -> 3) as a linked list
# * Then the linked list looks like: (D -> 1 -> 2 -> 3)
# * Thus, after the first swap we have (D -> 2 -> 1 -> 3)
# *     - By the end of the swap, "prev" will point to the node that holds the value 1
# !     - But there is only one node remaining, so it isn't possible to perform another swap
from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # * Handle case where there is no list, or we only have 1 node (can't swap)
        if not head or not head.next:
            return head

        # * We need something to attach the first swapped pair to
        dummy = ListNode(-1)
        dummy.next = head

        # * Prev points to the node we need to attach the swapped pairs to
        prev = dummy

        # * We can only swap if there are two nodes ahead of the current
        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next

            # * Perform the swap
            first.next = second.next
            second.next = first
            prev.next = second

            # * Move prev to the end of the swapped pair
            prev = first

        return dummy.next


list = ListNode(1)
list.next = ListNode(2)
list.next.next = ListNode(3)
list.next.next.next = ListNode(4)

sol: Solution = Solution()
print(sol.swapPairs(list))

# * Time: O(n) - The time taken scales with the size of the input

# * Space: O(1) - The memory usage remains constant regardless of input size
