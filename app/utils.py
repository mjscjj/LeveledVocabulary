#!/usr/bin/env python3
# encoding: utf-8
# @File: word_utils.py
# @Author : Leon Chu <leon_chu@apple.com>
# @Time : 2018-12-08 15:49
from datetime import datetime


def objs_to_dicts(objs):
    # 把对象列表转换为字典列表
    obj_arr = []
    for o in objs:
        # 把Object对象转换成Dict对象
        dict = {}
        dict.update(o.__dict__)
        obj_arr.append(dict)
    return obj_arr


def get_format_time():
    return datetime.now().__format__('%Y-%m-%d %H:%M:%S')


def get_date():
    return datetime.now().date()
