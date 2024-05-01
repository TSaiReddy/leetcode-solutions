class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def evaluateTree(self, root) -> bool:
        if not root:
            return 0

        if root.val == 1:
            return 1

        left = self.evaluateTree(root.left)
        right = self.evaluateTree(root.right)

        if root.val == 3:
            return left and right
        else:
            return left or right
