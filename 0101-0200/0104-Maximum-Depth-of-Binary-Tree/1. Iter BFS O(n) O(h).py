# 104. Maximum Depth of Binary Tree

# * The depth of a tree is the number of nodes along the path + 1

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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        deq = deque[Optional[TreeNode]]([root])
        depth: int = 0

        # * If we perform a BFS, the max depth = the depth of the last level
        while deq:
            length: int = len(deq)

            for _ in range(length):
                node = deq.popleft()

                if node is None:
                    continue

                if node.left:
                    deq.append(node.left)

                if node.right:
                    deq.append(node.right)

            # * We move onto the next level
            depth += 1

        return depth


# * Time: O(n) - We need to process every node regardless of input size

# * Space: O(h) - The size of the deque is at most 2^(h-1)
