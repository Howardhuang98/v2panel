#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   celery.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2021/10/17 11:15  
------------      
"""
# celery 配置文件 与 settings.py 同级

from celery import Celery
from django.conf import settings
import os

# 指定django的settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'v2panel.settings')

app = Celery('v2panel')
app.conf.update(
    broker_url='redis://:123456@huanghao.space:6379/1'
)
# 自动去app中寻找tasks
app.autodiscover_tasks(settings.INSTALLED_APPS)
