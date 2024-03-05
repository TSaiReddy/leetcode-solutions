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
    def mergeNodes(self, head):
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        current = dummy
        sum = 0

        while head:
            if head.val == 0:
                if sum > 0:
                    current.next = ListNode(sum)
                    current = current.next
                sum = 0
            else:
                sum += head.val

            head = head.next

        return dummy.next


head = ListNode(0, ListNode(2, ListNode(
    3, ListNode(0, ListNode(5, ListNode(5, ListNode(0)))))))

solution = Solution()
solution.mergeNodes(head)
