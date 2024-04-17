class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root):
        stack = []

        self._inOrder(root, stack)

        dummy = TreeNode(-1)
        result = dummy
        while stack:
            result.right = TreeNode(stack.pop(0))
            result = result.right

        return dummy.right

    def _inOrder(self, root, result):
        if not root:
            return root
        if root.left:
            self._inOrder(root.left, result)
        result.append(root.val)
        if root.right:
            self._inOrder(root.right, result)
