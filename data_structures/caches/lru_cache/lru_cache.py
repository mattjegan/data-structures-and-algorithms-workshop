from datetime import datetime

class Value:
    def __init__(self, value):
        self.value = value
        self.accessed = datetime.now()


class LRUCache:
    def __init__(self, limit):
        self.limit = limit
        self.data = {}

    def set_value(self, key, value):
        pass

    def get_value(self, key):
        pass

    def __len__(self):
        return len(self.data)
