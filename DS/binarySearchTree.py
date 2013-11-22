#!/usr/bin/python

from treeNode import Node
from queue import queue

class BST:
	'''Binary Search Tree'''	
	def __init__(self):
		   self.__root=None

	@property
	def root(self):
		return self.__root

	def insert(self,y):
		if self.__root:
			cur=self.__root
		else:
			self.__root=Node(y)
			return
		while True:
			if y<=cur.val and cur.left:
				cur=cur.left
			elif y>cur.val and cur.right:
				cur=cur.right
			else:
				break
		if y<=cur.val:
			cur.left=Node(y)
		elif y>cur.val:
			cur.right=Node(y)

	def find(self,y):
		if self.__root:
			cur=self.__root
		else:
			return -1
		while True:
			if y==cur.val:
				return True
			elif y<cur.val and cur.left:
				cur=cur.left
			elif y>cur.val and cur.right:
				cur=cur.right
			else:
				return False

	def delete(self,y):
		if self.__root:
			pre,cur=None,self.__root
		else:
		   	print "Empty Tree!"
			return
		while True:
	    		if y==cur.val:
				break
			elif y>cur.val and cur.right:
				pre,cur=cur,cur.right
			elif y<cur.val and cur.left:
				pre,cur=cur,cur.left
			else:
			   print "Node (with value %d) not found!"%y
			   return
	#If the node to be deleted has no children
		if not cur.left and not cur.right:
			if pre.left==cur:
				pre.left==None
			else:
				pre.right=None
	#If the node to be deleted has a child
		elif not cur.left or not cur.right:
			if not cur.left:
				if pre.left==cur:
					pre.left=cur.right
				else:
					pre.right=cur.right
			else:
				if pre.right==cur:
					pre.right=cur.left
				else:	
					pre.left=cur.left
	#If the node to be deleted has two children
		else:
	#Find the smallest node (a.k.a replacement-node) in the right subtree
			nextNode=cur.right 
			while nextNode.left:
				parentOfNextNode,nextNode=nextNode,nextNode.left

	#Detach the replacement-node from its parent
			if parentOfNextNode.left==nextNode:
				parentOfNextNode.left=None
			else:
				parentOfNextNode.right=None

	#If the replacement-node has a child on right, attach the child to replacement node's parent
			if nextNode.right:
				parentOfNextNode.right=nextNode.right
	   			nextNode.right=None

	#Connect the replacement-node with the children of the node to be deleted
	   			nextNode.left=cur.left	
	   			nextNode.right=cur.right

	#Attach the replacement-node to the parent of the node to be deleted
	   		if pre.right==cur:
	   			pre.right=nextNode
	   		elif pre.left==cur:
	   			pre.left=nextNode
	   		print "Deleted node with value = %d"%y


	def getNodeRef(self,y):
		   if self.__root:
			   cur=self.__root
			   while True:
				   if y==cur.val:
					   return cur
				   elif y<cur.val and cur.left:
					   cur=cur.left
				   elif y>cur.val and cur.right:
					   cur=cur.right
				   else:
					   print "Node with value %d doesn't exist."%y
					   return
		   else:
			   print "Empty tree!"

   	def findParentRef(self,y):
		   if self.__root:
			   pre,cur=None,self.__root
			   while True:
				   if y==cur.val:
					   if  pre:
						   return pre
					   else:
						   print "This node has no parent (root node)."
						   break
			  	   elif y<cur.val and cur.left:
				   	pre,cur=cur,cur.left
				   elif y>cur.left and cur.right:
					   pre,cur=cur,cur.right
				   else:
					   print "Couldn't find a node with value %d!"%y
					   break
		   else:
			   print "Empty tree!"

	def findMin(self):
		if self.__root:
			cur=self.__root
			while cur.left:
				cur=cur.left
		   	return cur.val
	   	else:
			print "Empty tree!"

	def findMax(self):
		if self.__root:
			cur=self.__root
			while cur.right:
				cur.right
			return cur.val
		else:
			print "Empty tree!"

	def printTree(self,opt):
		if type(opt)==type(""):
			options={'pre':self.__preorderP,'in':self.__inorderP,'post':self.__postorderP}
			if opt in options:
				l=[]
				options[opt](self.__root,l)
				print l
				return l
			else:
				print "Invalid option!"

	def __inorderP(self,node,l=[]):
		if node:
			self.__inorderP(node.left,l)
			l.append(node.val)
			self.__inorderP(node.right,l)

	def __preorderP(self,node,l=[]):
		 if node:
			l.append(node.val)
			self.__preorderP(node.left,l)
			self.__preorderP(node.right,l)

	def __postorderP(self,node,l=[]):
		if node:
			self.__postorderP(node.left,l)
			self.__postorderP(node.right,l)
			l.append(node.val)

	def __dfs(self,node):
		if node:
			print node.val,
		else:
			return
		if node.left:	
			self.__dfs(node.left)
		if node.right:
			self.__dfs(node.right)

	def DFS(self):
		self.__dfs(self.__root)
		print ''

	def BFS(self):
		q=queue()
		node=self.__root
		if node:
			q.enqueue(node)
		else:
			return []
		while not q.isEmpty():
			node=q.dequeue()
			print node.val,
			if node.left:
				q.enqueue(node.left)
			if node.right:
				q.enqueue(node.right)
		print ''

	def __getH(self,node):
		if not node:
			return 0
		return 1+max(self.__getH(node.left),self.__getH(node.right))

	def getHeight(self):
		return self.__getH(self.__root)

	def __printGivenLevel(self,node,level):
		if not node:
			return
		if level==1:
			print node.val,
		elif level>1:
			self.__printGivenLevel(node.left,level-1)
			self.__printGivenLevel(node.right,level-1)

	def levelOrderTraversal_dfs(self):
		for i in range(1,self.getHeight()+1):
			self.__printGivenLevel(self.__root,i)
			print ''

	def levelOrderTraversal_bfs(self,l=None):
		if not self.__root:
			return
		if not l:
			l=[]
		curL,nexL=queue(),queue()
		curL.enqueue(self.__root)
		temp=[]
		while not curL.isEmpty():
			node=curL.dequeue()
			if node:
				temp.append(node.val)
				if node.left:
					nexL.enqueue(node.left)
				if node.right:
					nexL.enqueue(node.right)
			if curL.isEmpty():
				l.append(temp)
				temp=[]
				curL,nexL=nexL,curL
		return l

	def serializeTree(self):
		return self.__serializeTree(self.__root)

	def __serializeTree(self,node,l=None):
		if not l:
			l=[]
		q=queue()
		if not node:
			return [None]
		else:
			q.enqueue(node)
		
		while not q.isEmpty():
			x=q.dequeue()
			if not x:
				l.append(None)
			else:
				l.append(x.val)
				q.enqueue(x.left)	
				q.enqueue(x.right)
		return l

	@staticmethod
	def deserializeTree(arr):
		if not arr:
			return None

		q=queue()
		root=Node(arr[0])
		q.enqueue(root)
	
		index=0
		while not q.isEmpty():
			x=q.dequeue()
			
			if arr[2*index+1]:
				x.left=Node(arr[2*index+1])
				q.enqueue(x.left)
			else:
				x.left=None
						
			if arr[2*index+2]:
				x.right=Node(arr[2*index+2])
				q.enqueue(x.right)
			else:
				x.right=None
		
			index+=1

		return root
		
	
		
	@staticmethod
	def checkDeserialization(node):
		if node:
			BST.checkDeserialization(node.left)
			print node.val,
			BST.checkDeserialization(node.right)				

	@staticmethod
	def maketree1(preorder, inorder):
		if len(preorder) == 0 or len(inorder)==0:
			return None

		rootVal = preorder[0]
		rootIndex = inorder.index(rootVal)
		linorder = filter(lambda x: inorder.index(x)<rootIndex, inorder)
		rinorder= filter(lambda x: inorder.index(x)>rootIndex, inorder)
		lpreorder = filter(lambda x: x in linorder, preorder)
		rpreorder = filter(lambda x: x in rinorder, preorder)
		
		root=Node(rootVal)
		root.left=maketree1(lpreorder,linorder)
		root.right=maketree1(rpreorder,rinorder)

		return root


	@staticmethod
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
			
		
			
