class Solution:
    def maxSlidingWindow(self, nums, k: int):
        arr = []
        deque = []  # should only contains k size elements

        # Processing only the first window, so that left element in deque is large and
        # next to elements are less that it's previous values
        for i in range(k):
            while deque and nums[i] > deque[-1]:
                deque.pop()
            deque.append(nums[i])

        arr.append(deque[0])

        # Processing the remaining elements
        for j in range(k, len(nums)):
            # Remove the first element from deque if it's outside the window
            if deque and deque[0] == nums[j - k]:
                deque.pop(0)

            # Insert the new element into deque
            while deque and nums[j] > deque[-1]:
                deque.pop()
            deque.append(nums[j])

            # Append the maximum element to the result array
            arr.append(deque[0])

        return arr


s = Solution()
print(s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7],  3))
print(s.maxSlidingWindow([1, 3, 1, 2, 0, 5],  3))
