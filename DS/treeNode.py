#!/usr/bin/python

class Node:

	def __init__(self,x=0):
		self.left,self.right,self.val=None,None,x

	@property
	def val(self):
		return self.val

	@val.setter
	def val(self,x):
		if type(x)==type(self.val):
			self.val=x
		else:
			print "Type mismatch!"

	@property
	def left(self):
		return self.left

	@left.setter
	def left(self,n):
		if isinstance(n,Node):
			self.left=n
		else:
			print "Not a tree node!"

	@property
	def right(self):
		return self.right

	@right.setter
	def right(self,n):
		if isinstance(n,Node):
			self.right=n
		else:
			print "Not a tree node!"

