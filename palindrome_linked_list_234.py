class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head) -> bool:
        if not head or not head.next:
            return True

        slow, fast = head, head
        stack = []

        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        # If the number of nodes in the linked list is odd, the fast pointer will be None when the loop ends,
        # whereas if it's even, the fast pointer will be pointing to the last node.
        if fast:
            slow = slow.next

        while slow is not None:
            if slow.val != stack[-1]:
                return False
            else:
                stack.pop()
                slow = slow.next

        return True


head = ListNode(1, ListNode(0, ListNode(1)))

solution = Solution()
print(solution.isPalindrome(head))
