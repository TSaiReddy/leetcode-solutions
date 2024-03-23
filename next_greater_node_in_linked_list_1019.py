class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:
#     def nextLargerNodes(self, head):
#         current = head
#         answer = []

#         while head:
#             answer.append(0)
#             print(head.val, current.val)
#             while current:
#                 if current.val > head.val:
#                     answer[-1] = current.val
#                     break
#                 current = current.next
#             head = head.next
#             current = head

#         return answer


# solution = Solution()

# head = ListNode(2, ListNode(1, ListNode(5)))

# print(solution.nextLargerNodes(head))


class Solution:
    def nextLargerNodes(self, head):
        stack = []
        answer = []

        while head:
            answer.append(head.val)
            head = head.next

        for i in range(len(answer)-1, -1, -1):
            if not stack:
                stack.append(answer[i])
                answer[i] = 0
            else:
                if answer[i] < stack[-1]:
                    val = answer[i]
                    answer[i] = stack[-1]
                    stack.append(val)
                else:
                    while stack and stack[-1] <= answer[i]:
                        stack.pop()

                    if stack:
                        val = answer[i]
                        answer[i] = stack[-1]
                        stack.append(val)
                    else:
                        stack.append(answer[i])
                        answer[i] = 0

        return answer


solution = Solution()

# head = ListNode(2, ListNode(7, ListNode(4, ListNode(3, ListNode(5)))))
# print(solution.nextLargerNodes(head))

head = ListNode(2, ListNode(2))
print(solution.nextLargerNodes(head))
