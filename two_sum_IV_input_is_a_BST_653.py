class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.hash = {}

    def findTarget(self, root, k: int) -> bool:
        if not root:
            return False

        if self.hash.get(k-root.val) != None:
            return True

        self.hash[root.val] = root.val
        return self.findTarget(root.left, k) or self.findTarget(root.right, k)
