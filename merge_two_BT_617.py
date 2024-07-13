from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # if not root1 and not root2:
        #     return None

        # newTree = TreeNode()
        # queue = deque([(root1, root2, newTree)])

        # while queue:
        #     node1, node2, newNode = queue.popleft()

        #     if node1 or node2:
        #         val = 0
        #         if node1:
        #             val += node1.val
        #         if node2:
        #             val += node2.val

        #         newNode.val = val

        #         if node1 and node1.left or node2 and node2.left:
        #             newNode.left = TreeNode()
        #             queue.append((node1.left if node1 else None,
        #                          node2.left if node2 else None, newNode.left))

        #         if node1 and node1.right or node2 and node2.right:
        #             newNode.right = TreeNode()
        #             queue.append((node1.right if node1 else None,
        #                          node2.right if node2 else None, newNode.right))

        # return newTree

        ############ Other Solution ############

        if root1 and root2:
            root = TreeNode(root1.val+root2.val)
            root.left = self.mergeTrees(root1.left, root2.left)
            root.right = self.mergeTrees(root1.right, root2.right)
            return root
        else:
            return root1 or root2
