class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def exp_tree():
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