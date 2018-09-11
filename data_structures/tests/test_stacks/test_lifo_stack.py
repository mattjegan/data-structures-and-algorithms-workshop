from unittest import TestCase
from data_structures.stacks.lifo_stack.lifo_stack import LifoStack
from data_structures.solutions.stacks.lifo_stack.lifo_stack import LifoStack as LifoStackSolution

class TestLifoStack(TestCase):
    def test_solution_push(self):
        self._test_push(LifoStackSolution)
    
    def test_push(self):
        self._test_push(LifoStack)

    def test_solution_pop(self):
        self._test_pop(LifoStackSolution)
    
    def test_pop(self):
        self._test_pop(LifoStack)

    def test_solution_peek(self):
        self._test_peek(LifoStackSolution)
    
    def test_peek(self):
        self._test_peek(LifoStack)

    def test_solution_is_empty(self):
        self._test_is_empty(LifoStackSolution)
    
    def test_is_empty(self):
        self._test_is_empty(LifoStack)

    def test_solution_len(self):
        self._test_len(LifoStackSolution)
    
    def test_len(self):
        self._test_len(LifoStack)

    def _test_push(self, LifoStackKlass):
        stack = LifoStackKlass()
        assert stack.data == []

        stack.push(1)
        assert stack.data == [1]

        stack.push(2)
        assert stack.data == [1, 2]

    def _test_pop(self, LifoStackKlass):
        stack = LifoStackKlass()
        assert stack.data == []

        stack.push(1)
        stack.push(2)

        assert stack.pop() == 2
        assert stack.pop() == 1
        assert stack.pop() is None

    def _test_peek(self, LifoStackKlass):
        stack = LifoStackKlass()
        assert stack.data == []

        stack.push(1)
        stack.push(2)

        assert stack.peek() == 2
        assert stack.peek() == 2

        stack.pop()

        assert stack.peek() == 1

        stack.pop()

        assert stack.peek() is None
    
    def _test_is_empty(self, LifoStackKlass):
        stack = LifoStackKlass()
        assert stack.data == []
        assert stack.is_empty()

        stack.push(1)

        assert stack.is_empty() is False

        stack.pop()

        assert stack.is_empty()

    def _test_len(self, LifoStackKlass):
        stack = LifoStackKlass()
        assert len(stack) == 0

        stack.push(1)
        assert len(stack) == 1

        stack.pop()
        assert len(stack) == 0
