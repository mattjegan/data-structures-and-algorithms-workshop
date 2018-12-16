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
        # Test basic deletion
        lru_cache = LRUCacheKlass(2)
        lru_cache.set_value('A', 123)
        lru_cache.set_value('B', 456)
        lru_cache.set_value('C', 789)

        assert len(lru_cache) == 2
        assert lru_cache.get_value('A') is None
        assert lru_cache.get_value('B') is 456
        assert lru_cache.get_value('C') is 789

    def _test_get_value(self, LRUCacheKlass):
        # Test updates least recently accessed
        lru_cache = LRUCacheKlass(2)
        lru_cache.set_value('A', 123)
        lru_cache.set_value('B', 456)

        assert len(lru_cache) == 2
        assert lru_cache.get_value('A') is 123

        lru_cache.set_value('C', 789)
        assert len(lru_cache) == 2
        assert lru_cache.get_value('B') is None
        assert lru_cache.get_value('A') is 123
        assert lru_cache.get_value('C') is 789
