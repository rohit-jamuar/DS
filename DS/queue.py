#!/usr/bin/python

class queue:
	'''This implementation is based on the built-in type : list'''
	
	def __init__(self):
		self.__q=[]

	def enqueue(self,x):
		self.__q.append(x)

	def dequeue(self):
		if len(self.__q):
			temp=self.__q[0]
			self.__q.remove(self.__q[0])
			return temp
		else:
			print "Empty queue!"
	
	def isEmpty(self):
		if len(self.__q)==0:
			return True
		return False
	
	def printQ(self):
		for i in self.__q:
			print i,
		print ""
