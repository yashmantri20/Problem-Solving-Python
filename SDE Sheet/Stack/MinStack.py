class MinStack:

    def __init__(self):
        self.stack = []
        self.currentMin = float('inf')
        self.prevMins = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.currentMin:
            self.prevMins.append(self.currentMin)
            self.currentMin = val
        

    def pop(self) -> None:
        if self.stack[-1] == self.currentMin:
            self.currentMin = self.prevMins.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.currentMin


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()