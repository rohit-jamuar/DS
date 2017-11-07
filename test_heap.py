#!/usr/bin/env python

import unittest
from heap import Heap
import sys

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
