from collections import deque
class TreeNode:
    
    def __init__(self, data):
        self.queue = deque()
        self.bfs = []
        self.pre_order = []
        self.pre_order = []
        self.in_order = []
        self.post_order = []
        self.size = 0
        self.total = 0
        self.data = data
        self.left = None
        self.right = None

    def pre_order_traversal(self, root):
        if not root:
            return None
        self.pre_order.append(root.data)
        self.pre_order_traversal(root.left)
        self.pre_order_traversal(root.right)
        return self.pre_order

    def in_orderTraversal(self, root):
        if not root:
            return None
        self.in_orderTraversal(root.left)
        self.in_order.append(root.data)
        self.in_orderTraversal(root.right)
        return self.in_order
        
    def post_order_traversal(self, root):
        if not root:
            return None
        self.post_order_traversal(root.left)
        self.post_order_traversal(root.right)
        self.post_order.append(root.data)
        return self.post_order

    def size_of_tree(self, root):
        if not root:
            return None
        self.size += 1
        self.size_of_tree(root.left)
        self.size_of_tree(root.right)
        return self.size

    def sum_of_tree(self, root):
        if not root:
            return None
        self.total += root.data
        self.sum_of_tree(root.left)
        self.sum_of_tree(root.right)
        return self.total

    def level_order_traversal(self, root):
        self.queue.append(root)
        while self.queue:
            # print(self.queue.popleft())
            first_node = self.queue.popleft()
            self.bfs.append(first_node.data)
            if first_node.left:
                self.queue.append(first_node.left)
            if first_node.right:
                self.queue.append(first_node.right)
        return self.bfs

# Creating the nodes
root = TreeNode('A')
left = TreeNode('B')
right = TreeNode('C')
root.left = left
root.right = right

# Creating children of left and right nodes
left.left = TreeNode('D')
left.right = TreeNode('E')
right.left = TreeNode('F')
right.right = TreeNode('G')

right.right.right = TreeNode('H')
right.right.right.right = TreeNode('I')

print('\nRoot and Left, Right')
print(root.data)
print(root.left.data)
print(root.right.data)

print('\nLeft Sub Tree')
print(root.left.data)
print(root.left.left.data)
print(root.left.right.data)

print('\nRight Sub Tree')
print(root.right.data)
print(root.right.left.data)
print(root.right.right.data)

# Pre-order traversal of the tree
print("\nPre-order Traversal of the tree:")
print(root.pre_order_traversal(root))

print("\nIn-order Traversal of the tree:")
print(root.in_orderTraversal(root))

print("\nPost-order Traversal of the tree:")
print(root.post_order_traversal(root))

print("\nSize of the tree:")
print(root.size_of_tree(root))

print('Creating Binary Tree with Integer Values')
# Creating the nodes
root_int = TreeNode(10)
left_int = TreeNode(20)
right_int = TreeNode(30)
root_int.left = left_int
root_int.right = right_int

# Creating children of left and right nodes
left_int.left = TreeNode(40)
left_int.right = TreeNode(50)
right_int.left = TreeNode(60)
right_int.right = TreeNode(70)

right_int.right.right = TreeNode(80)
right_int.right.right.right = TreeNode(90)

print('\nRoot and Left, Right')
print(root_int.data)
print(root_int.left.data)
print(root_int.right.data)

print('\nLeft Sub Tree')
print(root_int.left.data)
print(root_int.left.left.data)
print(root_int.left.right.data)

print('\nRight Sub Tree')
print(root_int.right.data)
print(root_int.right.left.data)
print(root_int.right.right.data)

# Pre-order traversal of the tree
print("\nPre-order Traversal of the tree:")
print(root_int.pre_order_traversal(root_int))

print("\nIn-order Traversal of the tree:")
print(root_int.in_orderTraversal(root_int))

print("\nPost-order Traversal of the tree:")
print(root_int.post_order_traversal(root_int))

print("\nSize of the tree:")
print(root_int.size_of_tree(root_int))

print("\nSum of the tree:")
print(root_int.sum_of_tree(root_int))

print("\nLevel order traversal of the tree:")
print(root_int.level_order_traversal(root_int))