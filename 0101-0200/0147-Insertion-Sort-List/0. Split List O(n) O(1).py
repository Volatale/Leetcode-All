# 147. Insertion Sort List

# * In the array version of insertion sort, conceptually, the elements are partitioned within the array
# *     - Partially Sorted side
# *     - Unsorted side
# * The partially sorted side is "partially" sorted because it doesn't contain ALL of the potential elements yet
# *     - But the elements it DOES contain are in sorted order
# * The unsorted side is "unsorted" because we know almost nothing about the elemnts over there
# *     - Thus, we cannot make any assumptions about the properties it holds, unlike the partially sorted side
# ! The easiest thing to do here is to split the linked list up into two partitions like above, but literally
# *     - In the array version, this is implicit and happens naturally due to the iterations
# *     - Anything on the left of `i` is said to be partially sorted, and anything to the right is unsorted
# * In the array version, usually we use a "j" pointer and "drag" elements back using:
# *     - if nums[j] < nums[j - 1], swap them, then j-- (to "follow" the element)
# * Here, there's no need to iterate backwards since we have linked lists
# * We merely track a "prev" pointer that points to the node that exists one before the "current" node should exist
# * It then becomes trivial to insert the "current" node between `prev` and `prev.next`
from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode] = None) -> Optional[ListNode]:
        # * Base Case: Nothing to sort
        if head is None or head.next is None:
            return head

        # * Head may move, so we need a dummy node to attach nodes to
        dummy: ListNode = ListNode(-1)
        dummy.next = head

        # * Split the list up into two: Partially Sorted and Unsorted
        curr: Optional[ListNode] = head.next
        head.next = None

        while curr:
            prev: Optional[ListNode] = dummy  # * Insert nodes at prev.next
            next: Optional[ListNode] = curr.next  # * Keeps reference to rest of list

            # * Move `prev` until we find the insertion position for `curr`
            while prev.next and prev.next.val < curr.val:
                prev = prev.next

            # * `curr` is inserted between prev and prev.next
            curr.next = prev.next
            prev.next = curr
            curr = next

        return dummy.next


# * Time: O(n^2) - In the worst case, the list is sorted in descending order
# * Within each iteration, it is possible `prev` has to iterate the entire list
# * There are `n` nodes, and thus this may occur `n` times

# * Space: O(1) - The memory usage remains constant regardless of input size
