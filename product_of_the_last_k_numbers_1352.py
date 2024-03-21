class ProductOfNumbers:

    def __init__(self):
        self.queue = []

    def add(self, num: int) -> None:
        if num == 0:
            self.queue = [num]
        else:
            self.queue.append(num)

    def getProduct(self, k: int) -> int:
        product = 1
        for i in range(len(self.queue) - 1, -1, -1):
            if k > 0:
                product *= self.queue[i]
                k -= 1

        return product


obj = ProductOfNumbers()
obj.add(3)
obj.add(0)
obj.add(2)
obj.add(5)
obj.add(4)
param_2 = obj.getProduct(2)
print(param_2)
