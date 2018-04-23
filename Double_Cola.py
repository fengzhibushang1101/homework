#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @Time    : 2018/4/22 16:50
 @Author  : jyq
 @Software: PyCharm
 @Description: 
"""

def whoIsNext(names, r):
    length = len(names)
    count = 1
    while r / length >= 1:
        r -= length
        length = length * 2
        count = count * 2
    return names[int((r-1)/count)]
names = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
r = 1802
print whoIsNext(names, r)



def whoIsNext2(names, r):
    length = len(names)
    while r > length:
        r = (r-length+1) / 2
    return names[r-1]

    # your code