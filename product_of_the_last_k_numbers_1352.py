class ProductOfNumbers:

    def __init__(self):
        self.arr = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.arr = [1]
        else:
            self.arr.append(self.arr[-1]*num)

    def getProduct(self, k: int) -> int:
        if len(self.arr) - 1 < k:
            return 0
        return self.arr[-1]//self.arr[len(self.arr)-1-k]


obj = ProductOfNumbers()
obj.add(3)
obj.add(0)
obj.add(2)
obj.add(5)
obj.add(4)
param_2 = obj.getProduct(2)
print(param_2)
