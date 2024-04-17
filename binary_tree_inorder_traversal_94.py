class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root):
        result = []

        self._inOrder(root, result)
        return result

    def _inOrder(self, root, result):
        # left, root, right
        if not root:
            return root

        if root.left:
            self._inOrder(root.left, result)
        result.append(root.value)
        if root.right:
            self._inOrder(root.right, result)
