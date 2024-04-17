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
    def removeNodes(self, head):
        stack = []

        current = head
        while current:
            curVal = current.val
            while stack and stack[-1] < curVal:
                stack.pop()
            else:
                stack.append(curVal)

            current = current.next

        print(stack)

        dummy = ListNode(0)
        newList = dummy

        while stack:
            val = stack.pop(0)
            newList.next = ListNode(val)
            newList = newList.next

        return dummy.next


head = ListNode(5, ListNode(2, ListNode(13, ListNode(3, ListNode(8)))))

solution = Solution()
solution.removeNodes(head)
