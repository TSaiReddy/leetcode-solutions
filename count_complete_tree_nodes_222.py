from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def leftHeight(node) -> int:
            height = 0
            while node:
                height += 1
                node = node.left
            return height

        def rightHeight(node) -> int:
            height = 0
            while node:
                height += 1
                node = node.right
            return height

        left = leftHeight(root)
        right = rightHeight(root)

        if left == right:
            return 2**left - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
