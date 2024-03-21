class Solution:

    def timeRequiredToBuy(self, tickets, k):
        value, seconds = 0, 0
        for i in range(len(tickets)):
            if i == k:
                value = tickets[i]
                break

        for i in range(len(tickets)):
            if i <= k:
                if tickets[i] <= value:
                    seconds += tickets[i]
                else:
                    seconds += value
            else:
                if tickets[i] <= value:
                    seconds += tickets[i]
                else:
                    seconds += value-1

        return seconds


s = Solution()
# s.timeRequiredToBuy([2, 3, 2], 2)
# s.timeRequiredToBuy([5, 1, 1, 1], 0)
print(s.timeRequiredToBuy([84, 49, 5, 24, 70, 77, 87, 8], 3))
