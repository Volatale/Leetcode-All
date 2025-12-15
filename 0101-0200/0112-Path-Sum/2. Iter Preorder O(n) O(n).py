# 112. Path Sum

# * A leaf node is a node with no children (whether they be left or right)
# * Thus, we can only "validate" our path's sum once we reach a root
# * We can incrementally build up our sum as we path through nodes in a preorder-manner
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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        # * Node -> Path_Sum
        stack: list[tuple[TreeNode, int]] = [(root, 0)]

        while stack:
            node, path_sum = stack.pop()

            # * Add the current node's value to the path sum
            path_sum += node.val

            # * Check if curr is a leaf and that path_sum == targetSum
            if node.left is None and node.right is None and path_sum == targetSum:
                return True

            if node.left:
                stack.append((node.left, path_sum))

            if node.right:
                stack.append((node.right, path_sum))

        return False


# * Time: O(n) - We have to process every node regardless

# * Space: O(n) - In the worst case, the binary tree resembles a linked list
# * Therefore, the stack's size scales with the number of nodes
