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
    def addTwoNumbers(self, l1, l2):
        stack1 = []
        stack2 = []

        while l1:
            stack1.insert(0, l1.val)
            l1 = l1.next

        while l2:
            stack2.insert(0, l2.val)
            l2 = l2.next

        carry = 0
        head = None

        while stack1 or stack2 or carry:
            sum_value = carry + \
                (stack1.pop(0) if stack1 else 0) + \
                (stack2.pop(0) if stack2 else 0)

            carry = sum_value // 10

            node = ListNode(sum_value % 10)
            node.next = head
            head = node

        print_linked_list(head)


head1 = ListNode(7, ListNode(2, ListNode(4, ListNode(3))))
head2 = ListNode(5, ListNode(6, ListNode(4)))

# head1 = ListNode(5)
# head2 = ListNode(5)
# head1 = ListNode(0)
# head2 = ListNode(7, ListNode(3))
solution = Solution()
solution.addTwoNumbers(head1, head2)
