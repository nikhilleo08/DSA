from collections import deque
from collections import defaultdict

class Node:
    '''
    Node class to create a node of a Binary Search Tree
    '''
    def __init__(self, val=0):
        self.left = None
        self.value = val
        self.right = None

    def __repr__(self):
        return f"Node({self.value})"


class TreeViews:
    def __init__(self):
        pass
    
    def left_view(self):
        if not self.root:
            return []

        result = []
        queue = deque([self.root])

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()

                # Append value of the first node of each level
                if i == 0:
                    result.append(node.value)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result
    
    def right_view(self):
        if not self.root:
            return []

        result = []
        queue = deque([self.root])

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()

                # Append value of the last node of each level
                if i == level_size - 1:
                    result.append(node.value)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result

    def top_view(self):
        '''
        **Core Idea**:
            - We need to track two things:
                - Horizontal Distance (HD) from the root
                - Level Order Traversal (BFS) to make sure we take the topmost node per column
        '''
        if not self.root:
            return []
        freq = defaultdict(list)
        queue = deque([(self.root, 0)])
        min_idx = float('inf')
        max_idx = float('-inf')
        while queue:
            # level_size, idx = len(queue)
            popped, idx = queue.popleft()
            freq[idx].append(popped.value)
            min_idx = min(min_idx, idx)
            max_idx = max(max_idx, idx)
            if popped.left:
                queue.append((popped.left, idx-1))
            if popped.right:
                queue.append((popped.right, idx+1))
        result = []
        for i in range(min_idx, max_idx+1):
            result.append(freq[i][0])
        return result

    def bottom_view(self):
        '''
        **Core Idea**:
            - We need to track two things:
                - Horizontal Distance (HD) from the root
                - Level Order Traversal (BFS) to make sure we take the topmost node per column
        '''
        if not self.root:
            return []
        freq = defaultdict(list)
        queue = deque([(self.root, 0)])
        min_idx = float('inf')
        max_idx = float('-inf')
        while queue:
            # level_size, idx = len(queue)
            popped, idx = queue.popleft()
            freq[idx].append(popped.value)
            min_idx = min(min_idx, idx)
            max_idx = max(max_idx, idx)
            if popped.left:
                queue.append((popped.left, idx-1))
            if popped.right:
                queue.append((popped.right, idx+1))
        result = []
        for i in range(min_idx, max_idx+1):
            result.append(freq[i][-1])
        return result

class TreeTraversal:
    def __init__(self):
        pass
    
    def inorder_traversal(self):
        return self._inorder_recursive(self.root, [])
    
    def _inorder_recursive(self, current, ans):
        if not current:
            return
        self._inorder_recursive(current.left, ans)
        ans.append(current.value)
        self._inorder_recursive(current.right, ans)
        return ans
    
    def pre_order_traversal(self):
        return self._pre_order_recursive(self.root, [])
    
    def _pre_order_recursive(self, current, ans):
        if not current:
            return
        ans.append(current.value)
        self._pre_order_recursive(current.left, ans)
        self._pre_order_recursive(current.right, ans)
        return ans

    def post_order_traversal(self):
        return self._post_order_recursive(self.root, [])
    
    def _post_order_recursive(self, current, ans):
        if not current:
            return
        self._post_order_recursive(current.left, ans)
        self._post_order_recursive(current.right, ans)
        ans.append(current.value)
        return ans

    def level_order_traversal(self):
        '''
        Intuition:
            Here’s how level-order works:
                * Start from the root.
                * Enqueue it into a queue.
                * While the queue is not empty:
                    * Dequeue the front node.
                    * Visit it (append to ans)
                    * Enqueue its left child (if it exists).
                    * Enqueue its right child (if it exists).
        '''
        ans = []
        if not self.root:
            return ans
        q = deque()
        q.append(self.root)
        while q:
            popped = q.popleft()
            ans.append(popped.value)
            if popped.left:
                q.append(popped.left)
            if popped.right:
                q.append(popped.right)
        return ans

class BinarySearchTree(TreeTraversal, TreeViews):
    '''
    A class to represent binary search tree and it's methods
    \nIn a Binary Search Tree, the rule is:
    \nFor any node:
        \n* All values in the left subtree are less than node.value
        \n* All values in the right subtree are greater than node.value
    '''
    def __init__(self):
        self.root = None

    def insert(self, val):
        """
        Description:
            Think of insert(value) like dropping the value from the top, and it "bubbles down" to the correct position based on comparisons.
        
        Goal:
            Place the new value at the correct leaf position that maintains the BST property.

        3 Simple Steps to Insert a Value:
            - If the tree is empty (no root):
                - Set the new node as the root.
            - If tree has a root, compare value with current node:
                - If value < current.value, go left
                - If value > current.value, go right
            - Repeat recursively (or iteratively) until we reach a None position, then insert the new node there.

        Args
            val (int): Insert the following value into the Binary Search Tree
        """
        if not self.root:
            self.root = Node(val)
        else:
            self._insert_recursive(self.root, val)
    
    def _insert_recursive(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert_recursive(current.left, value)
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert_recursive(current.right, value)
        else:
            print('Value already exists')
    
    def search(self, value):
        return f'Value {value} found in the Binary Search Tree' if self._search_recursive(self.root, value) else f'Value {value} not found in the Binary Search Tree'

    def _search_recursive(self, current: Node, value):
        # If current value is None, return False
        if current is None:
            return False
        # If value is found in tree return True
        if current.value == value:
            return True
        # Recurse to left tree if the value to search is less than the current root
        if value < current.value:
            return self._search_recursive(current.left, value)
        # Recurse to right tree if the value to search is greater than the current root
        if value > current.value:
            return self._search_recursive(current.right, value)
    
    def delete(self, val):
        self._delete_recursive(self.root, val)

    def _delete_recursive(self, current, val):
        # If the node is not present return None
        if not current:
            return None
        # Traverse the tree until the node is found
        # Step 1: Traverse the tree
        if val < current.value:
            current.left = self._delete_recursive(current.left, val)
        elif val > current.value:
            current.right = self._delete_recursive(current.right, val) 
        else:
            # Step 2: Found the node to delete
            # Case 1: No child
            if not current.left and not current.right:
                return None
            # Case 2: One child
            if not current.left:
                return current.right
            if not current.right:
                return current.left            
            # Case 3: Two children
            successor = self._find_min(current.right)
            current.value = successor.value
            current.right = self._delete_recursive(current.right, successor.value)
        return current

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node

#   10
#  /  \
# 5   15
#     /
#   12
# bst = BinarySearchTree()
# bst.insert(10)
# bst.insert(5)
# bst.insert(15)
# bst.insert(12)
# print(bst.search(12))  # True
# print(bst.search(7))   # False
# print('In Order Traversal of the Binary Search Tree:', bst.inorder_traversal()) # 5, 10, 12, 15
# print('Pre Order Traversal of the Binary Search Tree:', bst.pre_order_traversal()) # 10, 5, 15, 12
# print('Post Order Traversal of the Binary Search Tree:', bst.post_order_traversal()) # 5, 12, 15, 10
# print('Level Order Traversal of the Binary Search Tree:', bst.level_order_traversal()) # 10, 5, 15, 12
# print('Left View of the Binary Search Tree: ', bst.left_view())
# print('Right View of the Binary Search Tree: ', bst.right_view())

# bst_1 = BinarySearchTree()
# for val in [10, 5, 15, 3, 7, 12, 18, 4, 16, 8, 11, 20, 13, 94, 1, 9]:
#     bst_1.insert(val)

# print("Level-order:", bst_1.level_order_traversal()) # Level-order: [10, 5, 15, 3, 7, 12, 18]
# print("Top View of the tree", bst_1.top_view()) # 10, 5, 15, 3, 18, 1, 9, 94
# print("Bottom View of the tree", bst_1.bottom_view()) # 10, 5, 15, 3, 18, 1, 9, 94

bst = BinarySearchTree()
for val in [10, 5, 15, 2, 6, 20]:
    bst.insert(val)

print("Top view:", bst.top_view())  # Output: [2, 5, 10, 15, 20]
print("Bottom view:", bst.bottom_view())  # Output: [2, 5, 6, 15, 20]
