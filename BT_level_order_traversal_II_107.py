class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def levelOrderBottom(self, root):
        result = []
        if not root:
            return result

        queue = [root]

        while queue:
            arr_len = len(queue)
            sub_arr = []

            while arr_len > 0:
                node = queue.pop(0)
                sub_arr.append(node.val)
                arr_len -= 1

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.insert(0, sub_arr)

        return result
