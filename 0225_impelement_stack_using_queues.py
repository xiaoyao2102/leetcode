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
