class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = []
        self.size = k
        self.queue_len = 0

    def enQueue(self, value: int) -> bool:
        if self.queue_len < self.size:
            self.queue.append(value)
            self.queue_len += 1
            return True
        return False

    def deQueue(self) -> bool:
        if self.queue_len:
            self.queue.pop(0)
            self.queue_len -= 1
            return True
        return False

    def Front(self) -> int:
        return self.queue[0] if self.queue else -1

    def Rear(self) -> int:
        return self.queue[-1] if self.queue else -1

    def isEmpty(self) -> bool:
        return self.queue_len == 0

    def isFull(self) -> bool:
        return self.queue_len == self.size


# myCircularQueue = MyCircularQueue(3)
# print(myCircularQueue.enQueue(1))
# print(myCircularQueue.enQueue(2))
# print(myCircularQueue.enQueue(3))
# print(myCircularQueue.enQueue(4))
# print(myCircularQueue.Rear())
# print(myCircularQueue.isFull())
# print(myCircularQueue.deQueue())
# print(myCircularQueue.enQueue(4))
# print(myCircularQueue.Rear())


myCircularQueue = MyCircularQueue(8)
print(myCircularQueue.enQueue(3))
print(myCircularQueue.enQueue(9))
print(myCircularQueue.enQueue(5))
print(myCircularQueue.enQueue(0))
print(myCircularQueue.deQueue())
print(myCircularQueue.deQueue())
print(myCircularQueue.isEmpty())
print(myCircularQueue.isEmpty())
print(myCircularQueue.Rear())
print(myCircularQueue.Rear())
print(myCircularQueue.deQueue())
