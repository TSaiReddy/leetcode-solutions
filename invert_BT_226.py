from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root):
        dq = deque([root])

        while dq:
            for _ in range(len(dq)):
                node = dq.popleft()
                node.left, node.right = node.right, node.left

                if node.left:
                    dq.append(node.left)

                if node.right:
                    dq.append(node.right)

        return root
