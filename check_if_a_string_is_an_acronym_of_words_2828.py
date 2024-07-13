from typing import List


class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        if len(words) > len(s) or len(s) > len(words):
            return False
        for idx, word in enumerate(words):
            if word[0] != s[idx]:
                return False

        return True
