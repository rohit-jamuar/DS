#!/usr/bin/python

def bar():
	'''WaFunc which behaves as a queue wherein when the user types:\n+ str : str is enqueued, and\n- : the first character is dequeued.
\nThe user should start by indicating the number of lines which have to read from the STDIO. The function will print the number of values which the queue holds.'''
	val=input()
	result,finStr=0,""
	while val>0:
		ip=raw_input().split()
		if ip[0]=='+':
			finStr+=ip[1]
			result+=getLen(finStr)
		elif ip[0]=='-':
			finStr=finStr[1:]
			result+=getLen(finStr)
		val-=1
	print result

def isPalindrome(s):
	l=str(s)
	return True if l==l[::-1] else False
	
def isPrime(n):
	for i in range(2,n/2):
		if n%i==0:
			return False
	return True

def baz(n):
	'''converts an integer to its binary form and returns bin-representation'''
	if n==0:
		return ''
	else:
		return baz(n/2)+str(n%2)

def test1(s):
	'''Convert a string into a compressed string e.g. hello -> h1e1l2o1. Return the compressed result only if its length is lesser than that of the original string'''
	fin=''
	index1=0
	while index1<len(s):
		char=s[index1]
		count,index2=0,index1
		while index2<len(s) and s[index2]==char:
			index2+=1
			count+=1
		fin+=char+str(count)
		index1=index2
	return fin if len(fin)<len(s) else s

def minimum_coins(v,e):
	from sys import maxint
        c_min=maxint
        from itertools import combinations
	v=sorted(v)
	for i in range(1,len(v)+1):
		for j in combinations(v,i):
			val,index,c_intermediate=e,-1,0
			while val and index>=-len(j):
				while val>=j[index]:
					c_intermediate+=1
					val-=j[index]
				index-=1
			if val==0:
				print j,"  ",c_intermediate
				if c_intermediate<c_min:
					c_min=c_intermediate
					
	if c_min==maxint:
		print None
	else:
		print c_min

def sOe(k):
	'''Sieve of Eratosthenes'''
	l=[0,0]
	l.extend([1]*(k-2))
	result=''
	for i in range(2,len(l)):
		if l[i]==0:
			continue
		for j in range(i+1,len(l)):
			if l[j]==0:
				continue
			if j%i==0:
				l[j]=0
	for i in range(k):
		if l[i]==1:
			result+=str(i)+','
	print result[:-1]

def largestCompositeWord(l):
	l=sorted(l,key=len,reverse=True)
	for i in range(len(l)):
		val=l[i]
		index=0
		while index<len(val):
			if val[:index] in l:
				val=val[index:]
				index=0
			else:
				index+=1
		if  val in l and val!=l[i]:
			return l[i]

def pascalTriangle1(n):
	#O(n^2) space needed!
	grid=[[1 if j==0 or (i!=0 and i==j) else 0 for j in range(n)]for i in range(n)]
	for row in range(2,len(grid)):
		for col in range(1,len(grid[0])):
			grid[row][col]=grid[row-1][col]+grid[row-1][col-1]
	return grid

def pascalTriangle2(n):
	grid=[[1]]
	for i in range(1,n):
		grid.append([[1]+[sum(j) for j in zip(grid[i-1],grid[i-1][1:])]+[1]])
	return grid

def numberedGrid(n):
	return [[n*i+j for j in range(1,n+1)]for i in range(n)]

def emptyGrid(m,n):
	return [[0 for j in range(n)]for i in range(m)]	

def printGrid(g):
	for r in range(len(g)):
		for c in range(len(g[0])):
			print '%4d'%g[r][c],
		print ''

def permute(s):
	l=[]
	if len(s)==1:
		l.append(s)
	else:
		for pos in range(len(s)):
			for j in permute(s[:pos]+s[pos+1:]):
				l.append(s[pos]+j)
#	print l
	return l

def permuteOnlyAlphas(s):
	from re import findall
	from string import digits
	fin=[]
	alphas=''.join(findall(r'[a-zA-Z]+',s))
	indexOfDigits=[i for i in range(len(s)) if s[i] in digits]
	permutationsOfAlphas=permute(alphas)
	for i in permutationsOfAlphas:
		temp=list(i)
		for j in indexOfDigits:
			temp.insert(j,s[j])
		fin.append(''.join(temp))
	return fin


def nextNumberWithSameDigits(n):
	num=str(n)
	for i in range(len(num)-1,-1,-1):
		index=i-1
		while index>=0:
			if int(num[i])>int(num[index]):
				return int(num[:index]+num[i]+num[index+1:i]+num[index]+num[i+1:].strip())
			else:
				index-=1
	return None


class LB:
	#load-balancer class
	def __init__(self,l):
		
		self.__bal={}
		for i in l:
			self.__bal[i[0]]=int(i[1])
		self.__cycle=sum(self.__bal.values())
		self.__currentIter=0
		self.__chosenB=[]

	def getLB(self):

		from random import choice

		curChoice=choice(self.__bal.keys())
		while curChoice in self.__chosenB and self.__chosenB.count(curChoice)>=self.__bal[curChoice]:
			curChoice=choice(self.__bal.keys())
		self.__chosenB.append(curChoice)
		print self.__chosenB[-1],
		self.__currentIter+=1
		if self.__currentIter==self.__cycle:
			self.__currentIter=0
			self.__chosenB=[]


def __getOperatorPermutations():
	operators=['+','-','/','*']
	return (i+j+k+l+m+' ' for m in operators for l in operators for k in operators for j in operators for i in operators)

def getToTargetValue(l,k):
	'''Given 6 integers and 1 target value, write a function to get the target value using 6 integers with any on these operations +,*,-,/ '''
	try:	
		for operatorList in __getOperatorPermutations():
			evaluationString=''.join([str(j) for i in zip(l,operatorList) for j in i]).strip()
			if eval(evaluationString)==k:
				print evaluationString
				return True
	except StopIteration:
		return False

def nQueens(n):
	from itertools import permutations
	cols = range(n)
	for vec in permutations(cols):
	    if n == len(set(vec[i]+i for i in cols)) == len(set(vec[i]-i for i in cols)):
		print vec
		print "\n".join('.' * i + 'Q' + '.' * (n-i-1) for i in vec) + "\n===\n"

digit_map = {
    '0': '-',
    '1': '-',
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}

def word_numbers(num):
  ip = str(num)
  ret = ['']
  for char in ip:
    ret = [prefix+letter for prefix in ret for letter in digit_map[char]]
   # print ret
  return ret

