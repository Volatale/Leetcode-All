# 102 Binary Tree Level Order Traversal

# * A "level order traversal" is essentially just a BFS traversal
# *     - At each node, push the left and right children
# * Take a snapshot of the size of the deq at each level and iterate over the elements within the deque
# *     - This ensures we can iteratively produce an array of the nodes' values on the current level
# *     - If we don't, it becomes more difficult to "know" when the current level ends
# * If we enounter a "null" node, we should just continue
# *     - Null nodes don't have a value, thus we can't include it in the output

from __future__ import annotations
from collections import deque
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
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if root is None:
            return []

        results: list[list[int]] = []
        deq = deque[Optional[TreeNode]]([root])

        while deq:
            length: int = len(deq)
            nodes: list[int] = []

            # * Iterate over the nodes on this level
            for _ in range(length):
                node = deq.popleft()

                # Redundant; only used for typechecking purposes
                if node is None:
                    continue

                # * Add the node's value to the current list
                nodes.append(node.val)

                # * Only append nodes that are not null (lessens amount of work done)
                if node.left:
                    deq.append(node.left)

                if node.right:
                    deq.append(node.right)

            results.append(nodes)

        return results


# * Time: O(n) - We need to process every element in the tree

# * Space: O(h) - The size of the deque scales with the height of the tree
