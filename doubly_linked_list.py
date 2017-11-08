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

    def __getitem__(self, k):
        if any([k < 0, k >= self.length, not self.head]):
            return
        else:
            ctr = self.head
            while k:
                ctr = ctr.right
                k -= 1
            if ctr:
                return ctr.val

    def reverse(self):
        if self.head:
            front, back, ctr = self.head, self.tail, self.length//2
            while ctr >= 1:
                front.val, back.val = back.val, front.val
                front, back = front.right, back.left
                ctr -= 1

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
            self.length += 1
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
        if self.head:
            cur, pre = self.head, None
            while cur and cur.val != val:
                pre = cur
                cur = cur.right
            if cur:
                if cur == self.head:
                    return self.delete_at_start()
                elif cur == self.tail:
                    return self.delete_at_end()
                else:
                    val_to_return = cur.val
                    pre.right = cur.right
                    cur.right.left = pre
                    self.length -= 1
                    del(cur)
                    return val_to_return

    def delete_at_start(self):
        if self.head:
            cur = self.head
            val_to_return = cur.val
            self.head = cur.right
            if self.head:
                self.head.left = None
            if cur == self.tail:
                self.tail = self.head
            self.length -= 1
            del(cur)
            return val_to_return

    def delete_at_end(self):
        if self.tail:
            cur = self.tail
            val_to_return = cur.val
            self.tail = self.tail.left
            if self.tail:
                self.tail.right = None
            if cur == self.head:
                self.head = self.tail
            self.length -= 1
            del(cur)
            return val_to_return
