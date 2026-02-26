class Stack:

    def __init__(self):
        self.data = []
        self.top = -1  # empty stack

    def is_empty(self):
        return self.top == -1

    def push(self, value):
        # Pushing element  onto stack.
        self.data.append(value)
        self.top += 1

    def pop(self):
        
       # Removing and returning top element.
       # Raises error if stack is empty so  will use an exceptio nstatement.
        
        if self.is_empty():
            raise IndexError("Popping from an  empty stack")

        value = self.data[self.top]
        self.data.pop()
        self.top -= 1
        return value

    def peek(self):
        # Returning top element not removing it tho
        if self.is_empty():
            raise IndexError("Peek  from empty stack")

        return self.data[self.top]
    
def eval_postfix(expression):
    """
    Evaluating a postfix expression using a stack here

    Parameters im  using :
        expression : space-separated postfix expression

    This returns a  float or int: result of evaluation
    """

    if not expression:
        return None

    stack = Stack()
    operators = {"+", "-", "*", "/"}

    tokens = expression.split()

    for token in tokens:

        # If operand → push as number
        if token not in operators:
            stack.push(float(token))

        # If operator → pop two operands and apply operation
        else:
            if stack.top < 1:
                raise ValueError("Invalid postfix expression")

            right = stack.pop()
            left = stack.pop()

            if token == "+":
                result = left + right
            elif token == "-":
                result = left - right
            elif token == "*":
                result = left * right
            elif token == "/":
                if right == 0:
                    raise ZeroDivisionError("Division by zero")
                result = left / right

            stack.push(result)

    if stack.top != 0:
        raise ValueError("Invalid postfix expression")

    return stack.pop()

if __name__ == "__main__":
    expr = "5 1 2 + 4 * + 3 -"
    print("Result:", eval_postfix(expr))