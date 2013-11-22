#!/usr/bin/python

class Heap:
	
	def __init__(self,heapType='min'):
		if heapType not in ['min','max']:
			from sys import exit
			print "Invalid heap type!"
			exit()
		self.__data=[]
		self.__type=heapType
		
	@property
	def root(self):
		return self.__data[0]

	def size(self):
		return len(self.__data)

	def __minHeapify(self):
		i=len(self.__data)-1
		while i>0 and self.__data[i]<self.__data[(i-1)/2]:
			self.__data[i],self.__data[(i-1)/2]=self.__data[(i-1)/2],self.__data[i]
			i=(i-1)/2
	
	def __maxHeapify(self):
		i=len(self.__data)-1
		while i>0 and self.__data[i]>self.__data[(i-1)/2]:
			self.__data[i],self.__data[(i-1)/2]=self.__data[(i-1)/2],self.__data[i]
			i=(i-1)/2

	def insert(self,val):
		
		self.__data.append(val)
		if len(self.__data)==1:
			return
		
		if self.__type=='min': #minHeapify
			self.__minHeapify()
		elif self.__type=='max': #maxHeapify
			self.__maxHeapify()
	
	def remove(self,val):

		index=self.search(val)
		if index!=-1:
			self.__data[index]=self.__data[len(self.__data)-1]
			del self.__data[len(self.__data)-1]

			if self.__type=='min': #minHeapify
				while index<len(self.__data) and ((2*index+1<len(self.__data) and self.__data[index]>self.__data[2*index+1]) or (2*index+2<len(self.__data) and self.__data[index]>self.__data[2*index+2])):
					if self.__data[index]>self.__data[2*index+1]:
						self.__data[index],self.__data[2*index+1]=self.__data[2*index+1],self.__data[index]
						index=2*index+1
					elif self.__data[index]>self.__data[2*index+2]:
						self.__data[index],self.__data[2*index+2]=self.__data[2*index+2],self.__data[index]
						index=2*index+2


			elif self.__type=='max': #maxHeapify
				while index<len(self.__data) and ((2*index+1<len(self.__data) and self.__data[index]<self.__data[2*index+1]) or (2*index+2<len(self.__data) and self.__data[index]<self.__data[2*index+2])):
					if self.__data[index]<self.__data[2*index+1]:
						self.__data[index],self.__data[2*index+1]=self.__data[2*index+1],self.__data[index]
						index=2*index+1
					elif self.__data[index]<self.__data[2*index+2]:
						self.__data[index],self.__data[2*index+2]=self.__data[2*index+2],self.__data[index]
						index=2*index+2

		else:
			print "Element %d could not be found!"%val

	def searchIter(self,val): 
		try:
			return self.__data.index(val)
		except ValueError:
			return -1
		
	def searchRec(self,val):
		x=self.__search(val,0,len(self.__data))
		return -1 if x==None else x

	def __search(self,val,i1,i2):
		if i1>=i2:
			return
		if val==self.__data[i1]:
			return i1
		return self.__search(val,2*i1+1,i2) or self.__search(val,2*i1+2,i2)
	
	def printH(self):
		print self.__data
