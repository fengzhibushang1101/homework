#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @Time    : 2018/5/2 0002 下午 9:54
 @Author  : Administrator
 @Software: PyCharm
 @Description: 
"""
import math


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        c = nums1 + nums2
        c.sort()
        length = len(c)
        mid = length / 2
        return (c[mid] + c[mid - 1]) / 2.0 if not length % 2 else c[mid]


nums1 = [1, 3]
nums2 = [2, 4]
print Solution().findMedianSortedArrays(nums1, nums2)
