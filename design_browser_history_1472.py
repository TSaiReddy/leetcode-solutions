class ListNode:
    def __init__(self, val: str) -> None:
        self.val = val
        self.next = None
        self.prev = None


def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


class BrowserHistory:
    def __init__(self, homepage: str):
        self.head = ListNode(homepage)
        self.current = self.head

    def visit(self, url: str):
        newNode = ListNode(url)
        if not self.head:
            self.head = newNode
            self.current = self.head
        else:
            node = self.current
            self.current.next = newNode
            self.current = self.current.next
            self.current.prev = node
        print_linked_list(self.head)

    def back(self, steps: int):
        if not self.current.prev:
            return self.current.val

        dummy = self.current

        for _ in range(steps):
            if not dummy.prev:
                self.current = dummy
                return dummy.val
            node = dummy.prev
            dummy = node

        self.current = dummy
        print(dummy.val, "back", steps)
        return dummy.val

    def forward(self, steps: int):
        if not self.current.next:
            return self.current.val

        dummy = self.current
        count = 0

        while dummy.next and count < steps:
            dummy = dummy.next
            count += 1

        self.current = dummy
        print(dummy.val, "forward", steps)
        return dummy.val


history = BrowserHistory("leetcode.com")
history.visit("google.com")
history.visit("instagram.com")
history.visit("youtube.com")
history.back(1)
history.back(1)
history.forward(1)
history.visit("linkedin.com")
history.forward(2)
history.back(2)
history.back(7)
