

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = []

        for i in range(1, n+1):
            queue.append(i)

        i = 0
        while len(queue) > 1:
            idx = (i+k-1) % len(queue)
            queue.pop(idx)
            i = idx

        return queue[0]


s = Solution()
s.findTheWinner(5, 2)
