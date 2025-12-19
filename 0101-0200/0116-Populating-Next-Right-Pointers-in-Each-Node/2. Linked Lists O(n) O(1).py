# 117. Populating Next Right Pointers in Each Node II

# * Since we don't have a perfect binary tree, we need to handle "missing" nodes
# * For each node, we can create / contribute to a linked list of the NEXT level
# * Imagine we have a root node (1), and 1 has a left and right child
# * Now imagine the left child has its own left and right children
# * But the right child only has a right child
# *     - This leaves a gap, so it needs to be handled
# * The linked list saves us because we can simply create one per level
from __future__ import annotations
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

        curr: Optional[Node] = root  # * Current node we're processing
        dummy: Node = Node(-1)  # * Head of next level's linked list
        tail: Optional[Node] = dummy  # * Linked list of current level nodes

        while curr:
            # * Iterate the current level
            while curr:
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next
                if curr.right:
                    tail.next = curr.right
                    tail = tail.next

                # * Move to next subtree (if one exists)
                curr = curr.next

            curr = dummy.next  # * Move to the next level
            dummy.next = None  # * Set up a linked list for the next level
            tail = dummy

        return root


# * Time: O(n) - We have to process every node so the time taken scales with the number of nodes

# * Space: O(1) - The memory usage remains constant regardless of input size
