class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        dummy = ListNode(0)
        current = dummy

        while l1 or l2 or carry:
            sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry

            carry, reminder = divmod(sum, 10)

            current.next = ListNode(reminder)
            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


head1 = ListNode(9, ListNode(9, ListNode(
    9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
head2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))

solution = Solution()
solution.addTwoNumbers(head1, head2)
