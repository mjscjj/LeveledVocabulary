#!/usr/bin/env python3
# encoding: utf-8
# -*- coding: utf-8 -*-
# @Time : 2018-12-22 19:53
# @Author : Leon Chu <ieno_chu@apple.com>


primary_school = 'primary_school.txt'
middle_school = 'middle_school.txt'
high_school_must = 'must.txt'
high_school_select = 'select.txt'
high_school_duty = 'duty.txt'

middle_school_one = 'middle_one.txt'

import os

try:
    os.chdir('/Users/jiejiechu/workspace/word_classification/app/word_classify')
except:
    try:
        os.chdir('/Users/chujiejie/workspace/framework/word_classification/app/word_classify')
    except:
        os.chdir('/home/ubuntu/word_classification/app/word_classify')


def to_small(file):
    words = []
    with open(file, 'r') as f:
        for line in f.readlines():
            line = line.replace('\n', '')
            if len(line) < 2:
                continue
            line = line.lower()
            words.append(line)
    with open(file, 'w+') as f:
        for word in words:
            f.write(word + '\n')


def contains_letter(word):
    for s in word:
        if s.isalpha():
            return True
    return False


def contains_zh(word):
    for c in word:
        if '\u4e00' <= c <= '\u9fa5':
            return True
    return False


def contains_zh_all(word):
    for c in word:
        if not ('\u4e00' <= c <= '\u9fa5'):
            return False
    return True


def contains_en(word):
    for c in word:
        if is_alphabet(c):
            return True
    return False


def contains_en_all(word):
    for c in word:
        if not is_alphabet(c):
            return False
    return True


# 纯英文
def is_alphabet(char):
    if (char >= '\u0041' and char <= '\u005a') or (char >= '\u0061' and char <= '\u007a'):
        return True
    else:
        return False


def read_to_set(file):
    words = set()
    with open(file, 'r') as f:
        for line in f.readlines():
            line = line.replace('\n', '')
            if len(line) < 2:
                continue
            if line.startswith('=='):
                continue
            words.add(line)
    return words


def read_to_array(file):
    words = []
    with open(file, 'r') as f:
        for line in f.readlines():
            line = line.replace('\n', '')
            if len(line) < 2:
                continue
            if line.startswith('=='):
                continue
            words.append(line)
    return words


def append_word(file, word):
    with open(file, 'a') as f:
        f.write(word + '\n')
    return True


def read_all_list():
    res = []
    res.append(read_to_array(primary_school))
    res.append(read_to_array(middle_school))
    res.append(read_to_array(high_school_must))
    res.append(read_to_array(high_school_select))
    return res


if __name__ == '__main__':
    # to_small('primary_school.txt')
    # to_small('middle_school.txt')
    # to_small('must.txt')
    # to_small('select.txt')
    # to_small('duty.txt')
    # append_word('must.txt','abc')
    pass
