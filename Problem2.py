from Problem1 import exp_tree
# using prev problems code 

# Using preorder traversal here
# ie root -> left -> right
def preorder_trav(root):
    if root is None:
        return []

    result = [root.value]
    result += preorder_trav(root.left)
    result += preorder_trav(root.right)

    return result

# using postorder traversla here 
# left -> right -> root
def postorder_trav(root):
    if root is None:
        return []

    result = []
    result += postorder_trav(root.left)
    result += postorder_trav(root.right)
    result.append(root.value)

    return result

# using inorder traversal here 
# left -> root -> right
def inorder_trav(root):

    if root is None:
        return []

 
    if root.left is None and root.right is None:
        return [root.value]

    result = []

    result.append("(")
    result += inorder_trav(root.left)
    result.append(root.value)
    result += inorder_trav(root.right)
    result.append(")")

    return result

# trying out a test case here
if __name__ == "__main__":
    postfix_input = ["3", "4", "+", "2", "*"]

    root = exp_tree(postfix_input)

    print("Prefix:", preorder_trav(root))
    print("Infix:", inorder_trav(root))
    print("Postfix:", postorder_trav(root))