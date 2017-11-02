#!/usr/bin/env python3

from node_definition import Node

class BST:
    def __init__(self):
        self.root = None

    def height(self):
        def _height_internal(node):
            if not node:
                return -1
            return 1 + max([_height_internal(node.left),
                            _height_internal(node.right)])
        return _height_internal(self.root)

    def insert(self, val):
        new_node = Node(val)
        if not self.root:
            self.root = new_node
        else:
            pre, cur = None, self.root
            while cur:
                pre = cur
                if cur.val < val:
                    cur = cur.right
                else:
                    cur = cur.left
            if pre.val < val:
                pre.right = new_node
            else:
                pre.left = new_node

    def delete(self, val):
        pre, cur = None, self.root
        while cur and cur.val != val:
            pre = cur
            if cur.val < val:
                cur = cur.right
            else:
                cur = cur.left
        if cur:
            if not cur.left and not cur.right:
                ##is leaf
                if pre.left == cur:
                    pre.left = None
                else:
                    pre.right = None
            elif any([cur.left and not cur.right, not cur.left and cur.right]):
                ##has one child
                if cur.left:
                    if pre.right == cur:
                        pre.right = cur.left
                    else:
                        pre.left = cur.left
                else:
                    if pre.right == cur:
                        pre.right = cur.right
                    else:
                        pre.left = cur.right
            else:
                ##has both childern
                #find predecessor
                pred_par, pred = pre, cur
                while pred.left:
                    pred_par = pred
                    pred = pred.left
                while pred.right:
                    pred_par = pred
                    pred = pred.right
                #disconnect predecessor
                if pred_par.left == pred:
                    pred_par.left = None
                else:
                    pred_par.right = None
                #rewire predecessor to the rest of BST
                if pre.left == cur:
                    pre.left = pred
                else:
                    pre.right = pred
                if cur.left:
                    pred.left = cur.left
                if cur.right:
                    pred.right = cur.right
            del(cur)

    def traverse_bst(self, order='in'):
        if order == 'in':
            self._traverse_inorder(self.root)
        elif order == 'pre':
            self._traverse_preorder(self.root)
        else:
            self._traverse_postorder(self.root)

    def _traverse_inorder(self, node):
        if not node:
            return
        self._traverse_inorder(node.left)
        print(str(node.val))
        self._traverse_inorder(node.right)

    def _traverse_preorder(self, node):
        if not node:
            return
        print(str(node.val))
        self._traverse_preorder(node.left)
        self._traverse_preorder(node.right)

    def _traverse_postorder(self, node):
        if not node:
            return
        self._traverse_postorder(node.left)
        self._traverse_postorder(node.right)
        print(str(node.val))
