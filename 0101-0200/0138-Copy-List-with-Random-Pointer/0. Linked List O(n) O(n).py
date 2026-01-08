from __future__ import annotations
from typing import Optional


class Node:
    def __init__(
        self, x: int, next: Optional[Node] = None, random: Optional[Node] = None
    ):
        self.val = x
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        # * Base Case: No linked list
        if head is None:
            return None

        # * Original Node -> Copy
        node_map: dict[Node, Node] = {}
        curr: Optional[Node] = head

        # * Perform one pass to form the mappings between O.G node to copy
        while curr:
            node_map[curr] = Node(curr.val)
            curr = curr.next

        # * Perform a second pass to fix the connections between nodes
        curr = head

        while curr:
            copy: Node = node_map[curr]  # * Get the copy of curr
            copy.next = node_map.get(curr.next)
            copy.random = node_map.get(curr.random)

            curr = curr.next  # * Move onto the next node

        # * Return the copy of the head
        return node_map[head]


# * Time: O(n) - We perform two passes over the input linked list
# * So the time taken scales with the input size

# * Space: O(n) - We create `n` new nodes (one for each node), thus there are also `n` unique keys in the dict
