from collections import deque

class MyStack:

    def __init__(self):
        self._stack = deque()

    def push(self, x: int) -> None:
        deq = self._stack
        deq.append(x)
        for i in range(len(deq) - 1):
            deq.append(self.pop())

    def pop(self) -> int:
        return self._stack.popleft()

    def top(self) -> int:
        return self._stack[0]        

    def empty(self) -> bool:
        return len(self._stack) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

# class MyStack:

#     def __init__(self):
#         self._stack = []

#     def push(self, x: int) -> None:
#         self._stack.append(x)

#     def pop(self) -> int:
#         return self._stack.pop()

#     def top(self) -> int:
#         return self._stack[-1]        

#     def empty(self) -> bool:
#         return len(self._stack) == 0