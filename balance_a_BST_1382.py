class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        result = []
        self._inOrder(root, result)
        return self.construct(result)

    def construct(self,  arr) -> TreeNode:
        arrLen = len(arr)
        if arrLen == 0:
            return None
        mid = arrLen//2
        left = arr[:mid]
        right = arr[mid+1:]

        root = TreeNode(arr.pop(mid))
        root.left = self.construct(left)
        root.right = self.construct(right)
        return root

    def _inOrder(self, node, result):
        if not node:
            return node

        if node.left:
            self._inOrder(node.left, result)
        result.append(node.val)
        if node.right:
            self._inOrder(node.right, result)
        return node
