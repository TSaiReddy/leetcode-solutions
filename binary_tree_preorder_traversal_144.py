class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root):
        result = []

        self._preOrder(root, result)
        return result

    def _preOrder(self, root, result):
        # root, left, right
        if not root:
            return root

        result.append(root.val)
        if root.left:
            self._preOrder(root.left, result)

        if root.right:
            self._preOrder(root.right, result)
