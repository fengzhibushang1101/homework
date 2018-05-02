#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @Time    : 2018/5/2 0002 下午 9:02
 @Author  : Administrator
 @Software: PyCharm
 @Description: 
"""

# 自己的
# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         length = len(s)
#         _max = 0
#         for i in range(length):
#             j = i + 1
#             gap = 0
#             tmp = {s[i]: 1}
#             while j < length:
#                 if s[j] in tmp:
#                     gap = j - i
#                     break
#                 tmp[s[j]] = 1
#                 j += 1
#             gap = gap or length - i
#             _max = max(_max, gap)
#         return _max

# 比较优秀的方法

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        _max = 0
        max_s = ''
        for index, elem in enumerate(s):
            if elem in max_s:
                i = max_s.find(elem)
                _max = max(len(max_s), _max)
                max_s = max_s[i + 1:]
            max_s += elem
        _max = max(len(max_s), _max)
        return _max
s = "abcabcbb"

print Solution().lengthOfLongestSubstring(s)
