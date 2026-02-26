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