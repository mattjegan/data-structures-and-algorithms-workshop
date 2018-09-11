class LifoStack:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        try:
            return self.data.pop()
        except IndexError:
            return None

    def peek(self):
        try:
            return self.data[-1]
        except IndexError:
            return None

    def is_empty(self):
        return self.data == []

    def __len__(self):
        return len(self.data)

