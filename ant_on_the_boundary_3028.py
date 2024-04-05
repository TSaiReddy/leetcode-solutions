class Solution:
    def returnToBoundaryCount(self, nums) -> int:
        count = sum = 0

        for i in nums:
            sum += i
            if sum == 0:
                count += 1

        return count


s = Solution()
print(s.returnToBoundaryCount([3, 2, -3, -4]))
