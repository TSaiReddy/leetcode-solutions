class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.arr = []

    def getMinimumDifference(self, root) -> int:

        self._inOrder(root)

        minDiff = float("inf")

        arrLen = len(self.arr)
        for i in range(1, arrLen):
            minDiff = min(minDiff, abs(self.arr[i]-self.arr[i-1]))

        return minDiff

    def _inOrder(self, node):
        if not node:
            return node

        if node.left:
            self._inOrder(node.left)
        self.arr.append(node.val)
        if node.right:
            self._inOrder(node.right)

        return node
