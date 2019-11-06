#!/usr/bin/env python3
# encoding: utf-8
# @File: test.py
# @Author : Leon Chu <leon_chu@apple.com>
# @Time : 2018-12-07 22:21

import mysql.connector

# 创建引擎
# engine = create_engine("mysql+pymysql://root:Trending@Apple1984@17.87.18.36:3306/locdata", max_overflow=5)
# 执行sql语句
# result = engine.execute("select * from locdata.words where words.id=1;")
# result = engine.execute('select * from user')
# res = result.fetchall()

# print(res)

# # mysql1.py
config = {
    'host': '17.129.249.178',
    'user': 'root',
    'password': 'leon',
    'port': 3306,
    'charset': 'utf8'
}
cnn = mysql.connector.connect(**config)
try:
    cnn = mysql.connector.connect(**config)
except mysql.connector.Error as e:
    print('connect fails!{}'.format(e))
print("connect success")


def readWordId(cnn, content):
    cursor = cnn.cursor()
    sql = "select id from locdata.words where content = \'{}\'".format(content)
    print(sql)
    cursor.execute(sql)
    id = None
    for id in cursor:
        cursor.close()
        print('word id {}'.format(id[0]))
        return id[0]
    cursor.close()


def change_record(cnn, d1, wordId):
    cursor = cnn.cursor()
    sql = "update locdata.records set records.d1 = {} where word_id = {}".format(int(d1), wordId)
    print(sql)
    cnn.commit()
    cnn = mysql.connector.connect(**config)
    cursor.execute(sql)
    cursor.close()


original_must = {}


def readoriginal():
    import os
    with open('/Users/chujiejie/work/Trending_Framework/HK/datas/2019-03-14/word_list_original.txt', 'r') as f:
        for line in f.readlines():
            line = line.replace('\n', '')
            if line.__contains__('\t'):
                arr = line.split('\t')
                if len(arr) >= 3:
                    original_must[arr[0]] = arr[2]
        return original_must


import random


def readall_all():
    readoriginal()
    for k, v in original_must.items():
        v = int(v) * 100 + random.randint(0, 50)
        wordid = readWordId(cnn, k)
        change_record(cnn, v, wordid)


readall_all()


# readWordId(cnn, )


def execs(cnn, wordId):
    cursor = cnn.cursor()
    sql = "select must from locdata.trending_pools where word_id = {}".format(wordId)
    print(sql)
    cursor.execute(sql)
    try:
        data = cursor.fetchone()
        if data[0] == None:
            print('==== in ======')
            sql = 'update locdata.trending_pools set must = 0 where word_id = {}'.format(wordId)
            print(sql)
            cursor.execute(sql)
            cnn.commit()
            cnn = mysql.connector.connect(**config)
    except Exception as e:
        print(e)
        print('error')
    finally:
        cursor.close()
        print('end')

#
# f = open('/Users/chujiejie/rec_word_must.txt')
# lines = f.readlines()
#
# for line in lines:
#     if line.__contains__('\n'):
#         word = line.split('\t')[0]
#         print(word)
#         wordid = readWordId(cnn, word)
#         if wordid != None:
#             execs(cnn, wordid)
#
# cnn.close()
