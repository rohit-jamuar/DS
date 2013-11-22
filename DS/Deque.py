#!/usr/bin/python

from biNode import Node

class DQueue:
	
	def __init__(self):
		self.__head,self.__tail=None,None

	def enqueueFront(self,val):
		if not self.__head:
			self.__tail=self.__head=Node(val)
		else:
			temp=Node(val)
			temp.Next=self.__head
			self.__head.Prev=temp
			self.__head=temp

	def dequeueFront(self):
		if self.__head==self.__tail:
			self.__head=self.__tail=None
		elif self.__head:
			self.__head=self.__head.Next
			if self.__head:
				self.__head.Prev=None
		else:
			print "Deque is empty!"

	def enqueueBack(self,val):
		if not self.__tail:
			self.__tail=self.__head=Node(val)
		else:
			temp=Node(val)
			self.__tail.Next=temp
			temp.Prev=self.__tail
			self.__tail=temp

	def dequeueBack(self):
		if self.__head==self.__tail: # make sure to check if there is 1 element left <-- tricky case!
			self.__head=self.__tail=None
		elif self.__tail:
			self.__tail=self.__tail.Prev
			if self.__tail:
				self.__tail.Next=None
		else:
			print "Deque is empty!"

	def peekFront(self):
		if self.__head:
			return self.__head.val
		else:
			print "Deque is empty!"
	
	def peekBack(self):
		if self.__tail:
			return self.__tail.val
		else:
			print "Deque is empty!"

	def printDeque(self):
		cur=self.__head
		while cur:
			print cur.val,
			cur=cur.Next
		print ""
	
	def printDequeReverse(self):
		cur=self.__tail
		while cur:
			print cur.val,
			cur=cur.Prev
		print ""
