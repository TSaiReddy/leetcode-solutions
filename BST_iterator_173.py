class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root):
        self.root = TreeNode(0)
        self.dummy = self.root

        self._inOrder(root)

    def _inOrder(self, node):
        if not node:
            return None

        if node.left:
            self._inOrder(node.left)

        self.dummy.right = TreeNode(node.val)
        self.dummy = self.dummy.right

        if node.right:
            self._inOrder(node.right)

    def next(self) -> int:
        self.root = self.root.right
        return self.root.val

    def hasNext(self) -> bool:
        return True if self.root.right else False


root = TreeNode(7)
root.left = TreeNode(3)
root.right = TreeNode(15)
root.right.left = TreeNode(9)
root.right.right = TreeNode(20)

# Initialize the Solution object with the root of the tree
solution = BSTIterator(root)
