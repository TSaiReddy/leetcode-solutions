from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        if not root:
            return "None"

        tree_left = self.serialize(root.left)
        tree_right = self.serialize(root.right)

        return str(root.val) + "," + tree_left + ","+tree_right

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        dq = deque(data.split(","))

        def construct(dq):
            if not dq:
                return

            val = dq.popleft()
            if val == "None":
                return None

            root = TreeNode(val)
            root.left = construct(dq)
            root.right = construct(dq)
            return root

        return construct(dq)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
