#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @Time    : 2018/4/26 8:31
 @Author  : jyq
 @Software: PyCharm
 @Description: 
"""

# !/usr/bin/env python
# encoding: utf-8
from datetime import timedelta
from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/0')

app.conf.update(
    CELERYBEAT_SCHEDULE={
        'perminute': {
            'task': 'tasks.add',
            'schedule': timedelta(seconds=3),
            'args': (1, 1)
        }
    }
)


@app.task
def add(x, y):
    print x + y
    return x + y
