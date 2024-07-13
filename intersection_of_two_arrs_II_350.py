from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash = {}
        result = []

        for num in nums1:
            if num in hash:
                hash[num] += 1
            else:
                hash[num] = 1

        for num in nums2:
            if num in hash and hash[num] > 0:
                hash[num] -= 1
                result.append(num)

        return result


s = Solution()
s.intersect([1, 2, 2, 1], [2, 2])
