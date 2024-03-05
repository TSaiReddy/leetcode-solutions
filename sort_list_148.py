class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def splitList(self, head):
        tortoise, hare = head, head

        while hare.next and hare.next.next:
            tortoise = tortoise.next
            hare = hare.next.next

        return tortoise

    def merge(self, left, right):
        tail = dummy = ListNode()

        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next

            tail = tail.next

        if left:
            tail.next = left

        if right:
            tail.next = right

        return dummy.next

    def sortList(self, head):
        if not head or not head.next:
            return head

        left = head
        right = self.splitList(head)

        # Splitting list into two
        temp = right.next
        right.next = None
        right = temp

        left = self.sortList(left)
        right = self.sortList(right)

        return self.merge(left, right)


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
solution = Solution()
solution.sortList(head)
