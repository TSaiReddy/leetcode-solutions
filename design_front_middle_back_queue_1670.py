

class FrontMiddleBackQueue:

    def __init__(self):
        self.queue = []
        self.length = 0

    def pushFront(self, val: int) -> None:
        self.queue.insert(0, val)
        self.length += 1

    def pushMiddle(self, val: int) -> None:
        mid = self.length//2
        self.queue.insert(mid, val)
        self.length += 1

    def pushBack(self, val: int) -> None:
        self.queue.append(val)
        self.length += 1

    def popFront(self) -> int:
        if self.length < 0:
            return -1
        k = self.queue.pop(0)
        self.length -= 1
        return k

    def popMiddle(self) -> int:
        if self.length < 0:
            return -1
        mid = self.length//2
        self.length -= 1
        return self.queue.pop(mid)

    def popBack(self) -> int:
        if self.length < 0:
            return -1
        self.length -= 1
        return self.queue.pop()
