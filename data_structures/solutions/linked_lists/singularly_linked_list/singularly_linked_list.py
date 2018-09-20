
class Node:
    def __init__(self, next: "Node", value):
        self.next = next
        self.value = value


class SingularlyLinkedList:
    def __init__(self):
        self.head = Node(None, 1)
    
    def append(self, value):
        curr = self.head
        
        while curr.next is not None:
            curr = curr.next
        
        curr.next = Node(None, value)
    
    def insert(self, value, index):
        curr = self.head
        curr_index = 0

        while curr_index < index - 1 and curr.next is not None:
            curr = curr.next
            curr_index += 1
        
        if curr_index != index - 1:
            raise IndexError('Index not found in list')
         
        curr.next = Node(curr.next, value)
    
    def remove(self, index):
        curr = self.head
        curr_index = 0

        while curr_index < index - 1 and curr.next is not None:
            curr = curr.next
            curr_index += 1
        
        if curr_index != index - 1:
            raise IndexError('Index not found in list')
         
        curr.next = curr.next.next
    
    def get_index(self, index):
        curr = self.head
        curr_index = 0

        while curr_index < index - 1 and curr.next is not None:
            curr = curr.next
            curr_index += 1
        
        if curr_index != index - 1:
            raise IndexError('Index not found in list')

        return curr.next.value

    def __len__(self):
        curr = self.head
        count = 1

        while curr.next is not None:
            curr = curr.next
            count += 1

        return count
