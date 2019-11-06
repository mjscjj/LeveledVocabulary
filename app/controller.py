#!/usr/bin/env python3
# encoding: utf-8
# @File: controller.py
# @Author : Leon Chu <leon_chu@apple.com>
# @Time : 2018-12-08 15:32
from flask import Blueprint, current_app as app, request, jsonify, render_template, abort, flash, url_for

controller = Blueprint('controller', __name__)
from flask import request, send_from_directory

import time, datetime, json
from app.runner.worddocx import *
import os
import urllib


@controller.route('/', methods=['GET', 'POST'])
def hello():
    return render_template("index.html")


@controller.route('/ana', methods=['GET', 'POST'])
def hello_at():
    global file_name
    from .word_classify import classify, word_percentage, word_distributione
    fname = request.files.get('file')  # 获取上传的文件
    distributione = [[0, ], [0], [0, ], [0, ], [0, ], [0, ]]
    if not fname:
        return render_template("mains.html", dis=distributione)
    ntime = str(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()))
    file_name1 = "/root/word_classification/app/data/" + ntime + '.docx'
    file_name2 = "/Users/chujiejie/workspace/framework/word_classification/app/data/" + ntime + '.docx'
    file_name3 = "/home/ubuntu//word_classification/app/data/" + ntime + '.docx'
    try:
        fname.save(file_name1)
        file_name = file_name1
    except:
        try:
            fname.save(file_name2)
            file_name = file_name2
        except:
            fname.save(file_name3)
            file_name = file_name3
    content = ''
    if fname.filename.endswith('.docx'):
        content = readdocx(file_name)
    elif fname.filename.endswith('.txt'):
        import chardet
        with open(file_name, 'rb') as f:
            data = f.read(200)
            code = chardet.detect(data).get("encoding")
            print('detect encode: ', code)
        if code == None:
            code = 'utf-8'
        with open(file_name, 'r', encoding=code, errors="ignore") as f:
            content = f.read()
    else:
        return '文件格式不正确'
    content = content.replace('\r\n', '\n')
    result = classify(content)
    percentage = word_percentage(result)
    distributione = word_distributione(result)
    temp = os.remove(file_name)
    write_docx(file_name, result, percentage=percentage)
    return render_template("mains.html", messages=result, percentage=percentage, dis=distributione, file=file_name)


@controller.route('/ana_s', methods=['GET', 'POST'])
def hello_ats():
    global file_name
    from .word_classify import classify, word_percentage, word_distributione
    fname = request.files.get('file')  # 获取上传的文件
    distributione = [[0, ], [0], [0, ], [0, ], [0, ], [0, ]]
    if not fname:
        return render_template("mains.html", dis=distributione)
    ntime = str(time.time())
    file_name1 = "/root/word_classification/app/word_classify/temp_" + ntime + ".txt"
    file_name2 = "/Users/chujiejie/workspace/framework/word_classification/app/word_classify/temp_" + ntime + ".txt"
    file_name3 = "/home/ubuntu//word_classification/app/word_classify/temp_" + ntime + ".txt"
    try:
        fname.save(file_name1)
        file_name = file_name1
    except:
        try:
            fname.save(file_name2)
            file_name = file_name2
        except:
            fname.save(file_name3)
            file_name = file_name3
    import chardet
    with open(file_name, 'rb') as f:
        data = f.read(200)
        code = chardet.detect(data).get("encoding")
        print('detect encode: ', code)
    if code == None:
        code = 'utf-8'
    with open(file_name, 'r', encoding=code, errors="ignore") as f:
        content = f.read()
    result = classify(content)
    percentage = word_percentage(result)
    distributione = word_distributione(result)
    import os
    temp = os.remove(file_name)
    return render_template("mains_s.html", messages=result, percentage=percentage, dis=distributione)


@controller.route('/add_word', methods=['GET', 'POST'])
def add_word():
    file = request.form.get('class')
    word = request.form.get('word')
    from .word_classify.utils import append_word, read_all_list
    words_list = read_all_list()
    if file and word:
        dates = str(datetime.date.today())
        word = word.replace('\n', '--').replace('\r', '--').replace(' ', '--')
        words = word.split('--')
        append_word(file, '\n==' + dates)
        for wod in words:
            append_word(file, wod)
        success = '添加成功'
        return render_template("add_word.html", success=success)
    else:
        return render_template("add_word.html", wordslist=words_list)


@controller.route('/search', methods=['GET', 'POST'])
def search():
    from .word_classify import classify, word_percentage, word_distributione
    word = request.args.get('word')
    if request.args.get('kwdNamesStr'):
        word = request.args.get('kwdNamesStr')
    # \r\n环卫\r
    word = word.replace('\r\n', '\n').strip()
    print(word.encode('utf-8'), '========')
    if word.strip().__contains__(' '):
        content = word
        ntime = str(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()))
        file_name1 = "/root/word_classification/app/data/" + ntime + '.docx'
        file_name2 = "/Users/chujiejie/workspace/framework/word_classification/app/data/" + ntime + '.docx'
        file_name3 = "/home/ubuntu//word_classification/app/data/" + ntime + '.docx'
        try:
            with open(file_name1, 'w') as f:
                pass
            file_name = file_name1
        except:
            try:
                with open(file_name2, 'w') as f:
                    pass
                file_name = file_name2
            except:
                with open(file_name3, 'w') as f:
                    pass
                file_name = file_name3

        ntime = "export_" + ntime
        file_name1 = "/root/word_classification/app/data/" + ntime + '.docx'
        file_name2 = "/Users/chujiejie/workspace/framework/word_classification/app/data/" + ntime + '.docx'
        file_name3 = "/home/ubuntu//word_classification/app/data/" + ntime + '.docx'
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

        # file_export
        result = classify(content)
        percentage = word_percentage(result)
        distributione = word_distributione(result)
        temp = os.remove(file_name)
        write_docx(file_name, result, percentage=percentage)
        return render_template("mains.html", messages=result, percentage=percentage, dis=distributione, file=file_name)
    elif word:
        from .word_classify.word_classify import search_word
        searchr = "" + word + ","
        searchr = searchr + "class:" + search_word(word) + ','
        from .word_classify.youdao import connect
        tran = connect(word)
        result = searchr + tran
        result = result.split(',')

        return render_template('search.html', result=result)
    else:
        return render_template('search.html')


@controller.route('/word', methods=['GET', 'POST'])
def search_word():
    word = request.args.get('word')
    print(word)
    if word:
        from .word_classify.word_classify import search_word
        searchr = "" + word + ","
        searchr = searchr + "class:" + search_word(word) + ','
        from .word_classify.youdao import connect
        tran = connect(word)
        result = searchr + tran
        return result
    return ',,,,,,'


@controller.route('/download', methods=['GET', 'POST'])
def down_file():
    file_name = request.args.get('filename')
    print(file_name)
    return send_from_directory(os.path.dirname(file_name), os.path.basename(file_name), as_attachment=True)


def handle_docx(filename, result):
    pass
    return ''

@controller.route('/index/searchHeat', methods=['GET', 'POST'])
def extenf():
    return search()


@controller.route('/transform', methods=['GET', 'POST'])
def transform():
    from .word_classify.youdao import connect_simple
    word = request.args.get('word')
    words = []
    word = word.replace('\r\n', ' ').strip()
    word.replace("\n", " ")
    word.replace("\r", " ")
    word.replace("\t", " ")
    for w in word.split(" "):
        if len(w) > 2:
            print("transform:" + w)
            words.append(w)
    res = ""
    for w in words:
        res = res + " \n" + w + "  \t" + connect_simple(w)
    return res



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

    cmd = "bash ./app/dict.sh "
    file = "word.txt"
    for word in result:
        cmd = cmd + word[0]
        print(word)
        print(cmd)
        print("excute：" + str(os.system(cmd)))

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



