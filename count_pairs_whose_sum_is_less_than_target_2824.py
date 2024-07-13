from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        # count = 0
        # arr_len = len(nums)
        # for i in range(arr_len):
        #     for j in range(i+1, arr_len):
        #         if nums[i]+nums[j] < target:
        #             count += 1

        # return count

        nums.sort()
        count = 0

        left = 0
        right = len(nums)-1

        while left < right:
            if nums[left]+nums[right] < target:
                count += (right-left)
                left += 1
            else:
                right -= 1
        return count
