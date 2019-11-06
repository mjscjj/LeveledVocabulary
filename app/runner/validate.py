#!/usr/bin/env python3
# encoding: utf-8
# @File: validate.py
# @Author : Leon Chu <leon_chu@apple.com>
# @Time : 2018-12-12 09:06


def validate_trending_pools(content):
    # 判断是否含有特殊字符
    specials = {'`', '~', '!', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '[', ']', '\\', '<', '>', '?', '.', '/'}
    for ch in content:
        if ch in specials:
            return False
    # 判断格式
    spls = str.split(content, ' ')
    if 2 > len(spls) or len(spls) > 3:
        return False
    # 单词长度
    word = spls[0]
    if word is None or len(word) > 20:
        return False

    # sannos
    annos = []
    if spls[1].__contains__(','):
        annos = spls[1].split(',')
    else:
        annos.append(spls[1])
    if 1 > len(annos) > 10:
        return False

    # must
    if len(spls) == 3:
        must = spls[2]
        try:
            must = int(must)
        except:
            return False
        if must > 60 or must < 1:
            return False
    return True

# a = validate_trending_pools("asd` ovs 2")
# print(a)
