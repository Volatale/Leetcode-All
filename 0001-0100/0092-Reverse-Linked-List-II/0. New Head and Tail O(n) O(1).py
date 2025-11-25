from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val: int, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


# * 92. Reverse Linked List II


# * The key idea in this question is that we need to reverse a group of nodes
# * The number of nodes that are to be reversed in a group is variable
# ! Our goal is to ensure the elements NOT reversed stay in tact, in their relative orderings
# * Thus, we can split the linked list up like so:
# *     NOT REVERSED -> REVERSAL GROUP -> NOT REVERSED
# * Therefore, we need a pointer to the node just before the reversal group
# * And we need a pointer to the node just after the reversal group
# * Since we are given numbers to indicate the numbering of each node, we can use a simple for loop
# * Find the HEAD and the TAIL of the reversal group
# * Then, all we have to do is reverse up until the end of the reversal group
# * And re-attach the nodes and their pointers
class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        # * We need a dummy node just in case we must reverse the entire list
        dummy = ListNode(-1)
        dummy.next = head

        # * The node just before the reversal group
        prev = dummy

        # * Start / End of the reversal group
        newHead = head
        newTail = head

        # * Move our pointers to the desired nodes
        for i in range(1, right):
            if i < left:
                prev = prev.next
                newTail = newTail.next

            if i < right:
                newHead = newHead.next

        next = newHead.next  # * The remaining nodes AFTER our old tail
        prev.next = self.reverse(newTail, next)
        newTail.next = next

        return dummy.next

    def reverse(self, head: ListNode, limit: ListNode):
        prev = None
        next = None
        curr = head

        while curr and curr != limit:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev


# * Time: O(n) - The time taken scales with the size of the linked list

# * Space: O(1) - The memory usage remains constant regardless of input size
