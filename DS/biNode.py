#!/usr/bin/python

class Node:
	
	def __init__(self,x=0):
		self.__val,self.__Prev,self.__Next=x,None,None
	
	@property
	def val(self):
		return self.__val

	@property
	def Prev(self):
		return self.__Prev

	@Prev.setter
	def Prev(self,k):
		if isinstance(k,Node):
			self.__Prev=k
		else:
			print "Not a node!"

	@property
	def Next(self):
		return self.__Next


	@Next.setter
	def Next(self,k):
		if isinstance(k,Node):
			self.__Next=k
		else:
			print "Not a node!"

	def __str__(self):
		return "A node of doubly-linked list."
