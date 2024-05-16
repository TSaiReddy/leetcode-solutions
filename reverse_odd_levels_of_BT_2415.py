from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def reverseOddLevels(self, root):
        level = 0
        dq = deque([root])

        while dq:
            for _ in range(len(dq)):
                node = dq.popleft()

                if node.left:
                    dq.append(node.left)

                if node.right:
                    dq.append(node.right)

            level += 1
            if level % 2 != 0:
                left = 0
                right = len(dq)-1
                while left < right:
                    dq[left].val, dq[right].val = dq[right].val, dq[left].val
                    left += 1
                    right -= 1
        return root
