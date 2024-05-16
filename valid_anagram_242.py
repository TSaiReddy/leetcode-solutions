from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_val = Counter(s)
        t_val = Counter(t)
        return s_val == t_val
