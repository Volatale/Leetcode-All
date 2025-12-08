# 105. Construct Binary Tree from Preorder and Inorder Traversal

# * N L R -> Node is first for preorder. Take nodes from preorder
# * L N R -> Use inorder to determine where which subtree the nodes should be placed on
# * Lets say we have [1, 2, 3] and [2, 1, 3]
# * The root of our tree has to be 1 (which is preorder[0])
# * Then, since we have our root (node), we use `inorder` to split the tree
# * Find the index of the root node's value in inorder (in 1's case that is index 1)
# * Thus, we know that 2 is the left of 1 and 3 is the right of 1
# * Recursively call the function for each level of recursion

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
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        if len(preorder) == 0 or len(inorder) == 0:
            return None

        # * The first element in `preorder` is the root
        val = preorder[0]
        root = TreeNode(val)

        # * Find the root's index within `inorder` to split left/right subtrees
        mid: int = inorder.index(val)

        # * Elements before mid belong to left subtree, eleents after are right on the subtree
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])

        return root


sol: Solution = Solution()
print(sol.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]))

# * Time: O(n^2) - The time complexity of list.index is O(n), and we do that per call
# * There are 2n calls to buildTree total, so we get n * n = O(n^2)

# * Space: O(n^2) - The number of nodes created scales with the size of the inputs
# * At each level of recursion, we create subarray slices
