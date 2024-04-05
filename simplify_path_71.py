class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        arr = path.split("/")

        for char in arr:
            if not stack and char == "..":
                continue
            elif char == "." or char == "":
                continue
            elif stack and char == "..":
                stack.pop()
            else:
                stack.append(char)

        res = "/" + "/".join(stack)
        print(res)


s = Solution()
s.simplifyPath("/home/")
s.simplifyPath("/../")
s.simplifyPath("/home//foo/")
s.simplifyPath("/home/foo/../")
s.simplifyPath("/../home/user/Documents")
s.simplifyPath("/home/user/../../usr/local/bin")
s.simplifyPath("/home/user/./Downloads/../Pictures/././")
