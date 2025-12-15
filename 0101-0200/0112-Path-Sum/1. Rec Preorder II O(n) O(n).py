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
        def solve(curr: Optional[TreeNode], path_sum: int) -> bool:
            # * Base Case: Null Node
            if curr is None:
                return False

            path_sum += curr.val

            # * Validate the path sum
            if curr.left is None and curr.right is None and sum == targetSum:
                return True

            # * Try both the left and right subtrees
            return solve(curr.left, path_sum) or solve(curr.right, path_sum)

        return solve(root, 0)


# * Time: O(n) - We have to process every node regardless

# * Space: O(n) - In the worst case, the binary tree resembles a linked list
# * Therefore, the maximum recursion depth scales with the number of nodes
