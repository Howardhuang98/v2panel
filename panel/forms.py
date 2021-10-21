#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   forms.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2021/10/21 15:45  
------------      
"""
from django.forms import forms
from markdownx.fields import MarkdownxFormField


class mdForm(forms.Form):
    md = MarkdownxFormField()
