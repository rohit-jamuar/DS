#!/usr/bin/python

from treeNode import Node

def printT(node):
	if node:
		printT(node.left)
		print node.val,
		printT(node.right)

def maketree1(preorder, inorder):
	if len(preorder) == 0 or len(inorder)==0:
		return None

	rootVal = preorder[0]
	rootIndex = inorder.index(rootVal)
	linorder = filter(lambda x: inorder.index(x)<rootIndex, inorder)
	rinorder = filter(lambda x: inorder.index(x)>rootIndex, inorder)
	lpreorder = filter(lambda x: x in linorder, preorder)
	rpreorder = filter(lambda x: x in rinorder, preorder)
	
	root=Node(rootVal)
	root.left=maketree1(lpreorder,linorder)
	root.right=maketree1(rpreorder,rinorder)

	return root

def maketree2(postorder, inorder):
	if len(postorder) == 0 or len(inorder)==0:
		return None

	rootVal = postorder[-1]
	rootIndex = inorder.index(rootVal)
	linorder = filter(lambda x: inorder.index(x)<rootIndex, inorder)
	rinorder= filter(lambda x: inorder.index(x)>rootIndex, inorder)
	lpostorder = filter(lambda x: x in linorder, postorder)
	rpostorder = filter(lambda x: x in rinorder, postorder)
	
	root=Node(rootVal)
	root.left=maketree2(lpostorder,linorder)
	root.right=maketree2(rpostorder,rinorder)

	return root

def maketree3(preorder,postorder):
	if len(preorder)==0 or len(postorder)==0:
		return None
	rootVal=postorder[-1]
	rChildIndex=preorder.index(postorder[-2])
	lpreorder=filter(lambda x:preorder.index(x)<rChildIndex,preorder)
	rpreorder=filter(lambda x:preorder.index(x)>=rChildIndex,preorder)
	lpostorder=filter(lambda x:x in lpreorder,postorder)
	rpostorder=filter(lambda x:x in rpreorder,postorder)

	root=Node(rootVal)
	root.left=maketree3(lpreorder,lpostorder)
	root.right=maketree3(rpreorder,rpostorder)

	return root

'''
from priorityQ import PriorityQ
from task import Task

a=PriorityQ()
b={3:'three',4:'four',0:'zero',8:'eight',1:'one',5:'five'}
for i in b:
	a.insert(Task(i,b[i]))
a.printQ()
a.remove('one')
a.printQ()
'''

from binarySearchTree import BST
from random import choice
a=BST()
for i in [1, 2, 4, 8, 9, 5, 3, 6, 7]:
	a.insert(i)
print 'in:',
b=a.printTree('in')
print 'pre:',
c=a.printTree('pre')
print 'post:',
d=a.printTree('post')
printT(maketree1(c,b))
print ''
printT(maketree2(d,b))
print ''
printT(maketree3(c,d))
print ''
