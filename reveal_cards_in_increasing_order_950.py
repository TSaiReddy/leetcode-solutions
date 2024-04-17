

class Solution:
    # def deckRevealedIncreasing(self, deck):
    #     sortedDeck = sorted(deck)
    #     result = []
    #     arr = []

    #     for i in range(len(sortedDeck)):
    #         result.append(i)
    #         arr.append(i)

    #     while result:
    #         k = result.pop(0)
    #         arr[k] = sortedDeck.pop(0)
    #         if result:
    #             result.append(result.pop(0))

    #     print(arr)
    #     return arr

    def deckRevealedIncreasing(self, deck):
        sortedDeck = sorted(deck)
        result = []

        while sortedDeck:
            if result:
                result.insert(0, result.pop())
            result.insert(0, sortedDeck.pop())

        return result


s = Solution()
s.deckRevealedIncreasing([17, 13, 11, 2, 3, 5, 7])  # [2,13,3,11,5,17,7]
