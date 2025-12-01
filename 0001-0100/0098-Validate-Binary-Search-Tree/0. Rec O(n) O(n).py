# 98. Validate Binary Search Tree

# * A binary search tree states that for each node i:
# *     - The left subtree has nodes valued < i.val
# *     - The right subtree has nodes valued > i.val
# * Thus, we just need to make sure these conditions are upheld at each level
# * lower and upper will either be "None", or an int
# * If we travel left, then we want the node we travel to to have a value < the node we came from
# * If we travel right, then we want the node we travel to to have a value > the node we came from
# * For example, if we were at 3, and we moved left to 2, then we know 2 < 3, so this is fine
# * If lower is not None, then we traveled right, so we expect the current value to be >
# * If upper is not None, then we traveled left, so we expect the current value to be <
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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def solve(
            curr: Optional[TreeNode], lower: int | None, upper: int | None
        ) -> bool:
            # * Base Case: A null node is considered to be valid
            if curr is None:
                return True

            # * Ensure the validity of nodes
            if (lower is not None and curr.val <= lower) or (
                upper is not None and curr.val >= upper
            ):
                return False

            return solve(curr.left, lower, curr.val) and solve(
                curr.right, curr.val, upper
            )

        return solve(root, None, None)


# * Time: O(n) - We have to process every node in the tree

# * Space: O(n) - In the worst case, the binary search tree resembles a linked list
# * Therefore the maximum recursion depth is equal to `n` in that case
