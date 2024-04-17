class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.root = None

    def sortedListToBST(self, head):
        nums = []

        while head:
            nums.append(head.val)
            head = head.next

        self.sortedArrayToBST(nums)
        return self.root

    def sortedArrayToBST(self, nums):
        if not nums:
            return self.root

        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid+1:]

        if not self.root:
            self.root = TreeNode(nums[mid])
        else:
            self._insert(self.root, nums[mid])

        self.sortedArrayToBST(left)
        self.sortedArrayToBST(right)

    def _insert(self, node, num):
        if not node:
            node = TreeNode(num)

        if num < node.val:
            node.left = self._insert(node.left, num)
        if num > node.val:
            node.right = self._insert(node.right, num)
        return node
