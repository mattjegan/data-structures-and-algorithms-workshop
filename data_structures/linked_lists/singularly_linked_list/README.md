# Singularly Linked List

Singularly linked lists are the most basic of linked lists. They consist of a "head" which points to the initial node and each node has only two properties, "next" and "value" where "next" is the next node in the list and "value" is some value stored at that node.

In this module, you will need to implement a few methods for our singularly linked list:

* `append(self, value)`: Adds a node to the end of the list with the value.
* `insert(self, value, index)`: Inserts a node with the value before the current element at the given index.
* `remove(self, index)`: Removes the current node at the given index.
* `get_index(self, index)`: Returns the value stored on the node at the given index.
* `__len__(self)`: Returns the length of the linked list, that is the number of nodes in the linked list.