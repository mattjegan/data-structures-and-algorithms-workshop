
class Node:
    def __init__(self, next: "Node", prev: "Node", value):
        self.next = next
        self.prev = prev
        self.value = value


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None, None, 1)
    
    def append(self, value):
        pass
    
    def insert(self, value, index):
        pass
    
    def remove(self, index):
        pass
    
    def get_index(self, index):
        pass

    def __len__(self):
        pass
