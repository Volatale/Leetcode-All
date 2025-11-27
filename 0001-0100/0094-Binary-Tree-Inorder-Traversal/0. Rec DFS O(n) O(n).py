# 94. Binary Tree Inorder Traversal

# * The binary tree traversals follow a pattern:
# *     - Preorder -> N L R
# *     - Inorder -> L N R
# *     - Postorder -> L R N
# * Thus, we follow the Inorder pattern

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
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        def recurse(curr: Optional[TreeNode]):
            if curr is None:
                return

            recurse(curr.left)  # * L
            results.append(curr.val)  # * N
            recurse(curr.right)  # * R

        # * Base Case: Root is none
        if root is None:
            return []

        results: list[int] = []
        recurse(root)
        return results


# * Time: O(n) - In the worst case, the binary tree resembles a linked list
# * We have to process every node regardless of input

# * Space: O(n) - If the binary tree resembles a linked list, the recursion depth is proportional to the input size
