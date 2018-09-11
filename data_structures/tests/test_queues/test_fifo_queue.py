from unittest import TestCase
from data_structures.queues.fifo_queue.fifo_queue import FifoQueue
from data_structures.solutions.queues.fifo_queue.fifo_queue import FifoQueue as FifoQueueSolution

class TestFifoQueue(TestCase):
    def test_solution_push(self):
        self._test_push(FifoQueueSolution)
    
    def test_push(self):
        self._test_push(FifoQueue)

    def test_solution_pop(self):
        self._test_pop(FifoQueueSolution)
    
    def test_pop(self):
        self._test_pop(FifoQueue)

    def test_solution_peek(self):
        self._test_peek(FifoQueueSolution)
    
    def test_peek(self):
        self._test_peek(FifoQueue)

    def test_solution_is_empty(self):
        self._test_is_empty(FifoQueueSolution)
    
    def test_is_empty(self):
        self._test_is_empty(FifoQueue)

    def test_solution_len(self):
        self._test_len(FifoQueueSolution)
    
    def test_len(self):
        self._test_len(FifoQueue)

    def _test_push(self, FifoQueueKlass):
        queue = FifoQueueKlass()
        assert queue.data == []

        queue.push(1)
        assert queue.data == [1]

        queue.push(2)
        assert queue.data == [1, 2]

    def _test_pop(self, FifoQueueKlass):
        queue = FifoQueueKlass()
        assert queue.data == []

        queue.push(1)
        queue.push(2)

        assert queue.pop() == 1
        assert queue.pop() == 2
        assert queue.pop() is None

    def _test_peek(self, FifoQueueKlass):
        queue = FifoQueueKlass()
        assert queue.data == []

        queue.push(1)
        queue.push(2)

        assert queue.peek() == 1
        assert queue.peek() == 1

        queue.pop()

        assert queue.peek() == 2

        queue.pop()

        assert queue.peek() is None
    
    def _test_is_empty(self, FifoQueueKlass):
        queue = FifoQueueKlass()
        assert queue.data == []
        assert queue.is_empty()

        queue.push(1)

        assert queue.is_empty() is False

        queue.pop()

        assert queue.is_empty()

    def _test_len(self, FifoQueueKlass):
        queue = FifoQueueKlass()
        assert len(queue) == 0

        queue.push(1)
        assert len(queue) == 1

        queue.pop()
        assert len(queue) == 0
