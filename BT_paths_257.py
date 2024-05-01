class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.result = []

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.traverse(root, "")
        return self.result

    def traverse(self, root, val):
        if not root:
            return

        val += str(root.val)+"->"

        if not root.left and not root.right:
            self.result.append(val[:-2])

        if root.left:
            self.traverse(root.left, val)
        if root.right:
            self.traverse(root.right, val)
