class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root):
        result = []

        if not root:
            return result

        queue = [root]

        while queue:
            queue_len = len(queue)
            sub_arr = []

            while queue_len:
                node = queue.pop(0)
                queue_len -= 1
                sub_arr.append(node.val)

                if node.right:
                    queue.append(node.right)

                if node.left:
                    queue.append(node.left)
            result.append(sub_arr.pop(0))

        return result
