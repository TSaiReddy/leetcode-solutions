from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        arr1, arr2 = [], []

        def traverse(node, arr):
            if not node:
                return

            if not node.left and not node.right:
                arr.append(node.val)

            if node.left:
                traverse(node.left, arr)

            if node.right:
                traverse(node.right, arr)

        traverse(root1, arr1)
        traverse(root2, arr2)

        if arr1 == arr2:
            return True
        return False
