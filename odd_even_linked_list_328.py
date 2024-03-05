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
    def oddEvenList(self, head):
        if not head or not head.next:
            return head

        odd = head
        current = head.next
        even = current
        while current and current.next:
            odd.next = odd.next.next
            odd = odd.next
            current.next = current.next.next
            current = current.next

        odd.next = even

        return head


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

solution = Solution()
solution.oddEvenList(head)
