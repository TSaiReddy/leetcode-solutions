class Solution:
    def nextGreaterElement(self, nums1, nums2):
        hash = {}

        for i in range(len(nums2)):
            key = nums2[i]
            hash[key] = -1

            for j in range(i+1, len(nums2)):
                if key < nums2[j]:
                    hash[key] = nums2[j]
                    break

        arr = []
        for num in nums1:
            arr.append(hash[num])

        return arr


s = Solution()
s.nextGreaterElement([4, 1, 2], [1, 3, 4, 2])

s1 = Solution()
s1.nextGreaterElement([1, 3, 5, 2, 4], [6, 5, 4, 3, 2, 1, 7])
