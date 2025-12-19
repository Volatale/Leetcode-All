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


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return None

        # * Connect left child to right child
        if root.left:
            root.left.next = root.right

            # * Connect left subtree to right subtree
            if root.next:
                root.right.next = root.next.left

            self.connect(root.left)
            self.connect(root.right)

        return root


# * Time: O(n) - We have to process every node so the time taken scales with the number of nodes

# * Space: O(h) - The input is always a perfect binary tree
