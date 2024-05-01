class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, root) -> bool:
        val = root.val

        return self.traverse(root, val)

    def traverse(self, node, val):
        if not node:
            return True
        if node.val != val:
            return False

        return self.isUnivalTree(node.left) and self.isUnivalTree(node.right)
