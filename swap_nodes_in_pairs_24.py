
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head

        newHead = ListNode(-1, head)
        current = newHead

        while current.next and current.next.next:
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
