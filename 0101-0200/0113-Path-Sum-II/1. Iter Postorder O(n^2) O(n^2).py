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
        if root is None:
            return []

        results: list[list[int]] = []
        path_sum: int = 0
        path: list[int] = []

        stack: list[TreeNode] = []
        curr: Optional[TreeNode] = root
        prev: Optional[TreeNode] = None

        while curr or stack:
            while curr:
                # * Contribute to the path
                path_sum += curr.val
                path.append(curr.val)
                stack.append(curr)
                curr = curr.left

            curr = stack[-1]

            if curr.right == prev or curr.right is None:
                # * Validate our current path and its sum
                if curr.left is None and curr.right is None and path_sum == targetSum:
                    results.append(path[:])

                # * Remove the contribution to the path
                path_sum -= curr.val
                path.pop()

                stack.pop()
                prev = curr
                curr = None
            else:
                curr = curr.right

        return results


# * Time: O(n^2) - We have to process every node, so the time taken scales with the input size
# * Creating a copy takes O(n) and we may have to do so in every path in the absolute worst case
# * So its O(n) (for the traversal cost) + O(no. of valid paths * average path length)
# * If every path is the same length (n), then we get O(n^2), but on average it is more likely to be O(n)

# * Space: O(n^2) - If every path is valid and they are all of equal lengths, the memory usage scales quadratically
