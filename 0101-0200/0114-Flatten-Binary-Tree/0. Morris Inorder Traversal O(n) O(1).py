# 114. Flatten Binary Tree

# * This problem involves morris inorder traversals
# * We need to find the inorder predecessor of every node so we can attach them in order
# * Why? Because we can't manipulate what curr.right points to without losing node references in the process
# * Thus, by finding the inorder successor of curr.right and linking that to curr.right directly, we can safely manipulate the pointer
# * We are then safe to move the left subtree to the right
# *     - curr.right = curr.left
# *     - curr.left = None
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
    def flatten(self, root: Optional[TreeNode]):
        if root is None:
            return None

        curr: Optional[TreeNode] = root

        while curr:
            if curr.left:
                # * Find the inorder predecessor of curr.right (the node we'd visit right before curr)
                predecessor = curr.left

                while predecessor.right:
                    predecessor = predecessor.right

                # * Link predecessor's right pointer to curr's right
                predecessor.right = curr.right

                # * Now, we can safely modify curr's right pointer without losing any nodes
                curr.right = curr.left
                curr.left = None

            # * Do the same for all nodes
            curr = curr.right


# * Time: O(n) - We have to visit every node, so the time taken scales with the input size

# * Space: O(1) - The memory usage remains constant regardless of input size
