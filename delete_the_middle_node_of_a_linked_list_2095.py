class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


class Solution:
    def deleteMiddle(self, head):
        if not head or not head.next:
            return None
        tortoise = head
        hare = head.next

        while tortoise and hare.next and hare.next.next:
            tortoise = tortoise.next
            hare = hare.next.next

        tortoise.next = tortoise.next.next
        print_linked_list(head)
        return head


head = ListNode(1)
solution = Solution()
solution.deleteMiddle(head)
