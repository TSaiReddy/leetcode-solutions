class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head):
        if not head or not head.next:
            return False

        tortoise = head
        hare = head.next

        while hare and hare.next:
            if tortoise == hare:
                return True

            tortoise = tortoise.next
            hare = hare.next.next

        return False
