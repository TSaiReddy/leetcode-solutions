class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.curIdx = 0

    def buildTree(self, preorder, inorder):
        return self.insert(preorder, inorder)

    def insert(self,  preorder, inorder):
        idx = self.findIdx(inorder, preorder[self.curIdx])
        root = TreeNode(preorder[self.curIdx])
        self.curIdx += 1
        left = inorder[0:idx]
        right = inorder[idx+1:]

        if left:
            root.left = self.insert(preorder, left)
        if right:
            root.right = self.insert(preorder, right)

        return root

    def findIdx(self, arr, val):
        for i in range(len(arr)):
            if arr[i] == val:
                return i


s = Solution()
s.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
