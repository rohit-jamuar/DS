#!/usr/bin/env python

class Link:
    def __init__(self, value):
        self.val = value
        self.right = None

class SinglyLinkedList:
    def __init__(self):
        self.length = 0
        self.root = None

    def __len__(self):
        return self.length

    def __str__(self):
        ctr, output = self.root, ''
        while ctr:
            output += str(ctr.val)
            ctr = ctr.right
            if ctr:
                output += ' '
        return output

    def __repr__(self):
        return self.__str__()

    def __getitem__(self, k):
        if any([k < 0, k >= self.length, not self.root]):
            return
        else:
            ctr = self.root
            while k > 0:
                ctr = ctr.right
                k -= 1
            if ctr:
                return ctr.val

    def insert(self, val):
        self.insert_at_end(val)

    def insert_at_end(self, val):
        if not self.root:
            self.root = Link(val)
        else:
            cur = self.root
            while cur.right != None:
                cur = cur.right
            cur.right = Link(val)
        self.length += 1

    def insert_at_start(self, val):
        if not self.root:
            self.root = Link(val)
        else:
            new_node = Link(val)
            new_node.right = self.root
            self.root = new_node
        self.length += 1

    def insert_in_order(self, val):
        if not self.root:
            self.root = Link(val)
            self.length += 1
        else:
            pre, cur = None, self.root
            while cur and cur.val <= val:
                pre = cur
                cur = cur.right
            if cur and not pre:
                #first item
                self.insert_at_start(val)
            elif pre and not cur:
                #new last item
                self.insert_at_end(val)
            else:
                #new in-between-er
                new_node = Link(val)
                new_node.right = cur
                pre.right = new_node
                self.length += 1

    def find(self, val):
        ctr = self.root
        while ctr and ctr.val != val:
            ctr = ctr.right
        if not ctr:
            return False
        return ctr.val == val

    def delete(self, val):
        cur, pre = self.root, None
        while cur and cur.val != val:
            pre = cur
            cur = cur.right
        if cur:
            if cur == self.root:
                self.root = cur.right
            else:
                pre.right = cur.right
            val_to_return = cur.val
            del(cur)
            self.length -= 1
            return val_to_return

    def delete_at_start(self):
        if self.root:
            return self.delete(self.root.val)

    def delete_at_end(self):
        pre, cur = None, self.root
        while cur and cur.right:
            pre = cur
            cur = cur.right
        if pre:
            pre.right = None
            val_to_return = cur.val
            del(cur)
            self.length -= 1
            return val_to_return
