# Binary Tree Node Definition
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Inorder Traversal (Left, Root, Right)
def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.value, end=" ")
        inorder(node.right)


# Preorder Traversal (Root, Left, Right)
def preorder(node):
    if node is not None:
        print(node.value, end=" ")
        preorder(node.left)
        preorder(node.right)


# Postorder Traversal (Left, Right, Root)
def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.value, end=" ")


# Function to calculate the height of the tree
def height(node):
    if node is None:
        return -1
    return max(height(node.left), height(node.right)) + 1


# Main Program
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Display Results
print("Inorder Traversal:")
inorder(root)

print("\nPreorder Traversal:")
preorder(root)

print("\nPostorder Traversal:")
postorder(root)

print("\nHeight of the tree:")
print(height(root))