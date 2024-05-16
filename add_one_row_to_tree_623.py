from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def addOneRow(self, root, val: int, depth: int):
        if depth == 1:
            return TreeNode(val, root, None)

        height = 1

        dq = deque([root])

        while dq:
            dq_len = len(dq)

            if height == depth-1:
                for node in dq:
                    cur_left = node.left
                    cur_right = node.right
                    node.left = TreeNode(val, cur_left, None)
                    node.right = TreeNode(val, None, cur_right)
                break

            while dq_len:
                node = dq.popleft()
                dq_len -= 1

                if node.left:
                    dq.append(node.left)

                if node.right:
                    dq.append(node.right)

            height += 1

        return root
