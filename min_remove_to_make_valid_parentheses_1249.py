class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        queue = []
        result = ""

        for i in range(len(s)):
            if s[i] == "(":
                queue.append(")")
                result += s[i]
            elif queue and queue[-1] == s[i]:
                queue.pop()
                result += s[i]
            elif not queue and s[i] == ")":
                pass
            else:
                result += s[i]

        while queue:
            for j in range(len(result)-1, -1, -1):
                if not queue:
                    break
                if result[j] == "(":
                    result = result[:j]+""+result[j+1:]
                    queue.pop()

        return result


s = Solution()
# s.minRemoveToMakeValid("lee(t(c)o)de)")
# s.minRemoveToMakeValid("a)b(c)d")
s.minRemoveToMakeValid("))((")
s.minRemoveToMakeValid("(a(b(c)d)")
