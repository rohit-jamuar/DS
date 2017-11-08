#!/usr/bin/env python3

from doubly_linked_list import DoublyLinkedList

class Queue:
    def __init__(self):
        self.store = DoublyLinkedList()

    def __len__(self):
        return len(self.store)

    def __str__(self):
        return self.store.__str__()

    def __repr__(self):
        return self.__str__()

    def add(self, val):
        self.store.insert_at_end(val)

    def remove(self):
        return self.store.delete_at_start()

    def seek(self):
        return self.store[0]
