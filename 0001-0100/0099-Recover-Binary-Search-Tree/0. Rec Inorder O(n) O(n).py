# 99. Recover Binary Search Tree

# * Performing an inorder traversal on a BST will provide a sorted array of the nodes' elements
# * In our case, since two of the nodes' values are swapped, two of the values will be out of place
# * This allows us to visualise where the problem nodes are
# * Thus, in order to solve the problem we simply need to use two pointers
# * If prev and prev.val > curr.val, then we know that the previous node was out of place and needs swapping
# * We only perform the swaps at the very end of the function since there are only two bad nodes
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
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        def inorder(curr: Optional[TreeNode]):
            nonlocal first, second, prev

            # * Base Case: Null node
            if curr is None:
                return

            inorder(curr.left)  # * L

            # * Process the node
            if prev and prev.val > curr.val:
                if first is None:
                    first = prev
                second = curr

            prev = curr

            inorder(curr.right)  # * R

        first: Optional[TreeNode] = None
        second: Optional[TreeNode] = None
        prev: Optional[TreeNode] = None

        inorder(root)
        first.val, second.val = second.val, first.val


# * Time: O(n) - We need to process every node in the worst case

# * Space: O(n) - The maximum recursion depth tends toward n
