#!/usr/bin/env python3

class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

class TernanyNode:
    def __init__(self, val):
        self.val = val
        self.left = self.mid = self.right = None
