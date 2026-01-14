# 144. Binary Tree Preorder Traversal

# * Preorder Traversal follows this pattern:
# *     - Node -> Left -> Right
# * Thus, we just apply this logic at every node
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
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        def solve(curr: Optional[TreeNode]) -> None:
            if curr is None:
                return

            results.append(curr.val)  # * N
            solve(curr.left)  # * L
            solve(curr.right)  # * R

        # * Base Case: There are no nodes, thus no values
        if root is None:
            return []

        results: list[int] = []
        solve(root)
        return results


# * Time: O(n) - We have to process every node in the input regardless
# * Thus the time taken scales with the number of nodes in the tree

# * Space: O(n) - In the worst case, the tree resembles a linked list
# * The maximum recursion depth therefore scales with the size of the tree
