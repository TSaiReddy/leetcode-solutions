class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root, val: int):
        while root:
            if root.val == val:
                return root
            if val < root.val:
                root = root.left
            else:
                root = root.right
        else:
            return None
