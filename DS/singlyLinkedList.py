#!/usr/bin/python

from Node import Node

class SL:
	__size=0
	
	def __init__(self):
		self.__head=None

	def insert(self,x):
		if self.__head:
			cur=self.__head
			while cur.Next!=None:
				cur=cur.Next
			cur.Next=Node(x)
		else:
			self.__head=Node(x)
		SL.__size+=1

	def insertInOrder(self,x):
		if self.__head:
			pre,cur=None,self.__head
			while cur.Next and cur.val<=x:
				pre,cur=cur,cur.Next
			if cur==self.__head and pre==None:
				temp=Node(x)
				temp.Next=self.__head
				self.__head=temp
			elif cur.Next==None and pre:
				pre.Next=Node(x)
			else:
				pre.Next,pre.Next.Next=Node(x),cur
		else:
			self.__head=Node(x)
		SL.__size+=1

	def remove(self,x):
		if SL.__size:
			pre,cur=None,self.__head
			while cur.Next!=None and cur.val!=x:
				pre,cur=cur,cur.Next
			if cur.Next==None and cur.val!=x:
				print "Element %d not found"%x
			elif cur==self.__head:
				self.__head.Next=None
			elif cur.Next==None and cur.val==x:
				pre.Next=None
			else:
				pre.Next=cur.Next
		SL.__size-=1
	
	def size(self):
		print "The singly-linked list has %d elements"%SL.__size

	def traverse(self):
		cur=self.__head
		while cur:
			print cur.val,
			cur=cur.Next
		print ""

