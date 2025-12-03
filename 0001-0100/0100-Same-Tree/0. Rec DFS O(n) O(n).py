# 100. Same Tree

# * There are three cases to handle:
# *     - Both p AND q are null (identical)
# *     - Either p OR q are null (not identical)
# *     - p.val != q.val (not identical)
# * Validate these conditions across the entire tree at every level
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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # * Case 1: Both are null, so the structures are identical
        if p is None and q is None:
            return True

        # * Case 2: One is null, so the structures are different
        if p is None or q is None:
            return False

        # * Case 3: The values are different
        if p.val != q.val:
            return False

        # * Recursive ensure all of these properties hold at each level
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# * Time: O(n) - In the "worst case", we have to process every node, and both trees are the same

# * Space: O(n) - In the worst case, we have binary trees that resemble linked lists
