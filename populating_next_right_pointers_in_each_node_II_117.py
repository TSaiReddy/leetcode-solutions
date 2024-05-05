
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root):
        if not root:
            return

        queue = [root]
        while queue:
            queue_len = len(queue)

            while queue_len:
                node = queue.pop(0)
                queue_len -= 1

                node.next = None if queue_len == 0 else queue[0]

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return root
