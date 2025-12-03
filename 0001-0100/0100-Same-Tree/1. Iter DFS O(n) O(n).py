# 100. Same Tree

# * There are three cases to handle:
# *     - Both p AND q are null (identical)
# *     - Either p OR q are null (not identical)
# *     - p.val != q.val (not identical)
# * Validate these conditions across the entire tree at every level
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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # * Base Cases
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False

        # * Deque is used to simulate a stack
        deq = deque[tuple[Optional[TreeNode], Optional[TreeNode]]]([(p, q)])

        while deq:
            pNode, qNode = deq.pop()

            # * Case 1: Both are null, so the structures are identical
            if pNode is None and qNode is None:
                continue

            # * Case 2: One of them is not null, so the structures are different
            if pNode is None or qNode is None:
                return False

            # * Case 3: The values are different
            if pNode.val != qNode.val:
                return False

            # * Append the left children together, followed by the right children
            deq.append((pNode.left, qNode.left))
            deq.append((pNode.right, qNode.right))

        return True


# * Time: O(n) - In the "worst case", we have to process every node, and both trees are the same

# * Space: O(n) - In the worst case, we have binary trees that resemble linked lists
