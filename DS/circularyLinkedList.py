#!/usr/bin/python

from Node import Node

class CL:

	__size=0
	
	def __init__(self):
		self.__head=None
	
	def insert(self,x):
		if self.__head:
			cur=self.__head
			while cur.Next!=self.__head:
				cur=cur.Next
			cur.Next=Node(x)
			cur.Next.Next=self.__head	
		else:
			self.__head=Node(x)
			self.__head.Next=self.__head
		CL.__size+=1

	def insertInOrder(self,x):
		if self.__head:
			pre,cur=None,self.__head
			while cur.Next!=self.__head and x>cur.val:
				pre,cur=cur,cur.Next
			temp=Node(x)
			if not pre:
			# ^^ conditional check takes care of the cases where the insertion has to be made at the beginning or end
				temp.Next=cur
				self.__head=temp
			else:
				temp.Next=pre.Next
				pre.Next=temp
		else:
			self.__head=Node(x)					
		CL.__size+=1

	def remove(self,x):
		if CL.__size:
			cur=self.__head
			while cur.Next!=self.__head and cur.val!=x:
				pre,cur=cur,cur.Next
			if cur.val!=x:
				print "Value %d could not be found"%x
			elif cur==self.__head:
				self.__head=self.__head.Next
			elif cur.Next==self.__head:
				pre.Next=self.__head
			else:
				pre.Next=cur.Next
			CL.__size-=1
		else:
			print "Empty list!"
		
	
	def traversal(self):
		cur=self.__head
		while cur and CL.__size:
			print cur.val,
			if cur.Next!=self.__head:
				cur=cur.Next
			else:
				print ""
				break

	def shift(self,i=1):
		if type(i)==type(1):
			while i!=0:
				self.__head=self.__head.Next
				i-=1

	def size(self):
		print "Number of elements in the list = %d"%CL.__size
