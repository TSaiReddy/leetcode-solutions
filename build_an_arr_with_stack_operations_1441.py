class Solution:
    def buildArray(self, target, n):
        stack = []

        for i in range(n):
            if not target:
                return stack
            if i+1 == target[0]:
                stack.append("Push")
                target.pop(0)
            else:
                stack.extend(["Push", "Pop"])

        return stack


s = Solution()
print(s.buildArray([1, 3], 3))
print(s.buildArray([1, 2, 3], 3))
print(s.buildArray([1, 2], 4))
