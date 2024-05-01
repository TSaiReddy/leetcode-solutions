class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.result = "~"

    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.traverse(root, "")
        return self.result

    def traverse(self, root, val):
        if not root:
            return

        val = chr(root.val+97)+val

        if not root.left and not root.right:
            self.result = min(self.result, val)

        self.traverse(root.left, val)
        self.traverse(root.right, val)
