# 129. Sum Root to Leaf Numbers

# * We essentially have to handle place value at each level of recursion
# * Thus, we need to track the state of the sum so we have something to contribute to
# * A BFS approach is possible since we'll eventually reach the leaf nodes
from __future__ import annotations
from typing import Optional, Deque
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
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total_sum: int = 0

        # * (Node, Sum)
        deq: Deque[tuple[TreeNode, int]] = deque([(root, 0)])

        while deq:
            curr, sum = deq.popleft()

            # * Handle the place value
            sum = sum * 10 + curr.val

            # * Check if the current node is a leaf
            if curr.left is None and curr.right is None:
                total_sum += sum

            # * Add the children if they exist
            if curr.left:
                deq.append((curr.left, sum))
            if curr.right:
                deq.append((curr.right, sum))

        return total_sum


# * Time: O(n) - We have to process every node in the tree

# * Space: O(h) - In the worst case, the deque's size scales with the height of the tree
