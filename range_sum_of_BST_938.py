class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root, low: int, high: int) -> int:
        result = 0
        if root:
            if root.val >= low and root.val <= high:
                result += root.val
        if root.left:
            result += self.rangeSumBST(root.left, low, high)
        if root.right:
            result += self.rangeSumBST(root.right, low, high)
        return result
