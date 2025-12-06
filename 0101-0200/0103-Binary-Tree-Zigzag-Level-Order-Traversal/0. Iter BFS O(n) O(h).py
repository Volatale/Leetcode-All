# 103. Binary Tree Zigzag Level Order Traversal

# * We essentially want to execute a level-order BFS
# * At each level, we know how many nodes will exist
# *     - Thus we can pre-populate an array for each level
# * Since we want a BFS, we always want to pop from the left (dequeue)
# * If we want the nodes in `ltr` order, we simply add them to the array in sequence
# * But if we want the nodes in `rtl` order, we need to add the elements to the array in reverse
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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if root is None:
            return []

        deq = deque[Optional[TreeNode]]([root])
        results: list[list[int]] = []
        ltr: bool = True

        while deq:
            length: int = len(deq)
            nodes: list[int] = [0] * length

            for i in range(length):
                # * The deque should act as a queue if ltr, else it acts like a stack
                node = deq.popleft()

                # * Redundant; only used for typechecking purposes
                if node is None:
                    continue

                if ltr:
                    nodes[i] = node.val
                else:
                    nodes[length - i - 1] = node.val

                if node.left:
                    deq.append(node.left)

                if node.right:
                    deq.append(node.right)

            results.append(nodes)
            ltr = not ltr  # * Toggle between ltr and rtl

        return results


tree = TreeNode(9)
tree.left = TreeNode(1)
tree.left.left = TreeNode(3)
tree.left.right = TreeNode(4)
tree.right = TreeNode(2)
tree.right.left = TreeNode(5)
tree.right.right = TreeNode(7)
sol: Solution = Solution()

# *              9
# *         1         2
# *        3 4       5 7
print(sol.zigzagLevelOrder(tree))

# * Time: O(n) - We need to process every element regardless of input size

# * Space: O(h) - The size of the deque scales with the height of the tree
# * If the list has 3 levels, in the worst case, the deque's size is at most 2^2
# * This generalizes to 2^(h-1) where `h` is the height of the tree
