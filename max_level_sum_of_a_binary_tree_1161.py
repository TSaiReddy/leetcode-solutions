class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root):
        if not root:
            return root

        level = 1
        max_level = 1
        max_sum = root.val
        queue = [root]

        while queue:
            cur_sum = 0
            queue_len = len(queue)

            while queue_len > 0:
                node = queue.pop(0)
                queue_len -= 1
                cur_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if cur_sum > max_sum:
                max_sum = cur_sum
                max_level = level
            level += 1
        return max_level
