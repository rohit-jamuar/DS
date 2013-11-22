#!/usr/bin/python

class Task:
	
	def __init__(self,taskPri,taskname="Anonymous"):
		self.__name=taskname
		self.__pri=taskPri

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self,k):
		if type(k)==type(""):
			self.__name=k
		else:
			print "Task name has to be a string!"

	@property
	def pri(self):
		return self.__pri

	@pri.setter
	def pri(self,n):
		if type(n)==type(1):
			self.__pri=n
		else:
			print "Task priority has to be an integer"
