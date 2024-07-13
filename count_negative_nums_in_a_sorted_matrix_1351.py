from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        total = 0
        for arr in grid:
            left = 0
            right = len(arr)

            while left < right:
                mid = (left+right)//2
                if arr[mid] >= 0:
                    left = mid+1
                else:
                    total += right-mid
                    right = mid

        return total


s = Solution()
s.countNegatives([[4, 3, 2, -1], [3, 2, 1, -1],
                 [1, 1, -1, -2], [-1, -1, -2, -3]])


s.countNegatives([[3, 2], [1, 0]])
