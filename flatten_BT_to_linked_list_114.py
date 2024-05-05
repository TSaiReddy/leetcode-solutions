class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        current = root

        def flat(node):

            if not node:
                return

            nonlocal current

            temp_right = node.right

            if node.left:
                current.right = node.left
                node.left = None
                current = current.right
                flat(current)

            if temp_right:
                current.right = temp_right
                current = current.right
                flat(current)

        flat(root)
