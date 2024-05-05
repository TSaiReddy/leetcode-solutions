class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def removeLeafNodes(self, root, target: int):
        if not root:
            return

        if root.left:
            root.left = self.removeLeafNodes(root.left, target)

        if root.right:
            root.right = self.removeLeafNodes(root.right, target)

        if root.val == target and not root.left and not root.right:
            return None

        return root
