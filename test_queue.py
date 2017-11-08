#!/usr/bin/env python

import unittest
from queue import Queue
import sys
from utils import exec_and_capture_stdout

class TestQueueOps(unittest.TestCase):
    def setUp(self):
        self.q = Queue()
        for i in range(5):
            self.q.add(i)

    @exec_and_capture_stdout
    def test_add(self):
        print(self.q)
        self.assertEqual(sys.stdout.getvalue().strip(), '0 1 2 3 4')
        self.assertEqual(len(self.q), 5)

    def test_remove(self):
        self.assertEqual(self.q.remove(), 0)
        self.assertEqual(self.q.remove(), 1)
        self.assertEqual(self.q.remove(), 2)
        self.assertEqual(self.q.remove(), 3)
        self.assertEqual(self.q.remove(), 4)
        self.assertFalse(self.q.remove())

    def test_seek(self):
        self.assertEqual(self.q.seek(), 0)

if __name__ == '__main__':
    unittest.main()
