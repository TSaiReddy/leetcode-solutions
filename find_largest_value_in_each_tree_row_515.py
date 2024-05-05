class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root):
        result = []

        if not root:
            return result

        queue = [root]

        while queue:
            queue_len = len(queue)
            max_val = float("-inf")

            while queue_len:
                node = queue.pop(0)
                queue_len -= 1
                if node.val > max_val:
                    max_val = node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(max_val)

        return result
