class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root) -> str:
        """Encodes a tree to a single string.
        """

        tree_to_str = ""

        def traverse(root):
            nonlocal tree_to_str
            if not root:
                return

            tree_to_str += str(root.val)+","
            if root.left:
                traverse(root.left)

            if root.right:
                traverse(root.right)

        traverse(root)
        return tree_to_str

    def deserialize(self, data: str):
        """Decodes your encoded data to tree.
        """

        arr = list(map(int, data.strip(",").split(",")))
        root = TreeNode(arr.pop(0))

        def insert(node, val):
            if not node:
                return TreeNode(val)

            if node.val > val:
                node.left = insert(node.left, val)

            if node.val < val:
                node.right = insert(node.right, val)

            return node

        for s in arr:
            insert(root, s)

        return root


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

ser = Codec()
deser = Codec()
tree = ser.serialize(root)
ans = deser.deserialize(tree)
