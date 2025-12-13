# 110. Balanced Binary Tree

# * A balanced binary tree is a binary tree whose subtrees differ by no more than 1 for each node


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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def solve(curr: Optional[TreeNode]) -> int:
            nonlocal balanced

            # * Base Case: Null node, or we already know the tree is unbalanced
            if curr is None or not balanced:
                return 0

            # * Get the max depth of the left and right subtrees
            left: int = solve(curr.left)
            right: int = solve(curr.right)

            # * Determine if the subtrees are height-balanced
            if abs(left - right) > 1:
                balanced = False

            # * Return the maximum height of both subtrees
            return max(left, right) + 1

        balanced: bool = True
        solve(root)
        return balanced


# * Time: O(n) - We have to process every node in the "worst case"

# * Space: O(n) - In the worst case, the maximum recursion depth is equal to the size of the tree
