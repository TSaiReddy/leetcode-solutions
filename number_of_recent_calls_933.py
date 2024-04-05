class RecentCounter:

    def __init__(self):
        self.queue = []

    def ping(self, t: int) -> int:
        self.queue.append(t)
        sum = t-3000
        print(self.queue, "ppp", sum)
        while self.queue and self.queue[0] < sum:
            self.queue.pop(0)
        else:
            return len(self.queue)


obj = RecentCounter()
print(obj.ping(642))
print(obj.ping(1849))
print(obj.ping(4921))
print(obj.ping(5936))
print(obj.ping(5957))
