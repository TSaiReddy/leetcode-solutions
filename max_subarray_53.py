class Solution:
    def maxSubArray(self, nums) -> int:
        maxSum = nums[0]
        curSum = 0

        for i in nums:
            curSum = max(i+curSum, i)
            maxSum = max(maxSum, curSum)

        print(curSum, "ppp", maxSum)
