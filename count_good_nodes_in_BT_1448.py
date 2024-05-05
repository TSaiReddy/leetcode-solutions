class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def goodNodes(self, root: TreeNode) -> int:
        total = 0

        def traverse(node, max_val):
            if not node:
                return

            nonlocal total

            if max_val >= node.val:
                total += 1
                max_val = node.val

            if node.left:
                traverse(node.left, max_val)

            if node.right:
                traverse(node.right, max_val)

        traverse(root, root.val)
        return total
