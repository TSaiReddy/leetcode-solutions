class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:

    def __init__(self, root):
        self.hash = set()

        def recover(root, val):
            if root:
                root.val = val
                self.hash.add(val)
            if root.left:
                root.left = recover(root.left, 2*root.val+1)
            if root.right:
                root.right = recover(root.right, 2*root.val+2)

            return root
        recover(root, 0)
        print(self.hash)

    def find(self, target: int) -> bool:
        return target in self.hash

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
