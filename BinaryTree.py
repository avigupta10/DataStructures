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


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.right = Node(5)
tree.root.left.left = Node(4)
tree.root.right.right = Node(6)
tree.root.left.left.left = Node(7)
tree.root.right.right.right = Node(8)

print(tree.print_tree())


def deepestLeavesSum(root):
    """
        :type root: TreeNode
        :rtype: int
        """

    def count(node, target, c1, c2):
        if node:
            if node.value == target:
                return c1, c2
            if node.left:
                count(node.left, target, c1 + 1, 0)
            if node.right:
                count(node.right, target, 0, c2 + 1)

    return count(root, 5, 0, 0)


print(deepestLeavesSum(tree.root))
