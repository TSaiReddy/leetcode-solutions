class Solution:

    def minOperations(self, logs) -> int:
        stack = []

        for log in logs:
            if log == "./":
                continue
            elif stack and log == "../":
                stack.pop()
            elif log != "../" and log != "./":
                stack.append(log)

        print(len(stack), stack)
        return len(stack)


s = Solution()
s.minOperations(["d1/", "d2/", "../", "d21/", "./"])

s1 = Solution()
s1.minOperations(["./", "../", "./"])

s2 = Solution()
s2.minOperations(["d1/", "../", "../", "../"])
