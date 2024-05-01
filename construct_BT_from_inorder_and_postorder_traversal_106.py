class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.curIdx = -1

    def buildTree(self, inorder, postorder):
        idx, left, right = self.findIdx(inorder, postorder[self.curIdx])
        print(idx, left, right)
        root = TreeNode(inorder[idx])
        self.curIdx -= 1
        if left:
            root.left = self.buildTree(left, postorder)
        if right:
            root.right = self.buildTree(right, postorder)
        return root

    def findIdx(self, arr, val):
        for idx, item in enumerate(arr):
            if item == val:
                left = arr[0:idx]
                right = arr[idx+1:]
                return idx, left, right
        return 0, [], []


s = Solution()
s.buildTree([9, 3, 15, 20, 7],   [9, 15, 7, 20, 3])
