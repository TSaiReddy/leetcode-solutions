"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""


class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """

    def getList(self) -> [NestedInteger]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """


class NestedIterator:
    def __init__(self, nestedList):
        self.queue = []
        self._flattenList(nestedList)

    def next(self) -> int:
        return self.queue.pop(0)

    def hasNext(self) -> bool:
        return True if self.queue else False

    def _flattenList(self, nestedList):
        for i in nestedList:
            if not i.isInteger():
                self._flattenList(i.getList())
            else:
                self.queue.append(i.getInteger())


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())


n = NestedIterator([[1, 1], 2, [1, 1]])
print(n.hasNext())
print(n.hasNext())
print(n.hasNext())
print(n.hasNext())
print(n.hasNext())
