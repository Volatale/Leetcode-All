# 104. Maximum Depth of Binary Tree

# * The depth of a tree is the number of nodes along the path + 1

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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        # * Max depth is max(left, right) + 1
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


# * Time: O(n) - We need to process every node regardless of input size

# * Space: O(n) - In the worst case, the number of nodes is equal to the max depth
