class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.sum = 0
        self.prev = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        self._traverse(root)
        self.assignValues(root)
        return root

    def assignValues(self, root):
        if not root:
            return None

        if root.left:
            self.assignValues(root.left)

        self.prev = root.val
        root.val = self.sum
        self.sum -= self.prev

        if root.right:
            self.assignValues(root.right)

    def _traverse(self, root):
        if not root:
            return None

        self.sum += root.val
        if root.left:
            self._traverse(root.left)

        if root.right:
            self._traverse(root.right)


root = TreeNode(4)
root.left = TreeNode(1)
root.left.left = TreeNode(0)
root.left.right = TreeNode(2)
root.left.right.right = TreeNode(3)
root.right = TreeNode(6)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(8)
s = Solution()
s.bstToGst(root)
