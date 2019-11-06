#!/usr/bin/env python3
# encoding: utf-8
# -*- coding: utf-8 -*-
# @Time : 2018-12-22 19:53
# @Author : Leon Chu <ieno_chu@apple.com>


small_file = '/Users/chujiejie/workspace/framework/word_classification/app/runner/small.txt'

middle_file = '/Users/chujiejie/workspace/framework/word_classification/app/runner/middle.txt'

mix_file = '/Users/chujiejie/workspace/framework/word_classification/app/runner/mix.txt'

small = []
middle = []
must = []
select = []
outrange = []


def build_samll():
    global small
    content = read_file(small_file)
    small = content.split('\n')


def build_middle():
    global middle
    content = read_file(middle_file)
    middle = content.split('\n')


def build_mix():
    global must, select, middle, outrange, small
    lines = []
    content = read_file(mix_file)
    arr = content.split('\n')
    for line in arr:
        line = line.strip()
        if len(line) < 2:
            continue
        if line.__contains__('\t'):
            for cont in line.split('\t'):
                if len(cont) > 1:
                    lines.append(cont)
        else:
            lines.append(line)

    for line in lines:
        if len(line) < 2:
            continue
        if line.__contains__('('):
            line.replace('(', ' ').replace(')', ' ')
            if line.__contains__('**'):
                line = line.replace('*', '')
                for word in line.split(' '):
                    if len(word) < 2:
                        continue
                    select.append(word)
            elif line.__contains__('*'):
                line = line.replace('*', '')
                for word in line.split(' '):
                    if len(word) < 2:
                        continue
                    must.append(word)
            for word in line.split(' '):
                if len(word) < 2:
                    continue
                outrange.append(word)
        else:
            if line.__contains__('**'):
                line = line.replace('*', '')
                select.append(line)
            elif line.__contains__('*'):
                line = line.replace('*', '')
                must.append(line)
            else:
                outrange.append(line)
    global middle
    middle = middle + outrange


def read_file(file_name):
    content = ''
    with open(file_name, 'r') as f:
        try:
            for line in f.readlines():
                content += line
        except Exception as e:
            print('read error')
            print(e)
    return content


def read_content():
    build_samll()
    build_mix()
    build_middle()
    result = []
    with open('/Users/chujiejie/workspace/framework/word_classification/app/runner/temp.txt', 'r') as f:
        lines = f.readlines()

    for line in lines:
        if len(line) > 1:
            arrs = line.split(' ')
            for arr in arrs:
                origin = arr + ''
                word = arr
                replaces = ["'s", "\'s", '\'', "'", ",", ".", "?", '\n', '"', '\"', "\."]
                if word.endswith('s'):
                    word = word[0:-1]
                for re in replaces:
                    word = word.lower()
                    word = word.replace(re, ' ')
                word = word.strip()

                if word in small:
                    print(word, 'small')
                    result.append([origin, '#008B8B'])
                elif word in middle:
                    print(word, 'middle')
                    result.append([origin, '#00FFFF'])
                elif word in must:
                    print(word, 'must')
                    result.append([origin, '#FFE4C4'])
                elif word in select:
                    print(word, 'select')
                    result.append([origin, '#008000'])
                elif len(word) > 3:
                    print("---" + word + '===', 'out of range')
                    result.append([origin, '#FF4500'])
                else:
                    result.append([origin, "*"])
                result.append([' ', "*"])

        result.append(['\n', '*'])
    print('it' in small)
    return result


def main():
    global must, select, middle, outrange, small
    build_samll()
    build_middle()
    build_mix()
    example_file = 'example.txt'
    word_lines = read_file(example_file)
    replaces = ['\'', "'", ",", ".", "?", '\n', '"', '\"', "\."]
    for re in replaces:
        word_lines = word_lines.replace(re, ' ')
    arrs = word_lines.split(' ')

    words = []
    for arr in arrs:
        if len(arr) > 0 and arr != 's':
            # continue
            # print('-' + arr + '=', len(arr))
            words.append(arr)

    for word in words:
        if len(word) < 2:
            continue
        word = word.lower()
        if word in small:
            print(word, 'small')
        elif word in middle:
            print(word, 'middle')
        elif word in must:
            print(word, 'must')
        elif word in select:
            print(word, 'select')
        else:
            print(word, 'out of range')
    # print(small)
    # build_mix()
    # print(middle)


if __name__ == '__main__':
    main()
