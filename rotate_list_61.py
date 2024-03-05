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
    def rotateRight(self, head, k):
        if not head or k == 0:
            return head

        length = 1
        current = head

        while current.next:
            length += 1
            current = current.next

        k = k % length
        if k == 0:
            return head

        fast = head

        for _ in range(length - k - 1):
            fast = fast.next

        newHead = fast.next
        fast.next = None

        current = newHead
        while current.next:
            current = current.next

        current.next = head

        return newHead


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

solution = Solution()
solution.rotateRight(head, 2)
