from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_counter = Counter(s)
        t_counter = Counter(t)
        min_nums = 0

        for k, v in s_counter.items():
            if v > t_counter[k]:
                min_nums += v-t_counter[k]
            elif not t_counter[k]:
                min_nums += v

        return min_nums


s = Solution()
# s.minSteps("bab", "aba")
s.minSteps("leetcode", "practice")
