
SIZE = 100

class HashTable:
    def __init__(self):
        # This hash table only has 100 slots to store stuff in
        self.data = [None for _ in range(SIZE)]
    
    @staticmethod
    def _hash(key):
        # Returns an index between 0 and SIZE to store some value at
        pass

    def get_value(self, key):
        pass
    
    def set_value(self, key, value):
        pass
    
    def delete_value(self, key):
        pass
