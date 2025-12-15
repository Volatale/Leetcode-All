# 112. Path Sum

# * A leaf node is a node with no children (whether they be left or right)
# * Thus, we can only "validate" our path's sum once we reach a root
# * We can incrementally build up our sum as we path through nodes in a preorder-manner
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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def solve(curr: Optional[TreeNode]):
            nonlocal found, sum

            # * Base Case: Null Node, or found valid path already
            if curr is None or found:
                return 0

            # * Add the current value to the path sum
            sum += curr.val

            # * If curr is a leaf and sum == target, we were successful
            if curr.left is None and curr.right is None:
                found = True
                return

            # * Travel to the left and right subtrees
            solve(curr.left)
            solve(curr.right)

            # * Subtract the current value from the path sum
            sum -= curr.val

        found: bool = False
        sum: int = 0
        solve(root)
        return found


# * Time: O(n) - We have to process every node regardless

# * Space: O(n) - In the worst case, the binary tree resembles a linked list
# * Therefore, the maximum recursion depth scales with the number of nodes
