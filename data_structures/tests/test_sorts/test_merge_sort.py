
from unittest import TestCase
import random
from data_structures.sorts.merge_sort.merge_sort import merge_sort

class TestMergeSort(TestCase):
    def test_sort(self):
        self._test_sort(merge_sort)
    
    def _test_sort(self, merge_sort_func):
        array = [random.randrange(0, 100) for _ in range(100)]
        assert merge_sort_func(array) == sorted(array)
