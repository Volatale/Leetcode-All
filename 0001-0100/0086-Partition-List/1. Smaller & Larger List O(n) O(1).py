# 86. Partition List

from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


# * We want to partition the elements < x and the elements >= x
# * Since we already did this with arrays, we can do the same with linked lists
# * Simply reconfigure the links at the end
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None:
            return head

        curr = head

        # * Partition the node values into two linked lists
        smaller: Optional[ListNode] = ListNode(-1)
        larger: Optional[ListNode] = ListNode(-1)

        # * Tracks progress through the above linked lists
        low = smaller
        high = larger

        # * Partition the linked lists into two
        while curr:
            if curr.val < x:
                low.next = curr
                low = low.next
            else:
                high.next = curr
                high = high.next

            curr = curr.next

        high.next = None
        low.next = larger.next

        return smaller


my_list = ListNode(1)
my_list.next = ListNode(4)
my_list.next.next = ListNode(3)
my_list.next.next.next = ListNode(2)
my_list.next.next.next.next = ListNode(5)
my_list.next.next.next.next.next = ListNode(2)

sol: Solution = Solution()
print(sol.partition(my_list, 3))

# * Time: O(n) - It takes O(n) to iterate through the linked list itself

# * Space: O(1) - The memory usage remains constant regardless of input size
