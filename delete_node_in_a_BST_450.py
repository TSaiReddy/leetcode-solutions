class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root, key: int):
        if not root:
            return root

        if root.val > key:
            root.left = self.deleteNode(root.left, key)

        if root.val < key:
            root.right = self.deleteNode(root.right, key)

        if root.val == key:
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            root.val = self.traverse(root.right)
            print(root.val)
            root.right = self.deleteNode(root.right, root.val)

        return root

    def traverse(self, node):
        if not node:
            return node

        if node.left:
            return self.traverse(node.left)

        return node.val


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(6)
root.right.right.right = TreeNode(7)


s = Solution()
s.deleteNode(root, 3)
