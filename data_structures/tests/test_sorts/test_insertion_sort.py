
from unittest import TestCase
import random
from data_structures.sorts.insertion_sort.insertion_sort import insertion_sort

class TestInsertionSort(TestCase):
    def test_sort(self):
        self._test_sort(insertion_sort)
    
    def _test_sort(self, insertion_sort_func):
        array = [random.randrange(0, 100) for _ in range(100)]
        assert insertion_sort_func(array) == sorted(array)
