class Solution:

    def sortColors(self, nums) -> None:
        left = 0
        right = len(nums)-1

        i = 0
        while i <= right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
            elif nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
            else:
                i += 1

        print(nums)
        return nums


s = Solution()
s.sortColors([2, 0, 2, 1, 1, 0])
s.sortColors([2, 0, 1])
s.sortColors([1, 2, 0])
