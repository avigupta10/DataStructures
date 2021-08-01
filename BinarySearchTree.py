class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            return self._insert(self.root, value)

    def _insert(self, curr_node, value):
        if value < curr_node.value:
            if curr_node.left is None:
                curr_node.left = Node(value)
                curr_node.left.parent = curr_node
            else:
                self._insert(curr_node.left, value)
        elif value > curr_node.value:
            if curr_node.right is None:
                curr_node.right = Node(value)
                curr_node.right.parent = curr_node
            else:
                self._insert(curr_node.right, value)
        else:
            print('Value Already Present -> ', value)

    def search(self, value):
        if self.root is not None:
            return self._search(self.root, value)
        else:
            return False

    def _search(self, curr_node, value):
        if value == curr_node.value:
            return True
        elif value < curr_node.value and curr_node.left is not None:
            return self._search(curr_node.left, value)
        elif value > curr_node.value and curr_node.right is not None:
            return self._search(curr_node.right, value)
        else:
            return 'value not found'

    def find(self, value):
        if self.root.value != value:
            return self._find(self.root, value)
        else:
            return self.root.value

    def _find(self, curr_node, value):
        if value == curr_node.value:
            return curr_node.value
        elif value < curr_node.value and curr_node.left is not None:
            return self._find(curr_node.left, value)
        elif value > curr_node.value and curr_node.right is not None:
            return self._find(curr_node.right, value)
        else:
            return 'value not found'

    def delete(self, value):
        pass

    def display(self):
        if self.root is not None:
            return self._display(self.root)

    def _display(self, curr_node):
        if curr_node is not None:
            self._display(curr_node.left)
            print(str(curr_node.value))
            self._display(curr_node.right)


tree = BST()
tree.insert(10)
tree.insert(1)
tree.insert(12)
tree.insert(2)
tree.insert(13)
tree.insert(13)
tree.display()
# print(tree.find(82))
