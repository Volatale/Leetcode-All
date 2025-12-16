# 113. Path Sum II

# * We want ALL of the root-to-leaf paths, so this implies backtracking
# * Contribute to the current path as we encounter each node
# *     - path_sum += curr.val
# *     - path.append(curr.val)
# * Then, remove that contribution as we exit the node (return to caller)
# *     - path_sum -= curr.val
# *     - path.pop() (removes most recent)

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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> list[list[int]]:
        def solve(curr: Optional[TreeNode], path_sum: int, path: list[int]) -> None:
            # * Base Case: Null Node
            if curr is None:
                return

            # * Contribute to the path as we arrive at each node
            path_sum += curr.val
            path.append(curr.val)

            # * Validate the path sum and leaf-ness
            if curr.left is None and curr.right is None and path_sum == targetSum:
                results.append(path[:])

            # * Try left and right subtrees
            solve(curr.left, path_sum, path)
            solve(curr.right, path_sum, path)

            # * Remove contribution since we're leaving the node
            path_sum -= curr.val
            path.pop()

        results: list[list[int]] = []
        solve(root, 0, [])
        return results


# * Time: O(n^2) - We have to process every node, so the time taken scales with the input size
# * Creating a copy takes O(n) and we may have to do so in every path in the absolute worst case
# * So its O(n) (for the traversal cost) + O(no. of valid paths * average path length)
# * If every path is the same length (n), then we get O(n^2), but on average it is more likely to be O(n)

# * Space: O(n^2) - If every path is valid and they are all of equal lengths, the memory usage scales quadratically
# * The maximum recursion depth can be at most `n`
