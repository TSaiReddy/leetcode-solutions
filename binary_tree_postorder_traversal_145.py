class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root):
        result = []

        self._postOrder(root, result)
        return result

    def _postOrder(self, root, result):
        # left, right, root
        if not root:
            return root

        if root.left:
            self._postOrder(root.left, result)

        if root.right:
            self._postOrder(root.right, result)

        result.append(root.val)
