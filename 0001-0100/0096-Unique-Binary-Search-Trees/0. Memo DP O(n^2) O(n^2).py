# 95. Unique Binary Search Trees II

# * A binary search tree states that for a node with a value `i`
# *     - All nodes on the left subtree have values < i
# *     - All nodes on the right subtree have values > i
# * We want to return a list of all of the unique binary search trees that contain each unique value in the range [1, n]
# * If we pick a root `i`, that splits the problem into two independent subproblems
# *     - Left subtree -> built from {1, 2, ..., i - 1}
# *     - Right subtree -> built from {i + 1, ..., n}
# * Each of these can themselves be any BST that fits within that range
# * Thus, if we want ALL of the possible BSTs:
# *     - Loop `i` from 1 to n and choose `i` as the root
# *     - Recursively generate all BSTs that can be made from numbers < i
# *     - Recursively generate all BSTs that can be made from numbers > i
# *     - For each combination of left and right subtrees, combine them under root `i`
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
    def numTrees(self, n: int) -> int:
        def build(start: int, end: int) -> int:
            # * Check for memoized subproblemms
            if (start, end) in memo:
                return memo[(start, end)]

            # * Base Case: Empty subtree or a single node -> 1 valid BST
            if start > end:
                return 1

            count: int = 0

            # * Try using every node in the range [start, end] as the root at every level of recursion
            for root_val in range(start, end + 1):
                left_count = build(start, root_val - 1)
                right_count = build(root_val + 1, end)

                # * Every left subtree can pair with every right subtree (rule of product applies)
                count += left_count * right_count

            memo[(start, end)] = count
            return count

        # * There are no nodes
        if n == 0:
            return 1

        memo: dict[tuple[int, int], int] = {}
        return build(1, n)


sol: Solution = Solution()
print(sol.numTrees(0))  # * 0
print(sol.numTrees(1))  # * 1
print(sol.numTrees(2))  # * 2
print(sol.numTrees(3))  # * 5
print(sol.numTrees(4))  # * 14
print(sol.numTrees(5))  # * 42

# * Time: O(n^2) - We have two non-constant parameters (start and end), and both have `n` unique values individually
# * We memoize each pair of values to avoid the recomputation of subproblems

# * Space: O(n^2) - There are `n` unique values for each non-constant parameter
# * And we need to memoize each subproblem's results, so there are (start * end) possible pairings
