#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   base.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2021/10/21 14:40  
------------      
"""
import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(is_safe=True)
def custom_markdown(value):
    return mark_safe(markdown.markdown(value,
                                       extensions=['markdown.extensions.extra',
                                                   'markdown.extensions.toc',
                                                   'markdown.extensions.sane_lists',
                                                   'markdown.extensions.nl2br',
                                                   'markdown.extensions.codehilite', ],
                                       safe_mode=True,
                                       enable_attributes=False))
