class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root):
        result = []

        if not root:
            return result

        queue = [root]
        cur_direction = "left"
        while queue:
            sub_arr = []
            queue_len = len(queue)

            while queue_len > 0:
                node = queue.pop(0)
                sub_arr.append(node.val)
                queue_len -= 1

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(sub_arr if cur_direction ==
                          "left" else reversed(sub_arr))
            cur_direction = "right" if cur_direction == "left" else "left"
        return result
