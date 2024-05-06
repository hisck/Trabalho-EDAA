import time
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.key:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.key)
        if self.right:
            self.right.inorder_traversal()

    def preorder_traversal(self):
        print(self.key)
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()

    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(self.key)

    def find(self, value, comparison_count):
        time.sleep(0.000001)
        if value < self.key:
            comparison_count = comparison_count + 1
            if self.left is None:
                return [False, comparison_count + 1]
            else:
                return self.left.find(value, comparison_count + 1)
        elif value > self.key:
            comparison_count = comparison_count + 2
            if self.right is None:
                return [False, comparison_count + 1]
            else:
                return self.right.find(value, comparison_count + 1)
        else:
            return [self.key, comparison_count + 2]
        
        # Time complexity: Best case O(log N), worst case (n)
        # auxiliary space: O(1)
    
    