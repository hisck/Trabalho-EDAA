import time
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.h = 1

class AVLTree:
    def __init__(self):
        self.root = None
    
    def height(self, node):
        if not node:
            return 0
        return node.h
    
    def balance(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)
    
    def insert(self, root, value):
        if not root:
            return Node(value)
        elif value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        root.h = 1 + max(self.height(root.left), self.height(root.right))

        balance = self.balance(root)

        if balance > 1 and value < root.left.value:
            return self.right_rotate(root)
        
        if balance < -1 and value > root.right.value:
            return self.left_rotate(root)
        
        if balance > 1 and value > root.left.value:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        
        if balance < -1 and value < root.right.value:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        
        return root
    
    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.h = 1 + max(self.height(z.left), self.height(z.right))
        y.h = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.h = 1 + max(self.height(z.left), self.height(z.right))
        y.h = 1 + max(self.height(y.left), self.height(y.right))

        return y
    
    def find(self, root, value, comparison_count):
        time.sleep(0.000000001)
        if not root:
            return [False, comparison_count + 1]
        
        if value < root.value:
            comparison_count += 1
            return self.find(root.left, value, comparison_count)
        
        elif value > root.value:
            comparison_count += 2
            return self.find(root.right, value, comparison_count)
        
        else:
            return [root.value, comparison_count + 2]
        
        # Time complexity: O (log N)
        # auxiliary space: O(log N)    

    def insert_value(self, value):
        self.root = self.insert(self.root, value)

    def search_value(self, value):
        return self.find(self.root, value, 0)
    
    def find_deepest_node(self, root):
        if root is None:
            return None
        
        queue = [root]
        deepest_node = None

        while queue:
            node = queue.pop(0)
            deepest_node = node
            
            if node.left:
                queue.append(node.left)
                
            if node.right:
                queue.append(node.right)

        return deepest_node