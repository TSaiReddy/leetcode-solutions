class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode):
        result = []
        self._inOrder(root1, result)
        self._inOrder(root2, result)
        return sorted(result)

    def _inOrder(self, node, result):
        if not node:
            return node

        if node.left:
            node.left = self._inOrder(node.left, result)

        result.append(node.val)
        if node.right:
            node.left = self._inOrder(node.right, result)
