# 101. Symmetric Tree


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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def solve(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            # * Case 1: Both are null, structures are identical
            if p is None and q is None:
                return True

            # * Case 2: One is not null, structures are not identical
            if p is None or q is None:
                return False

            # * Case 3: Values are different
            if p.val != q.val:
                return False

            deq = deque[tuple[Optional[TreeNode], Optional[TreeNode]]]([(p, q)])

            while deq:
                pNode, qNode = deq.pop()

                # * Case 1: Both are null, structures are identical
                if pNode is None and qNode is None:
                    continue

                # * Case 2: One is not null, structures are not identical
                if pNode is None or qNode is None:
                    return False

                # * Case 3: Values are different
                if pNode.val != qNode.val:
                    return False

                # * Append the left and right children together, then the right and left
                deq.append((pNode.left, qNode.right))
                deq.append((pNode.right, qNode.left))

            return True

        return solve(root, root)


# * Time: O(n) - In the "worst case", the entire tree is symmetric, so we process every node

# * Space: O(n) - If the binary tree resembles a linked list, the deque's size is `n`
