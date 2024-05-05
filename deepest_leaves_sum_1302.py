from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root) -> int:
        maxSum = 0

        if not root:
            return

        queue = deque([root])

        while queue:
            queueLen = len(queue)
            levelSum = 0

            while queueLen:
                node = queue.popleft()
                queueLen -= 1

                levelSum += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            maxSum = levelSum

        return maxSum
