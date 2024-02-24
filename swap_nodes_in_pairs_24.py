
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head

        newHead = ListNode(-1)
        newHead.next = head
        current = newHead

        while current.next is not None and current.next.next is not None:
            first = current.next
            second = current.next.next

            #  Swap nodes
            first.next = second.next
            second.next = first
            current.next = second

            current = current.next.next

        return newHead.next


node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)
node.next.next.next.next = ListNode(5)

sol = Solution()
print(sol.swapPairs(node))
