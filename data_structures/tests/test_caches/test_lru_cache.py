from unittest import TestCase
from data_structures.caches.lru_cache.lru_cache import LRUCache
from data_structures.solutions.caches.lru_cache.lru_cache import LRUCache as LRUCacheSolution

class TestLRUCache(TestCase):
    def test_solution_set_value(self):
        self._test_set_value(LRUCacheSolution)
    
    def test_set_value(self):
        self._test_set_value(LRUCache)

    def test_solution_get_value(self):
        self._test_get_value(LRUCacheSolution)
    
    def test_get_value(self):
        self._test_get_value(LRUCache)

    def _test_set_value(self, LRUCacheKlass):
        lru_cache = LRUCacheKlass()
        # TODO

    def _test_get_value(self, LRUCacheKlass):
        hash_table = LRUCacheKlass()
        # TODO
