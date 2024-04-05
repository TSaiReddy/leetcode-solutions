from collections import OrderedDict


class Solution:

    def firstUniqChar(self, s: str) -> int:
        hash = OrderedDict()
        for char in s:
            hash[char] = (hash.get(char, 0) or 0) + 1

        for i, char in enumerate(s):
            if hash[char] == 1:
                return i

        return -1


s = Solution()
print(s.firstUniqChar("leetcode"))
