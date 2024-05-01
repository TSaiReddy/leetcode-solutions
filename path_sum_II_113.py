class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def traverse(root, val, arr):
            nonlocal result
            if not root:
                return []

            val += root.val
            arr = arr.copy()
            arr.append(root.val)

            if not root.left and not root.right:
                if val == targetSum:
                    result.append(arr)
                    arr = []

            traverse(root.left, val, arr)
            traverse(root.right, val, arr)

        return traverse(root, 0, [])
