class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums):
        ele, left, right = self.getMaxValueWithIdx(nums)
        root = TreeNode(ele)

        if left:
            root.left = self.constructMaximumBinaryTree(left)

        if right:
            root.right = self.constructMaximumBinaryTree(right)

        return root

    def getMaxValueWithIdx(self, nums):
        maxVal = float("-inf")
        maxValIdx = 0
        for idx, val in enumerate(nums):
            if maxVal < val:
                maxVal = val
                maxValIdx = idx

        return maxVal, nums[:maxValIdx], nums[maxValIdx+1:]


s = Solution()
s.constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])
