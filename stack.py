#!/usr/bin/env python3

from linked_list import SinglyLinkedList

class Stack:
    def __init__(self):
        self.store = SinglyLinkedList()

    def __len__(self):
        return len(self.store)

    def __str__(self):
        return self.store.__str__()

    def __repr__(self):
        return self.__str__()

    def push(self, val):
        self.store.insert_at_start(val)

    def pop(self):
        return self.store.delete_at_start()

    def seek(self):
        return self.store[0]
