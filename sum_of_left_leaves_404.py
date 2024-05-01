class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root) -> int:
        total_sum = 0
        has_left = False

        def traverse(node, has_left):
            nonlocal total_sum

            if not node.left and not node.right and has_left:
                total_sum += node.val

            if node.left:
                has_left = True
                traverse(node.left, has_left)

            if node.right:
                has_left = False
                traverse(node.right, has_left)

        traverse(root, has_left)
        return total_sum
