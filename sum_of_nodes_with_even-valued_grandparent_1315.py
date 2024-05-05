from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        result = 0

        if not root:
            return 0

        dp = deque([(root, None, None)])

        while dp:

            node, parent, grandParent = dp.popleft()

            if grandParent and node.val % 2 == 0:
                result += node.val

            if node.left:
                dp.append((node.left, node, parent))
            if node.right:
                dp.append((node.right, node, parent))
        return result
