#!/usr/bin/python

from biNode import Node

class DL:
	__size=0

	def __init__(self):
		self.__head,self.__tail=None,None

	def insert(self,x):
		if self.__head:
			cur=self.__head
			while cur.Next:
				cur=cur.Next
			temp=Node(x)
			temp.Prev,cur.Next,self.__tail=cur,temp,temp
		else:
			self.__tail=self.__head=Node(x)
		DL.__size+=1

	def insertInOrder(self,x):
		if self.__head and self.__tail:
			pre,cur=None,self.__head
			while cur.Next and cur.val<=x:
				pre,cur=cur,cur.Next
			if cur==self.__head:
				temp=Node(x)
				temp.Next=self.__head
				self.__head.Prev=temp
				self.__head=temp
			elif cur.Next==None:
				cur.Next=Node(x)
				cur.Next.Prev=cur
				self.__tail=cur.Next
			else:
				pre.Next=Node(x)
				pre.Next.Prev=pre
				pre.Next.Next=cur
				cur.Prev=pre.Next
		else:
			self.__tail=self.__head=Node(x)
		DL.__size+=1
		
	def remove(self,x):
		if DL.__size:
			cur=self.__head
		while cur.Next and cur.val!=x:
			pre,cur=cur,cur.Next
		if not cur.Next and cur.val!=x:
			print "The value %d could not be found!"%x
		elif cur==self.__head:
			self.__head=self.__head.Next
		elif not cur.Next and pre:
			pre.Next=None
			self.__tail=pre
		else:
			pre.Next=cur.Next
			cur.Next.Prev=pre
		DL.__size-=1

	def traversal(self):
		cur=self.__head
		while True:
			print cur.val,
			if cur.Next:
				cur=cur.Next
			else:
				print ""
				break

	def Rtraversal(self):
		cur=self.__tail
		while cur:
			print cur.val,
			if cur.Prev:
				cur=cur.Prev
			else:
				print ""
				break
