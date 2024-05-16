from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root) -> bool:
        result = True
        level = 0

        dq = deque([root])

        while dq:
            dq_len = len(dq)
            arr = deque([])

            while dq_len:
                node = dq.popleft()
                dq_len -= 1
                arr.append(node.val)

                if node.left:
                    dq.append(node.left)

                if node.right:
                    dq.append(node.right)

            even_or_odd = level % 2 == 0
            arr_len = len(arr)
            for idx, ele in enumerate(arr):
                if arr_len > idx+1:
                    if even_or_odd:
                        if ele >= arr[idx+1]:
                            result = False
                            break
                    else:
                        if ele <= arr[idx+1]:
                            result = False
                            break

                if ele % 2 != even_or_odd:
                    result = False
                    break

            if result == False:
                return result

            level += 1

        return result
