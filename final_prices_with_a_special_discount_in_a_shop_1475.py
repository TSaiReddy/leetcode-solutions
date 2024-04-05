class Solution:

    def finalPrices(self, prices):
        stack = []

        for i in range(len(prices)):
            cur_price = prices[i]
            while stack and cur_price <= prices[stack[-1]]:
                idx = stack.pop()
                prices[idx] -= cur_price

            stack.append(i)

        return prices


s = Solution()
print(s.finalPrices([8, 4, 6, 2, 3]))
print(s.finalPrices([1, 2, 3, 4, 5]))
print(s.finalPrices([8, 7, 4, 2, 8, 1, 7, 7, 10, 1]))
