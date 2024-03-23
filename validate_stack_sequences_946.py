class Solution:
    def validateStackSequences(self, pushed, popped) -> bool:
        stack = []
        idx = 0

        for i in pushed:
            stack.append(i)
            while stack and stack[-1] == popped[idx]:
                stack.pop()
                idx += 1

        return not stack


s = Solution()
print(s.validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
