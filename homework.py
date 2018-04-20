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
#
#
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

def parti(num, max_num=None):
    if max_num is None:
        max_num = num+1
    return partition(num, max_num-1)

# print partition(8)
# print parti(8, 9)


#

def partition2(num, max_num=None, cache=None):
    cache = {} if cache is None else cache
    max_num = max_num or num
    k = "%s-%s" % (num, max_num)
    if cache.get(k):
        return cache[k]
    if num == 1 or max_num == 1:
        return 1
    # elif num < max_num:
    #     return partition2(num, num)
    elif num <= max_num:
        return 1 + partition2(num, num - 1)
    res = partition2(num-max_num, max_num, cache) + partition2(num, max_num-1, cache)
    cache[k] = res
    return res


def partition3(num, mx, arr=list()):
    # print num, mx
    while mx > 0:
        new_arr = arr[:]
        new_arr.append(mx)
        if num-mx > mx:
            return
        elif num-mx == mx:
            partition3(num - mx, num-mx-1, new_arr)
        elif num-mx > 0:
            partition3(num-mx, num-mx, new_arr)
        else:
            print new_arr
        mx -= 1
partition3(5, 5)
partition3(8, 8)


# if __name__ == "__main__":
#     print partition2(100)




# print partition2(8)
