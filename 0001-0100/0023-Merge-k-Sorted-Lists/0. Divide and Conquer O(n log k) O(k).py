# * 23. Merge k Sorted Lists

# * We are given an array of `k` (singly) linked lists and each is sorted into ascending order
# * The goal is to merge all of the linked lists into ONE sorted linked list
# ! In a brute force manner, we could simply iterate over every linked list
# *     - Simply merge them one by one using the "merge sorted list" strategy
# * The issue with this is that the time complexity is O(k * m)
# *     - Where `k` is the number of linked lists
# *     - And `m` is the length of the longest list
# ! Instead, we can apply a divide and conquer approach
# * Ultimately, we want there to be a single linked list remaining
# * We can continuously merge linked lists into one in pairs of two
# * If we start with [head1, head2, head3, head4], then `k` = 4
# *     - Merge `head1` and `head2`
# *     - Then merge `head3` and `head4`
# * Then, we're left with two linked lists
# *     - Merge `list1` and `list2`
# * Now, we are left with a SINGLE linked list
# ! Notice how we grab lists in pairs, and the number of merges halves each successive level
# *     - 4 -> 2 ->1
# *     - 16 -> 8 -> 4 -> 2 -> 1
# * The time complexity becomes logarithmic
# *     - Merging two sorted lists costs O(n + m), but merging all `k` at once naively costs O(k * n)
# *     - If we halve the number of subproblems each round, the total work forms a geometric series -> O(n log k)
# * We do O(n) work each iteration, and there are log(k) iterations in total, hence O(n log k) and not O(k log n)
from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        # * Keep merging until only one list (subproblem) remains
        while len(lists) > 1:
            merged: list[Optional[ListNode]] = []

            # * Merge pairs of lists (groups of two)
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None

                merged.append(self.mergeTwoLists(l1, l2))

            # * Our new set of subproblems
            lists = merged

        return lists[0]

    def mergeTwoLists(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # * We need a dummy node so we can attach the first node to something
        dummy = ListNode(-1)
        curr = dummy

        # * Merge the lists into one
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next

            curr = curr.next

        # * Handle the leftover nodes
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2

        return dummy.next


sol: Solution = Solution()

head1 = ListNode(1)
head1.next = ListNode(4)
head1.next.next = ListNode(5)

head2 = ListNode(1)
head2.next = ListNode(3)
head2.next.next = ListNode(4)

head3 = ListNode(2)
head3.next = ListNode(6)

print(sol.mergeKLists([head1, head2, head3]))

# * Time: O(n log(k)) - The number of lists that need to be merged is halved at each level
# * Within each iteration, we do O(n) work, and there are `k` lists

# * Space: O(k) - The memory usage scales with the number of lists in the input
# * If k = 8, then within the first iteration, `merged` has a length of 4 (8 / 2)
# * On the next iteration, merged has a length of 2 (4 / 2)
# * So the true space complexity is O(k  / 2), but we simply and drop constants
