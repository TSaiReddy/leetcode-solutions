class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.stack = []
        self.stackLen = 0

    def kthSmallest(self, root, k: int) -> int:
        self._inOrder(root, k)
        return self.stack[k-1]

    def _inOrder(self, root, k):
        if not root:
            return
        self._inOrder(root.left, k)
        self.stack.append(root.val)
        self.stackLen += 1
        if k == self.stackLen:
            return
        self._inOrder(root.right, k)
