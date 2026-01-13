# 143. Reorder List

# * The most important observation is that half of the list needs to be reversed
# * Notice that the sequence goes: l_0 -> l_n-1 -> l_1 -> l_n-2 -> etc.
# * It isn't normally possible to iterate over a singly-linked list in reverse
# ! That is, unless WE reverse it ourselves
# * But we can't, rather, we don't want to split the entire list
# * Thus, we need to find the halfway point of the linked list and split it into two
# * Then, we are safe to reverse the second half of the linked list
# *     - This will allow us to iterate over it in such a way that we get the l_n-1 -> l_n-2 -> l_n-3 -> etc. order
# * After that, we have two singly linked lists, and from here, we can use a two pointer approach
# * All we have now is the forming of the "reordered" linked list
# * Simply alternate between taking nodes from the 1st and 2nd linked list in that order
from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
            # * Nothing to reverse
            if head is None or head.next is None:
                return head

            curr: Optional[ListNode] = head
            prev: Optional[ListNode] = None

            while curr:
                next: Optional[ListNode] = curr.next
                curr.next = prev
                prev = curr
                curr = next

            return prev

        # * Base Case: Either we have a null head, or there is nothing to reorder
        if head is None or head.next is None:
            return
        slow: Optional[ListNode] = head
        fast: Optional[ListNode] = head.next

        # * Find the middle of the list so we can split it in two
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # * Split the list in two so we can later reverse the second half
        head_2: Optional[ListNode] = slow.next
        slow.next = None

        # * Reverse the second half of the linked list
        head_2 = reverse_list(head_2)

        # * Now we can reorder the list as intended
        dummy: ListNode = ListNode(-1)
        dummy.next = head
        curr = dummy

        slow = head
        fast = head_2

        while slow or fast:
            if slow:
                curr.next = slow
                slow = slow.next
                curr = curr.next
            if fast:
                curr.next = fast
                fast = fast.next
                curr = curr.next


# * Time: O(n) - The time taken scales linearly with the input size
# * It takes O(n / 2) to split the list in half, and O(n / 2) to reverse half of the list
# * Then, simultaneously iterating over both lists takes O(n / 2) + O(n / 2) = O(n)

# * Space: O(1) - The memory usage remains constant; we only ever create a single dummy node
