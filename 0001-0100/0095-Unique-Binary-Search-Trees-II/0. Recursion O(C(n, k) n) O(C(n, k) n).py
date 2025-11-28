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
    def generateTrees(self, n: int) -> list[TreeNode]:
        def build(start: int, end: int) -> list[TreeNode]:
            # * Base Case: Empty subtree
            if start > end:
                return [None]

            trees: list[TreeNode] = []

            # * Choose each number as root at every level of recursion
            for root_val in range(start, end + 1):
                # * All possible left and right subtrees
                left_subtree = build(start, root_val - 1)
                right_subtree = build(root_val + 1, end)

                # * Combine the trees
                for left in left_subtree:
                    for right in right_subtree:
                        root = TreeNode(root_val)
                        root.left = left
                        root.right = right
                        trees.append(root)

            return trees

        # * There are no nodes
        if n == 0:
            return []

        return build(1, n)


sol: Solution = Solution()
print(sol.generateTrees(2))

# * Time: O(C(n, k) * n) - The no. of unique BST structures for n nodes is the nth Catalan number
# * For each of these structures, we spend O(n) time to allocate and wire pointers

# * Space: O(C(n, k) * n) - There are O(C(n, k)) unique BST structures, and they all need to be stored
