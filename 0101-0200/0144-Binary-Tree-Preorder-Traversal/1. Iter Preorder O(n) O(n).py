# 144. Binary Tree Preorder Traversal

# * Preorder Traversal follows this pattern:
# *     - Node -> Left -> Right
# * Thus, we just apply this logic at every node
from __future__ import annotations
from typing import Optional
from collections import deque


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
        # * Base Case: There are no nodes, thus no values
        if root is None:
            return []

        results: list[int] = []
        curr: Optional[TreeNode] = root
        stack: list[TreeNode] = []

        while curr or stack:
            while curr:
                results.append(curr.val)  # * N
                stack.append(curr)
                curr = curr.left  # * L

            curr = stack.pop().right  # * R

        return results


# * Time: O(n) - We have to process every node in the input regardless
# * Thus the time taken scales with the number of nodes in the tree

# * Space: O(n) - The size of the stack scales with the number of nodes in the worst case
