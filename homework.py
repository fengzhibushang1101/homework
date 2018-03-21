#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @Time    : 2018/3/21 16:21
 @Author  : jyq
 @Software: PyCharm
 @Description: 
"""
a = [1, 2, 3]


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def perm2(arr, k=0, cursor=0):
    """
    求数组中数组中k的数的组合
        如果不加大小的判断,为排列
    :param arr:
    :param k:
    :param cursor:
    :return:
    """
    length = len(arr)
    k = k or length
    if cursor == k:
        print arr[0:k]
    else:
        for i in range(cursor, length):
            if cursor > 0 and arr[i] < arr[cursor - 1]:
                continue
            swap(arr, cursor, i)
            perm2(arr, k, cursor=cursor + 1)
            swap(arr, cursor, i)


# perm2([1, 2, 3, 4, 5], 3)


def kk(arr, new_arr=None, checked_count=0):
    """
    输入[0,1,0,1] 输出[2,1,4,3]
    :param arr:
    :param new_arr:
    :param checked_count:
    :return:
    """
    length = len(arr)
    new_arr = new_arr or [None] * length
    for i in range(length - 1, -1, -1):
        if arr[i] > i:
            return "input is illegal !"
        origin_num = arr[i]
        arr[i] -= 1
        if origin_num == 0:
            new_arr[i] = length - checked_count
            checked_count += 1
            if length == checked_count:
                return new_arr
            arr[i] = -1
            return kk(arr, new_arr, checked_count)


def partition(num, max_num=None):
    """
    partition(2, 2) = [[2], [1,1]] partition(3,3) = [[3], [2, 1], [1, 1, 1]]
    :param num:
    :param max_num:
    :return:
    """
    def add_max(arr):
        arr.append(max_num)
        return arr

    if max_num is None:
        max_num = num
    if max_num < 1:
        return []
    if num == 0:
        return [[]]
    if max_num > num:
        max_num = num
    return partition(num, max_num - 1) + map(add_max, partition(num - max_num, max_num))


print partition(8)


#

# def partition2(num, max_num=None):
#     def add_max(arr):
#         arr.append(max_num - 1)
#         # print arr
#         return arr
#
#     if max_num is None:
#         max_num = num + 1
#     if num == 0:
#         return [[]]
#     if max_num <= 1:
#         return []
#     return partition2(num, max_num - 1) + map(add_max, partition2(num - max_num + 1, num - max_num + 2))
#
#
# print partition2(8)
