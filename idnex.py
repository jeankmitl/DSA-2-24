class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_expression_tree(prefix):
    stack = []
    for symbol in reversed(prefix):
        if symbol.isalnum():  
            stack.append(Node(symbol))
        else:  
            node = Node(symbol)
            node.left = stack.pop()
            node.right = stack.pop()
            stack.append(node)
    return stack[-1]

def inorder(node):
    if not node:
        return ""
    return f"({inorder(node.left)}{node.value}{inorder(node.right)})"

def preorder(node):
    if not node:
        return ""
    return f"{node.value}{preorder(node.left)}{preorder(node.right)}"

def postorder(node):
    if not node:
        return ""
    return f"{postorder(node.left)}{postorder(node.right)}{node.value}"

prefix_expression = ['+', '-','*', 'A', '+', 'B', 'C', '/', 'D', 'E', '*', 'F', 'G']

root = build_expression_tree(prefix_expression)

infix = inorder(root)
prefix = preorder(root)
postfix = postorder(root)

if infix.startswith("(") and infix.endswith(")"):
    infix = infix[1:-1]

print("Infix Expression:", infix)
print("Prefix Expression:", prefix)
print("Postfix Expression:", postfix)