# 160. Intersection of Two Linked Lists

# * We can apply an idea similar to finding the cycle node in the "tortoise and the hare" algorithm, with some adjustments
# * Logically speaking, there are (n + m) nodes in total
# * Now, it is not guaranteed that (n == m), so it is possible one list has more (or less) nodes than the other
# !     - This creates an offset in the balance
# * One thing to note is that (A + B == B + A), or, in other words, addition is commutative
# * Lets say there are 9 nodes, headA's length is 5, and headB's length is 4
# *     - 9 - 5 = 4
# *     - 9 - 4 = 5
# * If the list lengths are not equal, then there is an offset somewhere
# * One of the nodes has LESS nodes than the other, and conversely, the other lsit has MORE nodes than the other
# * Lets say we travel along `headA`; we are technically "1 node behind headB"
# * That also means that `headB` is "1 node ahead of headA"
# ! All we have to do from here is make the respective pointers iterate over the OTHER list
# *     - 9 - 5 = 4, and we know the OTHER list has a length of 4
# *     - 9 - 4 = 5, and we know the OTHER list has a length of 5
# * Thus, by iterating over both lists with both pointers, if an intersection exists, when both have iterated over 9 nodes, they'll meet
# * And mathematically speaking, the node they meet at will be guaranteed to be the intersection node
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

        # * Addition is commutative; by traveling along both lists each, any offsets are removed
        while currA != currB:
            if currA is not None:
                currA = currA.next
            else:
                currA = headB  # * Now `currA` travels along the headB

            if currB is not None:
                currB = currB.next
            else:
                currB = headA  # * `currB` now travels along headA

        # * If there IS an intersection, both `currA` and `currB` point to it; otherwise, there isn't one
        return currA


# * Time: O(n + m) - In the worst case there is no intersection, so we iterate over both lists entirely

# * Space: O(1) - The `visited` set's size scales with the size of `headA`
