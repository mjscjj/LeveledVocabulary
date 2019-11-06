
#!/usr/bin/env python3
# encoding: utf-8
# -*- coding: utf-8 -*-
# @Time : 2018-12-22 19:53
# @Author : Leon Chu <ieno_chu@apple.com>
import time, datetime, json, os



def write_export(result):
    ntime = str(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()))
    ntime = "export_" + ntime
    file_name1 = "/root/word_classification/app/data/" + ntime + '.txt'
    file_name2 = "/Users/chujiejie/workspace/framework/word_classification/app/data/" + ntime + '.txt'
    file_name3 = "/home/ubuntu//word_classification/app/data/" + ntime + '.txt'
    try:
        with open(file_name1, 'w') as f:
            pass
        file_export = file_name1
    except:
        try:
            with open(file_name2, 'w') as f:
                pass
            file_export = file_name2
        except:
            with open(file_name3, 'w') as f:
                pass
            file_export = file_name3

    cmd = "bash dict.sh "
    file = "word.txt"
    for word in result:
        print("excute：" + str(os.system(cmd + word[0])))

    res = {}
    with open(file, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            line = line.replace("\n", "")
            line = line.replace("\t\n", "")
            res[line.split(" ")[0]] = line
    print(res)

    file_lines = []
    file_lines.append("小学单词:\n")
    for item in result:
        if item[1] == "#2F4F4F":
            con = res[item[0]]
            if con != None and not file_lines.__contains__(con):
                file_lines.append(con)

    file_lines.append("初中单词:\n")
    for item in result:
        if item[1] == "#4169E1":
            con = res[item[0]]
            if con != None and not file_lines.__contains__(con):
                file_lines.append(con)

    file_lines.append("高中必修单词:\n")
    for item in result:
        if item[1] == "#DAA520":
            con = res[item[0]]
            if con != None and not file_lines.__contains__(con):
                file_lines.append(con)

    file_lines.append("高中选修单词:\n")
    for item in result:
        if item[1] == "#3CB371":
            con = res[item[0]]
            if con != None and not file_lines.__contains__(con):
                file_lines.append(con)

    with open(file_export, 'w') as f:
        for line in file_lines:
            f.write(line + '\n')
    print(file_export)
    return file_export

def cover():
    print(os.getcwd())
    result = []
    for i in range(20):
        result.append(['hello', '#DAA520'])
    return write_export(result)

if __name__ == '__main__':
    cover()

