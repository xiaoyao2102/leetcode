class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.input.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.output:
            return self.output.pop()

        self.__copy_input_to_output()

        return self.output.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.output:
            return self.output[-1]

        self.__copy_input_to_output()

        return self.output[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not (self.input or self.output)

    def __copy_input_to_output(self):
        while self.input:
            self.output.append(self.input.pop())
