# 111. Minimum Depth of Binary Tree

# * A balanced binary tree is a binary tree whose subtrees differ by no more than 1 for each node


from __future__ import annotations
from typing import Optional
from collections import deque


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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # * Base Case: Null Root
        if root is None:
            return 0

        # * A deque acting as a queue
        deq = deque([root])
        depth: int = 0

        while deq:
            size: int = len(deq)

            # * Level-order traversal
            for _ in range(size):
                node = deq.popleft()

                # * Found a leaf node
                if node.left is None and node.right is None:
                    return depth + 1

                # * Add the children (assuming they aren't null)
                if node.left:
                    deq.append(node.left)

                if node.right:
                    deq.append(node.right)

            # * We are now processing the next level
            depth += 1

        return depth


# * Time: O(n) - We have to process every node, so the time taken scales linearly


# * Space: O(h) - The memory usage scales with the height of the tree
# * If we have a balanced binary tree, the bottom row contains 2^(h-1) nodes
