class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head) -> None:
        if not head or not head.next:
            return None

        # find middle value
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse elements from middle
        reverse = None
        while slow:
            temp = slow.next
            slow.next = reverse
            reverse = slow
            slow = temp

        # merging nodes
        merge = head
        while merge:
            temp1, temp2 = reverse.next, merge.next
            reverse.next = None
            merge.next = reverse
            reverse = temp1
            merge = merge.next
            merge.next = temp2
            merge = merge.next


head = ListNode(1, ListNode(2, ListNode(
    3, ListNode(4, ListNode(5)))))
solution = Solution()

solution.reorderList(head)
