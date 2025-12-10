# 107. Binary Tree Level Order Traversal II

from __future__ import annotations
from collections import deque
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
    def levelOrderBottom(self, root: Optional[TreeNode]) -> list[list[int]]:
        if root is None:
            return []

        results: list[list[int]] = []
        deq = deque[Optional[TreeNode]]([root])  # * Acts as a queue

        while deq:
            length: int = len(deq)
            nodes: list[int] = []

            # * Iterate over the nodes on this levle
            for _ in range(length):
                node = deq.popleft()

                if node is None:
                    continue

                # * Process the node
                nodes.append(node.val)

                if node.left:
                    deq.append(node.left)

                if node.right:
                    deq.append(node.right)

            results.append(nodes)

        # * Return the reversed array
        return results[::-1]


# * Time: O(n) - We need to process every element in the tree

# * Space: O(h) - The size of the deque scales with the height of the tree
