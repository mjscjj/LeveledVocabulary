# /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import uuid
import requests
import hashlib
import time

YOUDAO_URL = 'http://openapi.youdao.com/api'
APP_KEY = '2e0a3c0dfab0fbec'
APP_SECRET = 'l7GXiq6z8qeCnCscYzq5i5ld1LioJ6t1'


def encrypt(signStr):
    hash_algorithm = hashlib.sha256()
    hash_algorithm.update(signStr.encode('utf-8'))
    return hash_algorithm.hexdigest()


def truncate(q):
    if q is None:
        return None
    size = len(q)
    return q if size <= 20 else q[0:10] + str(size) + q[size - 10:size]


def do_request(data):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    return requests.post(YOUDAO_URL, data=data, headers=headers)


def connect(q='test'):
    data = {}
    data['from'] = 'EN'
    data['to'] = 'zh-CHS'
    data['signType'] = 'v3'
    curtime = str(int(time.time()))
    data['curtime'] = curtime
    salt = str(uuid.uuid1())
    signStr = APP_KEY + truncate(q) + salt + curtime + APP_SECRET
    sign = encrypt(signStr)
    data['appKey'] = APP_KEY
    data['q'] = q
    data['salt'] = salt
    data['sign'] = sign
    response = do_request(data)
    import json
    result = json.loads(response.content.decode('utf-8'))
    translation = result['translation']
    translate = ''
    type = ''
    explains = ''
    webs = ''
    try:
        translate = '-'.join(translation)
        type = '-'.join(result['basic']['exam_type'])
        explains = '-'.join(result['basic']['explains'])
        webs = ''
        for dic in result['web']:
            webs += "/" + "、".join(dic['value'])
    except Exception as e:
        print(e)
    return "翻译:" + translate + "," + "参考级别:" + type + "," + "解释:" + explains + "," + "网络释意:" + webs + ','


def connect_simple(q='test'):
    data = {}
    data['from'] = 'EN'
    data['to'] = 'zh-CHS'
    data['signType'] = 'v3'
    curtime = str(int(time.time()))
    data['curtime'] = curtime
    salt = str(uuid.uuid1())
    signStr = APP_KEY + truncate(q) + salt + curtime + APP_SECRET
    sign = encrypt(signStr)
    data['appKey'] = APP_KEY
    data['q'] = q
    data['salt'] = salt
    data['sign'] = sign
    response = do_request(data)
    import json
    result = json.loads(response.content.decode('utf-8'))
    translation = result['translation']
    translate = ''
    type = ''
    explains = ''
    webs = ''
    try:
        translate = '-'.join(translation)
        type = '-'.join(result['basic']['exam_type'])
        explains = '-'.join(result['basic']['explains'])
        webs = ''
        for dic in result['web']:
            webs += "/" + "、".join(dic['value'])
    except Exception as e:
        print(e)
    return "" + explains


if __name__ == '__main__':
    res = connect_simple('smart')
    import os
    print(os.getcwd())

    print(res)
