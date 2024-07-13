from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        left = 0
        right = len(nums)-1
        result = []

        while left < right:
            mid = (left+right)//2
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid+1
            else:
                result.append(mid)
                i = mid-1
                j = mid+1
                while i >= 0 and nums[i] == target:
                    result.insert(0, i)
                    i -= 1
                while j <= len(nums)-1 and nums[j] == target:
                    result.append(j)
                    j += 1
                break
        if left == right and nums[left] == target:
            result.append(left)

        return result


s = Solution()
s.targetIndices([1, 2, 5, 2, 3], 2)
