
from unittest import TestCase
import random
from data_structures.sorts.selection_sort.selection_sort import selection_sort

class TestSelectionSort(TestCase):
    def test_sort(self):
        self._test_sort(selection_sort)
    
    def _test_sort(self, selection_sort_func):
        array = [random.randrange(0, 100) for _ in range(100)]
        assert selection_sort_func(array) == sorted(array)
