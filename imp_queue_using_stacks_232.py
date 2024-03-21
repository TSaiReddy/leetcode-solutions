class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        if not self.output:
            for _ in range(len(self.input)):
                self.output.append(self.input.pop(-1))

        return self.output.pop()

    def peek(self) -> int:
        if not self.output:
            for _ in range(len(self.input)):
                self.output.append(self.input.pop(-1))

        return self.output[-1]

    def empty(self) -> bool:
        return not self.output and not self.input


obj = MyQueue()
obj.push(2)
obj.push(3)
param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
