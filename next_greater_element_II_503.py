# class Solution:
#     def nextGreaterElement(self, nums):
#         nums = nums+nums
#         arr = []
#         stack = []
#         for i in range(len(nums) - 1, -1, -1):
#             if not stack:
#                 stack.append(nums[i])
#                 arr.append(-1)
#             else:
#                 for j in range(len(stack) - 1, -1, -1):
#                     if nums[i] < stack[j]:
#                         arr.insert(0, stack[j])
#                         stack.append(nums[i])
#                         break
#                     if nums[i] >= stack[j]:
#                         stack.pop()
#                     if not stack:
#                         arr.insert(0, -1)
#                         stack.append(nums[i])
#                         break

#         print(arr[0: int(len(nums)/2)])
#         return arr[0: int(len(nums)/2)]


# s1 = Solution()
# s1.nextGreaterElement([1, 2, 1])
# # s1.nextGreaterElement([5, 4, 3, 2, 1])


class Solution:
    def nextGreaterElement(self, nums):
        nums = nums+nums
        arr = []

        for i in range(int(len(nums)/2)):
            arr.append(-1)
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    arr[-1] = nums[j]
                    break
        return arr


s1 = Solution()
s1.nextGreaterElement([1, 2, 1])
# s1.nextGreaterElement([5, 4, 3, 2, 1])
# s1.nextGreaterElement([1, 5, 3, 6, 8])
