
class Node:
    def __init__(self, next: "Node", value):
        self.next = next
        self.value = value


class SingularlyLinkedList:
    def __init__(self):
        self.head = Node(None, 1)
    
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
