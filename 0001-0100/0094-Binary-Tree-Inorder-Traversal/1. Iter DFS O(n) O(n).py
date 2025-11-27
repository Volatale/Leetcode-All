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
        # * Base Case: There are no nodes
        if root is None:
            return []

        results: list[int] = []
        stack: list[TreeNode] = []
        curr = root

        while curr or stack:
            # * Move as far left as possible (L)
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            results.append(curr.val)  # * Process the node (N)
            curr = curr.right  # * Go right (R)

        return results


# * Time: O(n) - In the worst case, the binary tree resembles a linked list
# * We have to process every node regardless of input

# * Space: O(n) - If the binary tree resembles a linked list, the stack's size is proportional to the input size
