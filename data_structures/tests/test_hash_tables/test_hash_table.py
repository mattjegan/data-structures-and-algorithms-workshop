from unittest import TestCase
from data_structures.hash_tables.hash_table.hash_table import HashTable
from data_structures.solutions.hash_tables.hash_table.hash_table import HashTable as HashTableSolution

class TestHashTable(TestCase):
    def test_solution_set_value(self):
        self._test_set_value(HashTableSolution)
    
    def test_set_value(self):
        self._test_set_value(HashTable)

    def test_solution_get_value(self):
        self._test_get_value(HashTableSolution)
    
    def test_get_value(self):
        self._test_get_value(HashTable)

    def test_solution_delete_value(self):
        self._test_delete_value(HashTableSolution)
    
    def test_delete_value(self):
        self._test_delete_value(HashTable)

    def _test_set_value(self, HashTableKlass):
        hash_table = HashTableKlass()
        hash_table.set_value('a', 2)
        assert hash_table.get_value('a') == 2

    def _test_get_value(self, HashTableKlass):
        hash_table = HashTableKlass()
        assert hash_table.get_value('a') is None

        hash_table.set_value('a', 2)
        assert hash_table.get_value('a') == 2
    
    def _test_delete_value(self, HashTableKlass):
        hash_table = HashTableKlass()
        hash_table.set_value('a', 2)
        assert hash_table.get_value('a') == 2

        hash_table.delete_value('a')
        assert hash_table.get_value('a') is None
