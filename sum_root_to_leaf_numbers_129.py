class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = 0

        def traverse(root, val):
            nonlocal result
            if not root:
                return

            val += str(root.val)

            if not root.left and not root.right:
                result += int(val)

            traverse(root.left, val)
            traverse(root.right, val)

        traverse(root, "")
        return result
