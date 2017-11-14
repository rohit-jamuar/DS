#!/usr/bin/env python

import unittest
from heap import Heap
import sys
from node_definition import PriorityQTask

class TestInsert(unittest.TestCase):
    def setUp(self):
        self.heap_min = Heap()
        self.heap_max = Heap('max')
        for i in [10, 13, 5, 65, 78]:
            self.heap_min.insert(i)
            self.heap_max.insert(i)

    def test_check_root(self):
        self.assertEqual(self.heap_min.seek_root(), 5)
        self.assertEqual(self.heap_max.seek_root(), 78)

class TestDelete(unittest.TestCase):
    def setUp(self):
        self.heap_min = Heap()
        self.heap_max = Heap('max')
        for i in [10, 13, 5, 65, 78]:
            self.heap_min.insert(i)
            self.heap_max.insert(i)

    def test_check_deleted_order_minHeap(self):
        self.assertEqual(self.heap_min.remove(), 5)
        self.assertEqual(self.heap_min.remove(), 10)
        self.assertEqual(self.heap_min.remove(), 13)
        self.assertEqual(self.heap_min.remove(), 65)
        self.assertEqual(self.heap_min.remove(), 78)

    def test_check_deleted_order_maxHeap(self):
        self.assertEqual(self.heap_max.remove(), 78)
        self.assertEqual(self.heap_max.remove(), 65)
        self.assertEqual(self.heap_max.remove(), 13)
        self.assertEqual(self.heap_max.remove(), 10)
        self.assertEqual(self.heap_max.remove(), 5)

    def test_deleted_noop(self):
        for i in range(len(self.heap_min)):
            self.heap_min.remove()
        self.assertFalse(self.heap_min.remove())

class TestPriorityQ(unittest.TestCase):
    def setUp(self):
        self.PQ = Heap()
        self.PQ.insert(PriorityQTask(100, 'socialize?'))
        self.PQ.insert(PriorityQTask(2, 'code'))
        self.PQ.insert(PriorityQTask(0, 'sleep'))
        self.PQ.insert(PriorityQTask(4, 'study'))
        self.PQ.insert(PriorityQTask(1, 'sleep, really!'))
        self.PQ.insert(PriorityQTask(3, 'plan ahead'))

    def test_ordering(self):
        self.assertEqual(self.PQ.remove().name, 'sleep')
        self.assertEqual(self.PQ.remove().name, 'sleep, really!')
        self.assertEqual(self.PQ.remove().name, 'code')
        self.assertEqual(self.PQ.remove().name, 'plan ahead')
        self.assertEqual(self.PQ.remove().name, 'study')
        self.assertEqual(self.PQ.remove().name, 'socialize?')
