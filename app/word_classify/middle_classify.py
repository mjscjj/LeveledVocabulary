#!/usr/bin/env python3
# encoding: utf-8
# -*- coding: utf-8 -*-
# @Time : 2018-12-22 19:53
# @Author : Leon Chu <ieno_chu@apple.com>

from utils import *


def read(f):
    words = []
    with open(f, 'r', encoding='utf-8', errors="ignore") as f:
        for line in f.readlines():
            line = line.replace('\n', '').lower()
            words.append(line)

            # print(line.encode('utf-8'))
            # # print(line)
            # if contains_zh(line) and contains_en(line):
            #     if line.__contains__('、'):
            #         line = line[line.index('、') + 1:].strip()
            #     word = line.split(' ')[0]
            #     words.append(word)
            #     print(word)

    with open('ren.txt', 'w') as f:
        for w in words:
            f.write(w + '\n')


# def split():
#     words = []
#     other = []
#     with open('wai.txt', 'r') as f:
#         for line in f.readlines():
#             line = line.replace('\n', '')
#             if len(line) < 1:
#                 continue
#             if line.__contains__('*'):
#                 line = line.replace("*", '')
#                 other.append(line)
#             else:
#                 words.append(line)
#         with open('wai_normal.txt', 'w') as f:
#             for word in words:
#                 word = word.lower()
#                 f.write(word + '\n')
#         with open('wai_other.txt', 'w') as f:
#             for word in other:
#                 word = word.lower()
#                 f.write(word + '\n')

def coommon():
    ren = ''
    words = []
    with open('wai_normal.txt', 'r') as f1, open('wai_other.txt', 'r') as f2, open('ren.txt', 'r') as f3:
        ren = f3.read()
        for word in f1.readlines():
            word = word.replace('\n', '')
            if ren.__contains__(word):
                words.append(word)
        for word in f2.readlines():
            word = word.replace('\n', '')
            if ren.__contains__(word):
                words.append(word)
    with open('middle_one.txt', 'w') as f:
        for w in words:
            f.write(w + '\n')


if __name__ == '__main__':
    coommon()
    print()
    # split()
    # read('../../datas/a.txt')
