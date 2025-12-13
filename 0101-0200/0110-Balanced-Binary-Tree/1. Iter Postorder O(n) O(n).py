# 110. Balanced Binary Tree

# * A balanced binary tree is a binary tree in which each node's subtree depths differ by no more than 1
# * Based on this, for each node, we need to get the left and right subtree depths
# * Then, determine whether the absolute difference between those depths is > 1
# * This pattern indicates that we should use postorder traversal -> L R N

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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # * Base Case: Null Root
        if root is None:
            return True

        node_map: dict[TreeNode | None, int] = {None: 0}  # * Node -> Max Depth
        stack: list[TreeNode] = []
        curr: Optional[TreeNode] = root
        prev: Optional[TreeNode] = None

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack[-1]

            if curr.right == prev or curr.right is None:
                # * Get the maximum depth of the left and right subtrees
                left: int = node_map[curr.left]
                right: int = node_map[curr.right]

                # * Validate whether the node is height-balanced
                if abs(left - right) > 1:
                    return False

                # * Update the node map with this node's maximum depth
                node_map[curr] = max(left, right) + 1

                stack.pop()
                prev = curr
                curr = None
            else:
                curr = curr.right

        return True


# * Time: O(n) - We have to process every node in the "worst case"

# * Space: O(n) - In the worst case, the maximum recursion depth is equal to the size of the tree
