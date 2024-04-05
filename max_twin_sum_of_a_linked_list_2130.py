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
    def __init__(self):
        self.stack = []
        self.maxStack = 0

    def pairSum(self, head) -> int:
        slow = fast = head

        while fast and fast.next:
            self.stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        while slow:
            self.maxStack = max(self.maxStack, slow.val+self.stack.pop())
            slow = slow.next

        return self.maxStack


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
solution = Solution()
solution.pairSum(head)
