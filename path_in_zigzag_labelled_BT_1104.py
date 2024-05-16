from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathInZigZagTree(self, label: int):
        arr = deque([[1]])

        sub_arr = []
        for num in range(2, label+1):
            sub_arr.append(num)
            if len(sub_arr) == len(arr[-1]) * 2:
                arr.append(sub_arr)
                sub_arr = []

        if sub_arr:
            arr.append(sub_arr)

        level = 1
        root = TreeNode(arr.popleft()[0])
        queue = deque([(root, level)])

        while queue and len(arr):
            queue_len = len(queue)
            ele = arr.popleft()

            node, level = queue.popleft()
            queue_len -= 1
            left_val = ele.pop(
                0) if level % 2 == 0 else ele.pop() if ele else None
            right_val = ele.pop(
                0) if level % 2 == 0 else ele.pop() if ele else None

            if left_val:
                node.left = TreeNode(left_val)
                queue.append((node.left, level + 1))

            if right_val:
                node.right = TreeNode(right_val)
                queue.append((node.right, level + 1))

        print("after", root)
        return root


s = Solution()
s.pathInZigZagTree(14)
