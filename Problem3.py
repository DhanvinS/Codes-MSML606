class Stack:

    def __init__(self):
        self.data = []
        self.top = -1  # empty stack

    def is_empty(self):
        return self.top == -1

    def push(self, value):
        # Pushing element onto stack.
        self.data.append(value)
        self.top += 1

    def pop(self):
        
       # Removing and returning top element.
       # Raises error if stack is empty so will use an exceptio nstatement.
        
        if self.is_empty():
            raise IndexError("Popping from an empty stack")

        value = self.data[self.top]
        self.data.pop()
        self.top -= 1
        return value

    def peek(self):
        # Returning top element not removing it tho
        if self.is_empty():
            raise IndexError("Peek from empty stack")

        return self.data[self.top]