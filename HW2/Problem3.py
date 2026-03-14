class Stack:
    """
    Stack ADT implementation using a list
    I am manually maintaining the 'top' index to follow stack logic
    """

    def __init__(self):
        self.data = []
        self.top = -1  # If top == -1, stack is empty

    def is_empty(self):
        return self.top == -1

    def push(self, value):
        self.data.append(value)
        self.top += 1  # manually update top

    def pop(self):
        # Edge case: popping from empty stack
        if self.is_empty():
            raise IndexError("Pop from empty stack")

        value = self.data[self.top]
        self.data.pop()
        self.top -= 1
        return value


def eval_postfix(expression):
    """
    Evaluating a space-separated postfix expression here
    modified this later but also including variious edge cases here
    """

    # Edge Case 1: Empty expression
    if not expression or expression.strip() == "":
        return None

    stack = Stack()
    operators = {"+", "-", "*", "/"}
    tokens = expression.split()

    for token in tokens:

        # If token is not an operator treat it as a number
        if token not in operators:
            try:
                # Edge Case 4: Invalid tokens handled here
                number = float(token)
                stack.push(number)
            except ValueError:
                raise ValueError(f"Invalid token detected: {token}")

        else:
            # Edge Case 2: Insufficient operands
            if stack.top < 1:
                raise ValueError("Malformed postfix expression: insufficient operands")

            right = stack.pop()
            left = stack.pop()

            if token == "+":
                result = left + right

            elif token == "-":
                result = left - right

            elif token == "*":
                result = left * right

            elif token == "/":
                # Edge Case 3: Division by zero
                if right == 0:
                    raise ZeroDivisionError("Division by zero is not allowed")
                result = left / right

            stack.push(result)

    # Edge Case 2 Too many operands
    if stack.top != 0:
        raise ValueError("Malformed postfix expression: too many operands")

    return stack.pop()


if __name__ == "__main__":
    expr = "5 1 2 + 4 * + 3 -"
    print("Result:", eval_postfix(expr))
