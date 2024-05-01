class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.result = 0

    def averageOfSubtree(self, root: TreeNode) -> int:

        def traverse(root):
            if not root:
                return 0, 0

            left_sum, left_len = traverse(root.left)
            right_sum, right_len = traverse(root.right)

            total_sum = left_sum + right_sum + root.val
            total_len = left_len + right_len + 1

            if total_sum // total_len == root.val:
                self.result += 1

            return total_sum, total_len

        traverse(root)
        print(self.result)


root = TreeNode(4)
root.left = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(1)
root.right = TreeNode(5)
root.right.right = TreeNode(6)


s = Solution()
s.averageOfSubtree(root)
