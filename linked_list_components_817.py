class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def numComponents(self, head, nums):
        current = head

        count = 0
        isBreak = True

        while current:
            if current.val in nums:
                if isBreak:
                    count += 1
                isBreak = False
            else:
                isBreak = True
            current = current.next

        return count


head = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))

solution = Solution()
solution.numComponents(head, [0, 3, 1, 4])
