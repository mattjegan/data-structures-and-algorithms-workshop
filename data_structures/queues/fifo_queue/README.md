# FIFO Queue

The FIFO Queue is the classic queue data structure. It only accepts items on to the end of the queue and only the oldest items at the front of the queue get returned. In this module you will need to implement various methods of the FIFO Queue:

* `push(self, item)`: Pushes an item on to the end of the queue.
* `pop(self)`: Removes and returns an item from the front of the queue.
* `peek(self)`: Returns the item at the front of the queue without removing it.
* `is_empty(self)`: Returns a boolean value indicating whether or not the queue is empty.
* `__len__(self)`: Returns the number of items in the queue.