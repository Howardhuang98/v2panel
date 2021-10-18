#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   tasks.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2021/10/17 11:22  
------------      
"""

from v2panel.celery import app


@app.task
def task1():
    print("task1")
    return "task1 runned"
