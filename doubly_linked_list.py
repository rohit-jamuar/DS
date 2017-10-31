#!/usr/bin/env python

class DoubleLink:
    def __init__(self, value):
        self.val = value
        self.left = self.right = None

class DoublyLinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def __str__(self):
        ctr, output = self.head, ''
        while ctr:
            output += str(ctr.val)
            ctr = ctr.right
            if ctr:
                output += ' '
        return output

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return self.length

    def __reversed__(self):
        ctr, output = self.tail, ''
        while ctr:
            output += str(ctr.val)
            ctr = ctr.left
            if ctr:
                output += ' '
        return output

    def insert(self, val):
        new_node = val if isinstance(val, DoubleLink) else DoubleLink(val)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.left = self.tail
            self.tail.right = new_node
            self.tail = new_node
        self.length += 1

    def insert_at_end(self, val):
        self.insert(val)

    def insert_at_start(self, val):
        new_node = val if isinstance(val, DoubleLink) else DoubleLink(val)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.right = self.head
            self.head.left = new_node
            self.head = new_node
        self.length += 1

    def insert_in_order(self, val):
        new_node = DoubleLink(val)
        if not self.head:
            self.head = self.tail = new_node
        else:
            pre, cur = None, self.head
            while cur and cur.val <= val:
                pre = cur
                cur = cur.right
            if cur == self.head:
                self.insert_at_start(new_node)
            elif pre == self.tail:
                self.insert_at_end(new_node)
            else:
                new_node.left = pre
                new_node.right = cur
                cur.left = pre.right = new_node
                self.length += 1

    def find(self, val):
        ctr = self.head
        while ctr and ctr.val != val:
            ctr = ctr.right
        return True if ctr and ctr.val == val else False

    def delete(self, val):
        pass

    def delete_at_start(self):
        pass

    def delete_at_end(self):
        pass
