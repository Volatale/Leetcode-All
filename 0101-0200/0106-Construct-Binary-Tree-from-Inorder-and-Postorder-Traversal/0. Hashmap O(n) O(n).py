# 106. Construct Binary Tree from Inorder and Postorder Traversal

# * The root is always the last element in postorder
# *     - Inorder -> L N R
# *     - Postorder -> L R N
# * The inorder traversal alone doesn't give us enough info to determine where the root is
# * The postorder traversal tells us the nodes we need to find
# * We can then use the inorder traversal to determine which nodes are part of which subtree

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
    def buildTree(self, inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        def solve(left: int, right: int) -> Optional[TreeNode]:
            nonlocal postorder_index

            # * Base Case: Out of Bounds
            if left > right:
                return None

            # * Pick a root from postorder
            val: int = postorder[postorder_index]
            root: TreeNode = TreeNode(val)
            postorder_index -= 1

            # * Find the split point within inorder (so we know the left/right subtree contents)
            mid: int = inorder_map[val]

            # * Build right first because we are building in reverse
            root.right = solve(mid + 1, right)
            root.left = solve(left, mid - 1)

            return root

        # * The root is postorder[-1] because the "root" is processed last
        postorder_index: int = len(postorder) - 1

        # * Avoids the necessity to call list.index to find the split point within inorder
        inorder_map: dict[int, int] = {val: i for i, val in enumerate(inorder)}

        return solve(0, postorder_index)


sol = Solution()
print(sol.buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3]))

# * Time: O(n) - Each node is processed once and it takes O(n) to build the inorder_map

# * Space: O(n) - The inorder map's size scales with `n`, as does the maximum recursion depth
