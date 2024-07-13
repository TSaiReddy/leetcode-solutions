from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        status = True

        def traverse(node, left, right):
            if not node:
                return
            nonlocal status
            if status:
                if node.left:
                    left += 1
                    traverse(node.left,   left, right)

                if node.right:
                    right += 1
                    traverse(node.right,   left, right)

            if abs(left-right) > 1:
                status = False
                return

        traverse(root, 0, 0)
        return status
