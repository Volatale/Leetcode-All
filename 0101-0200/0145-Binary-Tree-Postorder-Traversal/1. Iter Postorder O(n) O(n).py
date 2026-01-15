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
        if root is None:
            return []

        results: list[int] = []
        stack: list[TreeNode] = []
        curr: Optional[TreeNode] = root
        prev: Optional[TreeNode] = None

        while curr or stack:
            # * Travel as far left as possible
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack[-1]

            if curr.right is None or curr.right == prev:
                results.append(curr.val)  # * Process the node
                stack.pop()
                prev = curr
                curr = None
            else:
                # * Travel right
                curr = curr.right

        return results


# * Time: O(n) - We have to process every node in the tree, so the time taken scales linearly

# * Space: O(n) - If the tree resembles a linked list, the size of the stack scales with the input size
