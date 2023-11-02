class MinStack:
    def __init__(self):
        self.list = []

    def push(self, val: int) -> None:
        if self.list:
            minVal = self.list[-1][1]
            if val < minVal:
                minVal = val
            self.list.append((val, minVal))
        else:
            self.list.append((val, val))

    def pop(self) -> None:
            self.list.pop()

    def top(self) -> int:
            return self.list[-1][0]

    def getMin(self) -> int:
            return self.list[-1][1]
