class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def traverse(root, val):
            if not root:
                return

            val += root.val

            if not root.left and not root.right:
                if val == targetSum:
                    return True

            return traverse(root.left, val) or traverse(root.right, val)

        return traverse(root, 0)
