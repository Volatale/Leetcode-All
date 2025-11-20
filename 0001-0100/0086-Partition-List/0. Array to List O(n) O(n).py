# 86. Partition List

from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


# * We want to partition the elements < x and the elements >= x
# * So simply create an array for each, then return a new (merged) linked list
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None:
            return head

        # * Partition the node values into two arrays
        smaller: list[int] = []
        larger: list[int] = []
        curr = head

        while curr:
            if curr.val < x:
                smaller.append(curr.val)
            else:
                larger.append(curr.val)

            curr = curr.next

        # * Return a new linked list that is successfully partitioned
        return self._create_list(smaller, larger, x)

    def _create_list(
        self, smaller: list[int], larger: list[int], x: int
    ) -> Optional[ListNode]:
        dummy = ListNode(-1)
        curr = dummy

        # * Handle the elements < x first
        for val in smaller:
            curr.next = ListNode(val)
            curr = curr.next

        # * Then handle the elements >= x
        for val in larger:
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next


my_list = ListNode(1)
my_list.next = ListNode(4)
my_list.next.next = ListNode(3)
my_list.next.next.next = ListNode(2)
my_list.next.next.next.next = ListNode(5)
my_list.next.next.next.next.next = ListNode(2)

sol: Solution = Solution()
print(sol.partition(my_list, 3))

# * Time: O(n) - It takes O(n) to iterate through the linked list itself
# * Then, it takes O(n) to build the new merged linked list

# * Space: O(n) - For each element in the input, we create a new list node
