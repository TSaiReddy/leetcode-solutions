from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left, right = 0, len(numbers) - 1

        while left <= right:
            cur_sum = numbers[left] + numbers[right]
            if cur_sum == target:
                return [left+1, right+1]
            elif cur_sum > target:
                right -= 1
            else:
                left += 1


s = Solution()
s.twoSum([5, 25, 75], 100)
