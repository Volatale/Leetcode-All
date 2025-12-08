# 105. Construct Binary Tree from Preorder and Inorder Traversal

# * N L R -> Node is first for preorder. Take nodes from preorder
# * L N R -> Use inorder to determine where which subtree the nodes should be placed on
# * Lets say we have [1, 2, 3] and [2, 1, 3]
# * The root of our tree has to be 1 (which is preorder[0])
# * Then, since we have our root (node), we use `inorder` to split the tree
# * Find the index of the root node's value in inorder (in 1's case that is index 1)
# * Thus, we know that 2 is the left of 1 and 3 is the right of 1
# * Recursively call the function for each level of recursion
# ! One optimization we can make is that we can precompute the indices of `inorder`
# * Additionally, we can avoid the creation of subarray slices, which also implicitly reduces memory usage

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
        def solve(left: int, right: int) -> Optional[TreeNode]:
            nonlocal preorder_index

            # * Base Case: Out of Bounds
            if left > right:
                return None

            # * Pick a root from `preorder`
            val: int = preorder[preorder_index]
            preorder_index += 1
            root: TreeNode = TreeNode(val)

            # * Split by the inorder index
            mid = inorder_map[val]

            root.left = solve(left, mid - 1)
            root.right = solve(mid + 1, right)

            return root

        # * The index of the node we are trying to create (relative to `preorder`)
        preorder_index: int = 0

        # * Precompute the inorder_map of values in `inorder` (avoids the necessity to call list.index)
        inorder_map: dict[int, int] = {val: i for i, val in enumerate(inorder)}

        # * We start with the entire range of elements
        return solve(0, len(inorder) - 1)


sol: Solution = Solution()
print(sol.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]))

# * Time: O(n) - Each node is processed once, and it takes O(n) to generate the inorder map

# * Space: O(n) - The inorder map's size scales with the input size, and there are `n` levels of recursion
