class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def __init__(self) -> None:
#         self.root = None

#     def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
#         if not nums:
#             return self.root

#         mid = len(nums)//2
#         left = nums[:mid]
#         right = nums[mid+1:]

#         if not self.root:
#             self.root = TreeNode(nums[mid])
#         else:
#             self._insert(self.root, nums[mid])

#         self.sortedArrayToBST(left)
#         self.sortedArrayToBST(right)

#         return self.root

#     def _insert(self, node, num):
#         if not node:
#             node = TreeNode(num)

#         if num < node.val:
#             node.left = self._insert(node.left, num)
#         if num > node.val:
#             node.right = self._insert(node.right, num)
#         return node


class Solution:

    def sortedArrayToBST(self, nums):
        if not nums:
            return None

        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid+1:]

        root = TreeNode(nums[mid])

        root.left = self.sortedArrayToBST(left)
        root.right = self.sortedArrayToBST(right)

        return root


s = Solution()
s.sortedArrayToBST([-10, -3, 0, 5, 9])
