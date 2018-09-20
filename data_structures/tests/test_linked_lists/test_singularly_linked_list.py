from unittest import TestCase
from data_structures.linked_lists.singularly_linked_list.singularly_linked_list import SingularlyLinkedList
from data_structures.solutions.linked_lists.singularly_linked_list.singularly_linked_list import SingularlyLinkedList as SingularlyLinkedListSolution

class TestSingularlyLinkedList(TestCase):
    def test_append(self):
        self._test_append(SingularlyLinkedList)

    def test_solution_append(self):
        self._test_append(SingularlyLinkedListSolution)
    
    def test_insert(self):
        self._test_insert(SingularlyLinkedList)

    def test_solution_insert(self):
        self._test_insert(SingularlyLinkedListSolution)

    def test_remove(self):
        self._test_remove(SingularlyLinkedList)

    def test_solution_remove(self):
        self._test_remove(SingularlyLinkedListSolution)

    def test_get_index(self):
        self._test_get_index(SingularlyLinkedList)

    def test_solution_get_index(self):
        self._test_get_index(SingularlyLinkedListSolution)

    def test_len(self):
        self._test_len(SingularlyLinkedList)

    def test_solution_len(self):
        self._test_len(SingularlyLinkedListSolution)

    def _test_append(self, SingularlyLinkedListKlass):
        linked_list = SingularlyLinkedListKlass()
        linked_list.append(2)
        
        assert linked_list.head.next is not None
        assert linked_list.head.next.value == 2
        assert linked_list.head.next.next is None
    
    def _test_insert(self, SingularlyLinkedListKlass):
        linked_list = SingularlyLinkedListKlass()
        linked_list.append(2)
        linked_list.append(3)

        linked_list.insert(4, 1)
        linked_list.insert(5, 1)

        assert linked_list.head.value == 1
        assert linked_list.head.next.value == 5
        assert linked_list.head.next.next.value == 4
        assert linked_list.head.next.next.next.value == 2
        assert linked_list.head.next.next.next.next.value == 3
    
    def _test_remove(self, SingularlyLinkedListKlass):
        linked_list = SingularlyLinkedListKlass()
        linked_list.append(2)
        linked_list.append(3)

        linked_list.remove(1)

        assert linked_list.head.value == 1
        assert linked_list.head.next.value == 3
        assert linked_list.head.next.next is None

        linked_list.remove(1)

        assert linked_list.head.value == 1 
        assert linked_list.head.next is None
    
    def _test_get_index(self, SingularlyLinkedListKlass):
        linked_list = SingularlyLinkedListKlass()
        linked_list.append(2)
        linked_list.append(3)

        assert linked_list.get_index(1) == 2
        assert linked_list.get_index(2) == 3

    def _test_len(self, SingularlyLinkedListKlass):
        linked_list = SingularlyLinkedListKlass()
        assert len(linked_list) == 1
        
        linked_list.append(2)
        assert len(linked_list) == 2

        linked_list.append(3)
        assert len(linked_list) == 3
