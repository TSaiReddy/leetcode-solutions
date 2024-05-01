class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = 0

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.traverse(root, '')
        return self.result

    def traverse(self, root, val):
        if not root:
            return None

        val = val+str(root.val)
        if not root.left and not root.right:
            self.result += int(val, 2)

        if root.left:
            self.traverse(root.left, val)

        if root.right:
            self.traverse(root.right, val)
