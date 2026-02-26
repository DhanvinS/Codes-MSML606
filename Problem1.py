# Problem 1

# adding a basic node class here
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# converting the postfix into a expression tree here
def exp_tree(postfix_list):
    stack = []
    operators = {"+", "-", "*", "/"}

    for token in postfix_list:
        if token not in operators:
            node = Node(token)
            stack.append(node)
        else:
            right = stack.pop()
            left = stack.pop()

            node = Node(token)
            node.left = left
            node.right = right

            stack.append(node)

    return stack[0]


# small test case to see if my programme works
if __name__ == "__main__":
    postfix = ["3", "4", "+", "2", "*"]
    root = exp_tree(postfix)
    print(root.value)
