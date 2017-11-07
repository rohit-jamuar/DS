#!/usr/bin/env python3

class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

class TernanyNode:
    def __init__(self, val):
        self.val = val
        self.left = self.mid = self.right = None

class PriorityQTask:
    def __init__(self, priority, name=''):
        assert isinstance(priority, int), 'Priority of a task should be an integer!'
        self.priority = priority
        self.name = name

    def __eq__(self, other):
        assert isinstance(other, PriorityQTask), 'Can only compare two PriorityQTask objects!'
        return self.priority == other.priority

    def __lt__(self, other):
        assert isinstance(other, PriorityQTask), 'Can only compare two PriorityQTask objects!'
        return self.priority < other.priority
