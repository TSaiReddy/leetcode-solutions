class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.root = None

    def bstFromPreorder(self, preorder):
        if not preorder:
            return self.root
        self.root = TreeNode(preorder[0])

        for value in preorder[1:]:
            self._insert(self.root, value)

        return self.root

    def _insert(self, node, value):
        if node.val > value:
            if not node.left:
                node.left = TreeNode(value)
            else:
                self._insert(node.left, value)
        else:
            if not node.right:
                node.right = TreeNode(value)
            else:
                self._insert(node.right, value)


s = Solution()
s.bstFromPreorder([8, 5, 1, 7, 10, 12])
