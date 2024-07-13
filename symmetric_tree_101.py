from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        status = True

        def traverse(left, right):
            nonlocal status
            if not left and not right:
                return
            elif not right or not left:
                status = False
                return
            elif left and right and left.val != right.val:
                status = False
                return
            else:
                traverse(left.left, right.right)
                traverse(left.right, right.left)

        traverse(root.left, root.right)
        return status
