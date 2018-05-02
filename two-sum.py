#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @Time    : 2018/5/2 0002 下午 8:44
 @Author  : Administrator
 @Software: PyCharm
 @Description: 
"""


# 我自己的解法


#  优秀的解法
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tmp = {}
        for i, v in enumerate(nums):
            if v not in tmp:
                tmp[target - v] = i
            else:
                return [tmp[v], i]


nums = [2, 7, 11, 15]
target = 9

print Solution().twoSum(nums, target)
