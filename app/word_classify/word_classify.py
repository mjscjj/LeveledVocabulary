#!/usr/bin/env python3
# encoding: utf-8
# -*- coding: utf-8 -*-
# @Time : 2018-12-22 19:53
# @Author : Leon Chu <ieno_chu@apple.com>

import sys

sys.path.append('.')
from .utils import *
from .word_origin import *

primary = []
middle = []
must = []
select = []
duty = []

middle_one = []
word_origin = {}


def init():
    global primary, middle, must, select, duty, word_origin, middle_one
    primary = read_to_set(primary_school)
    middle = read_to_set(middle_school)
    must = read_to_set(high_school_must)
    select = read_to_set(high_school_select)
    duty = read_to_set(high_school_duty)

    middle_one = read_to_set(middle_school_one)


init()


def add_color(result, origin, word=''):
    if not word or len(origin) < 2:
        for s in origin:
            if s == "\n" or s == "\r":
                result.append(['', 'n'])
            elif s == " ":
                result.append(['', 's'])
            else:
                result.append([s, '*'])
        return
    if word in primary:
        # print(word, 'small')
        result.append([origin, '#2F4F4F'])
    elif word in middle_one:
        result.append([origin, '#000066'])
    elif word in middle:
        # print(word, 'middle')
        result.append([origin, '#4169E1'])
    elif word in must:
        # print(word, 'must')
        result.append([origin, '#DAA520'])
    elif word in select:
        # print(word, 'select')
        result.append([origin, '#3CB371'])
    elif word in word_origin.keys() and word != word_origin[word]:
        add_color(result, origin, word_origin[word])
        return
    elif word.endswith('s'):
        ends_word = word[:-1]
        add_color(result, origin, ends_word)
        return
    elif len(word) > 2:
        result.append([origin, '#FF4500'])
    else:
        result.append([origin, '*'])


def handle_s_tail(word):
    signs = ["\'ll", '\'s', '\'re']
    for sign in signs:
        if word.endswith(sign):
            return word[:word.index('\'')]
    return word


def classify(content):
    init()
    global word_origin
    word_origin = get_word_origin(content)
    result = []
    process = ''
    alphabet = ''
    for s in content:
        if is_alphabet(s) or s == "\'":
            alphabet += s
            if process:
                add_color(result, process)
                process = ''
        else:
            process += s
            if alphabet:
                # print(alphabet)
                word = alphabet + ''
                if word.__contains__("\'"):
                    word = handle_s_tail(word)
                word = word.lower()
                add_color(result, alphabet, word)
                alphabet = ''

    if process:
        add_color(result, process)
    if alphabet:
        word = alphabet + ''
        if word.__contains__("\'"):
            word = handle_s_tail(word)
        word = word.lower()
        add_color(result, alphabet, word)
    return result


def search_word(word):
    init()
    if word in primary:
        return '小学'
    elif word in middle:
        return '初中'
    elif word in must:
        return '高中必修'
    elif word in select:
        return '高中选修'
    else:
        return '超纲'


def word_percentage(words):
    p = 0
    m1 = 0
    m = 0
    mt = 0
    s = 0
    out = 0
    all = 0
    for word in words:
        word = word[0]
        if contains_letter(word):
            all += 1
            if word in primary:
                p += 1
            elif word in middle_one:
                m1 += 1
            elif word in middle:
                m += 1
            elif word in must:
                mt += 1
            elif word in select:
                s += 1
            else:
                out += 1
    pp, pm1, pm, pmt, ps, pout = round(float('%.2f' % (p / all)), 3) * 100, round(float('%.4f' % (m1 / all)),
                                                                                  3) * 100, round(
        float('%.4f' % (m / all)), 3) * 100, round(
        float('%.4f' % (mt / all)), 3) * 100, round(
        float('%.4f' % (s / all)),
        3) * 100, round(
        float('%.4f' % (out / all)), 3) * 100
    pp = round(pp, 4)
    pm1 = round(pm1, 4)
    pm = round(pm, 4)
    pmt = round(pmt, 4)
    ps = round(ps, 4)
    pout = round(pout, 4)
    result = {'primary': [pp, p], 'middle_one': [pm1, m1], 'middle': [pm, m], 'must': [pmt, mt], 'select': [ps, s],
              'out': [pout, out]}
    print(result)
    return result


def word_distributione(words):
    p = 0
    m = 0
    mt = 0
    s = 0
    out = 0
    all = 0
    for word in words:
        word = word[0]
        if contains_letter(word):
            all += 1
            if word in primary:
                p += 1
            elif word in middle:
                m += 1
            elif word in must:
                mt += 1
            elif word in select:
                s += 1
            else:
                out += 1
    pp, pm, pmt, ps, pout = round(p / all, 3) * 100, round(m / all, 3) * 100, round(mt / all, 3) * 100, round(s / all,
                                                                                                              3) * 100, round(
        out / all, 3) * 100

    result = [['primary', p], ['middle', m], ['must', mt], ['select', s], ['out', out]]
    return result


if __name__ == '__main__':
    for w in classify("wasn\'t   pregnant"):
        print(w)

    print("wasn't" in primary)
