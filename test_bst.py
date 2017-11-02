#!/usr/bin/env python

import unittest
from bst import BST
import sys
from utils import exec_and_capture_stdout

class TestInsertAndTraversal(unittest.TestCase):
    def setUp(self):
        self.bst = BST()
        for i in [50, 10, 70, 60, 90, 5]:
            self.bst.insert(i)

    @exec_and_capture_stdout
    def test_inorder_traversal(self):
        self.bst.traverse_bst()
        std_output = sys.stdout.getvalue().replace('\n', ' ').strip()
        self.assertEqual(std_output, '5 10 50 60 70 90')

    @exec_and_capture_stdout
    def test_preorder_traversal(self):
        self.bst.traverse_bst('pre')
        std_output = sys.stdout.getvalue().replace('\n', ' ').strip()
        self.assertEqual(std_output, '50 10 5 70 60 90')

    @exec_and_capture_stdout
    def test_postorder_traversal(self):
        self.bst.traverse_bst('post')
        std_output = sys.stdout.getvalue().replace('\n', ' ').strip()
        self.assertEqual(std_output, '5 10 60 90 70 50')

class TestHeight(unittest.TestCase):
    def setUp(self):
        self.bst = BST()
        for i in [50, 10, 70, 60, 90, 5]:
            self.bst.insert(i)

    def test_height(self):
        self.assertEqual(self.bst.height(), 2)

class TestDelete(unittest.TestCase):
    def setUp(self):
        self.bst = BST()
        for i in [50, 10, 70, 60, 90, 5]:
            self.bst.insert(i)

    @exec_and_capture_stdout
    def test_delete_leaf(self):
        self.bst.delete(5)
        self.bst.traverse_bst()
        std_output = sys.stdout.getvalue().replace('\n', ' ').strip()
        self.assertEqual(std_output, '10 50 60 70 90')

    @exec_and_capture_stdout
    def test_delete_single_child(self):
        self.bst.delete(10)
        self.bst.traverse_bst()
        std_output = sys.stdout.getvalue().replace('\n', ' ').strip()
        self.assertEqual(std_output, '5 50 60 70 90')

    @exec_and_capture_stdout
    def test_delete_two_children(self):
        self.bst.delete(70)
        self.bst.traverse_bst()
        std_output = sys.stdout.getvalue().replace('\n', ' ').strip()
        self.assertEqual(std_output, '5 10 50 60 90')

    @exec_and_capture_stdout
    def test_delete_inexistent(self):
        self.bst.delete(100)
        self.bst.traverse_bst()
        std_output = sys.stdout.getvalue().replace('\n', ' ').strip()
        self.assertEqual(std_output, '5 10 50 60 70 90')

if __name__ == '__main__':
    unittest.main()
