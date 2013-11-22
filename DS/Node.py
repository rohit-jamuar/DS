#!/usr/bin/python

class Node:
	def __init__(self,x=0):
		self.__val=x
		self.__Next=None
	
	@property
	def val(self):
		return self.__val

	@property
	def Next(self):
		return self.__Next

	@Next.setter
	def Next(self,x):
		if isinstance(x,Node):
			self.__Next=x
		else:
			print "Not a Node instance!"
	
	def __str__(self):
		return "Node - singly linked list"
