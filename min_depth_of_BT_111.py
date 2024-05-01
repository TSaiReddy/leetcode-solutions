class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root) -> int:
        if not root:
            return 0

        depth = 1
        result = [root]
        while root:
            result_len = len(result)

            while result_len > 0:
                cur = result.pop(0)
                result_len -= 1
                if not cur.left and not cur.right:
                    return depth

                if cur.left:
                    result.append(cur.left)

                if cur.right:
                    result.append(cur.right)
            depth += 1
