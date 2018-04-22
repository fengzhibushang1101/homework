#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @Time    : 2018/4/22 10:18
 @Author  : jyq
 @Software: PyCharm
 @Description: 
"""


class Calculator(object):

    op_arr = ["+", "-", "*", "/"]

    def evaluate(self, string):
        unit = self.split(string)
        print unit
        return self.cal(unit) if isinstance(unit, list) else unit

    @classmethod
    def split(cls, string, op=0):
        res = string.split(cls.op_arr[op])
        if len(res) == 1 and op < len(cls.op_arr) - 1:
            return cls.split(string, op+1)
        elif len(res) == 1 and op == len(cls.op_arr) - 1:
            return float(string)
        else:
            return [cls.op_arr[op]] + map(lambda x: cls.split(x), res)

    @classmethod
    def cal(cls, unit):
        op = unit[0]
        op_map = {
            "+": cls.add,
            "-": cls.minus,
            "*": cls.times,
            "/": cls.dividedBy
        }
        rest = map(lambda x: cls.cal(x) if isinstance(x, list) else x, unit[1:])
        return reduce(op_map[op], rest)

    @classmethod
    def add(cls, left, right):
        return left + right

    @classmethod
    def minus(cls, left, right):
        return left - right

    @classmethod
    def times(cls, left, right):
        return round(float(left * right), 3)

    @classmethod
    def dividedBy(cls, left, right):
        return float(left / right)


if __name__ == "__main__":
    print Calculator().evaluate("1.1 * 2.2 * 3.3")