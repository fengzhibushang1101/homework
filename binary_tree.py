#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @Time    : 2018/4/23 8:57
 @Author  : jyq
 @Software: PyCharm
 @Description: 
"""


class Node(object):
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
        self.rest = 3  # 3 是左右都为空 1是左为空 2是右为空 0是都不为空

    def copy(self):
        node = Node(self.val)
        node.left = self.left.copy() if self.left else None
        node.right = self.right.copy() if self.right else None
        node.rest = self.rest
        return node


def a(n, bst=None, current=1):
    bst = bst or []
    if current > n:
        print [[node.val, node.left.val if node.left else None, node.right.val if node.right else None]for node in bst]
        return
    cur_node = Node(current)
    if current == 1:
        bst.append(cur_node)
        a(n, bst, current + 1)
    else:
        for index, node in enumerate(bst):
            if node.rest:
                if node.rest == 1:
                    new_bst = [z.copy() for z in bst]
                    node = new_bst[index]
                    node.left = cur_node
                    new_bst.append(cur_node)
                    node.rest = 0
                    a(n, new_bst, current + 1)
                elif node.rest == 2:
                    new_bst = [z.copy() for z in bst]
                    node = new_bst[index]
                    node.right = cur_node
                    new_bst.append(cur_node)
                    node.rest = 0
                    a(n, new_bst, current + 1)
                else:
                    for i, v in enumerate(['left', 'right']):
                        new_bst = [z.copy() for z in bst]
                        node = new_bst[index]
                        setattr(node, v, cur_node)
                        new_bst.append(cur_node)
                        node.rest = node.rest-1-i
                        a(n, new_bst, current+1)

a(8)
