# 145. Binary Tree Postorder Traversal

# * Postorder Traversal follows the Left -> Right -> Node pattern
# * We simply apply this logic for every node
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
    def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        def solve(curr: Optional[TreeNode]) -> None:
            if curr is None:
                return

            solve(curr.left)
            solve(curr.right)
            results.append(curr.val)

        results: list[int] = []
        solve(root)
        return results


# * Time: O(n) - We have to process every node in the tree, so the time taken scales linearly

# * Space: O(n) - In the worst case, the tree resembles a linked list
# * Thus, the maximum recursion depth scales linearly with the number of input nodes
