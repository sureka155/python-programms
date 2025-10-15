class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # Height starts at 1

# Function to get height of a node
def get_height(node):
    if not node:
        return 0
    return node.height

# Function to get balance factor
def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)

# Right rotation
def right_rotate(z):
    y = z.left
    T3 = y.right
    y.right = z
    z.left = T3
    z.height = max(get_height(z.left), get_height(z.right)) + 1
    y.height = max(get_height(y.left), get_height(y.right)) + 1
    return y

# Left rotation
def left_rotate(z):
    y = z.right
    T2 = y.left
    y.left = z
    z.right = T2
    z.height = max(get_height(z.left), get_height(z.right)) + 1
    y.height = max(get_height(y.left), get_height(y.right)) + 1
    return y

# Insert a node into the AVL Tree
def insert(root, key):
    if not root:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root  # No duplicates

    # Update height
    root.height = 1 + max(get_height(root.left), get_height(root.right))

    # Balance the node
    balance = get_balance(root)

    # Left Left Case
    if balance > 1 and key < root.left.key:
        return right_rotate(root)

    # Right Right Case
    if balance < -1 and key > root.right.key:
        return left_rotate(root)

    # Left Right Case
    if balance > 1 and key > root.left.key:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    # Right Left Case
    if balance < -1 and key < root.right.key:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root

# Inorder traversal (sorted output)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

# ---------- MAIN PROGRAM ----------
root = None

while True:
    print("\n--- AVL Tree Menu ---")
    print("1. Insert")
    print("2. Display Inorder")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        key = int(input("Enter number to insert: "))
        root = insert(root, key)
        print(f"{key} inserted.")
    elif choice == "2":
        print("Inorder Traversal: ", end="")
        inorder(root)
        print()
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.")                                                                                   
