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
        if self.data.get(key, None) is None:

            if len(self.data) == self.limit:
                # We need to remove the LRU (Least Recently Used) value
                sorted_list = sorted([(k, v.accessed) for (k, v) in self.data.items()], key=lambda x: x[1])
                del self.data[sorted_list[0][0]]

            self.data[key] = Value(value)

    def get_value(self, key):
        value = self.data.get(key, None)
        if value:
            value.accessed = datetime.now()
            return value.value
        
        return None

    def __len__(self):
        return len(self.data)
