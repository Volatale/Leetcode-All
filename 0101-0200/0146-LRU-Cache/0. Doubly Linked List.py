# # 146. LRU Cache

# * We can use a doubly linked list for the purposes of tracking which nodes are recently used
# * Nodes closer to the head are the lesser recently used nodes
# * Conversely, nodes further from the head (closer to the tail) are more recently used
# * Since we're using a linked list, iterating over the list will take O(n) in the worst case
# ! We can alieviate this fact using a dictionary that tracks references to nodes via keys
# *     - Key -> Node (whose value holds a key)
# * The key that each node holds will be used to access yet another dictionary object
# *     - Except `this` dictionary acts as the cache itself
# * We only have to validate the capacity of the LRU cache AFTER insertion, so we can lazily evaluate its length
# * If we access something in the cache, it has been "recently used", thus it is added to the tail of the linked list
# * If the size of the cache > capacity, then we need to remove the least recently used node
# *     - In this case, it'll always be the node closest to the head
# *     - So, simply put, self.head.next is the least recently used cache
from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(
        self,
        key: int = 0,
        next: Optional[ListNode] = None,
        prev: Optional[ListNode] = None,
    ):
        self.key = key
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head: ListNode = ListNode(-(1 << 31))
        self.tail: ListNode = ListNode((1 << 31) - 1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def append_right(self, node: ListNode) -> None:
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node

    def append_left(self, node: ListNode) -> None:
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def move_to_back(self, node: ListNode) -> None:
        # * This node is already the most recently used
        if node == self.tail.prev:
            return

        node.prev.next = node.next
        node.next.prev = node.prev

        self.append_right(node)

    def drop_least_recent(self) -> None:
        self.head.next = self.head.next.next
        self.head.next.prev = self.head


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.cache: dict[int, int] = {}  # * The LRU cache itself
        self.node_map: dict[int, ListNode] = {}  # * Provides fast access to any node
        self.list = DoublyLinkedList()

    def get(self, key: int) -> int:
        # * Key doesn't exist
        if key not in self.cache:
            return -1

        node: ListNode = self.node_map[key]
        self.list.move_to_back(node)  # * This node is now the most recently used
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # * Add the node to the cache (and the node map)
            node: ListNode = ListNode(key)
            self.list.append_right(node)
            self.node_map[key] = node
        else:
            # * Mark as most recent
            node: ListNode = self.node_map[key]
            self.list.move_to_back(node)

        self.cache[key] = value

        # * Validate the capacity requirements
        if len(self.cache) > self.capacity:
            front: ListNode = self.list.head.next
            self.list.drop_least_recent()
            del self.cache[front.key]
            del self.node_map[front.key]
