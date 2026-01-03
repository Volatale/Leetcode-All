# 133. Clone Graph

# * We need to create a mapping of (original node -> cloned node)
# * Exploring all of the neighbors of the original node can be done using DFS or BFS
# *     - The neighbours[] that exists in each node tells us what links to what
# *     - In other words, it is an edge list
# * It is possible to handle this in two DFS
# *     - One to create a clone of each of the nodes
# *     - And one to form the new graph
# * However, we could simply do both at once (we lazily create nodes)
from __future__ import annotations
from typing import Optional


class Node:
    def __init__(self, val: int = 0, neighbors: list[Node] = []):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        # * Base Case
        if node is None:
            return node

        # * Original Node -> Copy of Node (also acts as visited set)
        clone_map: dict[Node, Node] = {}
        clone_map[node] = Node(node.val)

        # * Stack for DFS
        stack: list[Node] = [node]

        while stack:
            curr: Node = stack.pop()  # * OG Node
            clone: Node = clone_map[curr]

            # * Explore the neighbors of curr
            for neighbor in curr.neighbors:
                # * If we haven't visited it, a clone doesn't exist yet
                if neighbor not in clone_map:
                    clone_map[neighbor] = Node(neighbor.val)
                    stack.append(neighbor)

                clone.neighbors.append(clone_map[neighbor])

        # * The copy of the original node
        return clone_map[node]


# * Time: O(n) - Every node in the input must be processed at least once, so the time taken is linear

# * Space: O(n) - The memory usage scales with the number of nodes in the input
# * We need to create a copy of each node (and there are `n` nodes in total)
