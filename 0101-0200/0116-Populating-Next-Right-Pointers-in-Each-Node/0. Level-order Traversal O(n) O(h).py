# 116. Populating Next Right Pointers in Each Node

from __future__ import annotations
from collections import deque
from typing import Optional


class Node:
    def __init__(
        self,
        val: int = 0,
        left: Optional[Node] = None,
        right: Optional[Node] = None,
        next: Optional[Node] = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# * Simply perform a level-order traversal using BFS and process nodes as they come
# * Why? We only ever need to set `next` pointers relative to the same level
# *     - For example, nodes in level 1 point to other nodes in level 1
# *     - The same logic holds for every level after 1
class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if root is None:
            return root

        # * Deque is used to simulate a queue for Level-order Traversal (BFS)
        deq = deque([root])

        while deq:
            size: int = len(deq)

            for i in range(size):
                node = deq.popleft()

                # * Attach current node to the next in line (within current level)
                if i < size - 1:
                    node.next = deq[0]

                # * Add the children if they exist
                if node.left:
                    deq.append(node.left)

                if node.right:
                    deq.append(node.right)

        return root


# * Time: O(n) - We have to process every node so the time taken scales with the number of nodes

# * Space: O(h) - The input is always a perfect binary tree, so the maximum queue size = the no. of nodes on the bottom level
