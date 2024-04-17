class Solution:
    def maxSubarraySumCircular(self, nums) -> int:
        maxSum = nums[0]
        curSum = 0
        curMin = 0
        minVal = nums[0]
        total = 0

        for i in nums:
            total += i
            curSum = max(i+curSum, i)
            curMin = min(i+curMin, i)
            maxSum = max(maxSum, curSum)
            minVal = min(minVal, curMin)

        print(max(maxSum, total-minVal) if maxSum > 0 else maxSum)
        return max(maxSum, total-minVal) if maxSum > 0 else maxSum


s = Solution()
s.maxSubarraySumCircular([1, -2, 3, -2])
s.maxSubarraySumCircular([5, -3, 5])
s.maxSubarraySumCircular([-3, -2, -3])
