#!/usr/bin/env python3
# encoding: utf-8
# -*- coding: utf-8 -*-
# @Time : 2018-12-22 19:53
# @Author : Leon Chu <ieno_chu@apple.com>

print(len("\n"))

duty = []
must = []
select = []
spe = []


def splits(line):
    line = line.strip()
    if line.__contains__('(') or line.__contains__('\\'):
        print(line.encode('utf-8'))
        return
    if line.__contains__('**'):
        line = line.replace('*', '').strip()
        if len(line) < 2: return
        select.append(line)
    elif line.__contains__('*'):
        line = line.replace('*', '').strip()
        if len(line) < 2: return
        must.append(line)
    else:
        line = line.replace('*', '').strip()
        if len(line) < 2: return
        duty.append(line)


def handle():
    with open('mix.txt') as f:
        for line in f.readlines():
            line = line.replace('\n', '')
            if len(line) < 2:
                continue
            if line.__contains__('\t'):
                for spli in line.split('\t'):
                    if len(spli) < 2:
                        continue
                    splits(spli)
            else:
                splits(line)
            # print(line.encode('utf-8'))
    with open('musts.txt', 'w') as f:
        for word in must:
            f.write(word + '\n')
    with open('selects.txt', 'w') as f:
        for word in select:
            f.write(word + '\n')
    with open('dutys.txt', 'w') as f:
        for word in duty:
            f.write(word + '\n')
    print('====')


# handle()
