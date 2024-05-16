class Solution:
    def reverse(self, x: int) -> int:
        s = int("-"+str(x)[:0:-1]) if x < 0 else int(str(x)[::-1])
        return 0 if 2**-31 < s or 2**31 > s else s


s = Solution()
s.reverse(123)
