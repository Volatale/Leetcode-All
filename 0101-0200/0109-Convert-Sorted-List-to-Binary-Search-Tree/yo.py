# 109. Convert Sorted List to Binary Search Tree

from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(
        self,
        val: int = 0,
        next: Optional[ListNode] = None,
    ):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional[TreeNode] = None,
        right: Optional[TreeNode] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def solve(left: int, right: int) -> Optional[TreeNode]:
            # * Base Case: Out of Bounds
            if left > right:
                return None

            # * The mid point is always the middle element in the range [left, right]
            mid: int = left + ((right - left) >> 1)

            root = TreeNode(nums[mid])

            # * Anything before mid is on the left subtree, and anythig after mid is on the right subtree
            root.left = solve(left, mid - 1)
            root.right = solve(mid + 1, right)

            return root

        # * Base Case: Null head
        if head is None:
            return None

        # * Iterate through the linked list and create an array of its nodes' values
        nums: list[int] = []
        curr: Optional[ListNode] = head

        while curr:
            nums.append(curr.val)
            curr = curr.next

        # * Now recursively create the BST by repeatedly choosing the mid element as root
        return solve(0, len(nums) - 1)


# * Time: O(n) - We need to create `n` nodes in total and process each element of the linked list

# * Space: O(n) - Since we create `n` nodes, the memory usage scales with the size of the input
# * Additionally, the maximum recursion depth scales at a rate of O(h) since the tree must be balanced
