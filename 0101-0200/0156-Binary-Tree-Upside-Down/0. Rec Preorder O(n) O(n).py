# 156. Binary Tree Upside Down

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
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or not root.left:
            return root

        new_root = self.upsideDownBinaryTree(root.left)  # * Travel to the leftmost node

        root.left.left = root.right  # * left child's left = original right
        root.left.right = root  # * left child's right = original root

        root.left = None
        root.right = None

        # * Bubble the new root back up the tree
        return new_root


# * Time: O(n) - We have to process every node in the tree, so the time taken scales with the number of nodes

# * Space: O(n) - In the worst case, the tree resembles a linked list
