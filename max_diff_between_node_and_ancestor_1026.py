class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root) -> int:

        final_max = float("-inf")

        def traverse(node, min_val, max_val):
            nonlocal final_max
            if not node:
                return

            val = node.val

            min_val = min(val, min_val)
            max_val = max(val, max_val)

            if node.left:
                traverse(node.left, min_val, max_val)

            if node.right:
                traverse(node.right, min_val, max_val)

            final_max = max(final_max,  abs(min_val-max_val))

        traverse(root, root.val, root.val)
        return final_max
