# 129. Sum Root to Leaf Numbers

# * We essentially have to handle place value at each level of recursion
# * Thus, we need to track the state of the sum so we have something to contribute to
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
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def solve(curr: Optional[TreeNode], sum: int) -> int:
            nonlocal total_sum

            # * Base Case: Out of Bounds nodes have no digit
            if curr is None:
                return 0

            # * Place value
            sum = sum * 10 + curr.val

            # * Check if this is a leaf node
            if curr.left is None and curr.right is None:
                return sum

            return solve(curr.left, sum) + solve(curr.right, sum)

        total_sum: int = 0
        solve(root, 0)
        return total_sum


# * Time: O(n) - We have to process every node in the tree regardless

# * Space: O(n) - In the worst case, the input resembles a linked list
# * Thus, the maximum recursion depth scales with the number of nodes
