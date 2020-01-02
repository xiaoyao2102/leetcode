class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        self._rotate()
        return self.queue.pop(0)

    def top(self) -> int:
        """
        Get the top element.
        """
        self._rotate()
        result = self.queue[0]
        self.queue.append(self.queue.pop(0))
        return result

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.queue

    def _rotate(self):
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.pop(0))


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(4)
obj.push(6)
param_3 = obj.top()
param_2 = obj.pop()
print(obj.pop())
print(obj.pop())
param_4 = obj.empty()
print(param_2)
print(param_3)
print(param_4)