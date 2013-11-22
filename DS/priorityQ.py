#!/usr/bin/python

from task import Task

class PriorityQ:

	def __init__(self):
		'''Initializes a priority queue'''
		self.__data=[]

	def __minHeapify(self):
			i=len(self.__data)-1
			while i>=0 and self.__data[i].pri<self.__data[(i-1)/2].pri:
				self.__data[i],self.__data[(i-1)/2]=self.__data[(i-1)/2],self.__data[i]
				i=(i-1)/2
	def insert(self,k):
		'''Inserts a 'Task' object to the PriorityQ.\nA 'Task' object takes its priority(\d+) and name(optional) as parameters'''
		if isinstance(k,Task):
			self.__data.append(k)
			if len(self.__data)>1:
				self.__minHeapify()
		else:
			print "Feed a 'Task' object!"

	def remove(self,k):
		'''Removes a 'Task' object with the name provided as the parameter (provided it exists!)'''
		if len(self.__data):
			if isinstance(k,str):
				index=-1
				for i in range(len(self.__data)):
					if self.__data[i].name==k:
						index=i
						break
				if index==-1:
					print "The task could not be found!"
					return
				else:
					self.__data[index]=self.__data[len(self.__data)-1]
					del self.__data[len(self.__data)-1]
					while index<len(self.__data) and ((2*index+1<len(self.__data) and self.__data[index].pri>self.__data[2*index+1].pri) or (2*index+2<len(self.__data) and self.__data[index].pri>self.__data[2*index+2].pri)):
						if self.__data[index].pri>self.__data[2*index+1].pri:
							self.__data[index],self.__data[2*index+1]=self.__data[2*index+1],self.__data[index]
							index=2*index+1
						elif self.__data[index].pri>self.__data[2*index+2].pri:
							self.__data[index],self.__data[2*index+2]=self.__data[2*index+2],self.__data[index]
							index=2*index+2
		else:
			print "Empty Q!"
			return
	
	def printQ(self):
		'''Prints the Priority Queue'''
		for i in self.__data:
			print i.name,i.pri,"  ",
		print ""
