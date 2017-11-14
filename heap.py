#!/usr/bin/env python

class Heap:
    def __init__(self, heap_type='min'):
        self.data = list()
        assert heap_type in ['min', 'max'], 'Invalid heap-type : should be min or max!'
        self.heap_type = heap_type

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return ' '.join(self.data)

    def __repr__(self):
        return self.__str__()

    def seek_root(self):
        if self.data:
            return self.data[0]

    def insert(self, val):
        self.data.append(val)
        if len(self.data) > 1:
           self._bubble_up()

    def remove(self, end=None):
        if self.data:
            item_removed = self.data[0]
            if len(self.data) > 1:
                self.data[0] = self.data[-1]
                self.data.pop(len(self.data)-1)
                self._bubble_down(end if end else len(self.data))
            else:
                self.data = list()
            return item_removed

    def _bubble_up(self):
        ctr = len(self.data)-1
        if self.heap_type == 'min':
            while ctr > 0:
                if self.data[ctr] < self.data[ctr//2]:
                    self.data[ctr], self.data[ctr//2] = self.data[ctr//2], self.data[ctr]
                ctr = ctr // 2
        else:
            while ctr > 0:
                if self.data[ctr] > self.data[ctr//2]:
                    self.data[ctr], self.data[ctr//2] = self.data[ctr//2], self.data[ctr]
                ctr = ctr // 2

    def _bubble_down(self, last_index):
        ctr, data_size = 0, last_index
        if self.heap_type == 'min':
            while ctr < data_size:
                inc_by_one, inc_by_two = False, False
                if (2*ctr+1) < data_size and self.data[ctr] > self.data[2*ctr+1]:
                    self.data[2*ctr+1], self.data[ctr] = self.data[ctr], self.data[2*ctr+1]
                    inc_by_one = True
                if (2*ctr+2) < data_size and self.data[ctr] > self.data[2*ctr+2]:
                    self.data[2*ctr+2], self.data[ctr] = self.data[ctr], self.data[2*ctr+2]
                    inc_by_two = True
                if inc_by_two:
                    ctr = 2*ctr + 2
                elif inc_by_one:
                    ctr = 2*ctr + 1
                else:
                    break
        else:
            while ctr < data_size:
                inc_by_one, inc_by_two = False, False
                if (2*ctr+1) < data_size and self.data[ctr] < self.data[2*ctr+1]:
                    self.data[2*ctr+1], self.data[ctr] = self.data[ctr], self.data[2*ctr+1]
                    inc_by_one = True
                if (2*ctr+2) < data_size and self.data[ctr] < self.data[2*ctr+2]:
                    self.data[2*ctr+2], self.data[ctr] = self.data[ctr], self.data[2*ctr+2]
                    inc_by_two = True
                if inc_by_two:
                    ctr = 2*ctr + 2
                elif inc_by_one:
                    ctr = 2*ctr + 1
                else:
                    break
