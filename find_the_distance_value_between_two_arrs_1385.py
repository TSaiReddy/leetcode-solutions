from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:

        arr2.sort()
        count = 0

        for ele in arr1:
            left, right = 0, len(arr2) - 1
            isMatch = True

            while left <= right:
                mid = (left + right) // 2
                if abs(ele - arr2[mid]) <= d:
                    isMatch = False
                    break
                elif arr2[mid] < ele:
                    left = mid + 1
                else:
                    right = mid - 1

            if isMatch:
                count += 1

        return count
