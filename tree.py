class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# Binary Tree class
class BinaryTree:
    def __init__(self):
        self.root = None

    # Insert node (level-order insertion)
    def insert(self, key):
        new_node = Node(key)
        if not self.root:
            self.root = new_node
            return

        queue = [self.root]
        while queue:
            temp = queue.pop(0)

            if not temp.left:
                temp.left = new_node
                break
            else:
                queue.append(temp.left)

            if not temp.right:
                temp.right = new_node
                break
            else:
                queue.append(temp.right)

    # Inorder Traversal (Left → Root → Right)
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.key, end=" ")
            self.inorder(node.right)

    # Preorder Traversal (Root → Left → Right)
    def preorder(self, node):
        if node:
            print(node.key, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    # Postorder Traversal (Left → Right → Root)
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.key, end=" ")

    # Level-order Traversal (Breadth-First Search)
    def level_order(self):
        if not self.root:
            return
        queue = [self.root]
        while queue:
            temp = queue.pop(0)
            print(temp.key, end=" ")
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
    # Example usage
if __name__ == "__main__":
    bt = BinaryTree()
    bt.insert(1)
    bt.insert(2)
    bt.insert(3)
    bt.insert(4)
    bt.insert(5)


    print("Inorder Traversal:")
    bt.inorder(bt.root)

    print("\nPreorder Traversal:")
    bt.preorder(bt.root)

    print("\nPostorder Traversal:")
    bt.postorder(bt.root)

    print("\nLevel-order Traversal:")
    bt.level_order()
