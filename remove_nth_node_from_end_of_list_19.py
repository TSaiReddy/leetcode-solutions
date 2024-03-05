class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):
        if not head or not head.next:
            return None

        dummy = ListNode(0, head)

        first = dummy
        second = dummy

        for _ in range(n):
            second = second.next

        while second.next:
            first = first.next
            second = second.next

        first.next = first.next.next
        return dummy.next


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
solution = Solution()
solution.removeNthFromEnd(head, 2)

# head = ListNode(1, ListNode(2, ListNode(3)))
# solution = Solution()
# solution.removeNthFromEnd(head, 2)
