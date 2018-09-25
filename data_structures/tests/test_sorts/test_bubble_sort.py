
from unittest import TestCase
import random
from data_structures.sorts.bubble_sort.bubble_sort import bubble_sort

class TestBubbleSort(TestCase):
    def test_sort(self):
        self._test_sort(bubble_sort)
    
    def _test_sort(self, bubble_sort_func):
        array = [random.randrange(0, 100) for _ in range(100)]
        assert bubble_sort_func(array) == sorted(array)
