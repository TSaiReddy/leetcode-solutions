from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        dq = deque([root])
        parents = {}
        leafs = []

        while dq:
            dq_len = len(dq)
            arr = []

            while dq_len:
                node = dq.popleft()
                dq_len -= 1
                arr.append(node)

                if node.left:
                    dq.append(node.left)
                    parents[node.left] = node

                if node.right:
                    dq.append(node.right)
                    parents[node.right] = node

            leafs.append(arr)

        l = leafs[-1]
        while len(l) > 1:
            l = list(set([parents[ele] for ele in l]))

        return l.pop()
