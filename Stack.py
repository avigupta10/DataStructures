class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        """
        Accepts an item as a parameter and appends it to the stack.
        Complexity for this method is O(1), or constant time,
        because appending to the end of a stack happens in constant time
        :rtype : None
        """
        self.stack.append(value)

    def pop(self):
        """
        Removes and Returns the last item in the stack,
        which is also the top item of the stack.
        Complexity for this method is O(1)
        :return: Last item in the stack
        """
        if self.stack:
            return self.stack.pop()
        else:
            return "Stack is empty"

    def peek(self):
        """
        Peek and Returns the last item in the stack,
        which is also the top item of the stack.
        Complexity for this method is O(1)
        :return: Last item in the stack
        """
        if self.stack:
            return self.stack[-1]

    def size(self):
        """
        Return the size of the stack
        Complexity for this method is O(1)
        :return: size of stack
        :rtype: int
        """
        return len(self.stack)

    def is_empty(self):
        """
        Returns True if the stack is empty. Otherwise False
        :return: boolean value
        :rtype: bool
        """
        return self.stack == []


stack = Stack()

for i in range(10):
    stack.push(i)

print(stack.stack)

print(stack.pop())

print(stack.size())

print(stack.peek())