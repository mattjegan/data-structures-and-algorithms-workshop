import random

SIZE = 100

class HashTable:
    def __init__(self):
        # This hash table only has 100 slots to store stuff in
        self.data = [None for _ in range(SIZE)]
    
    @staticmethod
    def _hash(key):
        # Returns an index between 0 and SIZE to store some value at
        random.seed(key)
        return random.randrange(0, SIZE)

    def get_value(self, key):
        return self.data[HashTable._hash(key)]
    
    def set_value(self, key, value):
        hash_value = HashTable._hash(key)
        if self.data[hash_value] is None:
            self.data[hash_value] = value
            return
        
        # There was a collision, let's double hash
        # TOD
    
    def delete_value(self, key):
        self.data[HashTable._hash(key)] = None
