class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self):
        return self.get_tree(self.root, '')

    def get_tree(self, start, val):
        if start:
            val = self.get_tree(start.left, val)
            val += (str(start.value) + ' ')
            val = self.get_tree(start.right, val)
        return val


tree = BinaryTree(1000)
tree.root.left = Node(100)
tree.root.right = Node(200)
tree.root.left.right = Node(50)
tree.root.left.left = Node(50)
tree.root.right.right = Node(250)
tree.root.right.left = Node(250)

print(tree.print_tree())
