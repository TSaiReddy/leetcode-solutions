class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root):
        if not root:
            return

        arr = [root]
        result = []

        while arr:
            subArr = []
            arr_len = len(arr)

            while arr_len > 0:
                node = arr.pop(0)
                subArr.append(node.val)
                arr_len -= 1

                if node.left:
                    arr.append(node.left)

                if node.right:
                    arr.append(node.right)

            result.append(self.avgVal(subArr))

        return result

    def avgVal(self, arr):
        total = 0
        l = 0
        for val in arr:
            total += val
            l += 1

        return total/l
