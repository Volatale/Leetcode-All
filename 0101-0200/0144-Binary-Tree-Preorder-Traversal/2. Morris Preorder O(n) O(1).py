# 144. Binary Tree Preorder Traversal

# * We can use Morris Traversal here to achieve O(1) space complexity
# * For each node, we need to find the inorder predecessor
# *     - That is, the node we'd process just before the "current" node
# * If the inorder predecessor does NOT have a link to "curr"
# *     - We haven't explored the left subtree entirely yet, so we say "pre.right = curr"
# * After that, we travel left using curr
# * That ephemeral link allows us to traverse back up the tree
# * If the inorder predecessor DOES have a link to curr, then we remove the link
# * Then, we travel right since we have already explored the left subtree in its entirety
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
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        # * Base Case: There are no nodes, thus no values
        if root is None:
            return []

        results: list[int] = []
        curr: Optional[TreeNode] = root

        while curr:
            if curr.left is None:
                results.append(curr.val)  # * N
                curr = curr.right  # * R (can't go left)
            else:
                # * Find the inorder predecessor of curr (the node we process just before)
                predecessor: Optional[TreeNode] = curr.left

                while predecessor.right and predecessor.right != curr:
                    predecessor = predecessor.right

                if predecessor.right is None:
                    # * Haven't explored left subtree fully yet
                    results.append(curr.val)
                    predecessor.right = curr  # * Create link back up the tree
                    curr = curr.left  # * L
                else:
                    # * Fully explored left subtree
                    predecessor.right = None  # * Remove the ephemeral link
                    curr = curr.right  # * R (already explored left subtree)

        return results


# * Time: O(n) - We have to process every node in the input regardless
# * Thus the time taken scales with the number of nodes in the tree

# * Space: O(1) - Assuming we don't count the space used by results, the morris traversal uses O(1) space
