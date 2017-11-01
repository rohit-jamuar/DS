#!/usr/bin/env python

import unittest
from doubly_linked_list import DoublyLinkedList
import sys
from utils import exec_and_capture_stdout

class TestInsertFindAndReverse(unittest.TestCase):
    def setUp(self):
        self.ll = DoublyLinkedList()
        for i in range(10):
            self.ll.insert(i)

    @exec_and_capture_stdout
    def test_insert(self):
        print(self.ll)
        self.assertEqual(sys.stdout.getvalue().strip(), '0 1 2 3 4 5 6 7 8 9')
        self.assertEqual(len(self.ll), 10)

    @exec_and_capture_stdout
    def test_insert_at_start(self):
        self.ll.insert_at_start(-1)
        print(self.ll)
        self.assertEqual(sys.stdout.getvalue().strip(), '-1 0 1 2 3 4 5 6 7 8 9')

    @exec_and_capture_stdout
    def test_insert_at_end(self):
        self.ll.insert_at_end(10)
        print(self.ll)
        self.assertEqual(sys.stdout.getvalue().strip(), '0 1 2 3 4 5 6 7 8 9 10')

    @exec_and_capture_stdout
    def test_insert_in_order(self):
        new_ll = DoublyLinkedList()
        new_ll.insert_in_order(10)
        new_ll.insert_in_order(1)
        new_ll.insert_in_order(12)
        new_ll.insert_in_order(3)
        new_ll.insert_in_order(1)
        new_ll.insert_in_order(4)
        print(new_ll)
        self.assertEqual(sys.stdout.getvalue().strip(), '1 1 3 4 10 12')

    def test_find(self):
        self.assertTrue(self.ll.find(6))
        self.assertFalse(self.ll.find(12))

    @exec_and_capture_stdout
    def test_reverse(self):
        self.ll.reverse()
        print(self.ll)
        self.assertEqual(sys.stdout.getvalue().strip(), '9 8 7 6 5 4 3 2 1 0')
        self.assertEqual(len(self.ll), 10)

    @exec_and_capture_stdout
    def test_reverse_odd_num_elements(self):
        new_ll = DoublyLinkedList()
        for i in range(9):
            new_ll.insert(i)
        new_ll.reverse()
        print(new_ll)
        self.assertEqual(sys.stdout.getvalue().strip(), '8 7 6 5 4 3 2 1 0')
        self.assertEqual(len(new_ll), 9)

    @exec_and_capture_stdout
    def test_multiple_reverse(self):
        self.ll.reverse()
        self.ll.reverse()
        self.ll.reverse()
        self.ll.reverse()
        print(self.ll)
        self.assertEqual(sys.stdout.getvalue().strip(), '0 1 2 3 4 5 6 7 8 9')
        self.assertEqual(len(self.ll), 10)

    def test_index(self):
        self.assertEqual(self.ll[2], 2)

    def test_index_noop(self):
        self.assertFalse(self.ll[17])

class TestDelete(unittest.TestCase):
    def setUp(self):
        self.ll = DoublyLinkedList()
        for i in range(10):
            self.ll.insert(i)

    @exec_and_capture_stdout
    def test_delete_multiple(self):
        self.ll.delete(0)
        self.ll.delete(9)
        self.ll.delete(4)
        self.ll.delete(5)
        print(self.ll)
        self.assertEqual(sys.stdout.getvalue().strip(), '1 2 3 6 7 8')
        self.assertEqual(len(self.ll), 6)

    @exec_and_capture_stdout
    def test_delete_at_start(self):
        self.ll.delete_at_start()
        print(self.ll)
        self.assertEqual(sys.stdout.getvalue().strip(), '1 2 3 4 5 6 7 8 9')
        self.assertEqual(len(self.ll), 9)

    @exec_and_capture_stdout
    def test_delete_at_end(self):
        self.ll.delete_at_end()
        print(self.ll)
        self.assertEqual(sys.stdout.getvalue().strip(), '0 1 2 3 4 5 6 7 8')
        self.assertEqual(len(self.ll), 9)

    @exec_and_capture_stdout
    def test_delete_noop(self):
        self.ll.delete(15)
        print(self.ll)
        self.assertEqual(sys.stdout.getvalue().strip(), '0 1 2 3 4 5 6 7 8 9')
        self.assertEqual(len(self.ll), 10)


if __name__ == '__main__':
    unittest.main()
