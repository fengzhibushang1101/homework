#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @Time    : 2018/4/24 21:33
 @Author  : jyq
 @Software: PyCharm
 @Description: 
"""


def string_keys_to_dict(key_string, callback):
    return dict.fromkeys(key_string.split(), callback)


def dict_merge(*dicts):
    merged = {}
    for d in dicts:
        merged.update(d)
    return merged


RESPONSE_CALLBACKS = dict_merge(
    string_keys_to_dict(
        'AUTH EXISTS EXPIRE EXPIREAT HEXISTS HMSET MOVE MSETNX PERSIST '
        'PSETEX RENAMENX SISMEMBER SMOVE SETEX SETNX',
        bool
    ),
    string_keys_to_dict(
        'BITCOUNT BITPOS DECRBY DEL GETBIT HDEL HLEN HSTRLEN INCRBY '
        'LINSERT LLEN LPUSHX PFADD PFCOUNT RPUSHX SADD SCARD SDIFFSTORE '
        'SETBIT SETRANGE SINTERSTORE SREM STRLEN SUNIONSTORE ZADD ZCARD '
        'ZLEXCOUNT ZREM ZREMRANGEBYLEX ZREMRANGEBYRANK ZREMRANGEBYSCORE '
        'GEOADD',
        int
    ))
print RESPONSE_CALLBACKS
