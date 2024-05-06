import time
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
    
    def sortedMerge(self, a, b):
        result = None

        if a == None:
            return b
        if b == None:
            return a
        
        if a.data <= b.data:
            result = a
            result.next = self.sortedMerge(a.next, b)
        else:
            result = b
            result.next = self.sortedMerge(a, b.next)
        return result
    
    def getMiddle(self, head):
        if (head == None):
            return head
        
        slow = head
        fast = head
        
        while (fast.next != None and fast.next.next != None):
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    def mergeSort(self, h):
        if h == None or h.next == None:
            return h
        
        middle = self.getMiddle(h)
        nextMiddle = middle.next

        middle.next = None

        left = self.mergeSort(h)

        right = self.mergeSort(nextMiddle)

        sortedlist = self.sortedMerge(left, right)
        return sortedlist
    # Time complexity O(N*logN)
    # Auxiliary Space: O(logN)
    
    def sequentialSearch(self, x):
        current = self.head
        comparison_count = 0

        while current != None:
            time.sleep(0.000001)
            comparison_count = comparison_count + 1
            if current.data == x:
                return [True, comparison_count]
            current = current.next
        
        return [False, comparison_count]
    # Time complexity O(N)
    # Auxiliary space: O(1)
    
    def sequentialSearchWithHash(self, x):
        hash_table = {}
        current = self.head
        
        while (current.next != None):
            hash_table[current.data] = current
            current = current.next
            time.sleep(0.000001)
        
        hash_table[current.data] = current

        if x in hash_table:
            time.sleep(0.000001)
            return [True, 1]
        else:
            return [False, 1]
        
    # Time complexity O(N)
    # Auxiliary space O(1)
