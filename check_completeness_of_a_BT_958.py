from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        result = True
        if not root:
            return result

        dq = deque([root])

        while dq:

            node = dq.popleft()
            if node:
                dq.append(node.left)
                dq.append(node.right)
            else:
                while dq:
                    if dq.popleft():
                        return False

        return True
