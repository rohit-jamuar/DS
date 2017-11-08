#!/usr/bin/env python

import unittest
from stack import Stack
import sys
from utils import exec_and_capture_stdout

class TestStackOps(unittest.TestCase):
    def setUp(self):
        self.stk = Stack()
        for i in range(5):
            self.stk.push(i)

    @exec_and_capture_stdout
    def test_push(self):
        print(self.stk)
        self.assertEqual(sys.stdout.getvalue().strip(), '4 3 2 1 0')
        self.assertEqual(len(self.stk), 5)

    def test_pop(self):
        self.assertEqual(self.stk.pop(), 4)
        self.assertEqual(self.stk.pop(), 3)
        self.assertEqual(self.stk.pop(), 2)
        self.assertEqual(self.stk.pop(), 1)
        self.assertEqual(self.stk.pop(), 0)
        self.assertFalse(self.stk.pop())

    def test_seek(self):
        self.assertEqual(self.stk.seek(), 4)

if __name__ == '__main__':
    unittest.main()
