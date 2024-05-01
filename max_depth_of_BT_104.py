class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root) -> int:
        depth = 0
        if not root:
            return depth
        queue = [root]

        while queue:
            queue_len = len(queue)

            while queue_len > 0:
                cur = queue.pop(0)
                queue_len -= 1

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

            depth += 1
        return depth
