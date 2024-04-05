class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize
        self.stack_len = 0

    def push(self, x: int) -> None:
        if self.stack_len < self.maxSize:
            self.stack.append(x)
            self.stack_len += 1

    def pop(self) -> int:
        if self.stack:
            self.stack_len -= 1
            return self.stack.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        k = k if k <= self.stack_len else self.stack_len
        for i in range(k):
            self.stack[i] = self.stack[i]+val

        print(self.stack)


c = CustomStack(20)
c.push(3)
c.push(1)
c.push(2)
c.pop()
c.push(2)
c.push(3)
c.push(4)
c.increment(5, 100)
c.increment(2, 100)
c.pop()
c.pop()
c.pop()
c.pop()
