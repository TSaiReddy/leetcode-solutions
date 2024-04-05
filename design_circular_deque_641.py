class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = []
        self.size = k
        self.deque_len = 0

    def insertFront(self, value: int) -> bool:
        if self.deque_len < self.size:
            self.deque.insert(0, value)
            self.deque_len += 1
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if self.deque_len < self.size:
            self.deque.append(value)
            self.deque_len += 1
            return True
        return False

    def deleteFront(self) -> bool:
        print(self.deque_len, "self.deque_len")
        if self.deque_len > 0:
            self.deque.pop(0)
            self.deque_len -= 1
            return True
        return False

    def deleteLast(self) -> bool:
        if self.deque_len > 0:
            self.deque.pop()
            self.deque_len -= 1
            return True
        return False

    def getFront(self) -> int:
        return self.deque[0]if self.deque_len > 0 else -1

    def getRear(self) -> int:
        return self.deque[-1]if self.deque_len > 0 else -1

    def isEmpty(self) -> bool:
        return self.deque_len == 0

    def isFull(self) -> bool:
        return self.deque_len == self.size


# Your MyCircularDeque object will be instantiated and called as such:
obj = MyCircularDeque(2)
param_1 = obj.insertFront(1)
param_2 = obj.insertLast(2)
param_3 = obj.deleteFront()
param_4 = obj.deleteLast()
param_5 = obj.getFront()
param_6 = obj.getRear()
param_7 = obj.isEmpty()
param_8 = obj.isFull()

print(param_1, param_2, param_3, param_4, param_5, param_6, param_7, param_8)
