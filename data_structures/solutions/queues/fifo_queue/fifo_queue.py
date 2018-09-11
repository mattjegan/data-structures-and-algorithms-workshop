class FifoQueue:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        try:
            item = self.data[0]
            del self.data[0]
            return item
        except IndexError:
            return None

    def peek(self):
        try:
            return self.data[0]
        except IndexError:
            return None

    def is_empty(self):
        return len(self.data) == 0

    def __len__(self):
        return len(self.data)

