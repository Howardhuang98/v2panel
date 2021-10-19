#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   celery.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2021/10/17 11:15  
------------      
"""
# celery 配置文件 与 settings.py 同级

import os

from celery import Celery
from decouple import config
from django.conf import settings

# 指定django的settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'v2panel.settings')

app = Celery('v2panel', timezone='Asia/Shanghai')

# app.config 自动从settings.py中寻找 CELERY_ 作为前缀
# app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.update(
    broker_url=config('BROKEN_RUL'),
    result_backend='django-db',


)
# 自动去app中寻找tasks
app.autodiscover_tasks(settings.INSTALLED_APPS)

app.conf.timezone = "Asia/Shanghai"
