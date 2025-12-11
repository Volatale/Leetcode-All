# 108. Convert Sorted Array to Binary Search Tree

# * Performing an inorder traversal on a BST will result in a sorted array
# * We already have the sorted array, so we essentially need to reverse our steps
# * An inorder traversal follows the "L N R" pattern
# * Based on the pattern, we know that the root is consistently processed in the middle of the array
# * Since the "root" is the middle, anything before the root is part of the left subtree
# * Similarly, anything after the root is part of the right subtree
# * And since a BST is recursive in nature, the same logic holds for each node
# * We can use the followig formula to achieve the mid point: left + floor((right - left) / 2)
from __future__ import annotations
from typing import Optional


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
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        def solve(left: int, right: int) -> Optional[TreeNode]:
            # * Base Case: Create a new node
            if left > right:
                return None

            # * The middle element in the range is always the root
            mid: int = left + ((right - left) >> 1)

            # * Create the node using the middle value in the range
            root = TreeNode(nums[mid])

            # * Anything before mid is on the left subtree, anything after is on the right subtree
            root.left = solve(left, mid - 1)
            root.right = solve(mid + 1, right)

            return root

        # * We start with the range of the entire array
        return solve(0, len(nums) - 1)


# * Time: O(n) - The time taken scales with the size of the input

# * Space: O(n) - We have to create a node for each element in the input, so the memory usage scales linearly
