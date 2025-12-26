# 124. Binary Tree Maximum Path Sum

# * A tree path is:
# *     - A single simple chain
# *     - No forks
# *     - No repeats
# *     - You may change direction exactly once at the "peak" of the path
# * Thus, if we have a tree like:
# *             10
# *           5    6
# * The "best" path sum is 5 -> 10 -> 6
# * Likewise, imagine we have
# *             10
# *        5         6
# *     2     4   3     5
# * We CANNOT include both the 2 and 4 (children of 5), nor both of 6's children
# * Thus, the optimal path is 4 -> 5 -> 10 -> 6 -> 5
# * Nothing about the definition of a path implies we HAVE to go down
# ! There are essentially TWO types of path to consider
# * The horizontal (turning-point path)
# *         - Handled via: left subtree -> curr -> right subtree
# *           which is handled via (curr.val + left + right)
# *         - Has one direction change and no branching
# *         - Cannot be extended, so it cannot be returned to parent
# * The vertical path
# *         - Handled via: curr.val + max(left, right)
# *         - Can only return either left or right subtree to parent
# *         - Branching is not allowed
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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def solve(curr: Optional[TreeNode]) -> int:
            nonlocal results

            # * Base Case
            if curr is None:
                return 0

            # * Postorder traversal (explore left and right subtrees first)
            left: int = max(solve(curr.left), 0)
            right: int = max(solve(curr.right), 0)

            # * Try the "horizontal" path
            results = max(results, curr.val + left + right)

            # * We can only pass ONE of the subtree sums to the parent (so choose the best)
            return curr.val + max(left, right)

        results: int = -(1 << 31)
        solve(root)
        return results


# * Time: O(n) - We have to process each node once at most

# * Space: O(n) - In the worst case, the tree resembles a linked list
# * Thus, the recursion depth is at most, equal to the number of nodes in the tree
